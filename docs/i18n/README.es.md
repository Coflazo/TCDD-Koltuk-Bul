# TCDD Koltuk Bul

**Un bot que caza los asientos que se liberan en trenes turcos agotados y los reserva al instante.**

Comprueba una y otra vez los trenes que elijas en la web de TCDD. En cuanto alguien
cancela, selecciona el asiento, activa la reserva temporal de TCDD y hace sonar una alarma
hasta que llegues al ordenador.

Funciona en toda la red, no en una sola línea: 460 estaciones, en ambos sentidos, YHT,
Anahat y Bölgesel. Las clases disponibles las lee del propio tren. Nada de eso está fijado
en el código.

## Instalación

No hace falta saber programar. Basta con una línea.

**macOS y Linux** (Terminal):
```bash
curl -fsSL https://raw.githubusercontent.com/Coflazo/TCDD-Koltuk-Bul/main/install.sh | bash
```

**Windows** (PowerShell):
```powershell
irm https://raw.githubusercontent.com/Coflazo/TCDD-Koltuk-Bul/main/install.ps1 | iex
```

Dónde se instala: si lo lanzas en el escritorio, crea allí una carpeta. Si ya estás en una
carpeta dentro del escritorio, se instala ahí mismo. Desde cualquier otro sitio, va al
escritorio. Al terminar deja un archivo para hacer doble clic: **Başlat.command** (macOS,
Linux) o **Baslat.bat** (Windows).

## Uso

1. Escribe origen y destino. Los caracteres turcos son opcionales y las erratas no
   importan: `sogutlucesme` encuentra SÖĞÜTLÜÇEŞME, y con `ankra` te sugiere ANKARA.
2. Qué día, o días. Si tienes flexibilidad, escribe `17 18 21` y vigilará los tres.
3. Te muestra todos los trenes de esos días con precios y plazas libres por clase.
4. Elige los trenes y las clases en las que de verdad viajarías.
5. Del resto se encarga él. Retiene la plaza y te despierta. El pago lo haces tú.

## Importante

- Solo para uso personal. Un viajero, una plaza. No para reventa.
- El pago nunca se automatiza. Nunca lee, guarda ni escribe datos de tarjeta.
- Las plazas para silla de ruedas no se vigilan por defecto, solo si las seleccionas
  expresamente. Existen para viajeros que no pueden usar ninguna otra plaza.
- Tus datos se quedan en tu ordenador.
- Cumplir las condiciones de uso de TCDD es responsabilidad tuya.

Documentación completa: [README](../../README.md) &nbsp;·&nbsp; [DISCLAIMER](../../DISCLAIMER.md)
