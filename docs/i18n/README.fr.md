# TCDD Koltuk Bul

[English](../../README.md) ·
[Türkçe](README.tr.md) ·
[Deutsch](README.de.md) ·
[Русский](README.ru.md) ·
[العربية](README.ar.md) ·
[فارسی](README.fa.md) ·
**Français** ·
[Español](README.es.md) ·
[Nederlands](README.nl.md) ·
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

**Un bot qui attrape les places libérées dans les trains turcs complets et les réserve aussitôt.**

Il vérifie en boucle les trains que vous avez choisis sur le site de TCDD. Dès que
quelqu'un annule, il sélectionne la place, déclenche la réservation temporaire de TCDD et
sonne l'alarme jusqu'à ce que vous soyez devant votre ordinateur.

Il couvre tout le réseau, pas une seule ligne : 460 gares, dans les deux sens, YHT, Anahat
et Bölgesel. Les classes disponibles sont lues sur le train lui-même. Rien de tout cela
n'est écrit en dur dans le code.

## Installation

Aucune connaissance en programmation n'est nécessaire. Une seule ligne suffit.

**macOS et Linux** (Terminal) :
```bash
curl -fsSL https://raw.githubusercontent.com/Coflazo/TCDD-Koltuk-Bul/main/install.sh | bash
```

**Windows** (PowerShell) :
```powershell
irm https://raw.githubusercontent.com/Coflazo/TCDD-Koltuk-Bul/main/install.ps1 | iex
```

Où il s'installe : lancé depuis le bureau, il y crée un dossier. Si vous êtes déjà dans un
dossier situé sous le bureau, il s'installe sur place. Depuis n'importe où ailleurs, il va
sur le bureau. À la fin, un fichier à double-cliquer vous attend : **Başlat.command**
(macOS, Linux) ou **Baslat.bat** (Windows).

## Utilisation

1. Indiquez le départ et l'arrivée. Les caractères turcs sont facultatifs et les fautes de
   frappe passent : `sogutlucesme` trouve SÖĞÜTLÜÇEŞME, et `ankra` propose ANKARA.
2. Le jour, ou plusieurs. Si vous êtes flexible, tapez `17 18 21` et il surveille les trois.
3. Tous les trains de ces jours s'affichent avec les prix et les places libres par classe.
4. Choisissez les trains et les classes qui vous conviennent vraiment.
5. Il fait le reste. Il retient la place et vous réveille. Le paiement reste à vous.

## Important

- Usage personnel uniquement. Un voyageur, une place. Pas pour la revente.
- Le paiement n'est jamais automatisé. Aucune donnée bancaire n'est lue, stockée ni saisie.
- Les places pour fauteuil roulant ne sont pas surveillées par défaut, seulement si vous
  les sélectionnez explicitement. Elles existent pour les voyageurs qui ne peuvent occuper
  aucune autre place.
- Vos données restent sur votre ordinateur.
- Il vous revient de respecter les conditions d'utilisation de TCDD.

Documentation complète : [README](../../README.md) &nbsp;·&nbsp; [DISCLAIMER](../../DISCLAIMER.md)
