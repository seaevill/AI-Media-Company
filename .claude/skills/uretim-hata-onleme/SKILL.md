---
name: uretim-hata-onleme
description: AI video modellerinin bilinen hatalarını (iç içe geçme, kaybolma–belirme, nesne çoğalması, morf, yüzen nesne, kapı/menteşe süpürmesi, ince esnek nesne kopması, prop tutma/bırakma, yön/yürüyüş, dönüşte kimlik kayması, karanlık/küçük kilit an, istenmeyen yazı/rakam) ÜRETİMDEN ÖNCE çekim tasarımıyla önler. Bir senaryo/storyboard çekimlere bölünüp prompt yazılmadan, kredi tahmini istenmeden ya da bir konsept ikinci kez başarısız olduktan sonra kullan. Kalite kontrol (üretilmiş klip) için değil: o `animasyon-kalite-kontrol`.
---
# Üretim hata önleme — v1, 2026-11-27 (G-0042). HİPOTEZ: üretimle test edilmedi.

## 1. Ne zaman
Senaryo → çekim listesi aşamasında, ücretsiz hazırlıkta. Prompt, kredi tahmini ve Bora'ya "max N kredi" talebinden ÖNCE. Aynı konsept 2. kez başarısızsa durmadan önce de.

## 2. Girdiler (yoksa DUR)
Senaryo/storyboard metni · karakter ve prop listesi · hedef süre ve model · Bora'nın onayladığı referans görünüm (CLAUDE.md kural 5).

## 3. Gerekli kaynaklar
`produksiyon/basarisiz-uretimler/README.md` (7 gerçek hata) · `hafiza/OGRENILEN-DERSLER.md` · `takimlar/produksiyon/takim.md` · `istihbarat/kaynaklar/2026-11-27-mesleki-yontemler.md` (en sondaki "G-0042 ek" bölümü: kaynaklı yöntemler).

## 4. Araçlar
Yalnızca okuma/yazma. Üretim, `estimate_*` dahil kredi araçları bu beceride çağrılmaz. Çıktı sonrası maliyet adımı `produksiyon-maliyet` takımında.

## 5. Adım adım yöntem
1. **Senaryo → çekim listesi.** Her çekim: TEK eylem, TEK karakter hareketi, sabit kamera, ≤ 4–5 sn. Kimin nereye gideceği (ekran yönü) yazılır. Gerçek temas gerektiren an ayrı çekim ya da kesme olur.
2. **Her çekim için risk tablosu** (14 sınıf, her satır D/O/Y = düşük/orta/yüksek + 1 cümle gerekçe):
   iç içe geçme (iki gövde 1 gövde boyundan yakın/yol kesişir) · kaybolma–belirme (prop çıkıp girer) · nesne çoğalması · morf · yüzen nesne (zemin/destek temasız) · kapı/menteşe süpürmesi (yay içinde karakter) · ince esnek nesne (şerit, ip, kumaş koparsa/uçarsa) · prop tutma/bırakma (el–nesne geçişi) · yön/yürüyüş · dönüşte tutarlılık (≥ 90° dönüş) · karanlık/küçük kilit an (< kadrajın 1/6'sı ya da ışık düşük) · istenmeyen yazı/rakam (saat, etiket, tabela) · kamera talimatı uygulanmaz riski · karakter sayısı ≥ 3.
3. **Yeniden tasarım kalıpları:** iki karakteri ayrı çekimlere böl, temas anını kesmeyle (cut on action) ya da kadraj dışı/sesle ver · kapıyı kapalı/açık iki ayrı kare yap, açılma anını gösterme · ince esnek nesneyi sabit/ kadraj dışı/ ayrı insert yap · prop'u elde başlat, elde bitir, geçişi kesmeyle ver · dönüşü yapma, iki ayrı açıdan kesmeyle ver · kilit anı yakın plan ve aydınlık ayrı çekim yap · saat/etiket/tabela yazısını prompta yazma, "boş", kurguda ekle (prompt'ta "no text" tek başına yetmez) · ilk kare (image-to-video) ve gerekirse son kare ile iki uç sabitle · sahne yönü, "bu çekimde X kadrajda yok" ve "yalnızca N karakter var" kilitlerini prompta yaz · ses/şaka zamanlaması montajda, modele bırakılmaz.
4. Yeniden yazılan çekimler için tabloyu tekrar doldur. En fazla 2 tur; hâlâ Y varsa 6. maddeye bak.

## 6. Karar kriterleri
"Çekimi yeniden yaz" (üretime gitmez): herhangi bir satır **Y** ise · iki karakter yolu aynı çekimde kesişiyorsa · menteşeli nesne yayında karakter varsa · ince nesne kopup/uçup devam ediyorsa · bir çekimde ≥ 2 olay ya da ≥ 3 karakter hareketi · kilit an küçük/karanlık ve ayrı çekim yapılamıyorsa. **O** satırlar: üretimde tam çözünürlük ek inceleme notu. Tüm satırlar D ise çekim "üretime hazır" (başarı garantisi değil).

## 7. İyi örnek (TAHMİN, üretilmedi)
Kapı v3: Çekim 1 kapalı kapı, kaz kadrajda tek, "sola bakar"; Çekim 2 vombat kapalı kapıya yaslı, tek karakter; Çekim 3 kapı zaten açık, ikisi aynı yönde yan yana (kapı hareketi gösterilmez). Hiçbir çekimde menteşe yayı ve iki yol kesişimi yok.

## 8. Kötü örnek (bizim gerçek hatalarımız)
- **kapi_v1:** tek 8 sn'de kapı + 2 karakter, yollar kesişti → vombat kazın içinden geçti (iç içe geçme; Bora yakaladı).
- **kapiA:** "kaz duvara gider" dendi, kapıya çekildi → sahne yönü kilidi yoktu. **kapiB:** kapı menteşesi tutarsız (yayda karakter vardı).
- **mini/flash:** 3 karakter + ince metre + koli kayması + kamera talimatı tek klipte → koli süzüldü, metre yok oldu, dönüşte morf.
- **hailuo:** aynı sahne ucuz modelde → koli çoğaldı, flamingo deforme, ses yok. Ders: sorun model fiyatı değil, tasarımdı.

## 9. Doğrulama
Her çekimin tablosu tamam ve kriter 6'ya göre karar yazılı mı? Her risk satırının gerekçesi bir çekim tasarımı değişikliğine ya da "D" kanıtına bağlı mı? Tasarımı Bekçi (üreten ekip kendi işini denetlemiş sayılmaz) ve sonunda Bora gözden geçirir. Bu bir tahmindir: gerçek sınav üretilen klip + `animasyon-kalite-kontrol` + Bora'nın izlemesi.

## 10. Çıktı formatı
```
SENARYO: <ad>  ÇEKİM SAYISI: <n>  TOPLAM SÜRE: <sn>
ÇEKİM <no> (<sn>, <kamera>): <tek eylem>
  riskler: <sınıf=D/O/Y — gerekçe> ...   KARAR: HAZIR | YENİDEN YAZ (<neden>)
MONTAJLA VERİLENLER: <temas, zamanlama, yazı, şaka sesi>
SONRA: Bora referans onayı → max N kredi talebi (bu beceri kredi harcamaz)
SKILL: uretim-hata-onleme v1
```

## 11. Durma koşulları
Girdi eksik (referans görünüm onayı, süre, model) · bir çekim 2 turda hâlâ Y · aynı konsept zaten 2 kez başarısız (kural 5: durulur, Bora'ya sorulur) · hikâye temas gerektiriyor ve kesmeyle verilemiyor (senaryo değişikliği Bora/kreatif-direktor kararı) · kredi/üretim aracı çağırma gereği doğarsa.

## 12. Ders kaydı
Üretimden sonra gerçekleşen hata tasarım tablosunda D/O yazdıysa tek satır `takimlar/produksiyon/defter.md`'ye (ders, olay değil) ve kaçan sınıf bu beceriye eklenmek üzere Chief'e bildirilir. Kaynaklar ve yöntem ayrıntıları: `istihbarat/kaynaklar/2026-11-27-mesleki-yontemler.md` "G-0042 ek".
