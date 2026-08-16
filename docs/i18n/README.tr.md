# TCDD Koltuk Bul

**Boş koltuk çıkınca saniyesinde yakalayıp yerini rezerve eden bot.**

TCDD e-bilet sitesinde istediğin seferleri sürekli kontrol eder. Biri biletini iptal edip
yer açıldığında koltuğu seçer, TCDD'nin kendi geçici rezervasyonunu başlatır ve sen
bilgisayara gelene kadar sesli alarm çalar.

Tüm ağda çalışır, tek bir hat için değil: 460 istasyon, her iki yön, YHT, Anahat ve
Bölgesel. Hangi vagon sınıflarının olduğunu da o seferden okur, koda yazılmış bir liste
yoktur.

## Kurulum

Programlama bilmene gerek yok. Tek satır yeter.

**macOS ve Linux** (Terminal):
```bash
curl -fsSL https://raw.githubusercontent.com/Coflazo/TCDD-Koltuk-Bul/main/install.sh | bash
```

**Windows** (PowerShell):
```powershell
irm https://raw.githubusercontent.com/Coflazo/TCDD-Koltuk-Bul/main/install.ps1 | iex
```

Nereye kurulur: Masaüstündeysen orada bir klasör açar. Zaten masaüstü altındaki bir
klasördeysen oraya kurar. Başka bir yerdeysen masaüstüne gider ve klasörü orada açar.
Bitince çift tıklayacağın bir dosya bırakır: **Başlat.command** (macOS, Linux) veya
**Baslat.bat** (Windows).

## Kullanım

1. Nereden nereye gideceğini yaz. Türkçe karakter şart değil, yazım hatası da sorun değil:
   `sogutlucesme` yazsan bulur, `ankra` yazsan "did you mean ankara?" der.
2. Hangi gün ya da günler. Esnekesen `17 18 21` yaz, üçünü birden izler.
3. O günlerin bütün seferlerini fiyatlarıyla ve boş koltuk sayılarıyla listeler.
4. Hangi trenleri ve hangi sınıfları kabul ettiğini seç.
5. Gerisini o halleder. Yer çıkınca tutar ve alarm çalar. Ödemeyi sen yaparsın.

## Önemli

- Kişisel kullanım içindir. Tek yolcu, tek koltuk. Satmak için değildir.
- Ödemeyi asla otomatik yapmaz. Kart bilgilerini görmez, saklamaz, yazmaz.
- Tekerlekli sandalye koltukları varsayılan olarak izlenmez. Sadece sen açıkça seçersen
  bakar. O koltuklar başka koltukta seyahat edemeyen yolcular içindir.
- Verilerin senin bilgisayarında kalır, hiçbir yere gönderilmez.
- TCDD'nin kullanım koşullarını okumak ve uymak senin sorumluluğundadır.

Tam dokümantasyon: [README](../../README.md) &nbsp;·&nbsp; [DISCLAIMER](../../DISCLAIMER.md)
