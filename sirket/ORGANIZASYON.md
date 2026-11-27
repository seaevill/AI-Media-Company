# ORGANİZASYON

Kaynak: manifesto §10, §34. İlke: **herkes sürekli çalışan ayrı ajan değildir.** 7 çekirdek ajan + çağrılabilir uzmanlık profilleri. Profiller ilgili çekirdek ajanın içinde, görev bazında ve **ayrı bölümler halinde** çalışır; gerçek bağımsızlık gereken kritik incelemelerde (konseyler, Bekçi) ayrı alt ajan bağlamı kullanılır.

## Şema (hedef yapı) ve bugünkü karşılığı

```text
FOUNDER — BORA
└── CHIEF OF STAFF / COO  ............................ ana oturum + vardiya yöneticisi
    ├── STRATEGY & INTELLIGENCE ...................... ajan: pazar-istihbarati
    │   Market Research · Trend Hunter · Competitor Intelligence · Early Signal Analyst · Platform Intelligence  (profil)
    ├── FOUR INDEPENDENT COUNCILS .................... ajan: konsey-koordinatoru
    │   Uzman · Creator · Tüketici · Muhalefet  (her biri ayrı alt ajan bağlamında)
    ├── CREATIVE DEPARTMENT .......................... ajan: kreatif-direktor
    │   Creative Director · Character Architect · Scriptwriter · Chaos Director · Storytelling Specialist  (profil)
    ├── PRODUCTION DEPARTMENT ........................ ajan: produksiyon-maliyet
    │   Higgsfield Specialist · Visual Director · Video Editor · Production Engineer  (profil)
    ├── GROWTH & DISTRIBUTION ........................ (Aşama 1 yayın onayı gelene kadar pasif; kreatif + analitik-gelir içinde profil)
    │   Growth Strategist · Platform Specialist · Community Analyst · Localization Specialist
    ├── MONETIZATION ................................. ajan: analitik-gelir
    │   Monetization Strategist · Digital Product · Affiliate · Commercial Partnerships  (profil)
    ├── DATA & FINANCE ............................... ajan: analitik-gelir + produksiyon-maliyet
    │   Performance Analyst · Experiment Designer · Financial Analyst · Cost Controller  (profil)
    └── INDEPENDENT AUDIT ............................ ajan: bekci
        Bekçi · Fact Checker · Reputation Analyst · Compliance Reviewer · Failure Investigator  (profil)
```

## Çekirdek ajanlar

| Ajan | Dosya | Model (varsayılan) | Ne zaman çağrılır | Başarı ölçütü |
|---|---|---|---|---|
| pazar-istihbarati | `.claude/agents/pazar-istihbarati.md` | sonnet | Araştırma görevleri (P4) | Kaynaklı kart sayısı değil; sonraki deney kararını değiştiren bulgu |
| kreatif-direktor | `.claude/agents/kreatif-direktor.md` | sonnet | Konsept/karakter/senaryo görevleri (P5) | Mahkemeden "deney adayı" çıkan fikir oranı; sonra gerçek performans |
| konsey-koordinatoru | `.claude/agents/konsey-koordinatoru.md` | sonnet (konsey alt bağlamları haiku/sonnet) | Mahkeme gerektiren fikirler | Tahminlerin gerçek sonuçlarla isabeti (`hafiza/` kalibrasyon tablosu) |
| produksiyon-maliyet | `.claude/agents/produksiyon-maliyet.md` | sonnet | Üretim hazırlığı, kredi tahmini, onaylı üretim | Kullanılabilir video başına gerçek kredi |
| analitik-gelir | `.claude/agents/analitik-gelir.md` | sonnet | Ölçüm zamanı gelen deneyler (P3), gelir haritası | Kararı değiştiren ölçüm; tahmin/gerçek ayrımı |
| bekci | `.claude/agents/bekci.md` | sonnet | Her kritik çıktı | Kaçırılan hata sayısı (haftalık denetimde) |

Model seçimi maliyet içindir: varsayılan `sonnet`; tek seferlik basit profil tarama işleri `haiku` olabilir; `opus` yalnızca gerekçeyle (STRATEJİ değişikliği, haftalık yönetim değerlendirmesi).

## Yeni rol açma (İşe Alım Protokolü)

Bkz. `sirket/ISE-ALIM-PROTOKOLU.md`. Yeni ajan dosyası açmak A0'dır ama ancak protokoldeki 7 soru yazılı cevaplanmışsa; çekirdek dışı her ajan haftalık denetimde "tut / birleştir / arşivle" kararına girer.

## Gerçek insan gereken yerler

Vergi/şirket kuruluşu, sözleşme, telif/marka tescili hukuki görüşü, gerçek tüketici araştırması (anket/görüşme). Bir AI profili bu sorumlulukları taşıyamaz; gerektiğinde raporda açıkça "gerçek uzman gerekiyor" yazılır.
