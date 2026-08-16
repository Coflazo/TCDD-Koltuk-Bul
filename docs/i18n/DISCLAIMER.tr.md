# Kullanım Koşulları, Sınırlar ve Sorumluluk Reddi

**Bu bir hukuki tavsiye değildir.**

Avukat değilim. Burada yazanların hiçbiri, bu yazılımı kullanmanın Türkiye'de ya da başka
bir yerde hukuka uygun olduğunun garantisi değildir. Bu belge yalnızca aracın ne yaptığını,
neyi bilerek yapmadığını ve sorumluluğun kimde olduğunu anlatır. Kendi kullanımının caiz
olup olmadığına karar vermek sana aittir.

---

## 1. Bu nedir

TCDD Koltuk Bul, `ebilet.tcddtasimacilik.gov.tr` üzerindeki herkese açık sefer sayfalarını
belirli aralıklarla kontrol eden, boş koltuk çıktığında kullanıcıyı uyaran ve TCDD'nin
kendi geçici rezervasyonunu başlatan kişisel bir araçtır. Bir insanın kendi tarayıcısında
yaptığı tıklamaların aynısını yapar.

## 2. Bilerek yapmadıkları

- **Ödeme yapmaz.** Ödeme adımında durur. Kart bilgilerini görmez, saklamaz, iletmez, yazmaz.
- **Hiçbir korumayı aşmaz.** Captcha çözmez, giriş atlamaz, ödeme atlamaz. Çıkış yapmış bir
  ziyaretçinin göremeyeceği hiçbir şeye erişmez.
- **Toplu rezervasyon yapmaz.** Tam olarak bir koltuk tutar. Çok yolculu mod yoktur, bu
  bilerek böyledir.
- **Sunucuyu yormaz.** Tek tarayıcı, 45 ila 90 saniyede bir kontrol, rastgele aralıklarla.
  Yük testi değildir ve öyle bir şeye çevrilmemelidir.
- **Veri toplamaz.** Okuduğu hiçbir veri bir yere yüklenmez, yayımlanmaz, satılmaz.

## 3. Ticari kullanım ve karaborsa

Bu araç ticari amaçla, bilet karaborsacılığı için veya başkasına satmak üzere yer tutma
amacıyla kullanılamaz. Biletlerin yetkisiz şekilde yeniden satılmasının Türkiye'de hukuki
sonuçları olabilir. Niyetin buysa bu yazılımı kullanma.

## 4. Engelli koltukları

Tekerlekli sandalye koltukları varsayılan olarak hariç tutulur ve yalnızca kullanıcı açıkça
seçerse izlenir. O koltuklar başka hiçbir koltukta seyahat edemeyen yolcular içindir.
İhtiyacın yokken birini almak, ihtiyacı olandan almak demektir.

## 5. Kişisel veri (KVKK)

Yazılım yalnızca senin yazdıklarını, kendi bilgisayarında saklar:

| Ne | Nerede |
|---|---|
| Seçtiğin istasyonlar ve bay/bayan | `~/.koltukbul.json` |
| Tarayıcı oturumu ve çerezler | `~/.koltukbul_profile` |
| Varsa hata ekran görüntüleri | `debug/` |

Kimlik numarası, ad, soyad, telefon veya kart bilgisi bu yazılım tarafından hiçbir zaman
okunmaz, saklanmaz veya iletilmez. Bunları açık bıraktığı tarayıcı penceresine kendin,
doğrudan TCDD'ye girersin. Sunucu tarafı, telemetri veya analitik yoktur.

## 6. TCDD'nin kullanım şartları

TCDD Taşımacılık A.Ş.'nin yayımladığı kullanım koşullarını okumak ve bunlara uymak
kullanıcının sorumluluğundadır. O koşullar TCDD tarafından belirlenir, her an değişebilir
ve burada yazan her şeyin üstündedir. Senin durumun için otomatik erişime izin verilmiyorsa
bu yazılımı kullanma.

## 7. Bağımsızlık

Bu proje resmî olmayan, bağımsız ve kişisel bir çalışmadır. TCDD Taşımacılık A.Ş. ile veya
iştirakleriyle hiçbir bağlantısı yoktur, onlar tarafından desteklenmez. "TCDD" adı yalnızca
yazılımın hangi siteyi okuduğunu belirtmek için geçer. Hiçbir marka veya logo kullanılmaz.

## 8. Garanti yok

"Olduğu gibi" sunulur, hiçbir garanti verilmez. Kaçırılan trenler, düşen rezervasyonlar,
harcanan para, sitenin değişmesiyle bozulması veya çalıştırılmasının başka herhangi bir
sonucu için sorumluluk kabul edilmez. TCDD sayfalarını değiştirdiğinde bozulacaktır.

## 9. Sorumluluk

Bu yazılımı çalıştıran kişi, kendi kullanımından tamamen kendisi sorumludur. Emin
değilsen, kendi ülkendeki yetkin bir avukata danış.
