# Dört bağımsız konsey — nasıl farklılar

Kaynak: manifesto §11–§15, §19. Konsey görüşleri **simülasyondur**; gerçek izleyici verisi değildir (Anayasa 7). Her konsey üyesinin tahmini yayımlanan içeriğin gerçek sonucuyla karşılaştırılır ve `konseyler/kalibrasyon.csv`'ye yazılır.

| Konsey | Sorduğu ana soru | Bilgi kaynağı | Yanılma eğilimi (kör nokta) |
|---|---|---|---|
| **Uzman** | "Bilimsel/teknik/ticari olarak neden işe yarar ya da yaramaz?" | Akademik çalışma, sektör raporu, veri | Açıklanabilir olanı başarılı sanmak |
| **Creator** | "Sahada bu bugün hâlâ çalışıyor mu, bizim ölçeğimize uyar mı?" | Creator'ların kamuya açık, kaynaklı yöntemleri | Ünlüye özgü başarıyı genellemek |
| **Tüketici** | "Akışta bunu görsem durur muyum, gönderir miyim, takip eder miyim?" | Davranış profilleri (simülasyon) | Kendi söylediğini gerçek davranış sanmak |
| **Muhalefet** | "Bu neden başarısız olur, neyi görmezden geliyoruz, daha ucuz yolu var mı?" | Karşı kanıt, başarısız örnekler, maliyet | Her şeye hayır demek (bu yüzden alternatif zorunlu) |

## Ortak çalışma kuralları
1. **Bağımsızlık:** Her konsey ayrı bir alt ajan bağlamında, yalnızca fikir dosyasını ve kendi KONSEY.md dosyasını görerek değerlendirir. Diğer konseylerin görüşü, kreatifin coşkusu veya Chief of Staff'ın tercihi verilmez.
2. **Bölümler içinde bağımsızlık:** Konsey içindeki her profil kendi bölümünü diğerlerini okumadan yazar gibi yazılır; "katılıyorum" cümlesi yasak, her profil kendi gerekçesini verir.
3. **Puan + gerekçe + kanıt türü:** her profil İçerik Puanlama tablosunda (bkz. medya-mahkemesi/MAHKEME.md) kendi alanına giren kriterlere 0–10 verir, kanıt türünü yazar: `kaynaklı` / `tecrübe-kaynaklı` / `sezgi`.
4. **Gerçek kişi taklidi yok:** Creator profilleri "X şöyle düşünürdü" demez; "X'in kamuya açık yöntemi (kaynak) şunu önerir" der.
5. **Muhalefet her eleştiride:** sorun · kanıt · olası sonuç · alternatif · düşük maliyetli doğrulama yolu.
6. **Maliyet:** Tek mahkemede 4 konsey alt ajanı (bağımsızlık için ayrı) + 1 finans/Bekçi birleşik değerlendirmesi. Profiller tek tek ayrı ajan olarak çağrılmaz.

## Çıktı biçimi (her konsey aynı)
```
KONSEY: <ad>      FİKİR: <dosya>      TARİH:
| Profil | Kriter | Puan (0-10) | Gerekçe (1-2 cümle) | Kanıt türü |
EN GÜÇLÜ YÖN:
EN BÜYÜK RİSK:
KONSEY ÖNERİSİ: deney adayı / geliştir / düşük öncelik / reddet (gerekçe)
AZINLIK GÖRÜŞÜ: (varsa — çoğunluktan farklı düşünen profil)
TAHMİN (kalibrasyon için): 72 saatte medyan izlenmeye göre beklenti: altında / benzer / üstünde
```
