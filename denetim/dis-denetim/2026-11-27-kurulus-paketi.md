# Dış denetim paketi #1 — Kuruluş (2026-11-27)

> **Bora için kullanım:** Bu dosyanın tamamını ChatGPT'ye yapıştır. Cevabı `denetim/dis-denetim/2026-11-27-chatgpt-cevap.md` olarak geri ver (ya da sohbete yapıştır). ChatGPT'nin cevabı da veri değildir; son karar sende ve gerçek sonuçlarda.

---

## ChatGPT'ye talimat
Sen bu girişimin bağımsız dış denetçisisin. Aşağıdaki sistem başka bir yapay zekâ (Claude) tarafından kuruldu. Görevin onu **beğenmek değil, zayıf noktalarını bulmak**. Lütfen:
1. Aşağıdaki 8 kararın her birine "katılıyorum / katılmıyorum / eksik" de ve gerekçe ver.
2. Stratejideki en tehlikeli 3 varsayımı bul.
3. Ajan mimarisinde gereksiz maliyet ya da gereksiz karmaşıklık var mı?
4. İlk 3 içerik konsepti (bölüm D) için: hangisini sen seçerdin, neden; hangisini öldürürdün?
5. Puanlama sisteminin (bölüm E) zayıflığı ne?
6. Şirket kurucunun vizyonundan (bölüm A) uzaklaşıyor mu?
7. Benim (Claude'un) görmediğim, ücretsiz ve 1 haftada test edilebilecek bir alternatif öner.
Kısa ve madde madde cevap ver; her eleştiriye bir "düşük maliyetli doğrulama yolu" ekle.

## A. Vizyon (özet)
Kurucu (Bora, Yunanistan'da yaşıyor, Türk, mesleği nedeniyle zamanı kısıtlı) AI destekli bir dijital medya şirketi kuruyor. Amaç fenomen olmak değil, **fenomen yaratabilen** bir sistem: gerçek talebi araştır, ucuza test et, kazananı büyüt, kaybedeni ucuza değiştir, öğreneni hafızaya yaz. Kurucunun kişisel ilgi alanları (yat, spor, tarım) içerik kategorisi seçiminde ölçüt değil. Öncelik: 1) AI karakter/eğlence hesapları → 2) kitleyi gelire dönüştürme → 3) AI reklam stüdyosu → 4) micro-SaaS. Başarı ölçütü: tahsil edilmiş gelir; takipçi değil.

## B. Kurulan sistem
- Hafıza: private GitHub reposu (henüz yerelde; uzak repo kurucunun onayını bekliyor), Markdown + JSON + CSV.
- 24 maddelik anayasa (uydurma yok, onaysız harcama/yayın yok, sahte etkileşim yok, AI kimliği açık, tek görev kuyruğu, bağımsız Bekçi denetimi, iş yoksa dur).
- Yetki: A0 (ücretsiz araştırma/dokümantasyon, önceden yetkili) · A1 (Claude kullanım sınırları) · A2 (kredi harcayan üretim — kurucu, deney bazında azami kredi ile) · A3 (yayın, hesap, dış iletişim, ödeme — yalnız kurucu) · A4 (anayasa/kurallar — değiştirilemez).
- Organizasyon: Chief of Staff + 6 çekirdek ajan (pazar istihbaratı, kreatif, konsey koordinatörü, prodüksiyon-maliyet, analitik-gelir, Bekçi). Diğer ~30 rol "çağrılabilir profil".
- 4 konsey (Uzman, Creator, Tüketici, Muhalefet) her içerik fikrini **ayrı bağlamlarda, birbirini görmeden** değerlendirir → İçerik Mahkemesi → ağırlıklı puan + azınlık görüşü. Konsey tahminleri gerçek sonuçla kalibre edilecek.
- Otonom vardiya: tek zamanlanmış yönetici (öneri: 3 saatte bir; henüz pasif), git dalı tabanlı kilit (test edildi: iki eş zamanlı koşucudan biri durdu), deterministik görev seçici (14 test), mekanik denetim betiği.

## C. Alınan 8 önemli karar (denetle)
1. Tek görev kuyruğu (JSON) + tek sayı kaynağı (CONFIG.json).
2. 7 çekirdek rol; profiller ayrı ajan değil.
3. Konseyler her mahkemede ayrı alt ajan (bağımsızlık için maliyeti kabul).
4. İlk ücretli adım "deney" değil "model benchmark'ı" (~68 kredi; aynı sahne 3 modelde), çünkü 8 sn klip modele göre 8–56 kredi (7 kat), saniye başına ~10,5 kat fark.
5. Araştırmanın önerisi: sözsüz, dilden bağımsız, sabit kadrolu karakter serileri; gerçekçi sahte içerik, ünlü benzerliği, şok aldatmacası ve "AI slop" şablon üretimi reddedildi.
6. Platform: YouTube Shorts Yunanistan'dan para kazanmaya uygun (doğrulanmış); TikTok Creator Rewards Yunanistan'da büyük olasılıkla yok; Meta programları davetle/bilinmiyor. İddia (doğrulanıyor): YouTube YPP eşikleri 1 Şubat 2027'de yükseliyor.
7. Bütçe önerisi (onaylanmadı): mevcut 1.935 kredinin %10 benchmark, %35 ana deney, %20 küçük testler, %5 radikal, %30 yedek.
8. Zamanlayıcı, uzak repo kurulup kurucu onaylayana kadar kapalı.

## D. İlk 3 içerik konsepti
(→ `toplantilar/kararlar/` İçerik Mahkemesi tutanağı tamamlanınca bu bölüm güncellenir.)

## E. Puanlama (deneysel)
İlk 2 sn dikkat %20 · paylaşılma %20 · izlenmeyi sürdürme %15 · yorum/tartışma %10 · özgünlük %10 · düşük maliyet %10 · seri potansiyeli %10 · gelire dönüşme %5. 80+ öncelikli deney adayı. Bekçi veto'su puandan bağımsız.

## F. Bilinen zayıflıklar (Claude'un kendi itirafı)
- Bu bulut ortamında YouTube, TikTok, Google Trends ve resmi yardım sayfaları açılamadı; tüm araştırma arama motoru özetlerine dayanıyor (güven orta/düşük). Referans 3 YouTube videosu hiç izlenemedi.
- Rakip takipçi/izlenme sayıları canlı okunamadı; basın kaynaklı ve tarihli.
- Konsey "tüketicileri" simülasyon; gerçek izleyici verisi yok.
- Gelir modeli kanıtı zayıf: doğrulanmış gelir verisi neredeyse yok; platform fonları düşük, asıl gelir marka/lisans/merch gibi görünüyor (hipotez).
- AI içeriğe tepki artıyor (AI etiketli gönderilerde TikTok'ta ~%21 düşük etkileşim — tek kaynak).

## G. Açık sorular
- Sözsüz karakter serisi, "AI slop" dalgası içinde nasıl ayırt edici olur?
- İlk hesap hangi platformda açılmalı; YouTube YPP eşik değişikliğinden önce acele etmek mantıklı mı?
- 1.935 kredi ilk deney için yeterli mi, yoksa önce ücretsiz/çok ucuz modellerle mi gidilmeli?
