# Kuru koşu A + B (eş zamanlı) — 2026-11-27 12:12–12:14 UTC

Ortam: yerel çıplak depo `/home/user/.ama-uzak.git` (gerçek GitHub reposu yok). İki ayrı alt ajan (sonnet), yalnızca YONETICI.md'yi uygulayarak, aynı anda başlatıldı; B 20 sn gecikmeli. Gerçek ücretli üretim, yayın, dış araç kullanımı: **yok**.

## Sonuçlar
| Test | Beklenen | Gerçek | Sonuç |
|---|---|---|---|
| A kilidi alır | `ALINDI` | `ALINDI d758c05` | ✅ |
| B taze kilidi görünce durur | çıkış 10 | `BASKA_KOSU_SURUYOR LOCK run=KURU-A-121226 (yaş 0 dk)`, çıkış 10 | ✅ |
| Eski görünümle ikinci alma reddedilir | push reddi | `! [rejected] (stale info)`, kilit dalı değişmedi | ✅ |
| A kilidi bırakır | `BIRAKILDI` | `BIRAKILDI cc58b2c` | ✅ |
| Doğru görevi seçer | onaylı, bağımlılığı tamam, en öncelikli | G-0007 (P4, A0) | ✅ (o anki kurala göre) |
| A2/A3 görevlerini almaz | onaysız → filtre | G-0010/11/12/13/18 gerekçesiyle atlandı | ✅ |
| Zamanı gelmemiş görevi almaz | `en_erken` | G-0016/17 atlandı | ✅ |
| Gereksiz ajan çağırmaz | kuru koşuda 0 | 0 | ✅ |
| Yetim yarım görevi fark eder | G-0006 in_progress | **Fark etmedi** → yeni görev aldı | ❌ → düzeltildi |

## Bulunan ve düzeltilen sorunlar
1. `kilit.sh` çalıştırma biti yoktu (126) → `chmod +x` + YONETICI'de `bash scripts/kilit.sh` + "0 dışındaki her kod = DUR".
2. Çıplak depo HEAD'i `master` → `git clone -b main` ve depo HEAD düzeltildi.
3. `ilk_kurulum` push hatasını yutuyordu → artık raporluyor, dal okunamazsa çıkış 13.
4. Etkileşimli oturum kontrolü kilitten sonraydı (gereksiz yazma) ve kendi commit'lerini ayırt edemiyordu → kilitten önceye alındı; vardiya commit'leri `Vardiya-Run:` satırı taşır.
5. **Seçici, `simdi` boşken `in_progress`/`review` görevleri görmüyordu** → kural 1b eklendi + 3 yeni test (14/14 geçti).
6. Vardiya ipucu gerekçesi yanıltıcıydı → eşleşme durumu yazılıyor.
7. DEVIR-TESLIM yoksa oluştur; yerel modda kayıt akışı; dosyaları tek tek okuma kuralı eklendi.

## Hâlâ açık
- Bayat kilit kuru koşuda test edilmedi (yalnızca `tests/test_kilit.sh` içinde `KILIT_BAYAT_DK=0` ile test edildi ✅).
- Etkileşimli oturum kilide uymak zorunda değil; CLAUDE.md "önce `kilit.sh durum`" diyor ama zorlayan mekanizma yok.
- PR akışı gerçek GitHub olmadan test edilemedi.

## İkinci koşu simülasyonu (aynı durumdan)
`tests/test_gorev_sec.py` "ikinci koşu bir sonraki görevi alır, tamamlananı değil" testi ✅. Düzeltmeden sonra gerçek DURUM.json ile seçici: `devam G-0001 (Bekçi denetimi bekliyor)` — yani bir sonraki vardiya önce denetimi bitirecek, yeni iş açmayacak. ✅
