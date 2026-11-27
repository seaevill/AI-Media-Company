# Kuruluş raporu — 2026-11-27

Bora için, Türkçe, 12 başlık (manifesto §41). Ayrıntılar dosya yollarında.

## 1. Vizyonu nasıl anladım
Amaç bir fenomen olmak değil; **fenomen üretebilen bir sistem** kurmak: gerçekte ne tüketildiğini araştırmak, fikirleri ucuza test etmek, kazananı büyütüp kaybedeni ucuza değiştirmek, her sonucu kalıcı hafızaya yazmak. Senin ilgi alanların (yat, spor, tarım) içerik seçiminde ölçüt değil; bunlar ileride Reklam Stüdyosu aşamasında avantaj olabilir. Başarı ölçütü tahsil edilmiş gelir; takipçi, izlenme ve dosya sayısı değil. Gelir senin çalışma saatlerine bağlı olmamalı; şirket senin başında olmana değil, önceden yazılmış yetki ve bütçe sınırlarına göre çalışmalı. → `VIZYON.md`

## 2. ALONI'den devralınanlar
Yalnızca okundu; ALONI'ye hiçbir şey yazılmadı, zamanlayıcılarına dokunulmadı.
- Anayasa → ajan kimliği → takım dosyaları (`takim.md` / `kurallar.md` salt okunur / `defter.md` tek ders) okuma sırası.
- Sağ kol (Chief of Staff) iş dağıtır; Bekçi bağımsızdır, düzeltme yapmaz, karar bloğu yazar; iki düzeltme hakkı, sonra sana gelir.
- Tek iş listesi (ALONI'nin `durum.json` geçişi) → burada `vardiyalar/DURUM.json`.
- İleri yönlü git dalında kilit (`lock/aloni` → `lock/medya`), `--force-with-lease`, bayat kilit devralma.
- Bekçi onayı denetlenen commit SHA'sına bağlı; yeni commit onayı geçersiz kılar.
- Her koşu kayıtla biter; haftalık `/denetim` ile tekrar eden dersler senin onayınla kurala dönüşür.
- **ALONI'nin hatasından alınan iki ders:** (a) sıklık ve günlük sınır iki dosyada farklı yazılmıştı (3 saat / yoğun mod, sınır 4 / 12) → burada tek kaynak `vardiyalar/CONFIG.json` ve bunu bir betik denetliyor; (b) repo kaynağı eklenmeden kurulan zamanlanmış görev 403 almış → zamanlayıcı uzak repo kurulmadan açılmayacak.

## 3. Oluşturulan bölümler (gerçek dosyalar)
- **Temel:** ANAYASA (24 madde), VIZYON, STRATEJI, KARARLAR, ROADMAP, CLAUDE.md, README; manifestonun birebir kopyası `arsiv/`.
- **Şirket:** AJAN-KIMLIGI, ORGANIZASYON, YETKI-MATRISI (A0–A4), ISE-ALIM-PROTOKOLU, TOPLANTI-PROTOKOLU, KALITE-STANDARTLARI.
- **Ajanlar (`.claude/agents/`):** pazar-istihbarati, kreatif-direktor, konsey-koordinatoru, produksiyon-maliyet, analitik-gelir, bekci (+ ana oturum Chief of Staff). Diğer ~30 rol çağrılabilir profil.
- **Komutlar:** `/kos`, `/mahkeme`, `/vardiya`, `/denetim`.
- **Konseyler + İçerik Mahkemesi** (puanlama, gündem şablonu, kalibrasyon tablosu).
- **Operasyon:** YONETICI.md, CONFIG.json, DURUM.json (20 görev), DEVIR-TESLIM, BLOCKERS, run-logs.
- **Betikler + testler:** `kilit.sh` (7/7 test), `gorev_sec.py` (14/14 test), `dogrula.py` (Bekçi'nin mekanik kontrolü), `mahkeme_skor.py`.
- **Şablonlar:** deney, Character Bible, araştırma kartı, vardiya raporu; finans CSV'leri; hafıza dosyaları.
- Manifestodaki tam klasör ağacının yalnızca aktif kısmı açıldı; kalanlar açılma koşuluyla ROADMAP'te (boş dosya üretilmedi).

## 4. Dört konsey nasıl farklı
| Konsey | Sorusu | Kör noktası |
|---|---|---|
| Uzman | Bilimsel/teknik/ticari olarak neden çalışır? | Açıklanabilir olanı başarılı sanmak |
| Creator | Sahada bugün hâlâ çalışıyor mu, bizim ölçeğe uyar mı? (yalnızca kaynaklı yöntemler, uydurma alıntı yok) | Ünlüye özgü başarıyı genellemek |
| Tüketici | Akışta durur muyum, gönderir miyim, ne zaman takipten çıkarım? (18 profil; Anti-AI, Skeptic, Unsubscriber, Silent her zaman dahil) | Söylenen ≠ yapılan |
| Muhalefet | Neden batar, neyi görmüyoruz, daha ucuzu var mı? (her eleştiri alternatif + ucuz doğrulama yolu içerir) | Her şeye hayır demek |
Her biri ayrı bağlamda, diğerlerini görmeden değerlendirir; tahminleri gerçek sonuçla kalibre edilecek.

## 5. İlk kuru koşuda ne oldu
İki vardiya yöneticisi **aynı anda** başlatıldı (yerel test deposu):
- A kilidi aldı; B "başka koşu sürüyor" deyip durdu ✅. Eski görünümle ikinci kilit alma reddedildi ✅. Kilit bırakıldı ✅.
- Seçici onaylı en öncelikli görevi seçti; A2/A3 ve zamanı gelmemiş görevleri doğru gerekçeyle atladı ✅; gereksiz ajan çağrılmadı ✅.
- **Bulunan gerçek hatalar (düzeltildi):** kilit betiği çalıştırılabilir değildi ve tanımsız hata kodu "devam" sanılabilirdi; seçici yarım kalmış görevleri göremiyordu (yetim görev) — 3 yeni testle düzeltildi; etkileşimli oturum kontrolü yanlış yerdeydi.
- Düzeltmeden sonra gerçek kuyrukla seçici: "önce bekleyen denetimleri bitir, yeni iş açma" ✅. → `vardiyalar/run-logs/2026-11-27-KURU-KOSU-A-B.md`

## 6. İlk pazar araştırmasının kapsamı
- 29 hesap/format kartı + 9 başarısız/kapanan hesap; 22 formatlık trend radarı (yaşam evresi, lehte/aleyhte kanıt); 6 fırsat hipotezi; platform kuralları (YouTube, TikTok, Instagram, Facebook, AB AI Yasası); gelir modelleri; 8 büyük + 6 AI-native creator yöntemleri.
- **Önemli kısıt:** YouTube, TikTok, Google Trends, Social Blade ve resmi yardım sayfaları bu ortamdan açılamadı. Hiçbir sayfa tam metin okunmadı; her şey arama motoru özetleri. Bu yüzden güven çoğunlukla düşük-orta.
- Referans 3 YouTube videosu **izlenemedi**. Rakamlar: 23 × 12 $ = 276 $ başka bir videoya (Mark Tilbury, 7 günlük vaka) ait görünüyor, iade iddiası bulunamadı; 1.047 $ / 389 $ hiçbir kaynakta çıkmadı. → `istihbarat/kaynaklar/REFERANS-VIDEOLAR.md`

## 7. En önemli ticari hipotezler
**Kanıta en yakın (Bekçi örneklemle doğruladı, arama özeti):**
- YouTube Partner Programı Yunanistan'da var. 1 Şubat 2027'den itibaren yeni başvuru eşiği 1.000 abone + (8.000 saat ya da 90 günde 20M Shorts) olacak; Shorts havuzundan pay için her ay 90 günde 10M görüntüleme. Yeni hesap için bu tarihten önce eski eşiği geçmek gerçekçi değil.
- TikTok Creator Rewards Yunanistan'da büyük olasılıkla yok; TikTok şimdilik büyüme kanalı.
- AB AI Yasası 50. madde (deepfake etiketi) Ağustos 2026'dan beri geçerli; AI etiketini her zaman koyacağız.
**Hipotez (test edilmedi):**
- Kazanan formatlar araç değil **karakter ve dünya** üzerine kurulu; sözsüz, dilden bağımsız, sabit kadrolu seriler en güçlü global kanıta sahip.
- Platform fonları küçük; asıl gelir marka anlaşması, lisans, merch ve uzun format (doğrulanmış gelir verisi neredeyse yok).
- Şablon tekrarı ve gerçekçi sahte içerik artık cezalandırılıyor (YouTube Temmuz 2026, Meta Mart 2026).
**İlk İçerik Mahkemesi:** Üçüncü Kat 60,9 · Kayıp Eşya Bürosu 57,6 · Dağ Kileri 50,4 — hiçbiri "deney adayı" eşiğini geçmedi; ana aday Üçüncü Kat, önce kredisiz animatik. → `toplantilar/kararlar/2026-11-27-ilk-portfoy-mahkemesi.md`

## 8. Çalışmayan / eksik
- **Uzak repo yok.** Tüm şirket şu an silinebilir bir bulut konteynerinde (yerel git). En acil risk.
- Zamanlayıcı kapalı (uzak repo + senin onayın gerekiyor).
- Ağ: YouTube/TikTok/Trends/resmi yardım sayfaları kapalı.
- Kuruluş belgeleri (Anayasa, kurallar) senin onayını bekliyor — Bekçi "İNSAN ONAYI GEREKLİ" dedi.
- Kling eklenti bağlantısı proxy yüzünden kurulamadı; Higgsfield çalışıyor.
- Hiçbir model kalitesi test edilmedi (0 kredi harcandı); benchmark boş.
- ChatGPT ile otomatik bağlantı yok; dış denetim senin üzerinden.
- Konsey tahminleri henüz hiçbir gerçek veriyle karşılaştırılamadı.

## 9. Kullanılan kaynak
- **Higgsfield: 0 kredi** (yalnızca bakiye, model listesi ve 10 fiyat tahmini okundu).
- **Claude:** 15 alt ajan koşusu (4 araştırma, 2 kuru koşu, 1 kreatif, 5 mahkeme, 3 Bekçi) — alt ajanlar toplam ~2,4 milyon token + ana oturum. Parasal karşılığı **bilinmiyor** (abonelik; ALONI ile paylaşılan limitten düştü).
- Nakit: 0 €.

## 10. Senden gereken kararlar
1. **Private GitHub reposu** `AI-Media-Company` aç ve bu ortama ekle (en acil).
2. **Kuruluş belgelerini onayla** (ANAYASA, YETKI-MATRISI). Madde 1'e "kaynaksız sayı çıktıya girmez", madde 10'a "hesap açma ve ödeme" açıkça eklendi.
3. **Ağ izinleri:** youtube.com, tiktok.com, trends.google.com, support.google.com, support.tiktok.com, help.instagram.com.
4. **Benchmark kredisi:** G-0012 karakter tutarlılığı testi için en fazla 80 kredi (bakiyenin ~%4'ü) — kredisiz storyboard bittikten sonra.
5. **Bilgi:** Higgsfield Ultra aylık ücreti ve kredi yenilenme tarihi.

## 11. Sıradaki üç somut görev
| # | Görev | Fayda | Maliyet | Bağımlılık |
|---|---|---|---|---|
| 1 | G-0010 uzak repoya ilk push + G-0011 zamanlayıcı | Hafıza kalıcı olur; şirket sen yokken çalışır | 0 | Karar 1 |
| 2 | G-0019 Üçüncü Kat revizyonu + kredisiz animatik | Ana adayın en zayıf noktasını (tekrar/özgünlük) para harcamadan düzeltir | 0 kredi, ~2 alt ajan | — |
| 3 | G-0012 karakter tutarlılığı benchmark'ı | Tüm sonraki kredi kararlarının dayanağı (hangi model, kullanılabilir saniye başına kaç kredi) | ≤80 kredi | G-0019 + Karar 4 |

## 12. ChatGPT denetim paketi
`denetim/dis-denetim/2026-11-27-kurulus-paketi.md` — olduğu gibi ChatGPT'ye yapıştırılabilir: vizyon özeti, kurulan sistem, denetlenecek 8 karar, 3 konseptin mahkeme sonucu, puanlama, Claude'un kendi itiraf ettiği zayıflıklar ve 7 soru. Cevabını geri getirirsen kayda işlerim.
