# TCDD Koltuk Bul

[English](../../README.md) ·
[Türkçe](README.tr.md) ·
[Deutsch](README.de.md) ·
[Русский](README.ru.md) ·
[العربية](README.ar.md) ·
[فارسی](README.fa.md) ·
[Français](README.fr.md) ·
[Español](README.es.md) ·
**Nederlands** ·
[Български](README.bg.md)

[Українська](README.uk.md) ·
[Polski](README.pl.md) ·
[Română](README.ro.md) ·
[Ελληνικά](README.el.md) ·
[Italiano](README.it.md) ·
[Azərbaycanca](README.az.md) ·
[ქართული](README.ka.md) ·
[中文](README.zh.md) ·
[日本語](README.ja.md) ·
[한국어](README.ko.md)

---

**Een bot die vrijgekomen stoelen in uitverkochte Turkse treinen opvangt en meteen vastzet.**

Hij controleert de treinen die jij kiest steeds opnieuw op de TCDD-site. Zodra iemand
annuleert, kiest hij de stoel, start de tijdelijke reservering van TCDD en blijft alarm
slaan tot jij achter je computer zit.

Werkt op het hele net, niet op één traject: 460 stations, beide richtingen, YHT, Anahat en
Bölgesel. Welke klassen er zijn leest hij van de trein zelf af. Niets daarvan staat vast
in de code.

## Installeren

Je hoeft niet te kunnen programmeren. Eén regel is genoeg.

**macOS en Linux** (Terminal):
```bash
curl -fsSL https://raw.githubusercontent.com/Coflazo/TCDD-Koltuk-Bul/main/install.sh | bash
```

**Windows** (PowerShell):
```powershell
irm https://raw.githubusercontent.com/Coflazo/TCDD-Koltuk-Bul/main/install.ps1 | iex
```

Waar hij zichzelf installeert: sta je op het bureaublad, dan maakt hij daar een map. Zit je
al in een map onder het bureaublad, dan blijft hij daar. Vanaf elke andere plek gaat hij
naar het bureaublad. Daarna is er een bestand om op te dubbelklikken:
**Başlat.command** (macOS, Linux) of **Baslat.bat** (Windows).

## Gebruik

1. Typ waarvandaan en waarnaartoe. Turkse tekens hoeven niet en typefouten mogen:
   `sogutlucesme` vindt SÖĞÜTLÜÇEŞME, en bij `ankra` stelt hij ANKARA voor.
2. Welke dag, of dagen. Ben je flexibel, typ dan `17 18 21` en hij bewaakt alle drie.
3. Alle treinen van die dagen verschijnen met prijzen en vrije stoelen per klasse.
4. Kies de treinen en de klassen waarin je echt wil zitten.
5. De rest doet hij zelf. Hij zet de stoel vast en maakt je wakker. Betalen doe je zelf.

## Belangrijk

- Alleen voor persoonlijk gebruik. Eén reiziger, één stoel. Niet om door te verkopen.
- Betalen gaat nooit automatisch. Kaartgegevens worden nooit gelezen, opgeslagen of getypt.
- Rolstoelplaatsen worden standaard niet bewaakt, alleen als je ze uitdrukkelijk kiest. Ze
  zijn bedoeld voor reizigers die geen andere stoel kunnen gebruiken.
- Je gegevens blijven op je eigen computer.
- Je bent zelf verantwoordelijk voor het naleven van de voorwaarden van TCDD.

Volledige documentatie: [README](../../README.md) &nbsp;·&nbsp; [DISCLAIMER](../../DISCLAIMER.md)
