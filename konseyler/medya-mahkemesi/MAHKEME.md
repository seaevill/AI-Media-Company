# İçerik Mahkemesi (Content Court)

Kaynak: manifesto §19, §20. Bir fikir yalnızca Creative Director beğendiği için üretime alınmaz. Komut: `/mahkeme <fikir dosyası>`.

## Akış
1. **Dosya:** Kreatif ekip fikri `toplantilar/gundem/<tarih>-<kısa-ad>.md` olarak sunar (şablon: aşağıda). Coşkulu sıfat yok; fikir, açılış hipotezi, hedef tüketici, seri planı, tahmini üretim.
2. **Bağımsız tur (paralel):** Uzman, Creator, Tüketici, Muhalefet konseyleri **ayrı alt ajan bağlamlarında**, yalnızca fikir dosyası + kendi KONSEY.md + ilgili istihbarat dosyalarıyla değerlendirir. Birbirlerinin çıktısını görmezler.
3. **Finans + Bekçi ön kontrol (tek bağlam):** maliyet tahmini (kredi aralığı, model, varyasyon sayısı) ve risk taraması (telif, gerçek marka, gerçek kişi, AI açıklaması, platform kuralı, çocuk, yanıltıcılık).
4. **Chief of Staff sentezi:** puanları tabloya koyar, ağırlıklı skoru hesaplar, **azınlık görüşünü** ayrı yazar, kararı verir.
5. **Karar:** deney adayı (EXP taslağı açılır) · geliştir · düşük öncelik · reddet · İNSAN ONAYI GEREKLİ. Tutanak `toplantilar/kararlar/<tarih>-<kısa-ad>.md`.

Çoğunluk kararı otomatik değildir: güçlü bir azınlık görüşü ucuz bir deneyle sınanabilir. Bekçi engeli (hak/etik/kural) puandan bağımsızdır; 95 puan da alsa engelli fikir yayımlanmaz.

## Puanlama (deneysel hipotez — bilimsel viral olasılığı DEĞİLDİR)
| Kriter | Ağırlık | Puanlayanlar (ortalama) |
|---|---:|---|
| İlk iki saniyede dikkat | %20 | Tüketici (Doomscroller, Impatient), Uzman (Behavioral, Visual), Creator (Hook) |
| Paylaşılma potansiyeli | %20 | Tüketici (Group Chat, Meme), Uzman (Behavioral, Sociologist) |
| İzlenmeyi sürdürme | %15 | Uzman (Storytelling), Creator (Hook), Tüketici (Silent) |
| Yorum ve tartışma | %10 | Tüketici (Comment Warrior), Muhalefet (Controversy) |
| Özgünlük | %10 | Muhalefet (Anti-Trend, Red Team), Tüketici (Meme, Anti-AI) |
| Düşük üretim maliyeti | %10 | Finans, Uzman (AI Production), Muhalefet (Cost Skeptic) |
| Seriye dönüştürülebilme | %10 | Creator (Seri), Tüketici (Repeat) |
| Gelire dönüşme | %5 | Uzman (Consumer, Marketing), Creator (Teklif) |

Skor = Σ(ortalama puan × ağırlık) × 10 → 0–100. Yorum: 80–100 öncelikli deney adayı · 65–79 test edilmeye değer · 50–64 geliştirilmeli · 0–49 düşük öncelik.
Gerçek veri biriktikçe ağırlıklar haftalık denetimde yeniden değerlendirilir; gelir aşamasında "gelire dönüşme" ve uzun vadeli kitle değeri ağırlığı artırılır (Bora onayıyla).

## Gündem dosyası şablonu
```
# FİKİR: <ad>
Kategori / format:
Bir cümlede:
İlk 2 saniye (açılış hipotezi):
Hikâye akışı (saniye saniye, ≤ 20 sn):
Hedef tüketici:
Dil bağımlılığı: sözsüz / az / yüksek
Seri potansiyeli (3 sonraki bölüm fikri):
Benzer mevcut içerik (kaynaklı) ve bizim farkımız:
Tahmini üretim: model, sahne sayısı, süre, çözünürlük, varyasyon
Gelir hipotezi:
Bilinen riskler:
```
