---
name: pazar-istihbarati-olcum
description: Sosyal medya hesaplarını ve formatları KAMUYA AÇIK PLATFORM SAYFASINDAN doğrudan ölçerek araştırır (abone/takipçi, Shorts izlenme medyanı, aykırı değer, platformlar arası karşılaştırma, başarısız karşı örnek). Rakip, trend, kategori ya da hesap araştırması istendiğinde kullan. Haber/arama özetindeki sayıları veri sayma.
---
# Pazar istihbaratı — ölçüm becerisi v1, 2026-11-27

## Ne zaman
"Şu kategoride hangi hesaplar büyüyor / ne kadar izleniyor / hangi format çalışıyor" türü her soru.

## Girdiler
Kategori tanımı (format, dil, platform), hedef hesap sayısı, zaman penceresi.

## Araçlar
WebSearch (yalnız ADAY bulmak için) · `python3 -I scripts/hesap_olc.py youtube @h …` · `python3 -I scripts/hesap_olc.py tiktok h …` · `curl -s -A "Mozilla/5.0"` (gerekirse). Instagram bu ortamda kapalı (403) → "ölçülemedi".

## Yöntem
1. **Aday listesi:** WebSearch ile 2–3 kat fazla aday topla (haber, liste, Reddit). Bu aşamadaki sayılar **OKUDUM-ÖZET**tir, tabloya veri olarak girmez.
2. **Doğrudan ölçüm:** her aday için hesap_olc.py çalıştır. Tabloya yalnızca betiğin okuduğu değerler, `olcum_utc` ile girer (**GÖRDÜM/ÖLÇTÜM**).
3. **Varlık doğrulama:** 404 / statusCode 10221 = hesap yok ya da adı yanlış → adayı düşür ya da adı düzelt; uydurma hesap = sıfır tolerans.
4. **Performans:** toplam takipçi değil, **son klipler medyanı** ve `medyan_izlenme_abone_orani` (> 1 = takipçi dışı erişim güçlü). `en_yuksek_medyana_orani` ≥ 3 = tek virale bağımlılık şüphesi. (Aykırı değer yaklaşımı: kanalın kendi medyanına göre performans — kaynak: `istihbarat/kaynaklar/2026-11-27-mesleki-yontemler.md`.)
5. **Platformlar arası:** aynı hesabı her platformda ölç; büyük farkı yaz (kanıt: meowtakeover TT 2,6M vs YT ~25K; Granny Spills TT 1,17M vs YT 2,32K).
6. **AI kullanımı kanıtı:** hesabın kendi beyanı / platform AI etiketi / güvenilir haber — hangisi olduğunu yaz; tahminse TAHMİN.
7. **Hayatta kalma yanlılığı:** aynı kategoride en az 1 küçük kalmış/kapanmış hesap ölç.
8. **Gelir:** yalnızca hesabın kendi beyanı veya belgelenmiş kaynak; izlenmeden gelir hesaplanmaz.

## Karar kriterleri
Bir hesap "büyüyor/başarılı" sayılır ancak ölçülmüş medyan izlenme ve abone/takipçi değeri varsa. Sadece haber sayısı olan hesap "ölçülmedi" sütununa gider.

## Örnek — iyi (gerçek)
`@NeuralViz | YouTube | 237K abone | son 6 Shorts medyan 118.500 (54K–347K) | medyan/abone 0,50 | ölçüm 2026-11-27T15:28:50Z | GÖRDÜM`
## Örnek — kötü (gerçek, bizim hatamız)
"Granny Spills YouTube 2,1M" — CreatorDB arama özetinden; sayfa 2,32K gösteriyor (G-0030 düzeltmesi). Neden kötü: üçüncü taraf sayısı doğrudan ölçülmeden veri yazıldı.

## Doğrulama
Bekçi rastgele 3 satırı hesap_olc.py ile yeniden ölçer; ±%5'ten büyük fark (aynı gün) = düzeltme.

## Çıktı formatı
Tablo: hesap · platform · URL · abone/takipçi · medyan (n) · min–max · medyan/abone · ölçüm_utc · kaynak etiketi · AI kanıtı · format/şaka · not. Ayrı tablo: başarısız/küçük örnekler. Son satır: `SKILL: pazar-istihbarati-olcum v1`.

## Durma koşulları
hesap_olc.py "engel" döndürürse (CAPTCHA/giriş) → aşma, "ölçülemedi" yaz. Hiç ölçüm yapılamadıysa rapor "BLOCKED" başlığı taşır.

## Ders kaydı
Yanlış çıkan her sayı → `takimlar/pazar-istihbarati/defter.md`'ye tek ders + düzeltilen dosyada not.
