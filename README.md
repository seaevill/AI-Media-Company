# AI-Media-Company (geçici iç proje adı)

Yapay zekâ destekli dijital medya şirketinin kalıcı hafızası ve işletim sistemi. Halka açık marka adı henüz belirlenmedi.

**Amaç:** gerçek pazar talebini araştıran, düşük maliyetli deneyler yapan, AI karakterler ve medya varlıkları üretip bunları sürdürülebilir gelire dönüştüren bir şirket. Ayrıntı: `VIZYON.md`, `STRATEJI.md`. Kurucu metnin birebir kopyası: `arsiv/KURULUS-MANIFESTOSU-v1.0.md`.

## Nereden başlamalı

| Kim | Ne okur |
|---|---|
| Bora | `raporlar/patron-ozeti/` (en yeni dosya) → `vardiyalar/DURUM.json` içindeki `bekleyen_kararlar` |
| Her ajan | `CLAUDE.md` → `ANAYASA.md` → `sirket/AJAN-KIMLIGI.md` |
| Vardiya yöneticisi | `vardiyalar/YONETICI.md` |
| Dış denetçi (ChatGPT/Codex) | `denetim/dis-denetim/` altındaki en yeni paket |

## Klasörler (aktif olanlar)

```
ANAYASA · VIZYON · STRATEJI · KARARLAR · ROADMAP   şirketin temel belgeleri
sirket/            kimlik, organizasyon, yetki, işe alım, toplantı, kalite (salt okunur)
konseyler/         Uzman · Creator · Tüketici · Muhalefet konseyleri + İçerik Mahkemesi
takimlar/          her çekirdek ajanın takim.md / kurallar.md / defter.md dosyası
istihbarat/        araştırma kartları, trend radarı, platform analizleri, kaynaklar
toplantilar/       mahkeme tutanakları ve kararları
deneyler/          deney şablonu, deney kayıt defteri (experiment-registry.json)
karakterler/       Character Bible şablonu, aday karakterler
produksiyon/       model testleri (benchmark)
finans/            bütçe, kredi ve gelir-gider kayıtları
hafiza/            öğrenilen dersler, başarısızlıklar, hipotezler, kanıtlanmış yöntemler
vardiyalar/        YONETICI, CONFIG (tek sayı kaynağı), DURUM (tek görev kuyruğu), devir teslim, engeller, koşu kayıtları
raporlar/          vardiya / günlük / haftalık / aylık / patron özeti
denetim/           Bekçi kuralları, onay protokolü, denetim kayıtları, dış denetim paketleri
scripts/           kilit.sh, gorev_sec.py, dogrula.py  (tests/ altında testleri)
.claude/           ajanlar ve komutlar
```

Manifestodaki tam ağaçtaki diğer klasörler (`medya-varliklari/`, `dagitim/`, `analytics/`, `monetization/` alt dalları vb.) **ilgili departman aktifleşince** açılır (`ROADMAP.md`). Boş klasör ve göstermelik dosya üretilmez.

## Medya dosyaları

Video/görsel dosyaları GitHub'a yüklenmez. Üretimler Higgsfield/Kling hesabında kalır; repoya yalnızca üretim kimliği, prompt, model, maliyet ve sonuç yazılır. Kalıcı depolama yöntemi (ör. Cloudflare R2) ilk gerçek üretimden önce kararlaştırılacak.

## Testler

```bash
python3 -I tests/test_gorev_sec.py && bash tests/test_kilit.sh && python3 -I scripts/dogrula.py
```
