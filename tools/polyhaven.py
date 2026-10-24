import json, os, sys, urllib.request
UA = {"User-Agent": "iron-swarm-asset-fetch/1.0"}
def get(u):
    return urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=60).read()
def save(u, p):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, "wb").write(get(u))
stage = sys.argv[1]
if stage == "catalog":
    tex = json.loads(get("https://api.polyhaven.com/assets?t=textures"))
    words = ["sand", "desert", "cliff", "sandstone", "canyon", "arid", "red rock", "rock", "gravel", "dry", "mud", "laterite"]
    cat = {}
    for k, v in tex.items():
        blob = " ".join([k, v.get("name", "")] + v.get("tags", []) + v.get("categories", [])).lower()
        if any(w in blob for w in words):
            cat[k] = {"name": v.get("name"), "tags": v.get("tags", []), "cats": v.get("categories", [])}
    os.makedirs("assets/catalog/tex", exist_ok=True)
    json.dump(cat, open("assets/catalog/textures.json", "w"), indent=1)
    for k in list(cat)[:90]:
        try: save(f"https://cdn.polyhaven.com/asset_img/thumbs/{k}.png?width=160&height=160", f"assets/catalog/tex/{k}.png")
        except Exception as e: print("thumb fail", k, e)
    hd = json.loads(get("https://api.polyhaven.com/assets?t=hdris"))
    hc = {}
    for k, v in hd.items():
        blob = " ".join([k, v.get("name", "")] + v.get("tags", []) + v.get("categories", [])).lower()
        if ("sunset" in blob or "dusk" in blob or "evening" in blob) and ("outdoor" in blob or "nature" in blob or "skies" in blob):
            hc[k] = {"name": v.get("name"), "tags": v.get("tags", [])}
    os.makedirs("assets/catalog/hdri", exist_ok=True)
    json.dump(hc, open("assets/catalog/hdris.json", "w"), indent=1)
    for k in list(hc)[:40]:
        try: save(f"https://cdn.polyhaven.com/asset_img/thumbs/{k}.png?width=256&height=128", f"assets/catalog/hdri/{k}.png")
        except Exception as e: print("thumb fail", k, e)
else:
    ids = [i.strip() for i in sys.argv[2].split(",") if i.strip()]
    hdri = sys.argv[3].strip() if len(sys.argv) > 3 else ""
    for i in ids:
        files = json.loads(get(f"https://api.polyhaven.com/files/{i}"))
        for m, key in [("diff", "Diffuse"), ("nor", "nor_gl"), ("rough", "Rough"), ("arm", "arm")]:
            node = files.get(key)
            if not node: continue
            for res in ("2k", "1k"):
                if res in node and "jpg" in node[res]:
                    save(node[res]["jpg"]["url"], f"assets/tex/{i}/{m}_{res}.jpg"); break
    if hdri:
        files = json.loads(get(f"https://api.polyhaven.com/files/{hdri}"))
        node = files["hdri"]["1k"]["hdr"]
        save(node["url"], f"assets/hdri/{hdri}_1k.hdr")
        try: save(f"https://dl.polyhaven.org/file/ph-assets/HDRIs/extra/Tonemapped%20JPG/{hdri}.jpg", f"assets/hdri/{hdri}.jpg")
        except Exception as e: print("tonemapped jpg fail", e)
    print("done")
