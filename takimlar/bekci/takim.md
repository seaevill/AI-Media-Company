# Takım: bekci

**Görev:** Bağımsız denetim.

**Ajan:** `.claude/agents/bekci.md`

**Koşu adımları:**

1. Okuma sırası (ajan dosyası).
2. 1. katman mekanik kontrol: `python3 -I scripts/dogrula.py --degisen <dosyalar>`.
3. 2. katman kural kontrolü (BEKCI-KURALLARI §2).
4. Örneklem doğrulaması (en az 3 iddia).
5. Karar bloğu + defter.

**Çıktı sonrası:** Bekçi denetimi; `defter.md`'ye tek ders.
