# TCDD Koltuk Bul

**Dolu Türkiyə qatarlarında boşalan yeri anında tutan bot.**

TCDD saytında seçdiyin səfərləri dayanmadan yoxlayır. Kimsə biletini ləğv edən kimi yeri
seçir, TCDD-nin öz müvəqqəti rezervasiyasını başladır və sən kompüterin yanına gələnə qədər
səsli xəbərdarlıq verir.

Bütün şəbəkədə işləyir, tək bir xətdə yox: 460 stansiya, hər iki istiqamətdə, YHT, Anahat
və Bölgesel. Hansı vaqon siniflərinin olduğunu isə həmin səfərin özündən oxuyur, kodda
yazılmış siyahı yoxdur.

## Quraşdırma

Proqramlaşdırma bilməyə ehtiyac yoxdur. Bir sətir bəsdir.

**macOS / Linux:**
```bash
curl -fsSL https://raw.githubusercontent.com/Coflazo/TCDD-Koltuk-Bul/main/install.sh | bash
```

**Windows (PowerShell):**
```powershell
irm https://raw.githubusercontent.com/Coflazo/TCDD-Koltuk-Bul/main/install.ps1 | iex
```

Hara quraşdırılır: masaüstündəsənsə orada qovluq yaradır. Artıq masaüstünün altındakı bir
qovluqdasansa elə orada quraşdırılır. Başqa yerdənsə masaüstünə keçir. Sonda iki dəfə
klikləyəcəyin bir fayl qalır: **Başlat.command** (macOS, Linux) və ya **Baslat.bat**
(Windows).

## İstifadə

1. Haradan haraya getdiyini yaz. Türk hərfləri vacib deyil, yazı səhvi də problem deyil:
   `sogutlucesme` yazsan SÖĞÜTLÜÇEŞME tapır, `ankra` yazsan ANKARA təklif edir.
2. Hansı gün və ya günlər. Çevikliyin varsa `17 18 21` yaz, üçünü birdən izləyir.
3. Həmin günlərin bütün qatarlarını qiymətləri və sinif üzrə boş yer sayı ilə göstərir.
4. Həqiqətən minəcəyin qatarları və sinifləri seç.
5. Qalanını özü edir. Yeri tutur və səni oyadır. Ödənişi sən edirsən.

## Vacib

- Yalnız şəxsi istifadə üçündür. Bir sərnişin, bir yer. Satmaq üçün deyil.
- Ödəniş heç vaxt avtomatlaşdırılmır. Kart məlumatlarını oxumur, saxlamır, yazmır.
- Əlil arabası yerləri standart olaraq izlənmir, yalnız sən açıq şəkildə seçsən. O yerlər
  başqa yerdə səyahət edə bilməyən sərnişinlər üçündür.
- Məlumatların öz kompüterində qalır.
- TCDD-nin istifadə şərtlərinə əməl etmək sənin məsuliyyətindir.

Tam sənədləşmə: [README](../../README.md) &nbsp;·&nbsp; [DISCLAIMER](../../DISCLAIMER.md)
