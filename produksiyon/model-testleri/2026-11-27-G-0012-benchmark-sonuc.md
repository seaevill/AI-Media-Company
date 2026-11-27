# G-0012 — Karakter tutarlılığı benchmark'ı: sonuç (2026-11-27)

Onay: Bora, 2026-11-27, max 80 kredi (K-014). Plan: `produksiyon/storyboard/2026-11-27-ucuncu-kat-b1.md` §3 (Bekçi ONAY @ 8f4548a).
**Gerçek harcama: 58,00 kredi** (bakiye 1.935,39 → 1.877,39; tahminlerle birebir). Tekrar yapılmadı. ≈ 93 TL (~1,6 TL/kredi beyanına göre).
**Plan sapması (harcamadan önce plan dosyasına yazılmadı — Bekçi notu; bundan sonra sapma önce plana yazılır):** Hailuo 2.3-fast ayrı referans görsel kabul etmiyor, yalnızca başlangıç karesi alıyor → üç referansla bir başlangıç karesi üretildi (+1,5 kredi). Planlanan 56,5 → gerçek 58,0; 70 iç tavanının ve 80 onayının altında.

## Üretimler (Higgsfield iş kimlikleri; medya repoda değil)
| Kalem | Model | Kredi | İş kimliği |
|---|---|---:|---|
| Referans: Tomruk | Nano Banana 2 (sunucu adı nano_banana_flash) | 1,5 | 5dd7fd90-16b1-4022-9d94-627af25bb4f8 |
| Referans: Cetvel | 〃 | 1,5 | 04e8e740-bdab-4829-9398-70d63d740fae |
| Referans: Anahtar | 〃 | 1,5 | acf5ff3e-7d37-41bf-929f-d4f3beaa26f0 |
| Başlangıç karesi (Hailuo için) | 〃 | 1,5 | efdb2c48-be26-4e76-99e4-c711059e7556 |
| Video A | Seedance 2.0 Mini, 8 sn, 720p, ses | 8 | 828f339f-6be2-420b-bea1-dc942bd8bf3d |
| Video B | Seedance 2.5 Flash, omni_reference, 8 sn, 720p, ses | 40 | 918c8ec7-5d20-42cd-ac83-efb6cca8f58b |
| Video C | Minimax Hailuo 2.3-fast, 6 sn, 768 | 4 | 336158d9-f948-4669-86e1-d9e43528a025 |

## Teknik ölçümler (ffprobe — nesnel)
| | Çözünürlük | Süre | Ses kanalı | Ses düzeyi (ortalama / tepe) |
|---|---|---|---|---|
| Mini | 720×1280 (9:16) | 8,04 sn | var | −24,7 / −2,3 dB |
| Flash | 720×1280 (9:16) | 8,04 sn | var | −23,3 / −1,3 dB |
| Hailuo | 768×1376 (~9:16) | 5,88 sn | **yok** | — |

## Puanlar (cetvel §3; değerlendiren: Chief of Staff, saniyede 1 karelik döşeme görüntüsünden, **tek değerlendirici, ses dinlenmedi**)
| Boyut (en çok) | Mini | Flash | Hailuo |
|---|---:|---:|---:|
| Tomruk (10) | 6 | 6 | 5 |
| Cetvel (10) | 5 | 6 | 5 |
| Anahtar (10) | 8 | 8 | 7 |
| Kimlik kayması (2) | 2 | 2 | 1 |
| **Tutarlılık (32)** | **21** | **22** | **18** |
| Hareket (10): koli / metre / bağımsız hareket / derinlik / damga | 2/1/1/1/2 = **7** | 2/1/1/1/1 = **6** | 0/1/0/2/1 = **4** |
| Ses (6) | ölçülmedi | ölçülmedi | **0** (kanal yok) |
| **Toplam (ses hariç 42 üzerinden)** | **28** | **28** | **22** |
| Ses tam puan alsa bile (48) | 34 | 34 | 22 |
| Biçim (9:16, ≥6 sn) | geçti | geçti | geçti (sınırda) |
| **Kullanılabilir saniye başına kredi** | **1,0** | **5,0** | — (kullanılamaz) |

Eşik (HİPOTEZ) ≥34/48: **net geçen yok.** Chief of Staff puanıyla Mini ve Flash ancak sesten tam puan alırlarsa eşiğe ulaşıyor; **Bekçi'nin bağımsız puanıyla (Mini ≈26–27, Flash ≈24–25 / 42) ses tam puan alsa bile ikisi de eşiğin altında** (`denetim/audit-logs/2026-11-27-G-0012.md`). Hailuo kaldı. Puanlar arasındaki fark tek değerlendiricinin sınırını gösteriyor; en zayıf karakter iki değerlendirmede de Cetvel (flamingo küçük, S boyun/gözlük okunmuyor).

## Gözlemler
- Mini ve Flash neredeyse aynı kompozisyonu ve kimlikleri üretti; ayırt edici fark görülmedi → **aynı sonuç için 5 kat fiyat farkı.**
- İkisi de "yukarıdan, üç kat" kamerasını uygulamadı (önden, tek kat merdiven); flamingo küçük ve kambur kaldı; vombat ayı/kedi silüetine kaydı (Tomruk'un "yuvarlak ağır gövde, geniş burun" çapası zayıf; kulak çentiği referansta bile görünmüyor).
- Şerit metrenin "kopup uçması" iki Seedance'te de belirsiz (Flash'ta sonunda kolinin üstüne düşüyor, Mini'de kayboluyor).
- Hailuo başlangıç karesinin üç katlı kompozisyonunu korudu ama nesne sürekliliği çöktü (koli çoğaldı, flamingo uçtu/deforme oldu) ve ses üretmedi.
- Başlangıç karesi (Nano Banana 2, 1,5 kredi) kompozisyonu en iyi tutan çıktı oldu → **ilk kare + referans** birlikte kullanılırsa Seedance'in kamera sorunu çözülebilir (hipotez).

## Karar önerisi (madde 1–2 yön gösterir; madde 3–4 yeni A2 onayı gerektirir)
1. Üretim modeli **adayı: Seedance 2.0 Mini** (gözlenen maliyet 1,0 kredi/sn; eşiği geçmedi, ama Flash'tan kötü değil — iki değerlendirmede de Mini ≥ Flash). Flash için 5 kat fiyatı haklı çıkaracak bir fark görülmedi.
2. Hailuo 2.3-fast bu format için kullanılmaz (ses yok, fizik bozuk).
3. Sonraki ucuz test (≤ 10 kredi, yeni A2 gerekir): Mini'ye referanslar + başlangıç karesi birlikte → kamera/kompozisyon tutuyor mu?
4. Tomruk ve Cetvel referansları yeniden çizilmeli (Tomruk: daha yuvarlak, daha "vombat", kulak çentiği; Cetvel: kadrajda büyük, S boyun ve gözlük okunur) — ~3 kredi, **yeni A2 gerekir**.
5. Ses puanı için videolar bir insan tarafından dinlenmeli (Bora ya da ileride gerçek izleyici testi).

## Sınırlar
Tek örnek, tek değerlendirici, ses dinlenmedi. Hailuo'ya ek olarak başlangıç karesi verildi; girdi eşit değil, kıyas bu yüzden tam adil değil. Sonuç kesin değil; yöntem bilgisidir (Kalite Standartları 11).

## Bora'nın değerlendirmesi (K-016, 2026-11-27)
- **Komedi: "hiç komik değil."** Test sahnesi bir gag olarak çalışmadı.
- **Görsel/animasyon fikri: "güzel."**
- **Ses: "yerinde."** (Ses puanı için tek insan değerlendirmesi: kabul edilebilir; nicel puan verilmedi.)
Yorum: Sorun model/üretim değil, **senaryo ve zamanlama**. Sonraki kredi harcaması komedi kâğıt üzerinde çözülmeden yapılmamalı.

## Bütçe sayacı
Harcanan toplam ve güncel bakiyenin tek kaynağı `finans/kredi-kayitlari.csv` (bu görev: 58,00; bakiye 1.877,39). `CONFIG.json`'daki `harcanan_kredi_toplam`/`bakiye_gozlenen` alanları korunan dosyada olduğu için ajanlar güncelleyemez; bu alanlar Bora onayıyla CONFIG'den çıkarıldı (K-017).
