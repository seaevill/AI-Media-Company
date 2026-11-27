# Finans + Bekçi ön kontrolü — İçerik Mahkemesi, 3 fikir (2026-11-27)

Kapsam: `ucuncu-kat`, `dag-kileri`, `kayip-esya-burosu` gündem dosyaları + `karakterler/adaylar/tomruk.md`.
Okunan: ANAYASA, YETKI-MATRISI, KALITE-STANDARTLARI, BEKCI-KURALLARI §2 m.12, finans/BUTCE.md, maliyet keşfi (G-0007), platform kuralları ("Bizim için kurallar" §6 + ilgili §1–3). Konsey çıktıları okunmadı.
Bu belge **ön kontroldür**: Anayasa 18 uyarınca bağımsız Bekçi denetiminin yerine geçmez. Yeni web araması yapılmadı; platform bilgisi, kaynak dosyadaki "arama özeti" güvenindedir (resmi sayfalar açılamamıştı). Harcama, üretim, yayın yok; yalnızca A0.

---

## A. FİNANS

### A.1 Ortak dayanak ve kredi ≠ para
- Bakiye **1.935,39 kredi**, plan Ultra (`finans/BUTCE.md`, 2026-11-27). Ücretsiz üretim hakkı görünmüyor (`unlim.available=false`).
- **Plan ücreti, yenilenme tarihi, kredi başına € bilinmiyor.** Bu belgedeki hiçbir rakam € değildir; yüzdeler yalnızca mevcut bakiyeye oranıdır. Kredi harcamak ilerleme değildir (Anayasa 8), başarısız üretimler de krediye sayılır (Yetki Matrisi kural 3).
- Birim tahminler (`estimate_*`, maliyet keşfi): Seedance 2.0 Mini 8 sn/720p/ses = 8; Hailuo 2.3-fast 6 sn/768p = 4; MAGI-2 8 sn/1080p = 20; Nano Banana 2 1k = 1,5; GPT Image 2.6 1k düşük = 0,75. Gündemlerdeki birim fiyatlar maliyet keşfiyle **birebir tutuyor**.
- **Ölçülmemiş:** deneme sayısı (klip başına kaç üretim gerekir), tahmin ↔ gerçek fatura farkı. `benchmark.csv` boş. Aşağıdaki "orta/kötü durum" tamamen **varsayım**dır.
- Varsayım tanımı: taban = her klip/görsel 1 denemede; orta = klip 3 deneme, görsel 2 deneme (gündemlerin varsayımı); kötü = klip 5 deneme, görsel 2 deneme.

### A.2 Gündem tahmini ↔ keşif karşılaştırması

| Fikir | Gündemin yazdığı | Keşiften yeniden hesap | Sonuç |
|---|---|---|---|
| Üçüncü Kat | taban 90, orta ~252, aralık ~165–400 | 9×8 + 12×1,5 = 90 ✓; orta 216+36 = 252 ✓; 2 deneme: 144+36 = **180**; 5 deneme: 360+36 = **396** | Taban/orta doğru. Alt uç "165" tutmuyor (180; 165 ancak görseller de 1 denemede ise ~162). Küçük sapma, sonucu değiştirmez. |
| Dağ Kileri | taban 84, orta ~240, aralık ~156–400 | 72+12 = 84 ✓; orta 216+24 = 240 ✓; 2 deneme: 144+24 = **168**; 5 deneme: 360+24 = **384** | Taban/orta doğru; alt uç "156" görseller 1 denemede ise doğru (aynı küçük sapma). |
| Kayıp Eşya | taban ~44, orta ~123, aralık ~80–195 | 36+7,5 = 43,5 ✓; orta 108+15 = 123 ✓; 80 ✓ (görsel 1 deneme); 195 ✓ | Aritmetik doğru. **Ama kapsam eksik** (A.3, madde 1). |

Gündemlerin "Seedance 2.5 varsayılan ~1.500 kredi" karşılaştırması da tutuyor (9×56 = 504 tek deneme; ×3 = 1.512).

### A.3 Kredi aralığı, ilk 3 bölüm

**1) Üçüncü Kat** (Seedance 2.0 Mini, 9 klip + ~12 referans görsel)

| Durum | Kredi | Bakiyenin % | Dayanak |
|---|---:|---:|---|
| Taban | 90 | %4,7 | 9×8 + 12×1,5; tek deneme (**varsayım**) |
| Orta | 252 | %13,0 | klip 3×, görsel 2× (**varsayım**) |
| Kötü | 400 (396) | %20,7 | klip 5×, görsel 2× (**varsayım**) |

Gizli/ölçülmemiş maliyet: (a) bölüm 1–3'te üç karakter aynı karede; Mini'nin üçlü kimliği tek karede tutup tutmadığı bilinmiyor, tutmazsa 5× aşılır. (b) Yedek model Seedance 2.5 olursa tek denemede 504 + 18 = 522 (%27). (c) **Sürdürülebilirlik:** gündem haftada ~3 bölüm istiyor = haftada ~9 klip ≈ ~250 kredi/hafta (orta) → 1.935 kredi yaklaşık 7–8 haftalık üretime yeter ve bakiye başka hiçbir şeye kalmaz. İlk 3 bölüm ucuz görünür; seri maliyeti ucuz değildir. (d) EXP-0001 kovası (~680 kredi, öneri) içinde orta tahmin kovanın %37'si, kötü %59'u.

**2) Dağ Kileri** (Seedance 2.0 Mini, 9 klip + ~8 görsel)

| Durum | Kredi | Bakiyenin % | Dayanak |
|---|---:|---:|---|
| Taban | 84 | %4,3 | 9×8 + 8×1,5 (**varsayım:** tek deneme) |
| Orta | 240 | %12,4 | klip 3×, görsel 2× (**varsayım**) |
| Kötü | 400 (384) | %20,7 | klip 5×, görsel 2× (**varsayım**) |

Gizli/ölçülmemiş maliyet: ASMR değeri **ses kalitesine** bağlı ve ses kalitesi bilinmiyor. Mini'nin sesi yetersizse yedek MAGI-2 (20/klip): taban 192 (%9,9), orta 564 (%29,1), kötü 924 (%47,7); MAGI-2'nin 9:16 desteği de doğrulanmadı (1080p sabit). Küçük konsept kovası (~390 kredi, "2 konsept × 2 video", öneri): orta tahmin kovanın %62'si, kötü tahmin kovayı aşıyor (%103). Ek benchmark (Mini vs MAGI-2) en fazla ~28 kredi, ayrı A2.

**3) Kayıp Eşya Bürosu** (Hailuo 2.3-fast, 6 sn klip + ~10 görsel)

| Durum | Kredi | Bakiyenin % | Dayanak |
|---|---:|---:|---|
| Taban | 43,5 (~44) | %2,2 | 9×4 + 10×0,75 (**varsayım:** tek deneme) |
| Orta | 123 | %6,4 | klip 3×, görsel 2× (**varsayım**) |
| Kötü | 195 | %10,1 | klip 5×, görsel 2× (**varsayım**) |

Gündem tahmininde **kapsam açığı:** bölüm süresi 19–20 sn, ama 3 klip × 6 sn = 18 sn. Gündem "bir klip uzatılır" diyor ama bunu bütçeye koymamış. 4 klip/bölüm (12 klip) ile düzeltilmiş: taban 55,5 (%2,9), orta 159 (%8,2), kötü 255 (%13,2). Diğer belirsizlikler: Hailuo'nun 9:16 seçeneği listede yok; sesi belirtilmemiş (ses ayrı bir maliyet/iş kalemi, tutarı **bilinmiyor**); metin kartları video modelinde değil kurguda eklenmeli, yoksa metin render hataları deneme sayısını şişirir. Yedek Seedance 2.0 Mini (9 klip): taban 79,5 (%4,1), orta 231 (%11,9), kötü 375 (%19,4). Radikal deney kovası (~100 kredi, öneri): orta tahmin (123) ve düzeltilmiş orta (159) kovayı **aşıyor**; yalnızca taban/ilk bölüm kovaya sığar.

### A.4 "Düşük üretim maliyeti" puanı (0–10; 10 = en ucuz ve en az belirsiz)
Ölçüt: orta durumun bakiyeye oranı + ölçülmemiş maliyet kalemleri + seri sürdürülebilirliği. Tüm puanlar tahmine dayalıdır; benchmark sonrası değişir.

| Fikir | Puan | Gerekçe |
|---|---:|---|
| Kayıp Eşya Bürosu | **7** | En düşük taban/orta (%2,2 / %6,4; düzeltmeyle %2,9 / %8,2). −3: 9:16, ses ve metin kartı belirsiz; klip süresi kapsam açığı; bölümler ayrı oylamaya bağlı olduğundan hız baskısı. |
| Dağ Kileri | **6** | Orta %12,4; 2 karakter ve durağan sahne tutarlılığı kolay görünüyor (hipotez). −4: ASMR sesi bilinmiyor, MAGI-2 yedeğinde orta %29'a çıkar. |
| Üçüncü Kat | **5** | Orta %13,0. −5: üç karakterli kareler, haftada ~250 kredilik sürekli maliyet (~7–8 hafta), Seedance 2.5'e düşüş senaryosu pahalı. |

### A.5 Finans şartları (hepsi için)
1. Hiçbir fikre harcama yetkisi yoktur; ilk adım G-0007 benchmark'ı (~68 kredi) olmalı, A2 onayı **azami kredi** ile (Yetki Matrisi kural 2). Benchmark sonrası orta/kötü tahminler ölçülmüş değerle yeniden yazılır.
2. Her fikir için azami kredi **tek bölümle** başlatılmalı (3 klip), 3 bölümlük paketle değil; ilk bölümün gerçek deneme sayısı varsayımları ölçer.
3. Plan ücreti Bora'dan öğrenilmeden hiçbir raporda "€/video" yazılmaz (Kalite #14).
4. Tüm yüzdeler "bakiyenin %"sidir; kova yüzdeleri `BUTCE.md` önerisidir, yetki değildir.

---

## B. BEKÇİ ÖN KONTROLÜ (BEKCI-KURALLARI §2 m.12)

Genel: üç fikirde de **gerçek kişi/marka adı, gerçek kişi görünümü, haber gibi sunulan sahte olay yok**; hepsinde AI kimlik açıklaması *planlı* (biyografi "AI-generated", platform etiketi, C2PA korunur). Hiçbirinde ENGEL düzeyi bulgu yok. Bu bir **plan**dır; yapılmadığı sürece uygulandı sayılmaz. Karakter/ad çakışma taraması (benzer mevcut karakter veya marka adı) **hiçbiri için yapılmadı** (`tomruk.md` de "henüz yapılmadı" diyor); bu, yayın öncesi ortak şarttır.

### B.1 Üçüncü Kat — **ŞARTLI**

| Alan | Bulgu |
|---|---|
| Gerçek marka/kişi/creator benzerliği | Gerçek marka/kişi yok; yelekte logo yok. Bandar Apna Dost ile ortak yön yalnızca "diyalogsuz, sabit karakterli komedi" (prensip, Anayasa 13 izin verir); karakter, ortam, tür farklı. **Ad/karakter çakışma taraması yapılmadı** (Tomruk, Cetvel, Anahtar, "Üçüncü Kat"). Cetvel ve Anahtar için Karakter Bible dosyası **yok** (gündem de belirtiyor). |
| Telif | Müzik yok (iyi). Seri fikri 2 "kova müziği" gelirse müzik kaynağı lisanslı/kendi olmalı (§6 #5). Model ses efektinin ticari kullanım hakkı **bilinmiyor**. Format parodisi yok. |
| AI kimlik planı | Planlı: bio "AI-generated animated characters. Fiction.", platform etiketi, C2PA silinmez. Stilize olduğundan fotogerçekçi etiket zorunluluğu muhtemelen yok ama etiket konacak. Yeterli plan; uygulanana kadar "planlı". |
| Platform riski | **Ana risk: YouTube "inauthentic content" / Meta "unoriginal"** (§1.2, §1.5, §3.2). İmza davranış (engel → pes → otur), sabit 18–20 sn, sabit koli "3/C" kancası, ortak prompt çekirdeği = şablon göstergesi; haftada ~3 bölüm "çok az farkla yüksek hacim" okunabilir. Gündemin önlemleri (her bölümde yeni çatışma, insan yazımı, kayıt) doğru yönde ama henüz yok. Oylama/etkileşim çağrısı yok. Platformlar arası aynı video paylaşımı için kural dosyası yalnızca "birden fazla hesap/kanalda tekrar yükleme"yi yasaklıyor; aynı sahibin farklı platformlarını açıkça kapsamıyor (**bilinmiyor**). |
| Çocuk / çocuksu algı | **Orta risk.** Hayvan karakterler + slapstick + `tomruk.md`'de "flat 3D animation style" çocuk çizgi filmi gibi okunabilir; YouTube otomatik "made for kids" sınıflaması mümkün. Karşı unsurlar: yetişkin senaryo (vardiya, yönetici, komşu), çocuk karakter ve şarkı yok, hedef 18–45. |
| Yanıltıcılık | Düşük. Tamamen kurgusal, haber gibi değil. Alna damga/merdivenden koliyle kayma hafif slapstick; `tomruk.md` "şiddete maruz kalmamak (komik düşme dışında)" ile uyumlu, ama sahne "taklit edilebilir tehlikeli davranış" olarak yeniden okunmalı. |

**Şartlar:** (1) Cetvel ve Anahtar Bible'ları, ad/karakter çakışma taraması (A0 WebSearch) üretimden önce. (2) Her bölüm için ayrı insan yazımı senaryo + prompt/kurgu kaydı (§6 #3–4); ilk 3 bölümde imza davranışın "yeni çatışma"yla farklılaştığı yazılı gösterilmeli. (3) Çocuk riski için: YouTube'da "çocuklara özel değil" işareti, pastel/şeker renk ve çocuk müziği yok, "flat 3D" stil kararı yetişkin tona göre yeniden onaylanmalı, ilk 3 bölümden sonra YouTube sınıflama sonucu kontrol edilmeli. (4) Model ses/ses efekti ticari hak durumu kaydedilmeli. (5) Aynı videonun platformlar arası paylaşımı için kural doğrulaması (resmi sayfa) gerekir.

### B.2 Dağ Kileri — **ŞARTLI** (üç fikir içinde en ağır şartlar)

| Alan | Bulgu |
|---|---|
| Gerçek marka/kişi/creator benzerliği | Gerçek kişi/marka yok; kavanoz etiketi yalnızca "1" damgası. **Creator estetiği riski:** gündem kendisi Meow Ziqi/Li Ziqi estetiğine yakınlık riskini yazıyor. Reçel/kurutma/mevsim ritüeli *kır yaşamı* türünün genel öğesi (prensip serbest, Anayasa 13), ama sahne kompozisyonu, kostüm veya kare düzeni birebir uyarlanırsa gri bölge. Bu kontrol yapılmadı. Gerçek creator adı/stili prompt'ta kullanılırsa özgünlük ihlali. |
| Telif | Müzik yok; ASMR sesi modelden/ses tasarımından. Model sesinin ticari hakkı **bilinmiyor**. Format parodisi yok. |
| AI kimlik planı | Planlı (bio, etiket, C2PA). **Görsel stil belirtilmemiş:** ASMR "doku" için ortam fotogerçekçi üretilirse YouTube'un Mayıs 2026 görünür etiketi ve Meta "AI info" zorunlu olur (§1.1, §6 #1). Karakterler stilize kalmalı; gerçek porsuk/kaplumbağa videosu sanılmamalı (gündem zaten kaçınıyor). |
| Platform riski | **YouTube "generic/repetitive" riski yüksek** (§1.2 grup 1); gündem ASMR benzeri içeriğin bu kategoriye yakın olduğunu kendisi yazıyor. Yapı "hazırlık → kavanoz → raf" üç bölümde de aynı iskelet. TikTok'ta AI etiketi erişim cezası (radar sinyali; kural değil). Oylama yok. |
| Çocuk / çocuksu algı | **Orta-yüksek risk.** Porsuk + kaplumbağa, sıcak kır yaşamı, kavanoz/ekmek, sözsüz sakin ASMR = "çocuk kitabı / çocuk uyku videosu" estetiğine çok yakın; YouTube sınıflaması yanlış çıkabilir. Gündemin önlemleri (yetişkin zanaat estetiği, şarkı yok, "çocuklara özel değil" işareti) gerekli ama yeterli kanıtlı değil. Anayasa 22: uyku/rahatlama içeriğinde bağımlılık/duygusal bağ sömürüsüne kaymamalı (gündem "sömürü yok" diyor). |
| Yanıltıcılık | Düşük-orta. Karakterler kurgusal, gerçek hayvan "anı" yok. Ancak içerik taklit edilebilir bir **gıda işlemi** gösteriyor (mum mühürlü reçel, açıkta kurutma); izleyici gerçek tarif sanıp uygulayabilir. Mum mühürlemenin gıda güvenliği açısından sorunlu olduğuna dair bilgim doğrulanmadı (düşük güven). Tarif/öğretici/sağlık iddiası yok, olmamalı (§6 "asla" #3). |

**Şartlar:** (1) Prompt kaydında hiçbir gerçek creator/marka adı veya "X tarzında" ifadesi yok; birebir sahne kompozisyonu kopyası yok (Bekçi prompt geçmişini denetler). (2) Görsel stil kararı yazılı: karakterler belirgin stilize; ortam fotogerçekçiyse etiket planı değişir. (3) Bölümler arası yapısal farklılaşma (olay/çatışma/hikâye çizgisi: kuş, yağmur, kar) yazılı; insan yazımı senaryo. (4) Çocuksu algı: "çocuklara özel değil", çocuk kitabı kodlu pastel/yuvarlak estetikten kaçınma, ilk bölümlerden sonra sınıflama sonucunun kontrolü; sonuç olumsuzsa durdurma kriteri. (5) "Tarif/öğretici değil" ibaresi ve gıda güvenliği açısından taklit edilebilir işlemden kaçınma (mum mührü yerine düz kapak gibi). (6) Ses kalitesi benchmark'ı ve ses ticari hak kaydı üretimden önce.

### B.3 Kayıp Eşya Bürosu — **ŞARTLI**

| Alan | Bulgu |
|---|---|
| Gerçek marka/kişi/creator benzerliği | Gerçek marka/kişi yok. Gossip Goblin ve Neural Viz yalnızca **yöntem** referansı (karakter/evren alınmadı, Anayasa 13). "Kayıp Eşya Bürosu / Lost Property Office" jenerik bir kavram ve ad; mevcut eser/marka adıyla çakışma **taranmadı**. Prompt'ta "Gossip Goblin tarzı" ifadesi yazılmamalı. |
| Telif | Müzik yok. **Yeni kalem:** metin kartlarının yazı tipi ticari kullanım lisansı (açık lisanslı font kullanılmalı). Hailuo'nun sesi belirtilmemiş; ses/ses efekti kaynağı belirsiz, lisanslı/kendi olmalı. Format parodisi yok (Fruit Love Island'dan bilerek kaçınılmış). |
| AI kimlik planı | Planlı (bio, etiket, C2PA). Stilize/sürreal; fotogerçekçi değil. Metin kartı dili İngilizce; yeterli. |
| Platform riski | **Oylama mekaniği:** "Yorumla: A/B" çağrısı. Platform kuralları dosyası yorum/oy çağrısı ("engagement bait" türü) politikalarını **ele almıyor**: YouTube, Meta ve TikTok'un bu çağrılara kuralı **bilinmiyor** (kaynak dosyada yok). Meta tarafında benzer çağrıların erişim düşürdüğü bilinen bir uygulama olabilir; doğrulanmadı. Anayasa 11: sahte yorum/oy, bot, kendi hesaplarımızla oy, koordineli kampanya yasak; gündem "sahte yorum yok, gerçek yorumdan sayım" diyor (doğru yön). İnauthentic/repetitive: her bölüm farklı eşya/hikâye, tekrar riski düşük-orta; sabit metin kartı kalıbı şablon izlenimi verebilir. Oylama sonucuna bağlı bölümler hız baskısı yaratır; gündem haftalık ritim öneriyor. |
| Çocuk / çocuksu algı | **Düşük.** Melankolik-bürokratik ton, yetişkin temalar; güve memur çocuk kodlu değil. Yine de antropomorfik böcek/hayvan kullanımı için YouTube'da "çocuklara özel değil" işaretlenir. |
| Yanıltıcılık | Düşük-orta. Kurgusal evren; ancak yorumlarda izleyiciler gerçek kayıp eşyalarını yazabilir. Hesap "gerçek kayıp eşya bürosu" gibi okunmamalı; iade/bulma hizmeti ima edilmemeli; kişisel veri (telefon, adres) yorumlardan toplanmamalı. Oylama sonuç raporu gerçek sayımla; küçük örneklemden kesin sonuç çıkarılmaz (Kalite #11). |

**Şartlar:** (1) Oylama CTA'sı için YouTube/Meta/TikTok "engagement bait / oy çağrısı" politikaları resmi kaynaktan doğrulanmadan yayın yok (A3 zaten Bora onaylı); doğrulanana kadar oy mekaniği olmadan, yalnızca açık uçlu soru (örn. "sence?") ile hazırlanır. (2) Yazılı oy kuralı: yalnızca organik yorum, hesap sahibi/ajan oy atmaz, sayım yöntemi ve ölçüt yayından önce deney dosyasında. (3) Açık lisanslı font ve ses kaynağı kaydı. (4) "Gerçek hizmet değil, kurgu" net; kişisel veri toplanmaz. (5) Ad çakışma taraması. (6) Bütçe: bkz. A.3 (süre/klip açığı ve kova aşımı).

---

## C. Özet tablo

| Fikir | Kredi (taban / orta / kötü) | % bakiye | Maliyet puanı | Bekçi |
|---|---|---|---:|---|
| Üçüncü Kat | 90 / 252 / 400 | %4,7 / %13,0 / %20,7 | 5 | ŞARTLI |
| Dağ Kileri | 84 / 240 / 400 | %4,3 / %12,4 / %20,7 | 6 | ŞARTLI (ağır) |
| Kayıp Eşya Bürosu | 44 / 123 / 195 (4 klip/bölümle 56 / 159 / 255) | %2,2 / %6,4 / %10,1 (%2,9 / %8,2 / %13,2) | 7 | ŞARTLI |

Ortak notlar: kredi aralıkları varsayımdır (deneme sayısı ölçülmedi); plan ücreti bilinmediğinden € hesabı yok; hiçbir harcama onaylı değil; ENGEL bulgusu yok, ama hiçbiri koşulsuz GEÇER değil (çakışma taraması, AI etiket uygulaması, platform kural teyidi bekliyor).
