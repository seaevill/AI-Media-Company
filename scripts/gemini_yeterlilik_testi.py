import json,os,sys,time,urllib.request,urllib.error
K=os.environ["GEMINI_API_KEY"]; B="https://generativelanguage.googleapis.com"
M=sys.argv[1] if len(sys.argv)>1 else "gemini-2.5-flash"
OUT=os.path.dirname(os.path.abspath(__file__))
def req(url,data=None,headers=None,method=None):
    h={"x-goog-api-key":K}; h.update(headers or {})
    r=urllib.request.Request(url,data=data,headers=h,method=method)
    with urllib.request.urlopen(r,timeout=300) as f: return f.read(), dict(f.headers)
def upload(path):
    size=os.path.getsize(path)
    _,h=req(B+"/upload/v1beta/files",json.dumps({"file":{"display_name":os.path.basename(path)}}).encode(),
        {"X-Goog-Upload-Protocol":"resumable","X-Goog-Upload-Command":"start","X-Goog-Upload-Header-Content-Length":str(size),"X-Goog-Upload-Header-Content-Type":"video/mp4","Content-Type":"application/json"})
    url=h.get("X-Goog-Upload-URL") or h.get("x-goog-upload-url") or h.get("X-Goog-Upload-Control-Url") or h.get("x-goog-upload-control-url")
    body,_=req(url,open(path,"rb").read(),{"X-Goog-Upload-Offset":"0","X-Goog-Upload-Command":"upload, finalize","Content-Length":str(size)})
    f=json.loads(body)["file"]
    while f.get("state")=="PROCESSING":
        time.sleep(3); f=json.loads(req(B+"/v1beta/"+f["name"])[0])
    return f["uri"]
PROMPT="""Bu kısa videoyu kare kare izle ve SADECE gözlemle cevap ver, JSON:
{"sure_sn":..,"karakterler":[{"tanim":..,"sayi":..}],
 "olaylar":[{"bas_sn":..,"bit_sn":..,"ne_oluyor":..}],
 "gorsel_hatalar":[{"bas_sn":..,"bit_sn":..,"tur":"iç içe geçme|kaybolma|çoğalma|morf|yüzen nesne|kopma|anatomi|diğer","aciklama":..,"guven":"yüksek|orta|düşük"}],
 "ses":{"var_mi":..,"konusma":"yok ya da birebir transkript","muzik":..,"efektler":[{"t_sn":..,"ne":..}]},
 "ekranda_yazi":..}
Emin olmadığını yazma ya da guven:düşük de. Zaman damgaları saniye, ondalıklı."""
def analiz(part,ad,deneme=0):
    body={"contents":[{"parts":[part,{"text":PROMPT}]}],"generationConfig":{"responseMimeType":"application/json","temperature":0}}
    t=time.time()
    try: r,_=req(f"{B}/v1beta/models/{M}:generateContent",json.dumps(body).encode(),{"Content-Type":"application/json"})
    except urllib.error.HTTPError as e:
        if e.code in (429,500,503) and deneme<4: time.sleep(20*(deneme+1)); return analiz(part,ad,deneme+1)
        raise
    d=json.loads(r); txt=d["candidates"][0]["content"]["parts"][0]["text"]; u=d.get("usageMetadata",{})
    json.dump({"ad":ad,"model":M,"sure_istek_sn":round(time.time()-t,1),"usage":u,"cevap":json.loads(txt)},open(f"{OUT}/{ad}.json","w"),ensure_ascii=False,indent=1)
    print(ad,"ok",u.get("totalTokenCount"))
V=os.environ.get("VIDEO_KLASOR","").rstrip("/")+"/"  # yerel MP4 klasörü (medya repoya girmez)
import os.path
for ad in ("kapiA","flash","tikirti","hailuo"):
    if os.path.exists(f"{OUT}/yerel_{ad}.json"): continue
    try: analiz({"file_data":{"mime_type":"video/mp4","file_uri":upload(V+ad+".mp4")}},"yerel_"+ad)
    except Exception as e: print(ad,"HATA",str(e)[:200])
try: analiz({"file_data":{"file_uri":"https://www.youtube.com/watch?v=jNQXAC9IVRw"}},"youtube_jNQXAC9IVRw")
except Exception as e: print("youtube HATA",str(e)[:300])
