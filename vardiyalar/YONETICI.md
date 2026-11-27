# VARDİYA YÖNETİCİSİ — tek zamanlanmış koşucu

Kaynak: manifesto §28–§30; ALONI `docs/autopilot/YONETICI.md` (2026-11-27 sürümü) uyarlaması.
Tek bir zamanlanmış görev («Medya yönetici») her tetiklendiğinde **yeni bir oturumda** bu dosyayı uygular. Departman başına ayrı zamanlayıcı yoktur.
**Sıklık, günlük sınırlar, kilit süresi ve bütçe bu dosyada yazılmaz; tek kaynak `vardiyalar/CONFIG.json`.** (`scripts/dogrula.py` bunu kontrol eder.)
ANAYASA.md, sirket/YETKI-MATRISI.md ve CLAUDE.md bu dosyanın üstündedir.

## 0. Kurulum
```
git clone --depth 50 -b main https://github.com/seaevill/AI-Media-Company AI-Media-Company && cd AI-Media-Company
git config push.negotiate false
RUN=$(date -u +%Y%m%d-%H%M)
```
**Kuru koşu:** tetik metni `KURU KOŞU` ile başlıyorsa 1–4. adımlar + kilit kanıtı (eski görünümle ikinci alma denemesi reddedilmeli) yapılır; kilit commit'leri ve `vardiyalar/run-logs/` dışında hiçbir şey yazılmaz; "ne yapardım" cevabı verilir.

## 1. Etkileşimli oturum kontrolü (kilitten ÖNCE, salt okuma)
`main`'de son `limitler.etkilesimli_oturum_sessizlik_dakika` içinde, mesajında `Vardiya-Run:` satırı OLMAYAN bir commit varsa: "Claude Code aktif – müdahale yok" yaz ve DUR (hiçbir şey yazmadan). Vardiya yöneticisinin kendi commit'leri her zaman `Vardiya-Run: <RUN>` satırı taşır. Kuruluş gibi etkileşimli bir oturumun hemen ardından gelen koşunun durması **beklenen davranıştır**.

## 1b. Kilit (aynı anda tek koşucu)
`bash scripts/kilit.sh al $RUN`
- **Çıkış kodu 0 değilse DUR.** 10 = taze LOCK var ("başka koşu sürüyor"), 11 = yarışı kaybetti, diğer her kod = kilit hatası (raporla, BLOCKERS'a yaz).
- Bayat kilit devralındıysa (çıktıda `BAYAT_KILIT_DEVRALINIYOR`) raporda söyle.
**Kilit alındıysa her çıkışta (hata dahil) en son adım:** `bash scripts/kilit.sh birak $RUN`.

## 2. Oku (bu sırayla)
Her dosyayı **ayrı** oku (toplu çıktı kırpılır; kuru koşu A dersi). Bir dosyayı tam okuyamadıysan raporda söyle.
`ANAYASA.md` → `sirket/AJAN-KIMLIGI.md` → `VIZYON.md` → `sirket/YETKI-MATRISI.md` → `vardiyalar/CONFIG.json` → `vardiyalar/DURUM.json` → `vardiyalar/DEVIR-TESLIM.md` → `vardiyalar/BLOCKERS.md` → `hafiza/OGRENILEN-DERSLER.md` (son 10 satır) → seçilen görevin takımının `takim.md`, `kurallar.md`, `defter.md`.

## 3. Gerçeği doğrula (tahmin yok)
Son tamamlanan görev; `simdi` alanı; açık PR'lar; Bora onayı bekleyen kararlar; zamanı gelmiş ölçümler (`deneyler/experiment-registry.json` > `olcum_zamani`); güncel kredi bakiyesi (A2 görev seçildiyse Higgsfield `balance` — salt okuma); başka oturumun aynı görevde çalışıp çalışmadığı.

## 4. Tek görev seç
`python3 -I scripts/gorev_sec.py` çalıştır ve kararına uy:
- `devam` → yarım görevi bitir (yeni görev alınmaz). `simdi` boş olsa bile `in_progress`/`review`/`needs_revision` durumundaki görev yarım sayılır; `review` ise yalnızca Bekçi denetimi (6. adım) yapılır.
- `gorev` → görevi `simdi`'ye taşı, `durum=in_progress`, `deneme+1`, `gunluk.ajanli_kosu+1`.
- `is_yok` / `sinir` → ajan çağırma; 7. adımdan yalnızca `son_kosu`/`gunluk` + run-log, 8. adımda tek satır rapor, DUR (Anayasa 21).
- `engel` → görevi `blocked` yap, soruyu `bekleyen_kararlar`'a yaz.

Seçicinin sırası: yarım iş → günlük sınır → filtre (durum ∈ approved/queued/needs_revision, `onay` dolu, deneme < azami, bağımlılıklar tamam, `en_erken` geçmiş) → öncelik P0…P7 → vardiya ipucu (CONFIG `vardiya_ipuclari`) → oluşturma tarihi.
Öncelikler: **P0** güvenlik/maliyet aşımı/hesap riski · **P1** başlamış işi bitirmek · **P2** onaylı yüksek değerli deney · **P3** zamanı gelen ölçüm · **P4** pazar araştırması · **P5** kreatif hipotez · **P6** sistem iyileştirme · **P7** bakım/dokümantasyon.
Onay gerektiren görev onaysızsa alınmaz; bağımsız başka onaylı görev varsa ona geçilir. Vardiya saatine uymak için daha değerli iş bekletilmez.

## 5. Uzman görevlendir
Repo ajanları yeni klonda ajan türü olarak yüklenmeyebilir: `general-purpose` alt ajan başlat, `.claude/agents/<ajan>.md` gövdesini kimlik olarak **aynen** ver, ardından yalnızca görev kimliğini, beklenen çıktıyı, kaynak sınırını ve başarı kriterini yaz. Koşu başına alt ajan sınırı CONFIG'dedir. Gereksiz ajan çağırma.
İçerik Mahkemesi gerekiyorsa `/mahkeme` akışını uygula (konseyler ayrı bağlamlarda, birbirini görmeden).

## 6. Bekçi
`.claude/agents/bekci.md` ile ayrı alt ajan. Girdi: görev kimliği, değişen dosyalar (`git diff --name-only`), commit SHA. Bekçi önce `python3 -I scripts/dogrula.py --degisen <dosyalar>` çalıştırır.
Karar: **ONAY · DÜZELTME GEREKLİ · RED · İNSAN ONAYI GEREKLİ**. Karar bloğu `denetim/audit-logs/<RUN>-<gorev>.md` dosyasına aynen yazılır ve `SHA:` satırı içerir. Denetlenen SHA'dan sonra yeni commit gelirse onay geçersizdir, yeniden denetim gerekir.
DÜZELTME GEREKLİ → gerekçeler aynen takıma, en fazla CONFIG `bekci_duzeltme_hakki` kez. Sonra hâlâ olmuyorsa görev `blocked`, engel `BLOCKERS.md`'ye.

## 7. Kayıt
- `DURUM.json`: görev `durum`, `son_calisma`, `gercek_maliyet`, `bekci_karari`, `sonraki_guvenli_adim`; `simdi`; `son_kosu`; `gunluk`.
- İlgili çıktılar (araştırma, deney, karakter, finans CSV).
- Ajan çalıştıysa ilgili `takimlar/<takim>/defter.md` dosyasına tek ders; şirket çapında önemliyse `hafiza/OGRENILEN-DERSLER.md`.
- `vardiyalar/run-logs/<RUN>.md`: okunan dosyalar, seçici çıktısı, çağrılan ajanlar, Bekçi kararı, kaynak kullanımı.
- Her commit mesajı `Vardiya-Run: $RUN` satırı içerir.
- Uzak repo yoksa (yerel mod): commit doğrudan `main`'e, Bekçi kaydı audit-logs'ta.
- Uzak repo varsa: kayıt dalı `kayit/<RUN>` → PR; Bekçi ONAY + `dogrula.py` temiz → birleştir. Korunan dosya içeren PR birleştirilmez, Bora'ya bırakılır.

## 8. Devir teslim ve rapor
`vardiyalar/DEVIR-TESLIM.md` (yoksa oluştur) en üstüne: ne yapıldı · ne öğrenildi · ne tamamlanmadı · kullanılan kaynak · bekleyen onaylar · en mantıklı sonraki görev.
`raporlar/vardiya/<RUN>.md`: `raporlar/templates/VARDIYA-RAPORU.md` biçiminde, Türkçe, 7 başlık. Hiçbir şey yapılmadıysa nedenini tek satırla yaz.

## 9. Dur
Kilidi bırak. Yeni görev icat etme. Son cevap (bildirim olur): Türkçe, en fazla 5 satır — ne tamamlandı, fayda, kaynak, Bora'dan gereken karar.

## Kesin duruşlar (Bora'ya sor, asla yapma)
A2 onaysız kredi harcamak · A3 her işlem (yayın, hesap, dış mesaj, ödeme, ürün yayına alma, zamanlayıcı değiştirme) · ANAYASA/sirket/kurallar.md değiştirmek · ALONI veya Two Islands Dallas'a dokunmak · platform korumalarını aşmak.

## Görev alanları
`id` (G-0001) · `baslik` · `kaynak` · `olusturma` · `oncelik` (P0–P7) · `departman` · `sorumlu_ajan` · `onay_seviyesi` (A0–A3) · `onay` (A0 ya da "Bora, tarih, kapsam[, max N kredi]") · `bagimliliklar` · `beklenen_cikti` · `basari_kriteri` · `azami_maliyet` · `gercek_maliyet` · `deneme` · `durum` · `en_erken` · `ilgili_dosyalar` · `ilgili_pr` · `bekci_karari` · `son_calisma` · `sonraki_guvenli_adim` · `surum`.
Durumlar: `proposed` → `approved` → `queued` → `in_progress` → `review` → (`needs_revision`) → `completed`; yan yollar `waiting_owner`, `blocked`, `cancelled`, `archived`.
Tamamlanan görev yeniden açılmaz; yeni veri gerekiyorsa yeni kimlik ya da `surum+1`.
