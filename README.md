<div align="center">

# TCDD Koltuk Bul

### Dolu trende boş koltuk çıkınca saniyesinde yakalayıp yerini tutan bot

A seat watcher and auto-reserve bot for TCDD e-bilet

![python](https://img.shields.io/badge/python-3.8%2B-3776AB?logo=python&logoColor=white)
![deps](https://img.shields.io/badge/runtime%20dependencies-1-brightgreen)
![platform](https://img.shields.io/badge/macOS%20·%20Windows%20·%20Linux-lightgrey)
![license](https://img.shields.io/badge/license-MIT-black)

`ebilet.tcddtasimacilik.gov.tr` &nbsp;·&nbsp; 460 stations &nbsp;·&nbsp; one file &nbsp;·&nbsp; one dependency

</div>

<div align="center">

**Read this in your language** &nbsp;(machine translated)

[Türkçe](https://github-com.translate.goog/Coflazo/TCDD-Koltuk-Bul?_x_tr_sl=auto&_x_tr_tl=tr&_x_tr_hl=tr) ·
[English](https://github.com/Coflazo/TCDD-Koltuk-Bul) ·
[Deutsch](https://github-com.translate.goog/Coflazo/TCDD-Koltuk-Bul?_x_tr_sl=auto&_x_tr_tl=de&_x_tr_hl=de) ·
[Русский](https://github-com.translate.goog/Coflazo/TCDD-Koltuk-Bul?_x_tr_sl=auto&_x_tr_tl=ru&_x_tr_hl=ru) ·
[العربية](https://github-com.translate.goog/Coflazo/TCDD-Koltuk-Bul?_x_tr_sl=auto&_x_tr_tl=ar&_x_tr_hl=ar) ·
[فارسی](https://github-com.translate.goog/Coflazo/TCDD-Koltuk-Bul?_x_tr_sl=auto&_x_tr_tl=fa&_x_tr_hl=fa) ·
[Français](https://github-com.translate.goog/Coflazo/TCDD-Koltuk-Bul?_x_tr_sl=auto&_x_tr_tl=fr&_x_tr_hl=fr) ·
[Español](https://github-com.translate.goog/Coflazo/TCDD-Koltuk-Bul?_x_tr_sl=auto&_x_tr_tl=es&_x_tr_hl=es) ·
[Nederlands](https://github-com.translate.goog/Coflazo/TCDD-Koltuk-Bul?_x_tr_sl=auto&_x_tr_tl=nl&_x_tr_hl=nl) ·
[Български](https://github-com.translate.goog/Coflazo/TCDD-Koltuk-Bul?_x_tr_sl=auto&_x_tr_tl=bg&_x_tr_hl=bg)

[Українська](https://github-com.translate.goog/Coflazo/TCDD-Koltuk-Bul?_x_tr_sl=auto&_x_tr_tl=uk&_x_tr_hl=uk) ·
[Polski](https://github-com.translate.goog/Coflazo/TCDD-Koltuk-Bul?_x_tr_sl=auto&_x_tr_tl=pl&_x_tr_hl=pl) ·
[Română](https://github-com.translate.goog/Coflazo/TCDD-Koltuk-Bul?_x_tr_sl=auto&_x_tr_tl=ro&_x_tr_hl=ro) ·
[Ελληνικά](https://github-com.translate.goog/Coflazo/TCDD-Koltuk-Bul?_x_tr_sl=auto&_x_tr_tl=el&_x_tr_hl=el) ·
[Italiano](https://github-com.translate.goog/Coflazo/TCDD-Koltuk-Bul?_x_tr_sl=auto&_x_tr_tl=it&_x_tr_hl=it) ·
[Azərbaycanca](https://github-com.translate.goog/Coflazo/TCDD-Koltuk-Bul?_x_tr_sl=auto&_x_tr_tl=az&_x_tr_hl=az) ·
[ქართული](https://github-com.translate.goog/Coflazo/TCDD-Koltuk-Bul?_x_tr_sl=auto&_x_tr_tl=ka&_x_tr_hl=ka) ·
[中文](https://github-com.translate.goog/Coflazo/TCDD-Koltuk-Bul?_x_tr_sl=auto&_x_tr_tl=zh-CN&_x_tr_hl=zh-CN) ·
[日本語](https://github-com.translate.goog/Coflazo/TCDD-Koltuk-Bul?_x_tr_sl=auto&_x_tr_tl=ja&_x_tr_hl=ja) ·
[한국어](https://github-com.translate.goog/Coflazo/TCDD-Koltuk-Bul?_x_tr_sl=auto&_x_tr_tl=ko&_x_tr_hl=ko)

</div>

---

Trains between İstanbul and Ankara sell out weeks ahead, but people cancel constantly.
The seat is there for a minute or two and then it is gone again. I got tired of
refreshing the page hoping to be the one looking at it when that happened, so I wrote
this. It waits, and when a seat appears it takes it and wakes me up.

<div align="center">

![TCDD Koltuk Bul demo](docs/demo.gif)

</div>

---

## Nasıl çalışır / How it works

**1. Asks where you are going.** Type any fragment of a station name. It pulls all 460
stations out of the page in one call and matches them locally, so Turkish characters are
optional and typos are fine. `sogutlucesme` finds SÖĞÜTLÜÇEŞME, and `ankra` gets you a
*did you mean ankara?*. The arrival list only ever offers stations you can actually
reach from the one you picked.

**2. Asks which day, or days.** One day if you are fixed, several if you are flexible:
`17 18 21` and it watches all three. Typing a day that already went past means next
month, because that is obviously what you meant.

**3. Opens Chrome and reads every train on those days.** Departure, arrival, duration,
and then it opens each train to read every class with its own price and free seat count.
The results page only shows the cheapest fare, which quietly hides that BUSİNESS is ₺465
more than EKONOMİ.

**4. Shows you the lot and asks what you want.** Pick by row number or by departure time,
since `08:23` is how you actually think about trains. Then pick which classes you would
genuinely sit in, out of the classes that route really runs.

**5. Then it waits.** A sweep every 45 to 90 seconds, randomised. One browser behaving
like a patient person, not a request flood.

**6. When a seat appears, it takes it.** Picks the class, hits Seçin and Devam Et, lands
on the seat map, finds a free seat, confirms bay/bayan and completes the selection. That
is a real hold on TCDD's side.

**7. Then it makes noise.** Beeps, opens a video, and leaves Chrome parked on the held
seat so you type your details and pay in that same window. It never sweeps again after
that, and it never touches your card.

```
stations ──► days ──► scrape every train ──► you pick trains + classes
                                                      │
                              ┌───────────────────────┘
                              ▼
                   sweep ──► seat found? ──no──► wait 45-90s ──┐
                              │                                │
                             yes                               └──(loop)
                              ▼
              pick class ──► Seçin ──► Devam Et ──► seat map
                              ▼
             click free seat ──► bay/bayan ──► Seçimi Tamamla
                              ▼
                    ALARM + browser parked on your seat
```

---

## Örnek / Example run

I want to be in Ankara on the 25th, I could live with the 26th, and I am not paying for
business class unless I really have to.

```
  TCDD Koltuk Bul  ·  TCDD boş koltuk takibi  ·  ctrl-c to quit

  from: ista
     1) İSTANBUL(PENDİK) , İSTANBUL
     2) İSTANBUL(HALKALI) , İSTANBUL
     3) İSTANBUL(BAKIRKÖY) , İSTANBUL
     4) İSTANBUL(BOSTANCI) , İSTANBUL
     5) İSTANBUL(SÖĞÜTLÜÇEŞME) , İSTANBUL
    which one? (number, or keep typing) 5
  to: ankra
    did you mean ankara?
     1) ANKARA GAR , ANKARA
     2) SİNCAN , ANKARA
    which one? (number, or keep typing) 1

  which day? one, or a few if you are flexible
    17         only the 17th
    17 18 21   any of those three, commas fine too
  days: 25 26

  25.08.2026 Salı
   1  05:30 → 09:59  4sa 29dk   YHT: 81002 İSTANBUL-ANKARA
      BUSİNESS ₺1.395,00 (38) · EKONOMİ ₺930,00 (233) · TEKERLEKLİ SANDALYE ₺930,00 (2)
   3  08:23 → 12:58  4sa 35dk   YHT: 81030 İSTANBUL - ANKARA
      BUSİNESS ₺1.395,00 (1) · EKONOMİ ₺930,00 (40) · LOCA DOLU · TEKERLEKLİ SANDALYE ₺930,00 (2)
   4  09:00 → 13:15  4sa 15dk   YHT: 81458 İSTANBUL-SİVAS   dolu

  watch which? [1 3 5 · 08:23 · all] 3 4

    1) BUSİNESS
    2) EKONOMİ
    3) LOCA
    4) TEKERLEKLİ SANDALYE   only for wheelchair users
  which classes would you take? [1 2 4 · enter = all but wheelchair · all = everything] 2

  travelling as bay or bayan? b

  watching 2 train(s)
    25.08 08:23  YHT: 81030 İSTANBUL - ANKARA → 12:58
    25.08 09:00  YHT: 81458 İSTANBUL-SİVAS → 13:15
    İSTANBUL(SÖĞÜTLÜÇEŞME) → ANKARA GAR · EKONOMİ · bay

  sweep 6 found nothing · looking again in  62s
```

An hour later somebody cancels:

```
  08:23 YHT: 81030 İSTANBUL - ANKARA -> 12:58  EKONOMİ ₺930,00 (1)
  held -> wagon 5, seat 21c

  press ENTER to stop the alarm...
  browser is left open on the seat. go and pay.  ctrl-c here when you are done.
```

---

## Kurulum / Setup

### Tek satır / One line

You do not need to know anything about programming. Paste one line and it handles Python,
the browser, and a double-clickable shortcut.

**macOS and Linux**, in Terminal:

```bash
curl -fsSL https://raw.githubusercontent.com/Coflazo/TCDD-Koltuk-Bul/main/install.sh | bash
```

**Windows**, in PowerShell:

```powershell
irm https://raw.githubusercontent.com/Coflazo/TCDD-Koltuk-Bul/main/install.ps1 | iex
```

Where it installs itself, which is the bit people always ask about:

| Where you run it from | What it does |
|---|---|
| Sitting on your Desktop | Makes a `TCDD-Koltuk-Bul` folder on the Desktop |
| Already inside a folder under the Desktop | Installs right there, no new folder |
| Anywhere else (home folder, `C:\`, a random path) | Goes to the Desktop and makes the folder there |

It finds your real Desktop even if it is renamed (Masaüstü, Schreibtisch) or redirected
into OneDrive.

When it finishes you get a file to double-click:

- macOS and Linux: **`Başlat.command`**
- Windows: **`Baslat.bat`**

### Elle kurulum / Manual setup

<details>
<summary>If you would rather do it yourself</summary>

**macOS and Linux**

```bash
git clone https://github.com/Coflazo/TCDD-Koltuk-Bul.git
cd TCDD-Koltuk-Bul
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
patchright install chromium
python3 koltukbul.py
```

**Windows PowerShell**

```powershell
git clone https://github.com/Coflazo/TCDD-Koltuk-Bul.git
cd TCDD-Koltuk-Bul
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
patchright install chromium
py koltukbul.py
```

If PowerShell blocks the activate script:
`Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`

**Windows cmd**

```bat
py -m venv .venv
.venv\Scripts\activate.bat
pip install -r requirements.txt
patchright install chromium
py koltukbul.py
```

</details>

### Try it without a TCDD account, a browser, or the internet

Real result pages from the live site are saved in `tests/fixtures/`. Replay mode runs the
actual scraper over them:

```bash
pip install beautifulsoup4 lxml
python3 koltukbul.py --replay
```

The parsers are not reimplemented for replay. `scan()` and `read_classes()` are the exact
same functions that read the live site, pointed at a saved page through a small shim, so
if a parser breaks the offline run breaks with it.

```bash
python3 koltukbul.py --test
```

Runs every parser check offline: date formats, the pick syntax, Turkish folding, the
did-you-mean ranking, the fixture-backed scrape, and the rule that a wheelchair place is
only ever watched when it was explicitly asked for. Prints `ok` and nothing else.

### Ayarlar / Settings

Nothing is hardcoded. Set any of these to change it:

| Variable | Default | What it does |
|---|---|---|
| `TCDD_POLL` | `45,90` | seconds between sweeps, randomised in this range |
| `TCDD_VIDEO` | a YouTube link | opened when a seat is found |
| `TCDD_PROFILE` | `~/.koltukbul_profile` | Chrome profile folder |
| `TCDD_STATE` | `~/.koltukbul.json` | remembered stations and gender |
| `TCDD_DEBUG` | `debug` | where failure screenshots are written |
| `TCDD_HOME` | TCDD e-bilet URL | site root |

```bash
TCDD_POLL=20,40 python3 koltukbul.py          # macOS and Linux
$env:TCDD_POLL="20,40"; py koltukbul.py       # PowerShell
```

Stations and gender are remembered between runs, so the second time is mostly enter.

---

## Ne kırıldı ve nasıl buldum / What broke and how I found it

None of the hard parts were the parts that looked hard. Every one of these was found by
running the thing and watching it fail, not by reading the HTML.

**Free seats are an image, not a class.** The seat map does not mark availability with a
CSS class. It swaps the seat image, and that image is an inline base64 blob. Hardcoding
the blob would break the first time TCDD redraws an icon. Instead it groups the seats by
image and picks the group whose size matches the wagon button's own "Boş" count. That
number is already on the page, so the map calibrates itself.

**A dropdown that closes when you open it.** The station input is a `data-toggle`.
Clicking it when the list is already open closes it, and every one of the 460 options
silently stops being clickable. Symptom was a 30 second timeout on an element that
Playwright could see in the DOM: `locator resolved to <button id="gidis-465">` followed by
`element is not visible`. Fixed by only opening it when it is shut.

**The same date, twice.** The calendar shows two months side by side and each one repeats
the other's spill-over days as `.off` cells, so `td[data-date="2026-09-05"]` matches two
elements and strict mode throws. I only caught it because I tested a date in the overlap:
`raw=2, :not(.off)=1`.

**`"İ".lower()` is not `"i"`.** Python turns it into an `i` plus a separate combining dot,
so an uppercase Turkish station name never matched anything a person typed. Fold the
Turkish letters flat first, lowercase second.

**Ranking, not matching, was the real problem.** Searching `ista` returned BAĞIŞTAŞ first,
which is a genuinely correct substring match, since "bağıştaş" folds to "bag**ista**s".
Matching was never broken. Scoring was missing. Name beats city, start beats middle.

**Cards move.** Trains were keyed by card position, `gidis1`, `gidis2`. As the day's early
departures leave, the list shifts up and `gidis1` quietly becomes a different train. Now
everything is keyed on departure time.

**The accordion closed the card I needed.** Scanning all trains left the last one expanded,
because Bootstrap's accordion only keeps one open. By the time the bot went back for the
train that actually had the seat, its wagon button was collapsed and unclickable. This one
would only ever have shown up at the exact moment it mattered.

**The date input eats its own clicks.** `.departureDate input` is covered by its wrapper
div, which owns the pointer events. The log said `<div class="datePickerInput
departureDate"> intercepts pointer events`, which is Playwright telling you exactly what
is wrong if you read past the timeout.

---

## Gerekenler / Requirements

| | |
|---|---|
| Python | 3.8 or newer |
| Runtime dependency | [`patchright`](https://github.com/Kaliiiiiiiiii-Vinyzu/patchright), or plain `playwright` |
| Browser | Chromium via `patchright install chromium`, or an installed Google Chrome |
| OS | macOS, Windows, Linux |
| Replay mode only | `beautifulsoup4` and `lxml`, not needed to run the bot |
| Everything else | standard library: `difflib`, `json`, `re`, `threading`, `webbrowser` |

It needs a desktop session, because the browser runs headful on purpose. Headless is the
easiest thing in the world for a site to spot, and there is nothing to hide here anyway:
this is one person's browser doing one person's booking.

---

## Kullanım koşulları / Use, limits and legal

Read [DISCLAIMER.md](DISCLAIMER.md) before using this. Short version:

- **Kişisel kullanım içindir.** One traveller, one seat. It holds exactly one seat and has
  no multi passenger mode, on purpose.
- **Ticaret için değildir.** Not for resale, not for scalping, not for booking inventory
  you intend to sell on. Reselling tickets can be an offence in Turkey and this tool will
  not help you do it.
- **Payment is never automated.** The bot stops at the payment step. It never sees, stores
  or types card details, and it never completes a purchase for you.
- **It does not bypass anything.** No captcha solving, no login bypass, no payment bypass,
  no paywall circumvention. It clicks the same public pages a person clicks.
- **Polite by design.** One browser, one sweep every 45 to 90 seconds, randomised. It is
  not a load test and must not be turned into one.
- **Your data stays on your machine.** The only things stored are your chosen stations and
  bay/bayan, in `~/.koltukbul.json`, plus a local Chrome profile. Nothing is sent anywhere
  except to TCDD, by your own browser, as you.
- **Wheelchair places are excluded by default** and are only ever watched if you
  explicitly select them. They exist for people who cannot use any other seat.
- **You are responsible for complying with TCDD's terms of use.** Read them. If automated
  access is not permitted for your use, do not use this.

**This is not legal advice and it is not a guarantee of legality.** I am not a lawyer, and
no README can make a tool "legally proof" under Turkish law or any other. What the above
describes is the design intent and the limits built into the code. Whether your particular
use is lawful is on you.

No warranty of any kind. See [LICENSE](LICENSE).

Not affiliated with, endorsed by, or connected to TCDD Taşımacılık A.Ş. in any way.
"TCDD" is used only to say which website this reads.
