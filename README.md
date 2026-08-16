<div align="center">

# TCDD Koltuk Bul

### Dolu trende boş koltuk çıkınca saniyesinde yakalayıp yerini tutan bot

A seat watcher and auto-reserve bot for TCDD e-bilet

[![tests](https://github.com/Coflazo/TCDD-Koltuk-Bul/actions/workflows/test.yml/badge.svg)](https://github.com/Coflazo/TCDD-Koltuk-Bul/actions/workflows/test.yml)
![python](https://img.shields.io/badge/python-3.8%2B-3776AB?logo=python&logoColor=white)
![deps](https://img.shields.io/badge/dependencies-1-brightgreen)
![license](https://img.shields.io/badge/license-MIT-black)

`ebilet.tcddtasimacilik.gov.tr` &nbsp;·&nbsp; 460 stations &nbsp;·&nbsp; one file &nbsp;·&nbsp; one dependency

</div>

---

Trains between İstanbul and Ankara sell out weeks ahead, but people cancel constantly.
The seat is there for a minute or two and then it is gone again. I got tired of
refreshing the page hoping to be the one looking at it when that happened, so I wrote
this. It waits, and when a seat appears it takes it and wakes me up.

Tek dosya, tek bağımlılık. One file, one dependency, no framework.

---

## Nasıl çalışır / How it works

**1. Asks where you are going.** Type any fragment of a station name. It pulls all 460
stations out of the page in one call and matches them locally, so Turkish characters are
optional and typos are fine — `sogutlucesme` finds SÖĞÜTLÜÇEŞME, and `ankra` gets you a
_did you mean ankara?_. The arrival list only ever offers stations you can actually
reach from the one you picked.

**2. Asks which day, or days.** One day if you are fixed, several if you are flexible —
`17 18 21` and it watches all three. Typing a day that already went past means next
month, because that is obviously what you meant.

**3. Opens Chrome and reads every train on those days.** Departure, arrival, duration,
and then it opens each train to read **every class with its own price and free seat
count**, because the price on the results page only shows the cheapest one and hides the
fact that BUSİNESS is ₺465 more.

**4. Shows you the lot and asks what you want.** Pick by row number or by departure time
— `08:23` is how you actually think about trains. Then pick which classes you would
genuinely sit in, out of the classes that route really runs.

**5. Then it waits.** A sweep every 45–90 seconds, randomised. One browser behaving like
a patient person, not a request flood.

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

Say I want to be in Ankara on the 25th, I could live with the 26th, and I am not paying
for business class unless I really have to.

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

  25.08 Salı      15 trains
  26.08 Çarşamba  15 trains

  25.08.2026 Salı
   1  05:30 → 09:59  4sa 29dk   YHT: 81002 İSTANBUL-ANKARA
      BUSİNESS ₺1.395,00 (38) · EKONOMİ ₺930,00 (233) · TEKERLEKLİ SANDALYE ₺930,00 (2)
   2  07:20 → 11:31  4sa 11dk   YHT: 81032 İSTANBUL- ANKARA
      BUSİNESS ₺1.395,00 (14) · EKONOMİ ₺930,00 (68) · TEKERLEKLİ SANDALYE ₺930,00 (2)
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

### Demo

<!-- Drop the recording at docs/demo.gif and uncomment the line below.
![TCDD Koltuk Bul demo](docs/demo.gif)
-->

_Recording not in the repo yet._ To make one: run with `TCDD_POLL=5,8` so the sweep
counter actually moves on camera, then either
[vhs](https://github.com/charmbracelet/vhs) (`vhs docs/demo.tape`) or
[asciinema](https://asciinema.org) plus [agg](https://github.com/asciinema/agg)
(`asciinema rec demo.cast` then `agg demo.cast docs/demo.gif`).

---

## Kurulum / Setup

Same on macOS, Linux and Windows. Python 3.8 or newer.

### macOS / Linux — Terminal

```bash
git clone https://github.com/Coflazo/TCDD-Koltuk-Bul.git
cd TCDD-Koltuk-Bul

python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
patchright install chromium

python3 koltukbul.py
```

### Windows — PowerShell

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

### Windows — cmd

```bat
py -m venv .venv
.venv\Scripts\activate.bat
pip install -r requirements.txt
patchright install chromium
py koltukbul.py
```

### Checking it works without opening a browser

```bash
python3 koltukbul.py --test
```

Runs every parser check offline — date formats, the pick syntax, Turkish folding, the
did-you-mean ranking, and the rule that a wheelchair place is only ever watched when it
was explicitly asked for. Prints `ok` and nothing else.

### Ayarlar / Settings

Nothing is hardcoded. Set any of these to change it:

| Variable | Default | What it does |
|---|---|---|
| `TCDD_POLL` | `45,90` | seconds between sweeps, randomised in this range |
| `TCDD_VIDEO` | a YouTube link | opened when a seat is found |
| `TCDD_PROFILE` | `~/.koltukbul_profile` | Chrome profile folder |
| `TCDD_STATE` | `~/.koltukbul.json` | remembered stations and gender |
| `TCDD_HOME` | TCDD e-bilet URL | site root |

```bash
TCDD_POLL=20,40 python3 koltukbul.py          # macOS / Linux
$env:TCDD_POLL="20,40"; py koltukbul.py       # PowerShell
```

Stations and gender are remembered between runs, so the second time is mostly enter.

---

## Gerekenler / Requirements

| | |
|---|---|
| Python | 3.8 or newer |
| Package | [`patchright`](https://github.com/Kaliiiiiiiiii-Vinyzu/patchright), or plain `playwright` |
| Browser | Chromium via `patchright install chromium`, or an installed Google Chrome |
| OS | macOS, Linux, Windows |
| Everything else | standard library only — `difflib`, `json`, `re`, `threading`, `webbrowser` |

It needs a desktop session, because the browser runs headful on purpose. Headless is the
easiest thing in the world for a site to spot, and there is nothing to hide here anyway:
this is one person's browser doing one person's booking.

---

## Bilinen sınırlar / Known limits

- Holds **one** seat. Multiple passengers are not implemented.
- Stops at payment. It never sees or types card details; you pay in the open window.
- TCDD's hold is temporary, so answer the alarm reasonably quickly.
- Wheelchair places are excluded unless you explicitly pick them. They exist for people
  who cannot use any other seat, and the bot should not be quietly taking one.

## Uyarı / Note

Kişisel kullanım içindir: tek yolcu, tek koltuk, nazik aralıklarla. For personal use
only. Not affiliated with TCDD Taşımacılık A.Ş.
