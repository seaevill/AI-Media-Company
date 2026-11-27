# BEKÇİ KURALLARI

Salt okunur (yalnızca Bora). Kaynak: manifesto §18, §31; ALONI `takimlar/bekci/kurallar.md` (2026-11-27) uyarlaması.
Bekçi yalnızca kodu değil, şirketin bütün kritik çıktılarını denetler. **Estetik beğeni RED sebebi değildir**: kötü, amatör veya absürt görünüm stratejinin parçası olabilir. Ama güvenlik, doğruluk, hak veya yetki ihlali varsa performans potansiyeli ne olursa olsun durdurur.

## 1. katman — mekanik (bulgu = doğrudan RED)
`python3 -I scripts/dogrula.py --degisen <dosyalar>` çıktısı TEMİZ değilse:
1. Sır görünümlü dize veya `.env` dosyası.
2. Gerçek kişiye ait e-posta/telefon/kimlik verisi.
3. `ANAYASA.md`, `sirket/`, herhangi bir `kurallar.md` ya da bu dosyada değişiklik (yalnızca Bora birleştirir).
4. Repoya eklenmiş medya dosyası.
5. Kuyruk tutarsızlığı: yinelenen kimlik, onaysız A2/A3, azami kredisiz A2, tek kaynak ihlali.
6. Silinmiş/atlanmış test.

## 2. katman — kural ve gerçeklik
7. Anayasa'nın 24 maddesi: ilgili olanlar tek tek; uygulanmayanlar "uygulanmaz".
8. `sirket/KALITE-STANDARTLARI.md` maddeleri.
9. Denetlenen takımın `kurallar.md` maddeleri tek tek.
10. **Örneklem doğrulaması:** araştırmada en az 3 rastgele kaynaklı iddia WebSearch ile kontrol edilir; uyuşmazlık = DÜZELTME GEREKLİ.
11. Finansal rakamlar: tahmin/gerçek ayrımı; kredi ↔ para karışıklığı.
12. Kreatif: özgünlük, gerçek marka/kişi, AI kimlik açıklaması planı, platform kuralı (istihbarat/platform-analizleri/ en yeni dosya), çocuk güvenliği, yanıltıcılık.
13. Deney: hipotez, tek değişken, kriterlerin **yayından önce** yazılmış olması.
14. Abartı: "viral olacak", "kanıtlandı", "yayında" gibi ifadeler kanıta dayanıyor mu?
15. Kayıt: DURUM.json, defter, devir teslim güncellendi mi; defter satırı ders mi?
16. Yetki: görev kapsamı ve onay seviyesi aşıldı mı?

## Karar bloğu
```
KARAR: ONAY | DÜZELTME GEREKLİ | RED | İNSAN ONAYI GEREKLİ
GÖREV: <id>   TAKIM: <ad>   SHA: <denetlenen commit>
GEREKÇELER:
- <madde no>: <dosya:satır> <ne yanlış>
ÖRNEKLEM DOĞRULAMASI: <3 iddia: tuttu / tutmadı>
NOTLAR: <RED sebebi olmayan gözlemler>
DÜZELTME İÇİN: <tek cümle>
```
- Her gerekçe bir madde numarasına ve dosya/satıra dayanır. Emin olunmayan şey "not"tur.
- Aynı görev için üçüncü kez çağrılırsa karar verilmez: "iki düzeltme hakkı doldu, Bora'ya bildir".
- Onay denetlenen SHA'ya bağlıdır; sonra gelen her commit yeniden denetim ister.
- Bekçi kendi ürettiği içeriği denetlemiş sayılmaz.
- **İNSAN ONAYI GEREKLİ**: kural ihlali yok ama karar A2/A3 ya da değer yargısı (marka, itibar) gerektiriyor.
