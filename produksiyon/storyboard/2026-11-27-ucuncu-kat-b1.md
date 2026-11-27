# Storyboard — Üçüncü Kat, Bölüm 1 "Koridor" (v2) + G-0012 benchmark test sahnesi

Durum: **hazırlandı (metin storyboard, kredisiz)**; görsel üretilmedi, Bekçi denetimi yok. Hazırlayan: kreatif-direktor, 2026-11-27, G-0019 (A0). Harcanan kredi: **0**.
Bağlı: `toplantilar/gundem/2026-11-27-ucuncu-kat-v2.md` §4 Bölüm 1; karakterler: `karakterler/adaylar/{tomruk,cetvel,anahtar}.md`.
Kural: yazı yok (kare içi tabela/damga metni yok); tek istisna, K10'daki "3/C" kodu **kurguda eklenir**, modele ürettirilmez. Müzik yok. Dikey 9:16. Süre ≈ 20 sn (klip A 0–7, B 7–14, C 14–20).

## 1. Ortak prompt blokları

**STİL (her karede aynı):**
`stylized matte 3D animation, adult-oriented comedy tone, desaturated muted palette (slate green, ochre, brick red, ink navy, dull bone white), practical low-key lighting, subtle film grain, no gloss, no big cute eyes, no pastel colors, vertical 9:16, no text, no letters, no logos`

**TOMRUK (çekirdek):**
`stylized adult wombat, short round heavy brown body, wide nose, drooping half-closed eyelids, faded orange courier vest without logo, single canvas shoulder bag, small notch in left ear`

**CETVEL (çekirdek):**
`stylized adult flamingo, tall thin body, long S-curved neck, dusty muted brick-rose feathers (desaturated, not pastel), charcoal grey wool vest, thin round metal glasses, yellow-black tape measure around neck, thin crease line on upper beak`

**ANAHTAR (çekirdek):**
`stylized adult goose, large heavy body, long neck leaning forward, dull bone-white feathers (matte), dark navy blazer with one missing button, large key ring at the belt with a rusty key and a red-taped key, small chip in the beak, one raised eyebrow, round ring stamp with keyhole silhouette in oxide red ink held in left wing`

**MEKÂN (koridor/merdiven):**
`old apartment building third-floor landing, slate-green walls, worn stairs and metal railing, flickering fluorescent ceiling light, brown doors marked only with small brass dots`
(Kapı numarası/yazı üretilmez; "3/B" vb. yazı kare içinde yok.)

**KOLİ (çekirdek):**
`oversized plain cardboard parcel box, taller than the door frame, packing tape, blank white shipping label with no text`

Prompt kuralı: **çekirdek (STİL + ilgili karakter çekirdekleri) hiç değişmez; yalnız "DEĞİŞKEN" satırı karedir.** Referans görseller (Nano Banana 2, A2) önce karakter başına 1 görsel (3/4, tam boy; bütçe §3); video modelinde çekirdek metin referansla birlikte verilir.

## 2. Kare kare storyboard (10 kare)

| Kare | Zaman | Plan / hareket | Ses | Prompt DEĞİŞKEN kısım |
|---|---|---|---|---|
| K1 | 0–2 | Koridor geniş, sabit kamera. Tomruk'un yüzü kapıyı tıkayan kolinin üzerine yapışık. Okunur açılış. | floresan vızıltısı, yorgun nefes | `wide static shot of the landing at 5am, TOMRUK standing with his face pressed flat against a huge parcel box that blocks his door completely, exhausted posture` + KOLİ |
| K2 | 2–4 | Orta plan. Tomruk omzuyla iter; koli kıpırdamaz. | karton gıcırtısı, homurtu | `medium shot, TOMRUK pushing the huge parcel with his shoulder, the box does not move, effort in his heavy body` |
| K3 | 4–5,5 | Alçak açı yukarı. Cetvel merdiven korkuluğundan eğilir, şerit metreyi aşağı sarkıtır. | metre çıtırtısı | `low angle looking up, CETVEL leaning over a metal railing, unrolling her yellow-black tape measure down toward the parcel, calm precise expression` |
| K4 | 5,5–7 | Yakın plan Cetvel: kanatlarıyla küçük "X". Kesme: Tomruk yarı kapalı gözlerle yukarı bakar. | tek tık | `close up, CETVEL crossing her two wings into a small X sign, glasses slightly lowered`; ardından `close up TOMRUK looking up with half-closed eyes, nose wrinkled` |
| K5 | 7–10 | Tomruk pes eder, koliye oturur; koli merdiven başında eğime girer, kayma başlar. | ağır sürtünme, karton | `TOMRUK sitting on top of the parcel box at the head of a staircase, shoulders dropped, the box starting to tilt and slide down the stairs` |
| **K6** | 10–12 | **Dikey merdiven boşluğu, yukarıdan aşağıya (9:16 için ideal): üç karakter aynı karede.** Cetvel üstte korkulukta, Tomruk koli üstünde kayıyor, Anahtar en altta. | kayma, metal korkuluk, uzaktan halka şıngırtısı | `tall vertical stairwell seen from above, three levels in one frame: CETVEL at the top railing, TOMRUK riding the sliding parcel in the middle, ANAHTAR at the bottom looking up` |
| K7 | 12–14 | Cetvel'in şerit metresi sonuna gelir, kopar, uçar; Tomruk koli üstünde ifadesiz iner. | metre kopma çıtırtısı | `CETVEL's tape measure snapping loose at the end and flying through the stairwell, TOMRUK sitting expressionless on the sliding box` |
| K8 | 14–16 | Zemin kat. Koli Anahtar'ın ayaklarının önünde durur; Anahtar damgayı kaldırır, havada duraklatır. | halka şıngırtısı, sessizlik | `ground floor hall, the parcel stopping at ANAHTAR's feet, ANAHTAR raising his ring stamp in his left wing and holding it in the air, left eyebrow raised` |
| K9 | 16–18 | Tomruk koliden iner, sırtı kameraya, merdivene yürür; Anahtar bakar. | yorgun adımlar | `back view of TOMRUK walking slowly up the stairs away from the parcel, ANAHTAR in background still holding the stamp` |
| K10 | 18–20 | Anahtar koliyi ayağıyla çevirir; kamera etikete yaklaşır. **Boş etiket üretilir, "3/C" kurguda eklenir.** Tomruk kadrajda yok. | karton sürtünmesi, floresan | `close up of the parcel's blank white shipping label as a goose's foot turns the box, floor reflection, no text on the label` (post: "3/C" kodu) |

Not: K1–K10 toplam ≈ 20 sn; üretim klipleri A (K1–K4: 0–7), B (K5–K7: 7–14), C (K8–K10: 14–20). Kazanan: Tomruk (sorumluluğu Anahtar'a devreder). Son türü: **nesne ipucu, karakter tepkisi yok.**

## 3. G-0012 benchmark test sahnesi (TEK sahne)

**Ad:** "Merdiven Boşluğu" (K6 genişletilmiş). **Mekân:** tek: yukarıdan görünen dikey merdiven boşluğu (3 kat, tek kamera). **Karakter:** 3 (Tomruk, Cetvel, Anahtar; hepsi aynı karede). **Süre:** 7 sn (Hailuo 2.3-fast için 6 sn sürüm; son saniye kırpılır). **Biçim:** 9:16, 720p, ses açık, müzik yok.

**Aksiyon (7 sn):**
- 0–2: Cetvel üst korkulukta metreyi sarkıtır; Tomruk koli üstünde oturur, kayma başlar; Anahtar altta yukarı bakar, damgayı kaldırır.
- 2–5: Koli bir kat süzülür; Cetvel metreyi uzatıp kaymayı ölçmeye çalışır; Tomruk hareketsiz; Anahtar damgayı havada tutar, kaşı kalkık.
- 5–7: Metre sonuna gelir, kopar, uçar; koli Anahtar'ın ayağına yaklaşır, durur.

**Prompt:** STİL + TOMRUK + CETVEL + ANAHTAR çekirdeği + MEKÂN + KOLİ + K6/K7 değişken satırı birleşimi. Aynı prompt ve aynı referans görseller 3 modelde; model başına **tek** üretim (G-0007 tahminleri).

**Benchmark bütçesi (G-0019 düzeltme 1; G-0012 tavanı azami 80 kredi, A2 onayı Bora; planlanan toplam ≤ 70, ≥ 10 kredi başarısız üretim payı):**
Seçim ve gerekçe: (a) referans görsel **karakter başına 1** (tek, 3/4 görünüm, tam boy) = 3 × 1,5; 4 açı yerine 1 görsel, çünkü benchmark tek sahne ölçer ve çok açı bütçeyi 18'e çıkarıyordu; (b) üçüncü model Seedance 2.5 varsayılan (56) yerine **Seedance 2.5 Flash** (40): aynı aile, 720p ve ses korunur (Biçim kriteri ölçülebilir); taslak 480p (24) 720p okunurluk ölçütünü bozacağı için seçilmedi.

| Kalem | Birim tahmin | Adet | Kredi |
|---|---:|---:|---:|
| Referans görsel: Nano Banana 2 1k (Tomruk, Cetvel, Anahtar; karakter başına 1) | 1,5 | 3 | 4,5 |
| Video: Hailuo 2.3-fast, 6 sn, 768p | 4 | 1 | 4 |
| Video: Seedance 2.0 Mini, 8 sn, 720p, ses açık | 8 | 1 | 8 |
| Video: Seedance 2.5 Flash, 8 sn, 720p, ses | 40 | 1 | 40 |
| **PLANLANAN TOPLAM** | | | **56,5** |
| Tavan altı pay (80 − 56,5) | | | 23,5 |
| Planlanan tavan (≤ 70) içinde tekrar payı (70 − 56,5) | | | 13,5 |

Tahminler `produksiyon/model-testleri/2026-11-27-maliyet-kesfi.md` (gerçek fatura ≠ tahmin olabilir; ilk üretimde `tahmini_kredi` ↔ `gercek_kredi` karşılaştırılır).

**İlk deneme başarısız çıkarsa:**
- Başarısızlık iki ayrı şeydir. **Kalite başarısızlığı** (üretim tamamlandı, puan düşük) tekrar sebebi **değildir**: o model için sonuç veridir, benchmark.csv'ye yazılır; tekrar yok.
- **Teknik başarısızlık** (iş hata verdi, boş/bozuk dosya, 9:16 yerine letterbox, ses yok): yalnızca ucuz kalemler için **en fazla 1 tekrar** (referans görsel 1,5; Hailuo 4; Seedance 2.0 Mini 8). Seedance 2.5 Flash (40) teknik hatada da **tekrar edilmez**; durulur, Bora'ya hata kaydı ve yeni onay talebi gider.
- Tekrarlar dahil **toplam harcama 70'i geçemez**; 70'e ulaşılırsa ya da bir tekrar da başarısız olursa **durulur** ve rapor edilir. 80 hiçbir koşulda aşılmaz. Referans görseller kullanılamazsa üç videoya geçilmez (referanssız sonuç ölçüt dışı).

**Ne ölçülür** (her madde 0–2: 0 bozuk, 1 kısmen, 2 doğru; hipotez eşikleri, Bible'daki "eşik yok" boşluğunu doldurur):

| Boyut | Madde | Puan |
|---|---|---|
| **Karakter tutarlılığı** (32 = 3 × 10 + 2) | Tomruk: yuvarlak silüet, yarı kapalı göz, turuncu yelek, kulak çentiği, çanta (5 çapa; her biri 0–2 → en çok 10) | 0–2 × 5 (en çok 10) |
| | Cetvel: kiremit-pembe S boyun silüeti, şerit metre, gözlük, yelek, gaga çizgisi | 0–2 × 5 (en çok 10) |
| | Anahtar: kemik-beyaz silüet, lacivert blazer, anahtar halkası, damga ikonu, gaga çentiği | 0–2 × 5 (en çok 10) |
| | Klip içinde ve başlangıç/son karesinde karakterlerin birbirine **karışmaması** (kimlik kayması) | 0–2 (en çok 2) |
| **Hareket** (10) | Koli kayma fiziği (süzülme/eğim, havada asılı kalmama) | 0–2 |
| | Şerit metre: sarkma, kopma, uçma (nesne sürekliliği) | 0–2 |
| | Üç karakterin aynı karede bağımsız hareketi; uzuv/boyun deformasyonu yok (flamingo boynu, kaz kanadı + damga) | 0–2 |
| | Kamera: dikey boşlukta derinlik (3 seviye) korunur | 0–2 |
| | Damga havada tutulur (el/kanat devamlılığı) | 0–2 |
| **Ses** (6) | Mekân sesi (floresan, karton, metal korkuluk) görüntüye senkron | 0–2 |
| | Karakter imzaları (halka şıngırtısı, metre çıtırtısı, nefes) duyulur ve karışmaz | 0–2 |
| | Müzik/konuşma/üretilmiş "yazı" yok (istenmeyen eklenti = 0) | 0–2 |
| **TOPLAM (puanlı boyutlar)** | 32 + Hareket 10 + Ses 6 | **en çok 48** |
| **Biçim** (bilinen boşluk) | 9:16 dikey gerçekten üretildi mi (letterbox yok), 720p okunurluk, süre ≥ 6 sn | geçti/kaldı |
| **Kredi** | kullanılabilir saniye başına kredi (G-0007 yöntemi) | sayı |

**Geçme önerisi (HİPOTEZ: ölçülmüş eşik değil, yaklaşık %70; Bora/Chief onayına tabi, Benchmark sonrası gözden geçirilir):** toplam ≥ 34/48 **ve** her karakterin tutarlılık puanı ≥ 6/10 (≈ 3 çapa tam okunur) **ve** kimlik kayması puanı ≥ 1/2 **ve** 9:16 geçti. En iyi model, geçerse A2 onayıyla Bölüm 1–3 üretimine (9 klip) taşınır; hiçbiri geçmezse tek karakterli sürüme (Muhalefet R1) dönülür. Tek örnek: sonuç kesin değil, yöntem bilgisidir (Kalite Standartları 11).
`benchmark.csv`'ye gerçek kredi ve puanlar yalnızca üretimden sonra yazılır.

## 4. Açık noktalar
- "3/C" kodu kurguda eklenir; modelin yazı üretimine güvenilmez.
- Damga ikonu (halka + anahtar deliği) küçük detay: 720p'de okunmazsa K8 yakın plan eklenir (ek klip = ek kredi, onay gerekir).
- Cetvel'in "X" jesti iki kanat çaprazı: modelin anatomisinde zor olabilir; K4 başarısızsa alternatif: tek kanat "hayır" sallama (jest ayrı bir Bible kararı, Chief'e danışılır).
