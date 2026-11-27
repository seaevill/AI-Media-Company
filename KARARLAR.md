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
