---
name: animasyon-kalite-kontrol
description: AI ile üretilmiş kısa animasyon/videoda yayın engelleyen görsel hataları kare kare bulur (iç içe geçme, kaybolma–belirme, nesne çoğalması, morf, yüzen nesne, kapı/menteşe süpürme çakışması, okunmayan kilit an, istenmeyen yazı, ses kanalı yok). Bir video yayın/teslim öncesi denetlenecekse ya da "kalite kontrol", "VIU", "hata var mı" dendiğinde kullan.
---
# Animasyon kalite kontrol (VIU-2 operasyonel beceri) — v1, 2026-11-27

## Ne zaman
Kendi ürettiğimiz her video klip; Bora'ya "izle" diye gönderilmeden ÖNCE. Pazar videoları için değil (o: `viral-video-analizi`).

## Girdiler (yoksa DUR)
1. Yerel MP4 yolu. 2. Amaçlanan sahne: karakterler, eylemler, beklenen zamanlar. 3. Scratch klasörü (kareler buraya; repoya medya yazılmaz).

## Araçlar
`ffprobe` · `python3 -I scripts/video_qc.py <mp4> --cikti <scratch>/viu --fps 8` · `ffmpeg` kırpma/büyütme · Read (kareleri açmak için). **Ses dinlenemez** — her raporda bunu yaz.

## Yöntem (sırayla, atlama)
1. **Teknik:** ffprobe → 9:16 mi, süre, ses kanalı var mı. Sesli içerikte ses kanalı yoksa → ENGEL.
2. **VIU-1:** video_qc.py → ani değişim anları, karanlık uyarısı. Bunlar yalnızca ipucudur; **kademeli hataları (iç içe geçme) yakalamaz** (kanıt: kapi_v1, `denetim/viu/kalibrasyon.csv`).
3. **Olay haritası:** amaçlanan sahneden ve 8 kare/sn genel tablodan şu anları listele: iki karakterin 1 karakter genişliğinden fazla yaklaştığı an · elle nesne tutma/bırakma · kapı/kapak/battaniye gibi büyük nesnenin hareketi · düşme/kayma · yeni nesnenin girişi.
4. **Her olay için yakın inceleme:** ±1 sn, **12 kare/sn, tam çözünürlük, gerekirse 2× kırpma**:
   `ffmpeg -v error -y -ss <t-1> -t 2 -i <mp4> -vf "fps=12,crop=<w>:<h>:<x>:<y>,scale=360:-2,tile=6x4" -frames:v 1 <scratch>/olay_<t>.png` → Read ile AÇ.
   Üç geçiş yap:
   a. **Sayım:** her karede karakter, uzuv ve prop sayısı (koli, damga, metre, çanta). Sayı değişiyorsa → kaybolma/çoğalma.
   b. **Derinlik:** kim kimin önünde olmalı (sahnedeki konuma göre)? Görülen sıra fiziğe aykırıysa → iç içe geçme/ters derinlik.
   c. **Temas ve destek:** nesne zemine/yüzeye değiyor mu, gölge var mı? Değmeden hareket → yüzme.
5. **Menteşeli/dönen nesne kuralı:** ilk ve son karede menteşe tarafını belirle; açılma yayını çiz; **yayın içinde duran her karakter/nesne çarpışmalıdır** — çarpışma görünmüyorsa "kanat arkasından geçiyor" = fizik hatası (kanıt: kapiB, B1).
6. **Okunurluk:** şakanın/hikâyenin kilit anı kadrajın en az ~1/6 yüksekliğinde ve yeterince aydınlık mı? video_qc ortalama parlaklık < 45/255 ise kilit anı ayrıca kırpıp kontrol et (kanıt: tikirti, T1). Eşikler HİPOTEZ.
7. **Yazı/rakam:** saat, tabela, etiket — istenmemişse ve beliriyorsa/değişiyorsa → hata (kanıt: tikirti, T2).
8. **Niyet:** amaçlanan her eylem gerçekleşti mi? Gerçekleşmeyen ana eylem → ENGEL (kanıt: hailuo H3).

## Karar kriterleri
- **YAYIN ENGELİ VAR:** iç içe geçme · kaybolma–belirme · nesne çoğalması · morf · gövde/uzuv kaybı · yüzen nesne · menteşe yayı çakışması · ana eylem yok · kilit an okunmuyor · gerekli ses yok.
- **BELİRSİZ:** yalnızca 8 kare/sn'de şüphe var ve 12 kare/sn yakın inceleme yapılamadı. (Belirsiz = yayınlanmaz.)
- **YOK:** tüm olaylar 12 kare/sn incelendi ve hiçbir kriter tetiklenmedi. Yine de **Bora izlemeden yayın kalitesi denmez**.

## Bilinen model zaafları (iç deney kanıtı, 2026-11-27, Seedance 2.0 Mini / 2.5 Flash / Hailuo 2.3-fast)
Tek kadrajda 3 karakter + zincir eylem · ince esnek nesne (şerit metre) · kayma/yerçekimi · kapı ve menteşe · iki karakterin yolunun kesişmesi · küçük ayrıntıya dayalı şaka · karanlık sahne · prop tutma/bırakma. Kaynak: `produksiyon/basarisiz-uretimler/README.md`, `denetim/viu/2026-11-27-denetci-{A,B}.md`.

## Örnek — iyi çıktı (gerçek)
`[kapi] [4.3–4.6 sn] [ters derinlik] kapı kanadı dışa açılırken kanadın kenarı kazın gözünün önünden geçiyor, 4.6 sn'de kaz yüzü kanadın arkasında; kaz holde olduğu için kanadın önünde olmalıydı [güven: yüksek] [kare: olay_4.3.png]` (VIU Denetçi B, 12 kare/sn kırpma).
## Örnek — kötü çıktı (gerçek, bizim hatamız)
"Kapı: yapı ekranda eksiksiz; vombat kazın önüne geçip onu kısmen kapatıyor." — 2 kare/sn, 160 px döşemeden yazıldı; iç içe geçmeyi "önünde durma" sandı (Chief of Staff, G-0026). Neden kötü: olay anı yakın incelenmedi, derinlik fiziğe göre sorgulanmadı.

## Doğrulama
Her bulgu: zaman aralığı + kare dosyası + tür + güven. İkinci bağımsız denetçi aynı videoyu ayrı bağlamda inceler; ayrışan videolar BELİRSİZ. Son hakem Bora (VIU-3).

## Çıktı formatı
```
VİDEO: <ad>  KARAR: YAYIN ENGELİ VAR | YOK | BELİRSİZ
TEKNİK: <ffprobe özeti>  SES: dinlenmedi
OLAYLAR İNCELENDİ: <liste, her biri fps/çözünürlük>
HATALAR:
- [başlangıç–bitiş sn] [tür] [tanım] [güven] [kare dosyası]
NİYET: <gerçekleşen / gerçekleşmeyen eylemler>
MONTAJLA ÇÖZÜLEBİLİR: <…>   MODEL KAPASİTESİ ÜSTÜNDE: <…>
SKILL: animasyon-kalite-kontrol v1
```

## Durma koşulları
Video yok/açılmıyor · ffmpeg yok · kareleri Read ile açamıyorsun → "BLOCKED: <neden>" yaz, tahminle karar verme.

## Ders kaydı
Bora'nın ya da diğer denetçinin bulup senin kaçırdığın her hata → `denetim/viu/kalibrasyon.csv`'ye bir satır; aynı türden 2. kaçırmada bu dosyanın "Yöntem" bölümüne kural önerisi (Bora onayıyla).
