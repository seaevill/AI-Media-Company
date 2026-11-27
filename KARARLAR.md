# KARARLAR

Her satır: tarih · karar · kaynak · onaylayan. Geçmiş silinmez; değişen karar `hafiza/DEGISTIRILEN-KARARLAR.md`'ye taşınır ve buraya yeni satır yazılır. **Bora'nın burada cevapladığı soru tekrar sorulmaz.**

## Bora'nın kuruluşta verdiği kararlar (manifesto v1.0, 2026-11-27)
| # | Karar | Kaynak |
|---|---|---|
| K-001 | Şirketin hafızası bağımsız, **private** bir GitHub reposu (`AI-Media-Company`, geçici ad); Markdown + JSON + CSV. GitHub Wiki ve Notion ana hafıza değil | §06, §08 |
| K-002 | Öncelik sırası: 1 AI Media/Influencer → 2 kitleyi gelire dönüştürme → 3 AI Commercial Studio → 4 Micro-SaaS | §04 |
| K-003 | Bora'nın kişisel ilgi alanları içerik kategorisi seçiminde ölçüt değildir | §02 |
| K-004 | Ücretli üretim, gerçek yayın, dış iletişim ve yeni harcama için genel yetki yok | Kuruluş emri |
| K-005 | ALONI ve Two Islands Dallas'a dokunulmaz; özel verileri taşınmaz | §07 |
| K-006 | Tek zamanlanmış yönetici; başlangıç önerisi 3 saatte bir; ALONI kilit mantığı uyarlanır | §28 |
| K-007 | Gerçek yayın yetkisi başlangıçta Bora'dadır | §36 |
| K-008 | ChatGPT bağımsız dış denetçidir; bağlantı Bora üzerinden | §32 |
| K-009 | Supabase, Cloudflare, Notion şimdilik zorunlu değil | §06 |
| K-010 | Raporlar Türkçe, kısa, jargonsuz | §33 |

## Chief of Staff'ın kuruluşta aldığı mimari kararlar (Bora'nın itiraz hakkı açık)
| # | Karar | Gerekçe | Tarih |
|---|---|---|---|
| M-001 | Sıklık/sınır/bütçe tek kaynağı `vardiyalar/CONFIG.json`; `dogrula.py` başka dosyada sıklık sayısını yakalar | ALONI'de 3 saat / yoğun mod çelişkisi | 2026-11-27 |
| M-002 | Tek kuyruk `vardiyalar/DURUM.json` (takım başına ayrı kuyruk yok); takımlar yalnızca kendi `defter.md`'sine yazar | Anayasa 17; ALONI'nin tek-liste geçişi | 2026-11-27 |
| M-003 | Onay seviyeleri A0–A4 (`sirket/YETKI-MATRISI.md`); araştırma/dokümantasyon A0 önceden yetkili | Kuruluş emri + §30 | 2026-11-27 |
| M-004 | 7 çekirdek rol (Chief of Staff + 6 ajan); diğer 30+ rol çağrılabilir profil | Maliyet (§10) | 2026-11-27 |
| M-005 | Konseyler her mahkemede ayrı alt ajan bağlamında; profiller konsey içinde bölüm | Bağımsızlık ↔ maliyet dengesi | 2026-11-27 |
| M-006 | Kilit: ileri-yönlü `lock/medya` dalı, `--force-with-lease`; bayatlama süresi CONFIG'de | ALONI'de kanıtlanmış mekanizma | 2026-11-27 |
| M-007 | Manifestodaki klasör ağacının yalnızca aktif bölümleri açıldı; kalanlar ROADMAP'te | "Yüzlerce boş dosya yaratma" (§08) | 2026-11-27 |
| M-008 | Bekçi kararları `denetim/audit-logs/`'a SHA ile yazılır (uzak repo olunca PR yorumu da) | Madde 18, §31 | 2026-11-27 |
| M-009 | Medya dosyaları repoya girmez (`.gitignore` + `dogrula.py`) | §08 | 2026-11-27 |

## Bora'nın 2026-11-27 (kuruluş raporu sonrası) kararları
| # | Karar | Kaynak |
|---|---|---|
| K-011 | Uzak repo: https://github.com/seaevill/AI-Media-Company (private, Bora açtı) | Bora, sohbet, 2026-11-27 (K-B2) |
| K-012 | Kuruluş belgeleri **onaylandı**: ANAYASA (madde 1 ve 10'daki eklemeler dahil), sirket/, takımların kurallar.md dosyaları, BEKCI-KURALLARI, ONAY-PROTOKOLU ve dogrula.py koruma listesinin genişletilmesi | Bora, "2-Onaylıyorum", 2026-11-27 (K-B1) |
| K-013 | Ağ izinleri onaylandı: youtube.com, tiktok.com, trends.google.com, support.google.com, support.tiktok.com, help.instagram.com | Bora, "3-Onaylıyorum", 2026-11-27 (K-B3) |
| K-014 | G-0012 karakter tutarlılığı benchmark'ı: **en fazla 80 Higgsfield kredisi** (A2) | Bora, "4-Onaylıyorum", 2026-11-27 (K-B4) |
| K-015 | Higgsfield Ultra: aylık ~4.800 TL, 3.000 kredi (Bora beyanı, "galiba" — kesin değil) → yaklaşık 1,6 TL/kredi. Bora'nın gördüğü bakiye 1.938; araç 1.935,39 okudu | Bora, 2026-11-27 (K-B5) |
| K-016 | G-0012 test videolarına Bora'nın tepkisi: **"hiç komik değil ama animasyon fikri güzel, ses yerinde."** İlk gerçek insan geri bildirimi (tek kişi, kurucu; izleyici verisi değil) | Bora, sohbet, 2026-11-27 |
| K-017 | Harcanan kredi ve güncel bakiye CONFIG.json'dan çıkarılır; tek kaynak `finans/kredi-kayitlari.csv`. CONFIG yalnızca sınır/onay tutar | Bora, "3-evet", 2026-11-27 (K-B9) |
| K-018 | Dizi/hesap adı kararı ekibe devredildi ("uluslararası olunca gözlem ve veri sizin elinizde"). Ekip veriyle seçer, Bora'ya bilgi verir; hesap açma yine A3 | Bora, "4-…ekibe bırakıyorum", 2026-11-27 |
| K-019 | **Kalıcı kredi yetkisi:** "Kredi sıkıntım yok, sınırsız kullan." Higgsfield (ve bağlıysa Kling) plan kredileriyle üretim artık deney bazında ayrı onay gerektirmez. Kapsam ve güvenlik çizgileri `sirket/YETKI-MATRISI.md` kalıcı yetki #1. Ek kredi/paket satın alma ve yeni ücretli abonelik (nakit) bu yetkiye dahil değil | Bora, sohbet, 2026-11-27 |
| K-020 | Bora'nın yönlendirmesi: Üçüncü Kat dünyası **hesaptan çok film/hikâye için** güçlü olabilir ("güzel bir hikâyeyle tutabilir"); **3D her zaman daha iyi**. Stratejik sıra (K-002) değişmedi; hikâye odaklı format test edilecek (G-0025) | Bora, sohbet, 2026-11-27 |
| K-021 | **Çalışma adı: "Unit 3C"** (ekip kararı, K-018 yetkisiyle). Gerekçe: dizinin bağlayıcı gizemi (var olmayan 3/C dairesi), dilden bağımsız, film/hikâye yönüne uygun, @unit3c TikTok ve YouTube'da boş görünüyor; çakışma bulunamadı (arama özeti). Yedek: "Landing 3" (@landingthree). Elenenler: Floor Three (handle'lar dolu, Third Floor tescilleri), The Third Floor, Yunanca ad. Marka tescili araştırması gerçek hukukçu işi | Chief of Staff, 2026-11-27, `istihbarat/pazar-firsatlari/2026-11-27-isim-secimi.md` |
