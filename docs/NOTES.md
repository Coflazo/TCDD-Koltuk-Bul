# What broke and how I found it

Notes for myself while building this. Every one of these came from running the thing and
watching it fail, not from reading the HTML. None of the hard parts were the parts that
looked hard.

## Free seats are an image, not a class

The seat map does not mark availability with a CSS class. It swaps the seat image, and
that image is an inline base64 blob. Grouping seats by class gave nothing useful:

```
{'total': 67, 'variants': [{'cls': 'seatMapClick', 'kids': 'IMG.carItemImg|DIV.seatNumber',
 'img': 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAoCAYAAACM...
```

Hardcoding that blob would break the first time TCDD redraws an icon. Instead: group the
seats by image src, then take the group whose size equals the wagon button's own "Boş"
count. That number is already printed on the page, so the map calibrates itself.

## A dropdown that closes when you open it

The station input is a `data-toggle`, so clicking it while the list is already open closes
it, and all 460 options stop being clickable. The symptom was a 30 second timeout on an
element Playwright could clearly see:

```
waiting for locator("#gidis-465")
  - locator resolved to <button type="button" id="gidis-465" class="dropdown-item station">
  - element is not visible
```

Resolved but not visible is the tell. Fix: only open it when it is shut.

## The same date, twice

The calendar renders two months side by side and each repeats the other's spill-over days
as `.off` cells, so the same `data-date` matches two elements and Playwright strict mode
throws. Only caught by testing a date inside the overlap:

```
2026-08-16  raw=1  :not(.off)=1
2026-08-31  raw=2  :not(.off)=1   <- would have thrown
2026-09-05  raw=2  :not(.off)=1   <- would have thrown
2026-10-04  raw=1  :not(.off)=0   <- not on screen yet, needs the next arrow
```

## "İ".lower() is not "i"

Python lowercases `İ` into an `i` plus a separate combining dot, U+0307. So an uppercase
Turkish station name never matched anything a person typed. Fold the Turkish letters flat
first with `str.maketrans`, lowercase second. Order matters and it is not obvious.

## Ranking, not matching, was the problem

Searching `ista` returned BAĞIŞTAŞ first. That is a correct substring match: "bağıştaş"
folds to "bag**ista**s". Matching was never broken, scoring was missing.

```
ista  ->  BAĞIŞTAŞ , ERZİNCAN        (before)
ista  ->  İSTANBUL(PENDİK)           (after)
```

Score: name starts with the query beats a word in the name starting with it, beats
anywhere in the name, beats the city part only.

## Cards move

Trains were keyed by card position: `gidis1`, `gidis2`, `gidis3`. As the day's early
departures leave, the list shifts up and `gidis1` becomes a different train. A watcher
running overnight would silently start watching the wrong service. Everything is keyed on
departure time now.

## The accordion closed the card I needed

Scanning all trains left the last one expanded, because Bootstrap's accordion keeps only
one open. By the time the bot went back for the train that actually had the seat, its
wagon button was collapsed and unclickable. This one would only ever have shown up at the
exact moment it mattered, which is the worst kind of bug to leave in.

## The date input eats its own clicks

`.departureDate input` sits under its wrapper div, which owns the pointer events:

```
- attempting click action
- <div class="datePickerInput departureDate">…</div> intercepts pointer events
```

Playwright names the exact element that is in the way, if you read past the timeout line.
Click the wrapper instead.

## Clicking a seat does not book it

Clicking a free seat only opens a bay/bayan popover. The hold lands when that is
confirmed, and there is a further "Seçimi Tamamla" after it. Proof that the hold is real
came from a second run: wagon 5 had dropped from 23 free to 22, and the seat the first run
touched was gone.
