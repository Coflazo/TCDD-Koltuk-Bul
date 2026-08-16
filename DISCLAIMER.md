# Use, Limits and Disclaimer

**This is not legal advice.**

I am not a lawyer. Nothing here is a guarantee that using this software is lawful in
Turkey or anywhere else. This document describes what the tool does, what it refuses to
do, and where responsibility sits. Deciding whether your own use is permitted is your
job, not this file's.

---

## 1. What this is

TCDD Koltuk Bul is a personal tool that checks publicly visible journey pages on TCDD
e-bilet at intervals, alerts the user when a seat becomes free, and places TCDD's own
temporary hold on it. It automates the same clicks a person makes in their own browser,
logged in as themselves or as a guest, on pages that require no circumvention to view.

## 2. What it deliberately does not do

- **No payment.** It never automates payment. It stops at the payment step, and it
  never sees, stores, transmits or types card details.
- **Nothing is bypassed.** No captcha solving, no login bypass, no payment bypass, no
  rate limit evasion beyond behaving like an ordinary browser, no access to anything a
  logged out visitor cannot already see.
- **No bulk holds.** It holds exactly one seat. There is no multi passenger
  mode and no queueing of multiple holds. This is a design decision, not an oversight.
- **No load.** One browser instance, one sweep every 45 to 90 seconds, randomised.
  It is not a load generator and must not be reconfigured into one.
- **No data harvesting.** No scraped data is uploaded, published, resold or aggregated. What is
  read stays on the machine that read it.

## 3. Resale

This tool must not be used for commercial ticket resale, scalping, or holding inventory
with the intention of selling it on. Reselling transport tickets without authorisation can
carry legal consequences in Turkey. If that is your intention, do not use this software.

## 4. Accessible seats

Wheelchair spaces are excluded by default and are only watched if the user explicitly
selects that class. These places exist for passengers who cannot use any other seat.
Taking one you do not need takes it from somebody who does.

## 5. Personal data (KVKK)

The software stores only what you type into it, locally on your own computer:

| What | Where |
|---|---|
| Chosen stations and bay/bayan | `~/.koltukbul.json` |
| Browser session and cookies | `~/.koltukbul_profile` |
| Failure screenshots, if any | `debug/` |

Identity number, name, phone and card details are never read, stored or transmitted by
this software. You type those yourself, directly to TCDD, in the browser window it leaves
open. There is no server component, no telemetry and no analytics.

## 6. TCDD's terms of use

It is the user's responsibility to read and comply with the terms of use published by
TCDD Taşımacılık A.Ş. Those terms are set by TCDD, they can change at any time, and they
take precedence over anything written here. If automated access is not permitted for your
use case, do not use this software. Using it does not grant you any right you do not
otherwise have.

## 7. No affiliation

This is an unofficial, independent, personal project. It is not affiliated with, endorsed
by, sponsored by, or connected to TCDD Taşımacılık A.Ş. or any of its subsidiaries. The
name "TCDD" appears only to identify which public website the software reads, which is
nominative use. No trademark, logo or branding of TCDD is reproduced, and no impression of
official status is intended or should be inferred.

## 8. No warranty

Provided "as is", without warranty of any kind, express or implied, as set out in
[LICENSE](LICENSE). The author accepts no liability for missed trains, lost holds, expired
reservations, money spent, site changes that break it, account issues, or any other
consequence of running it. It can and will break when TCDD changes their pages.

## 9. Responsibility

By running this software you accept that you alone are responsible for how you use it and
for ensuring that your use complies with all applicable law and with TCDD's terms. If you
are unsure, consult a qualified lawyer in your jurisdiction.
