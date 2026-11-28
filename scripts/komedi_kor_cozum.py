import json,statistics as st
P="""S01 2 3 2
S02 4 4 2
S03 4 3 2
S04 2 2 1
S05 4 4 4
S06 4 4 3
S07 4 5 3
S08 3 4 3
S09 4 4 4
S10 4 4 3
S11 4 5 4
S12 3 3 2
S13 4 4 3
S14 4 4 3
S15 4 4 3
S16 3 3 2
S17 5 5 3
S18 3 3 2"""
puan={l.split()[0]:list(map(int,l.split()[1:])) for l in P.splitlines()}
key=json.load(open('denetim/komedi-beceri/kor_anahtar_PUANLAMADAN_ONCE_ACMA.json'))
best=["S09","S14","S11","S08","S17","S07"]
def rapor(haric=()):
    out={}
    for c in ('temel','sonra'):
        ids=[s for s in puan if key[s]['kosul']==c and s not in haric]
        tot=[sum(puan[s]) for s in ids]
        r={"n":len(ids),"toplam_ort":round(st.mean(tot),2),"toplam_medyan":st.median(tot)}
        for i,k in enumerate("ABC"): r[k+"_ort"]=round(st.mean(puan[s][i] for s in ids),2); r[k+"_medyan"]=st.median(puan[s][i] for s in ids)
        for b in (1,2,3):
            bi=[sum(puan[s]) for s in ids if key[s]['brief']==b]
            r[f"brief{b}_ort"]=round(st.mean(bi),2) if bi else None; r[f"brief{b}_n"]=len(bi)
        r["en_iyi_sayisi"]=sum(1 for s in best if s in ids)
        out[c]=r
    return out
print(json.dumps({s:[key[s]['kosul'],key[s]['brief'],sum(puan[s])] for s in sorted(puan)},ensure_ascii=False))
print("TUM",json.dumps(rapor(),ensure_ascii=False))
print("S02S03_HARIC",json.dumps(rapor(("S02","S03")),ensure_ascii=False))
print("S02",key["S02"],"S03",key["S03"])
