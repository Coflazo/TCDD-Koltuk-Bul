# TCDD Koltuk Bul

[English](../../README.md) ·
[Türkçe](README.tr.md) ·
[Deutsch](README.de.md) ·
[Русский](README.ru.md) ·
[العربية](README.ar.md) ·
[فارسی](README.fa.md) ·
[Français](README.fr.md) ·
[Español](README.es.md) ·
[Nederlands](README.nl.md) ·
[Български](README.bg.md)

[Українська](README.uk.md) ·
**Polski** ·
[Română](README.ro.md) ·
[Ελληνικά](README.el.md) ·
[Italiano](README.it.md) ·
[Azərbaycanca](README.az.md) ·
[ქართული](README.ka.md) ·
[中文](README.zh.md) ·
[日本語](README.ja.md) ·
[한국어](README.ko.md)

---

**Bot, który wyłapuje zwolnione miejsca w wyprzedanych tureckich pociągach i od razu je blokuje.**

Raz za razem sprawdza wybrane przez ciebie pociągi na stronie TCDD. Gdy tylko ktoś zwróci
bilet, bot wybiera miejsce, uruchamia tymczasową rezerwację TCDD i dzwoni, dopóki nie
usiądziesz przy komputerze.

Działa w całej sieci, nie na jednej trasie: 460 stacji, w obie strony, YHT, Anahat i
Bölgesel. Jakie są klasy wagonów, odczytuje z samego pociągu. Nic z tego nie jest wpisane
na sztywno w kod.

## Instalacja

Nie musisz umieć programować. Wystarczy jedna linijka.

**macOS / Linux:**
```bash
curl -fsSL https://raw.githubusercontent.com/Coflazo/TCDD-Koltuk-Bul/main/install.sh | bash
```

**Windows (PowerShell):**
```powershell
irm https://raw.githubusercontent.com/Coflazo/TCDD-Koltuk-Bul/main/install.ps1 | iex
```

Gdzie się zainstaluje: uruchomiony na pulpicie tworzy tam folder. Jeśli jesteś już w
folderze pod pulpitem, instaluje się na miejscu. Skądkolwiek indziej idzie na pulpit. Na
koniec zostaje plik do dwukrotnego kliknięcia: **Başlat.command** (macOS, Linux) albo
**Baslat.bat** (Windows).

## Jak używać

1. Wpisz skąd i dokąd. Tureckie znaki nie są potrzebne, literówki nie przeszkadzają:
   `sogutlucesme` znajdzie SÖĞÜTLÜÇEŞME, a przy `ankra` podpowie ANKARA.
2. Który dzień, albo dni. Jeśli masz elastyczność, wpisz `17 18 21`, a będzie pilnował
   wszystkich trzech.
3. Pokaże wszystkie pociągi z tych dni, z cenami i liczbą wolnych miejsc w każdej klasie.
4. Wybierz pociągi i klasy, którymi naprawdę pojedziesz.
5. Resztą zajmie się sam. Zablokuje miejsce i cię obudzi. Płacisz ty.

## Ważne

- Tylko do użytku osobistego. Jeden podróżny, jedno miejsce. Nie do odsprzedaży.
- Płatność nigdy nie jest automatyczna. Dane karty nie są czytane, zapisywane ani wpisywane.
- Miejsca dla wózków inwalidzkich domyślnie nie są śledzone, tylko gdy wybierzesz je
  wyraźnie. Są dla podróżnych, którzy nie mogą skorzystać z żadnego innego miejsca.
- Twoje dane zostają na twoim komputerze.
- Za przestrzeganie regulaminu TCDD odpowiadasz ty.

Pełna dokumentacja: [README](../../README.md) &nbsp;·&nbsp; [DISCLAIMER](../../DISCLAIMER.md)
