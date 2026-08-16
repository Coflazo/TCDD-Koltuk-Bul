#!/usr/bin/env python3
"""TCDD Koltuk Bul - dolu trende bos koltuk bekleyip yerini tutan bot.

I got tired of refreshing the TCDD page every ten minutes hoping somebody would cancel,
so I made it do that for me. It asks where I am going, which days work, which trains and
which classes I would actually sit in, then keeps checking. When a seat turns up it takes
it, holds it on the seat map, and makes noise until I get to the laptop.

Setup:  patchright install chromium
Run:    python3 koltukbul.py
        python3 koltukbul.py --test      # parsers only, no browser needed

Nothing is hardcoded. Override with TCDD_HOME, TCDD_VIDEO, TCDD_POLL, TCDD_PROFILE,
TCDD_STATE.
"""
import contextlib
import difflib
import io
import json
import os
import platform
import random
import re
import sys
import threading
import time
import webbrowser
from datetime import date, datetime

try:  # patchright is a drop-in Playwright fork with the automation tells already patched out
    from patchright.sync_api import sync_playwright
    PATCHED = True
except ImportError:
    from playwright.sync_api import sync_playwright
    PATCHED = False

def env(name, fallback):
    return os.environ.get(name) or fallback


HOME = env("TCDD_HOME", "https://ebilet.tcddtasimacilik.gov.tr/")
VIDEO = env("TCDD_VIDEO", "https://www.youtube.com/watch?v=M7IdXA23JVI")
POLL = tuple(float(x) for x in env("TCDD_POLL", "45,90").split(","))   # sweep gap, randomised
PROFILE = env("TCDD_PROFILE", os.path.expanduser("~/.koltukbul_profile"))
STATE = env("TCDD_STATE", os.path.expanduser("~/.koltukbul.json"))

SEATS = re.compile(r"\((\d+)\)")
WHEELCHAIR = "TEKERLEKL"                        # matches TEKERLEKLİ without any i/İ casing pain
GUN = ("Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma", "Cumartesi", "Pazar")

TTY = sys.stdout.isatty()


def sty(s, code):
    return "\033[%sm%s\033[0m" % (code, s) if TTY else s


def dim(s):
    return sty(s, "2")


def bold(s):
    return sty(s, "1")


# ---------------------------------------------------------------- pure helpers (testable)

def free_seats(text):
    """Digs the number out of "(3)". If it says DOLU, or there is no number, we get 0."""
    m = SEATS.search(text or "")
    return int(m.group(1)) if m else 0


TR_FOLD = str.maketrans("ıİşŞçÇğĞöÖüÜâÂîÎûÛ", "iissccggoouuaaiiuu")


def fold(s):
    """Flattens Turkish letters so "SÖĞÜTLÜÇEŞME" and "sogutlucesme" are the same thing.

    Fold first, lower after. Python turns "İ".lower() into an i plus a separate combining
    dot, which never matches anything a person actually types. Cost me a while to spot.
    """
    return s.translate(TR_FOLD).lower()


def suggest(q, stations, limit=8):
    """What the user probably meant. Three tries, cheapest first.

    Straight substring, then every word somewhere in the label so "ank gar" works, and
    only if both come up empty, a fuzzy pass over all the words in the station list. That
    last one is what turns "ankra" into ANKARA and "eskisehr" into ESKİŞEHİR.
    """
    fq = fold(q).strip()
    if not fq:
        return [], ""
    hits = [s for s in stations if fq in s["fold"]]
    if hits:
        return rank(hits, fq)[:limit], ""
    toks = fq.split()
    if len(toks) > 1:
        hits = [s for s in stations if all(t in s["fold"] for t in toks)]
        if hits:
            return rank(hits, toks[0])[:limit], ""
    vocab = sorted({w for s in stations for w in re.split(r"[^\w]+", s["fold"])
                    if len(w) > 2})
    near = []
    for t in toks:
        near += [w for w in difflib.get_close_matches(t, vocab, n=3, cutoff=0.62)
                 if w not in near]
    hits = [s for s in stations if any(w in s["fold"] for w in near)]
    ordered = []
    for s in hits:                      # best-guess word first, then name-over-city
        i = min(near.index(w) for w in near if w in s["fold"])
        ordered.append(((i, score(s, near[i]), len(s["fold"]), s["label"]), s))
    ordered.sort(key=lambda p: p[0])
    return [s for _, s in ordered][:limit], ", ".join(near)


def score(s, needle):
    """Lower is better. Typing "ista" should give me İSTANBUL, not BAĞIŞTAŞ, even though
    "bağıştaş" does technically contain it. Name beats city, start beats middle."""
    name = s["fold"].split(",")[0]
    if name.startswith(needle):
        return 0
    if any(w.startswith(needle) for w in re.split(r"[^\w]+", name)):
        return 1
    if needle in name:
        return 2
    return 3 if needle in s["fold"] else 4


def rank(hits, needle):
    return sorted(hits, key=lambda s: (score(s, needle), len(s["fold"]), s["label"]))


def parse_date(s, today):
    """Takes 17, 17.08, 17.08.2026, 17/08 or 2026-08-17. I never want to type the year.

    If I type a day that already went past, I obviously mean the next one, so "3" on the
    28th is next month and not a date in the past.
    """
    s = s.strip()
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", s):
        return date.fromisoformat(s)
    # no spaces inside a single date on purpose. everywhere else in here a space means
    # "next item", and I did not want that to mean two different things
    parts = [int(p) for p in re.split(r"[./\-]+", s) if p]
    if not 1 <= len(parts) <= 3:
        raise ValueError("bad date: %r" % s)
    day = parts[0]
    month = parts[1] if len(parts) > 1 else today.month
    year = parts[2] if len(parts) > 2 else today.year
    if year < 100:
        year += 2000
    d = date(year, month, day)
    if d < today and len(parts) < 3:
        d = date(year + 1, month, day) if len(parts) > 1 else \
            date(year + (month == 12), month % 12 + 1, day)
    return d


def parse_dates(raw, today):
    """"17 18 21", "17,18,21", "21, 17 18" - all the same to me. Sorted, no repeats."""
    return sorted({parse_date(p, today) for p in re.split(r"[,\s]+", raw.strip()) if p})


def parse_pick(s, n):
    """"1 2 4", "1,3-5" or "all" -> row indexes, zero based.

    Space or comma, both fine, and I should never have to type them in order. Same deal
    at every prompt in this program, so there is nothing to remember.
    """
    s = s.strip().lower()
    if s in ("all", "hepsi", "*"):
        return list(range(n))
    out = []
    for part in re.split(r"[,\s]+", re.sub(r"\s*-\s*", "-", s)):
        if not part:
            continue
        if "-" in part:
            a, b = part.split("-", 1)
            out.extend(range(int(a) - 1, int(b)))
        else:
            out.append(int(part) - 1)
    picked = sorted({i for i in out if 0 <= i < n})
    if not picked:
        raise ValueError("nothing valid picked")
    return picked


def resolve_pick(s, rows):
    """Same as parse_pick but a departure time works too, because "08:23" is how I
    actually think about which train I want, not "row 3"."""
    by_time = {}
    for i, r in enumerate(rows):
        by_time.setdefault(r["dep"], []).append(i)
    picked, leftover = [], []
    for part in re.split(r"[,\s]+", re.sub(r"\s*-\s*", "-", s.strip().lower())):
        if not part:
            continue
        (picked.extend(by_time[part]) if part in by_time else leftover.append(part))
    if leftover:
        picked.extend(parse_pick(",".join(leftover), len(rows)))
    if not picked:
        raise ValueError("nothing valid picked")
    return sorted(set(picked))


def stamp():
    return datetime.now().strftime("%H:%M:%S")


def pause(a=0.4, b=1.2):
    time.sleep(random.uniform(a, b))


def ask(prompt):
    try:
        return input(prompt)
    except EOFError:
        sys.exit("\nno input, quitting")


def recall():
    try:
        with open(STATE) as f:
            return json.load(f)
    except Exception:
        return {}


def remember(**kw):
    got = recall()
    got.update(kw)
    try:
        with open(STATE, "w") as f:
            json.dump(got, f)
    except Exception:
        pass            # if this fails, whatever. never crash over a convenience file


# ---------------------------------------------------------------- browser

def open_browser(pw):
    opts = dict(
        user_data_dir=PROFILE,          # keep the profile so it ages like a normal one
        headless=False,                 # headless is the easiest thing in the world to spot
        locale="tr-TR",
        timezone_id="Europe/Istanbul",
        viewport={"width": 1440, "height": 900},
        args=["--disable-blink-features=AutomationControlled"],
    )
    try:
        return pw.chromium.launch_persistent_context(channel="chrome", **opts)
    except Exception:
        return pw.chromium.launch_persistent_context(**opts)


STATIONS_JS = """(prefix) => [...document.querySelectorAll('button[id^="' + prefix + '"]')]
    .map(e => {
        const t = e.querySelector('.textLocation');
        return {id: e.id, label: (t ? t.innerText : e.innerText).replace(/\\s+/g, ' ').trim()};
    })"""


def load_stations(page, box, prefix):
    """Grabs the entire dropdown in one go.

    Turns out TCDD puts all 460 stations in the DOM straight away instead of virtualising
    them, so I can do the matching here rather than asking the site on every keystroke.
    The arrival list only holds stations you can actually reach from the departure, which
    is why I read it after picking that one.
    """
    open_dropdown(page, box, prefix)
    out = page.evaluate(STATIONS_JS, prefix)
    for s in out:
        s["fold"] = fold(s["label"])
    return out


def open_dropdown(page, box, prefix):
    """Only open it if it is closed. The input is a data-toggle, so clicking it when the
    list is already open just shuts it again and then nothing is clickable. Got me once."""
    if page.locator('button[id^="%s"]:visible' % prefix).count() == 0:
        page.click(box)
        pause(0.8, 1.5)


def pick_station(page, box, st):
    open_dropdown(page, box, st["id"].split("-")[0] + "-")
    option = page.locator("#" + st["id"])
    option.wait_for(state="visible", timeout=15000)
    pause()
    option.click()      # playwright scrolls the long list down to it by itself


def choose_station(page, box, what, prefix, default=None):
    stations = load_stations(page, box, prefix)
    q = None
    while True:
        if q is None:
            hint = dim(" [enter = %s]" % default["label"]) if default else ""
            q = ask("  %s%s: " % (what, hint)).strip()
            if not q and default:
                try:
                    pick_station(page, box, default)
                    return default
                except Exception:
                    print(dim("    that station is not on this route, type a name"))
                    default = None
                    q = None
                    continue
            if not q:
                q = None
                continue
        hits, near = suggest(q, stations)
        if not hits:
            print(dim("    no station like %r, try fewer letters" % q))
            q = None
            continue
        if near:
            print(dim("    did you mean %s?" % near))
        if len(hits) == 1:
            print(dim("    %s" % hits[0]["label"]))
            page.click("#" + hits[0]["id"])
            pause()
            return hits[0]
        for i, h in enumerate(hits, 1):
            print("    %2d) %s" % (i, h["label"]))
        a = ask("    " + dim("which one? (number, or keep typing) ")).strip()
        if a.isdigit() and 1 <= int(a) <= len(hits):
            chosen = hits[int(a) - 1]
            page.click("#" + chosen["id"])
            pause()
            return chosen
        q = a or None


def pick_date(page, when):
    page.click(".departureDate")        # click the wrapper, the input itself eats nothing
    # the picker shows two months side by side and each one repeats the other's spill-over
    # days as .off, so the same data-date appears twice. :not(.off) keeps it to one
    cell = page.locator('td[data-date="%s"]:not(.off)' % when.strftime("%Y-%m-%d")).first
    # only walks forwards, which is fine because every sweep reloads the page and the
    # calendar always comes back on the current month
    for _ in range(12):
        if cell.count():
            break
        page.click("th.next.available")
        pause(0.2, 0.5)
    cell.wait_for(state="visible", timeout=15000)
    if "disabled" in (cell.get_attribute("class") or ""):
        raise RuntimeError("%s is not selectable (date has passed?)" % when)
    pause()
    cell.click()


def one_way(page):
    if not page.locator('input[name="radioBtnDirection"][value="false"]').is_checked():
        page.click('span[selenium-test="one-way"]')
        pause()


def search(page, frm, to, when):
    page.goto(HOME, wait_until="domcontentloaded")
    pause(1.5, 3.0)
    pick_station(page, "#fromTrainInput", frm)
    pick_station(page, "#toTrainInput", to)
    pick_date(page, when)
    one_way(page)
    pause()
    page.click("#searchSeferButton")
    try:
        page.wait_for_selector("#gidis1btn", timeout=30000)
    except Exception:
        return False    # not a crash. it just means nothing runs that day on this route
    pause(1.0, 2.0)
    return True


def open_card(card):
    card.locator("div.customPx[data-toggle=collapse]").first.click()
    card.locator("div[id^=collapse]").first.wait_for(state="visible", timeout=10000)
    pause()


def read_classes(card):
    """Every class on one train with its own price and how many seats are left."""
    out = []
    for btn in card.locator("button[id*=vagonType]").all():
        name = btn.locator("span.text-left").first.inner_text()
        price = btn.locator(".price")
        seat = btn.locator("span.emptySeat")
        out.append({"name": " ".join(name.split()),
                    "price": " ".join(price.first.inner_text().split()) if price.count() else "",
                    "seats": free_seats(seat.first.inner_text()) if seat.count() else 0,
                    "btn": btn.get_attribute("id")})
    return out


def scan(page, when=None, expand=None, note=None):
    """Reads the train cards off the results page.

    Headers are free so I always take those. `expand` is the departure times whose cards
    should also be opened for per-class prices, or "all". Opening one costs a click and a
    wait, so I only do the ones I care about. If the header says Dolu then every class is
    empty anyway and there is no point opening it at all.
    """
    out = []
    cards = page.locator('div.card[id^="gidis"]')
    for i in range(cards.count()):
        c = cards.nth(i)
        head = c.locator(".card-header")
        if not head.count():
            continue
        times = head.locator(".locationTime time")
        if times.count() < 2:
            continue
        price = head.locator(".priceArea .price")
        dur = head.locator(".mobileTimeMB")
        name = head.locator(".textDepartureArrival p.col")
        out.append({
            "cid": c.get_attribute("id"),
            "date": when,
            "dep": times.nth(0).get_attribute("datetime"),
            "arr": times.nth(1).get_attribute("datetime"),
            "dur": " ".join(dur.first.inner_text().split()) if dur.count() else "",
            "name": " ".join(name.first.inner_text().split()) if name.count() else "",
            "price": " ".join(price.first.inner_text().split()) if price.count() else "",
            "sold_out": "dolu" in head.inner_text().lower(),
            "classes": [],
        })

    todo = [t for t in out
            if not t["sold_out"] and (expand == "all" or (expand and t["dep"] in expand))]
    for n, t in enumerate(todo, 1):
        if note:
            print("\r%s %d/%d " % (note, n, len(todo)), end="", flush=True)
        card = page.locator("#" + t["cid"])
        open_card(card)
        t["classes"] = read_classes(card)
    if note and todo:
        print("\r" + " " * 60 + "\r", end="")
    return out


def available(page, deps, classes):
    """Seats on the trains I am watching, in a class I said I would take.

    Also hands back which departures were still on the page, so the loop can work out
    when a train I was waiting for has simply left without me.
    """
    hits, seen = [], set()
    for t in scan(page, expand=set(deps)):
        seen.add(t["dep"])
        if t["dep"] not in deps:
            continue
        for c in t["classes"]:
            if c["seats"] and (classes is None or c["name"] in classes):
                hits.append({"cid": t["cid"], "btn": c["btn"],
                             "label": "%s %s -> %s  %s %s (%d)" % (
                                 t["dep"], t["name"][:30], t["arr"],
                                 c["name"], c["price"], c["seats"])})
    return hits, seen


# ---------------------------------------------------------------- holding a seat

FREE_SEAT_JS = """(want) => {
    const seats = [...document.querySelectorAll('.seatMapClick:not(.notSaleable)')]
        .filter(e => e.offsetParent !== null);
    const groups = new Map();
    seats.forEach((e, i) => {
        const src = (e.querySelector('img') || {}).src || '';
        if (!groups.has(src)) groups.set(src, []);
        groups.get(src).push(i);
    });
    for (const [, idx] of groups) if (idx.length === want) return idx[0];
    return -1;
}"""


def pick_seat(page, gender):
    """Clicks a free seat. This is the bit that actually holds it.

    Annoyingly the map does not mark free seats with a class, it swaps the seat image, and
    that image is a base64 blob. Instead of pasting that blob in here I look for the image
    that shows up exactly as many times as the wagon button says are free. Works itself
    out, and it will still work the day TCDD redraws the icons.
    """
    wagons = page.locator("button.btnWagon")
    best, most = None, 0
    for i in range(wagons.count()):
        m = re.search(r"(\d+)\s*Boş", wagons.nth(i).inner_text())
        n = int(m.group(1)) if m else 0
        if n > most:
            best, most = i, n
    if best is None:
        raise RuntimeError("seat map shows no wagon with a free seat")
    wagons.nth(best).click()
    pause(1.0, 2.0)

    idx = page.evaluate(FREE_SEAT_JS, most)
    if idx < 0:
        # counts do not line up. rather shout and let me look than book the wrong seat
        raise RuntimeError("could not tell free seats apart on wagon %d" % (best + 1))
    seat = page.locator(".seatMapClick:not(.notSaleable):visible").nth(idx)
    label = " ".join(seat.inner_text().split())
    seat.click()
    pause(0.8, 1.5)
    # clicking the seat only opens the bay/bayan popover. the hold lands on confirming
    page.locator('.wagonGenderPopover button.popoverBtn:has(img[alt*="gender-%s"])'
                 % gender).first.click()
    pause(1.0, 2.0)
    page.locator("button:has-text('Seçimi Tamamla')").first.click()
    pause(2.0, 3.0)
    return "wagon %d, seat %s" % (best + 1, label)


def grab(page, hit, gender):
    """Takes a seat I found all the way to a held seat. That is as far as it can get
    without my ID details, so it stops there, one click short of the form."""
    card = page.locator("#" + hit["cid"])
    # accordion only keeps one card open, so scanning the rest closed this one again
    open_card(card)
    page.locator("#" + hit["btn"]).click()
    pause()
    card.locator('button[selenium-test^="btn-gidis"]').first.click()
    pause(1.0, 2.0)
    page.locator("button:has-text('Devam Et')").first.click()
    page.wait_for_url("**/koltuk-haritasi", timeout=30000)
    pause(1.0, 2.0)
    return pick_seat(page, gender)


# ---------------------------------------------------------------- alarm

def beep():
    sound = "/System/Library/Sounds/Glass.aiff"
    if platform.system() == "Darwin" and os.path.exists(sound):
        os.system("afplay " + sound)
    else:
        print("\a", end="", flush=True)


def alarm(lines):
    print()
    for h in lines:
        print("  " + bold(h))
    if not webbrowser.open(VIDEO):
        print("  could not open a browser, watch it yourself: " + VIDEO)
    stop = threading.Event()

    def ring():
        while not stop.is_set():
            for _ in range(3):
                if stop.is_set():   # checked per beep so ENTER stops it right away
                    return
                beep()
            stop.wait(1.0)

    threading.Thread(target=ring, daemon=True).start()
    ask("\n  press ENTER to stop the alarm... ")
    stop.set()


# ---------------------------------------------------------------- asking

def ask_dates(today):
    print(dim("\n  which day? one, or a few if you are flexible"
              "\n    17         only the 17th"
              "\n    17 18 21   any of those three, commas fine too"))
    while True:
        raw = ask("  days: ")
        try:
            days = parse_dates(raw, today)
        except ValueError as e:
            print(dim("    %s" % e))
            continue
        if days:
            return days


def ask_gender():
    saved = recall().get("gender")
    hint = dim(" [enter = %s]" % ("bay" if saved == "man" else "bayan")) if saved else ""
    while True:
        g = ask("  travelling as bay or bayan?%s " % hint).strip().lower()
        if not g and saved:
            return saved
        if g in ("b", "bay", "e", "erkek", "m", "man"):
            return "man"
        if g in ("k", "kadin", "kadın", "bayan", "w", "women"):
            return "women"


def ask_classes(rows):
    """Offers whatever this route actually runs. No hardcoded list of class names, the
    site knows better than I do - some routes have YATAKLI, most do not."""
    names = []
    for t in rows:
        for c in t["classes"]:
            if c["name"] not in names:
                names.append(c["name"])
    if not names:
        print(dim("\n  every train is sold out right now, so watching all classes"))
        return None                     # None here means "take whatever frees up"
    print()
    for i, n in enumerate(names, 1):
        extra = dim("   only for wheelchair users") if WHEELCHAIR in n.upper() else ""
        print("   %2d) %s%s" % (i, n, extra))
    ordinary = [n for n in names if WHEELCHAIR not in n.upper()]
    while True:
        raw = ask("  which classes would you take? "
                  + dim("[1 2 4 · enter = all but wheelchair · all = everything] ")).strip()
        if not raw:
            return set(ordinary)
        try:
            return {names[i] for i in parse_pick(raw, len(names))}
        except ValueError as e:
            print(dim("    %s" % e))


def show(rows):
    day = None
    for i, t in enumerate(rows, 1):
        if t["date"] != day:
            day = t["date"]
            print("\n  " + bold("%s %s" % (day.strftime("%d.%m.%Y"), GUN[day.weekday()])))
        line = "  %2d  %s → %s  %-9s  %s" % (i, t["dep"], t["arr"], t["dur"], t["name"][:38])
        if t["sold_out"]:
            print(dim(line + "   dolu"))
            continue
        print(line)
        if t["classes"]:
            print("      " + dim(" · ".join(
                "%s %s%s" % (c["name"], c["price"], " (%d)" % c["seats"] if c["seats"] else "")
                for c in t["classes"])))


def countdown(secs, sweep):
    end = time.time() + secs
    while True:
        left = end - time.time()
        if left <= 0:
            break
        print("\r  " + dim("sweep %d found nothing · looking again in %3ds"
                           % (sweep, int(left) + 1)), end="", flush=True)
        time.sleep(min(1.0, left))
    print("\r" + " " * 60 + "\r", end="")


# ---------------------------------------------------------------- main

def main():
    today = date.today()
    saved = recall()
    print(bold("\n  TCDD Koltuk Bul") + dim("  ·  TCDD boş koltuk takibi  ·  ctrl-c to quit\n"))
    with sync_playwright() as pw:
        ctx = open_browser(pw)
        if not PATCHED:
            ctx.add_init_script(
                "Object.defineProperty(navigator,'webdriver',{get:()=>undefined})")
        page = ctx.pages[0] if ctx.pages else ctx.new_page()
        page.goto(HOME, wait_until="domcontentloaded")
        pause(1.5, 3.0)

        frm = choose_station(page, "#fromTrainInput", "from", "gidis-", saved.get("frm"))
        to = choose_station(page, "#toTrainInput", "to", "donus-", saved.get("to"))
        days = ask_dates(today)
        remember(frm=frm, to=to)

        rows = []
        for d in days:
            label = "  " + dim("%s %s" % (d.strftime("%d.%m"), GUN[d.weekday()]))
            print("\r%s  looking..." % label, end="", flush=True)
            if not search(page, frm, to, d):
                print("\r%s  %s%s" % (label, dim("no trains this day"), " " * 20))
                continue
            found = scan(page, d, expand="all", note=label + "  reading")
            print("\r%s  %d trains%s" % (label, len(found), " " * 20))
            rows.extend(found)
        if not rows:
            sys.exit("  nothing runs between those stations on those days")
        show(rows)

        while True:
            try:
                watch = [rows[i] for i in resolve_pick(
                    ask("\n  watch which? " + dim("[1 3 5 · 08:23 · all] ")), rows)]
                break
            except ValueError as e:
                print(dim("    %s" % e))
        classes = ask_classes(rows)
        gender = ask_gender()
        remember(gender=gender)

        print("\n  " + bold("watching %d train(s)" % len(watch)))
        for t in watch:
            print("    %s %s  %s → %s" % (t["date"].strftime("%d.%m"), t["dep"],
                                          t["name"][:34], t["arr"]))
        print(dim("    %s → %s · %s · %s"
                  % (frm["label"].split(",")[0], to["label"].split(",")[0],
                     ", ".join(sorted(classes)) if classes else "any class",
                     "bay" if gender == "man" else "bayan")))

        # keyed on departure time, not on the card position. once the early trains leave
        # for the day everything shuffles up and gidis1 quietly becomes a different train
        by_day = {}
        for t in watch:
            by_day.setdefault(t["date"], []).append(t["dep"])

        sweep = 0
        while True:
            sweep += 1
            hits = []
            for d, deps in list(by_day.items()):
                try:
                    if not search(page, frm, to, d):
                        continue
                    found, seen = available(page, deps, classes)
                    gone = [x for x in deps if x not in seen]
                    if gone:    # left already, or TCDD dropped it off the day's list
                        print(dim("  %s %s %s no longer listed"
                                  % (stamp(), d.strftime("%d.%m"), ", ".join(gone))))
                        by_day[d] = [x for x in deps if x in seen]
                        if not by_day[d]:
                            del by_day[d]
                    if found:
                        hits = found
                        break
                except Exception as e:
                    print(dim("  %s %s: retrying (%s)" % (stamp(), d.strftime("%d.%m"), e)))
            if not by_day:
                sys.exit("  every train you were watching has gone. nothing left to do.")
            if hits:
                lines = [h["label"] for h in hits]
                try:
                    lines.append("held -> " + grab(page, hits[0], gender))
                except Exception as e:   # a broken click must never eat the alarm
                    lines.append("could not hold it, grab it by hand: %s" % e)
                alarm(lines)
                # stop here. no more sweeps, and do not close the browser, it is sitting
                # on the held seat and I want to pay in that exact window
                print(dim("\n  browser is left open on the seat. go and pay."
                          "  ctrl-c here when you are done."))
                while True:
                    time.sleep(60)
            countdown(random.uniform(*POLL), sweep)


def test():
    assert free_seats("EKONOMİ ₺930,00 (3)") == 3
    assert free_seats("BUSİNESS DOLU") == 0
    assert free_seats("") == 0 and free_seats(None) == 0

    t = date(2026, 8, 16)
    assert parse_date("2026-08-17", t) == date(2026, 8, 17)
    assert parse_date("17.08.2026", t) == date(2026, 8, 17)
    assert parse_date("17.08", t) == date(2026, 8, 17)
    assert parse_date("17/8", t) == date(2026, 8, 17)
    assert parse_date("17", t) == date(2026, 8, 17)
    assert parse_date("3", t) == date(2026, 9, 3)           # bare day gone -> next month
    assert parse_date("3.8", t) == date(2027, 8, 3)         # day.month gone -> next year
    assert parse_date("3", date(2026, 12, 20)) == date(2027, 1, 3)   # rolls the year too

    for form in ("17 18 21", "17,18,21", "21, 17 18", " 18 21 17 "):
        assert parse_dates(form, t) == [date(2026, 8, 17), date(2026, 8, 18),
                                        date(2026, 8, 21)], form
    assert parse_dates("17.08.2026, 21", t) == [date(2026, 8, 17), date(2026, 8, 21)]

    assert parse_pick("all", 4) == [0, 1, 2, 3]
    assert parse_pick("1,3", 4) == [0, 2]
    assert parse_pick("2-4", 4) == [1, 2, 3]
    assert parse_pick("3-4,1", 4) == [0, 2, 3]
    assert parse_pick(" 1 , 1 ", 4) == [0]                  # dupes collapse
    assert parse_pick("1 2 4", 5) == [0, 1, 3]              # spaces separate too
    assert parse_pick("1, 2 ,4", 5) == [0, 1, 3]            # mixed separators
    assert parse_pick("2 - 4", 5) == [1, 2, 3]              # spaced range
    for form in ("1 2 4", "1,2,4", "1, 2 , 4", "4, 2 1", " 4 2 1 ", "1,,2 4"):
        assert parse_pick(form, 5) == [0, 1, 3], form       # order and spacing never matter
    for bad in ("", "0", "9", "abc"):                       # out of range / junk must not pass
        try:
            parse_pick(bad, 4)
            raise AssertionError("should have rejected %r" % bad)
        except ValueError:
            pass

    assert fold("İSTANBUL(SÖĞÜTLÜÇEŞME)") == "istanbul(sogutlucesme)"
    assert fold("Ankara Gar") == "ankara gar" and fold("IĞDIR") == "igdir"
    st = [{"label": "İSTANBUL(SÖĞÜTLÜÇEŞME) , İSTANBUL"}, {"label": "ANKARA GAR , ANKARA"},
          {"label": "İZMİR(BASMANE) , İZMİR"}, {"label": "ESKİŞEHİR , ESKİŞEHİR"}]
    for x in st:
        x["fold"] = fold(x["label"])
    assert [h["label"] for h in suggest("sogutlucesme", st)[0]] == [st[0]["label"]]
    assert suggest("ANKARA", st)[0][0]["label"] == st[1]["label"]      # exact, no suggestion
    assert suggest("ankara", st)[1] == ""
    hits, near = suggest("ankra", st)                                  # typo -> did you mean
    assert hits and hits[0]["label"] == st[1]["label"] and "ankara" in near
    hits, near = suggest("eskisehr", st)
    assert hits and hits[0]["label"] == st[3]["label"]
    assert suggest("izmir basmane", st)[0][0]["label"] == st[2]["label"]   # words in any order
    assert suggest("basmane izmir", st)[0][0]["label"] == st[2]["label"]
    assert suggest("qqqq", st) == ([], "")
    # ranking: a name that starts with the query must beat one that merely contains it
    st2 = st + [{"label": "BAĞIŞTAŞ , ERZİNCAN"}, {"label": "ÇATALCA , İSTANBUL"},
                {"label": "İSTANBUL(BAKIRKÖY) , İSTANBUL"}, {"label": "AKŞEHİR , KONYA"},
                {"label": "BANAZ , UŞAK"}, {"label": "BANDIRMA , BALIKESİR"}]
    for x in st2:
        x["fold"] = fold(x["label"])
    assert suggest("ista", st2)[0][0]["label"].startswith("İSTANBUL")
    assert suggest("eskisehr", st2)[0][0]["label"].startswith("ESKİŞEHİR")
    assert suggest("bandrma", st2)[0][0]["label"].startswith("BANDIRMA")
    assert suggest("izmir", st2)[0][0]["label"].startswith("İZMİR")
    assert suggest("", st) == ([], "")

    rows = [{"dep": "05:30"}, {"dep": "07:20"}, {"dep": "08:23"}, {"dep": "08:23"}]
    assert resolve_pick("08:23", rows) == [2, 3]            # a time can match two trains
    assert resolve_pick("1,08:23", rows) == [0, 2, 3]
    assert resolve_pick("all", rows) == [0, 1, 2, 3]
    assert resolve_pick("2-3", rows) == [1, 2]
    try:
        resolve_pick("09:99", rows)
        raise AssertionError("should have rejected an unknown time")
    except ValueError:
        pass
    for form in ("1 08:23", "1,08:23", "08:23 , 1", "08:23,1"):
        assert resolve_pick(form, rows) == [0, 2, 3], form

    # this one matters. a wheelchair place is only ever watched if it was asked for
    cls = [{"classes": [{"name": "BUSİNESS"}, {"name": "TEKERLEKLİ SANDALYE"},
                        {"name": "EKONOMİ"}, {"name": "LOCA"}]}]
    real, hush = ask, io.StringIO()
    try:
        for reply, want in [("1 3", {"BUSİNESS", "EKONOMİ"}),
                            ("", {"BUSİNESS", "EKONOMİ", "LOCA"}),
                            ("all", {"BUSİNESS", "TEKERLEKLİ SANDALYE", "EKONOMİ", "LOCA"})]:
            globals()["ask"] = lambda p, r=reply: r
            with contextlib.redirect_stdout(hush):
                got = ask_classes(cls)
            assert got == want, (reply, got)
    finally:
        globals()["ask"] = real
    print("ok")


if __name__ == "__main__":
    try:
        test() if "--test" in sys.argv else main()
    except KeyboardInterrupt:
        print(dim("\n  bye"))
