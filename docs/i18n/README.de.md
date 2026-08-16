# TCDD Koltuk Bul

**Ein Bot, der freie Plätze in ausgebuchten türkischen Zügen abfängt und sofort reserviert.**

Er prüft die von dir gewählten Verbindungen auf der TCDD-Website immer wieder. Sobald
jemand storniert, wählt er den Platz aus, löst die zeitlich begrenzte Reservierung von
TCDD aus und schlägt so lange Alarm, bis du am Rechner bist.

Funktioniert im gesamten Netz, nicht nur auf einer Strecke: 460 Bahnhöfe, beide
Richtungen, YHT, Anahat und Bölgesel. Welche Wagenklassen es gibt, liest er direkt von der
jeweiligen Verbindung ab. Nichts davon steht fest im Code.

## Installation

Du brauchst keine Programmierkenntnisse. Eine Zeile genügt.

**macOS und Linux** (Terminal):
```bash
curl -fsSL https://raw.githubusercontent.com/Coflazo/TCDD-Koltuk-Bul/main/install.sh | bash
```

**Windows** (PowerShell):
```powershell
irm https://raw.githubusercontent.com/Coflazo/TCDD-Koltuk-Bul/main/install.ps1 | iex
```

Wohin installiert wird: Startest du es auf dem Desktop, legt es dort einen Ordner an. Bist
du bereits in einem Ordner unterhalb des Desktops, bleibt es dort. Von überall sonst geht
es zum Desktop. Danach gibt es eine Datei zum Doppelklicken: **Başlat.command** (macOS,
Linux) oder **Baslat.bat** (Windows).

## Bedienung

1. Start und Ziel eingeben. Türkische Sonderzeichen sind nicht nötig, Tippfehler kein
   Problem: `sogutlucesme` findet SÖĞÜTLÜÇEŞME, `ankra` schlägt ANKARA vor.
2. Datum, oder mehrere. Wenn du flexibel bist, tippe `17 18 21` und alle drei werden
   überwacht.
3. Alle Züge dieser Tage erscheinen mit Preisen und freien Plätzen je Klasse.
4. Wähle die Züge und die Klassen, die für dich infrage kommen.
5. Den Rest macht er allein. Er hält den Platz und weckt dich. Bezahlen musst du selbst.

## Wichtig

- Nur für den privaten Gebrauch. Ein Reisender, ein Platz. Nicht zum Weiterverkauf.
- Die Zahlung wird nie automatisiert. Kartendaten werden nie gelesen, gespeichert oder
  eingegeben.
- Rollstuhlplätze werden standardmäßig nicht überwacht, nur wenn du sie ausdrücklich
  auswählst. Sie sind für Reisende da, die keinen anderen Platz nutzen können.
- Deine Daten bleiben auf deinem Rechner.
- Für die Einhaltung der Nutzungsbedingungen von TCDD bist du selbst verantwortlich.

Vollständige Doku: [README](../../README.md) &nbsp;·&nbsp; [DISCLAIMER](../../DISCLAIMER.md)
