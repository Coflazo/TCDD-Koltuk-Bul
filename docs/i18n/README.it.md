# TCDD Koltuk Bul

**Un bot che intercetta i posti che si liberano sui treni turchi esauriti e li blocca subito.**

Controlla in continuazione i treni che hai scelto sul sito TCDD. Appena qualcuno disdice,
seleziona il posto, avvia la prenotazione temporanea di TCDD e suona la sveglia finché non
arrivi al computer.

Funziona su tutta la rete, non su una sola linea: 460 stazioni, in entrambe le direzioni,
YHT, Anahat e Bölgesel. Quali classi ci sono le legge dal treno stesso. Niente di tutto
questo è scritto fisso nel codice.

## Installazione

Non serve saper programmare. Basta una riga.

**macOS / Linux:**
```bash
curl -fsSL https://raw.githubusercontent.com/Coflazo/TCDD-Koltuk-Bul/main/install.sh | bash
```

**Windows (PowerShell):**
```powershell
irm https://raw.githubusercontent.com/Coflazo/TCDD-Koltuk-Bul/main/install.ps1 | iex
```

Dove si installa: se lo lanci dal desktop, crea lì una cartella. Se sei già in una cartella
sotto il desktop, si installa dove sei. Da qualunque altro punto va sul desktop. Alla fine
resta un file su cui fare doppio clic: **Başlat.command** (macOS, Linux) o **Baslat.bat**
(Windows).

## Come si usa

1. Scrivi da dove a dove. I caratteri turchi non servono e gli errori di battitura non sono
   un problema: `sogutlucesme` trova SÖĞÜTLÜÇEŞME, e con `ankra` ti propone ANKARA.
2. Quale giorno, o giorni. Se sei flessibile scrivi `17 18 21` e li tiene d'occhio tutti e tre.
3. Ti mostra tutti i treni di quei giorni con prezzi e posti liberi per classe.
4. Scegli i treni e le classi su cui viaggeresti davvero.
5. Al resto pensa lui. Blocca il posto e ti sveglia. Il pagamento lo fai tu.

## Importante

- Solo per uso personale. Un viaggiatore, un posto. Non per rivendita.
- Il pagamento non viene mai automatizzato. Non legge, non salva e non digita i dati della
  carta.
- I posti per sedia a rotelle non sono monitorati per impostazione predefinita, solo se li
  selezioni esplicitamente. Esistono per viaggiatori che non possono usare nessun altro posto.
- I tuoi dati restano sul tuo computer.
- Rispettare le condizioni d'uso di TCDD è responsabilità tua.

Documentazione completa: [README](../../README.md) &nbsp;·&nbsp; [DISCLAIMER](../../DISCLAIMER.md)
