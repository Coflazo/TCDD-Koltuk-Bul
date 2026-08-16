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
[Polski](README.pl.md) ·
**Română** ·
[Ελληνικά](README.el.md) ·
[Italiano](README.it.md) ·
[Azərbaycanca](README.az.md) ·
[ქართული](README.ka.md) ·
[中文](README.zh.md) ·
[日本語](README.ja.md) ·
[한국어](README.ko.md)

---

**Un bot care prinde locurile eliberate în trenurile turcești sold out și le rezervă imediat.**

Verifică iar și iar trenurile alese de tine pe site-ul TCDD. Imediat ce cineva anulează,
botul alege locul, pornește rezervarea temporară a TCDD și sună până vii la calculator.

Funcționează în toată rețeaua, nu pe o singură rută: 460 de stații, în ambele sensuri, YHT,
Anahat și Bölgesel. Ce clase există, citește chiar de la trenul respectiv. Nimic din toate
astea nu e scris fix în cod.

## Instalare

Nu trebuie să știi programare. E de ajuns o singură linie.

**macOS / Linux:**
```bash
curl -fsSL https://raw.githubusercontent.com/Coflazo/TCDD-Koltuk-Bul/main/install.sh | bash
```

**Windows (PowerShell):**
```powershell
irm https://raw.githubusercontent.com/Coflazo/TCDD-Koltuk-Bul/main/install.ps1 | iex
```

Unde se instalează: pornit de pe desktop, creează un folder acolo. Dacă ești deja într-un
folder de sub desktop, se instalează pe loc. De oriunde altundeva, merge pe desktop. La
final rămâne un fișier pe care dai dublu clic: **Başlat.command** (macOS, Linux) sau
**Baslat.bat** (Windows).

## Cum se folosește

1. Scrie de unde și până unde. Caracterele turcești nu sunt obligatorii, iar greșelile de
   tastare nu contează: `sogutlucesme` găsește SÖĞÜTLÜÇEŞME, iar la `ankra` îți propune ANKARA.
2. Ce zi, sau ce zile. Dacă ești flexibil, scrie `17 18 21` și le urmărește pe toate trei.
3. Îți arată toate trenurile din zilele alese, cu prețuri și locuri libere pe fiecare clasă.
4. Alege trenurile și clasele cu care ai călători cu adevărat.
5. Restul e treaba lui. Ține locul și te trezește. Plata o faci tu.

## Important

- Doar pentru uz personal. Un călător, un loc. Nu pentru revânzare.
- Plata nu este niciodată automatizată. Datele cardului nu sunt citite, salvate sau tastate.
- Locurile pentru scaun cu rotile nu sunt urmărite implicit, ci doar dacă le selectezi
  explicit. Ele există pentru călătorii care nu pot folosi niciun alt loc.
- Datele tale rămân pe calculatorul tău.
- Respectarea condițiilor TCDD este responsabilitatea ta.

Documentație completă: [README](../../README.md) &nbsp;·&nbsp; [DISCLAIMER](../../DISCLAIMER.md)
