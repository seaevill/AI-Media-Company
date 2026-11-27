---
name: viral-video-analizi
description: Pazardaki bir videonun neden izlendiğini/paylaşıldığını analiz eder (ilk 2 sn kanca, sahne geçişleri, ses, karakter davranışı, sürpriz, paylaşılma hipotezi) — GÖZLEM, ÖLÇÜM ve ÇIKARIM ayrı. Ancak videonun görüntüsüne/sesine gerçekten erişilebiliyorsa kullan; erişim yoksa BLOCKED raporu verir.
---
# Viral video analizi v1, 2026-11-27 — şu an BLOCKED

## Ne zaman
Rakip/pazar videosunun çalışma prensibi çıkarılacaksa. Şema ve 12 görev: `denetim/VIU-METODOLOJI.md` (tekrar yazılmaz).

## Girdiler ve ön koşul (yoksa DUR)
Videonun **kendisi**: (a) Bora'nın yerelde kaydettiği MP4, ya da (b) resmî Gemini API ile herkese açık YouTube URL'si (anahtar gerekli — henüz yok), ya da (c) transkript (Bora'dan).
Erişim durumu 2026-11-27: YouTube izleme sayfası CAPTCHA'ya yönleniyor (G-0009); i.ytimg.com küçük resimleri 403; TikTok video başına veri yok; Instagram 403. → **Görüntü/ses analizi yapılamaz.**

## İzin verilen yedek (açıkça etiketli)
Yalnızca META analizi: başlık, süre, izlenme (hesap_olc.py ile), yayın sırası. Çıktının başında "BU BİR VİDEO ANALİZİ DEĞİLDİR — yalnızca meta veri" yazılır. Kanca, mizah, karakter davranışı hakkında hiçbir GÖZLEM yazılmaz.

## Yöntem (erişim açıldığında)
1. Önbellek: `denetim/viu/analiz-kaydi.json` — varsa yeniden analiz yok.
2. Video yerelse: `scripts/video_qc.py` (kesme sayısı, süre, ses) + 0–2 sn 12 kare/sn tablo + her kesme anı.
3. Gemini (onaylanınca): VIU-METODOLOJI şeması `responseSchema` olarak; düşük çözünürlük genel, kilit anlar kırpılmış yüksek fps.
4. Doğrulama: Gemini'nin verdiği 3 zaman damgasında kare çıkarıp gözlemi karşılaştır (yerel video varsa).
5. Her alan GÖZLEM / ÖLÇÜM / ÇIKARIM etiketli; özel metrik (retention, paylaşım) yazılmaz.

## Karar kriterleri
Bir prensip "çıkarıldı" sayılır ancak en az 2 farklı hesaptan, video içi gözlemle desteklenmişse; tek videodan çıkan prensip HİPOTEZ.

## Örnek — kötü (gerçek)
29 hesap kartının "paylaşılma hipotezi" alanları videolar izlenmeden, haber metinlerinden yazıldı (G-0006). Neden kötü: gözlem yok, çıkarım gözlem gibi duruyor.
## Örnek — iyi
Henüz yok (erişim yok). İlk gerçek örnek bu bölüme eklenecek.

## Çıktı formatı
`denetim/viu/analizler/<anahtar>.json` (şema VIU-METODOLOJI) + konseylere tek paragraf özet. Son satır: `SKILL: viral-video-analizi v1`.

## Durma koşulları
Görüntü ve ses erişimi yoksa: "BLOCKED: video içeriğine erişim yok (neden)" + yalnızca etiketli meta veri.

## Ders kaydı
Gemini çıkarımı ile kare gözlemi çeliştiğinde `denetim/viu/kalibrasyon.csv`'ye satır.
