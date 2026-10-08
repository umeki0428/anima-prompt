# -*- coding: utf-8 -*-
"""漫画 1 ページの画像（NovelAI などで出したもの）から、コマを切り出して約 3 倍の大きさで描き直す（2026-10-08）。
クリスタに 1 コマずつ貼るための清書用。構図は anytest（Anima LLLite）で固定し、img2img で線と顔を LoRA の絵柄にそろえる。

  1) コマの位置を確かめる（自動検出して番号つきの確認画像を出すだけ）
     python panel_upscale.py ページ.png --detect
  2) 描き直す（自動検出のコマを全部 / 番号を選んで）
     python panel_upscale.py ページ.png
     python panel_upscale.py ページ.png --only 2,3
  3) 自動検出がずれたら、枠を手で指定（ページの画素で x0,y0,x1,y1、; 区切り）
     python panel_upscale.py ページ.png --boxes "419,0,832,366;0,370,832,1216"

プロンプトは「キャラの固定タグ（--char）＋コマを WD14 でタグ付けしたもの（色・文字・コマ割りのタグは除く）＋ --add」。
出力: <ページと同じ場所>\<ページ名>_panels\  NN_crop.png（切り出し）/ NN.png（描き直し）/ _検出.jpg / _一覧.jpg / _prompts.txt
ComfyUI を起動した状態で実行。"""
import argparse
import csv
import json
import re
import shutil
import sys
import time
import urllib.request
import uuid
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont

sys.stdout.reconfigure(encoding="utf-8")
COMFY = "http://127.0.0.1:8188"
ROOT = Path(r"C:\AI\ComfyUI_windows_portable\ComfyUI")
TAGGER = Path(r"C:\AI\wd14_tagger\wd-eva02-large-tagger-v3")
FONT = r"C:\Windows\Fonts\meiryo.ttc"

# キャラの固定タグ（色タグは入れない。白黒のときは monochrome, greyscale を先頭に足す）
CHARS = {
    "haruka": "aoi_ane, long hair, black hair, large breasts",          # 漫画 3 本目の遥
    "none": "",
}
LORAS = "aoi_ane.safetensors:0.9,XSJF Style V1.safetensors:0.3"
LINE = "thin lineart, fine lineart, delicate lineart, clean lineart, soft shading"
NEG = ("worst quality, low quality, score_1, score_2, score_3, artist name, signature, watermark, photorealistic, 3d render, "
       "text, japanese text, speech bubble, thought bubble, comic, multiple panels, panel border, border, frame, "
       "child, loli, shota, necklace, censored, mosaic censoring, bar censor, "
       "thick outlines, bold lineart, thick lineart, heavy lineart, outline, white outline, sticker, sketch, rough lines, screentone, halftone")
NEG_MONO = ", color, spot color, partially colored, colored eyes, brown eyes"
NEG_COLOR = ", monochrome, greyscale, sepia"

# WD14 のタグから外すもの（色・文字・コマ割り・白黒・画風）
DROP = re.compile(r"(^|_)(red|blue|brown|green|purple|pink|yellow|orange|grey|gray|white|black|blonde|silver|aqua|light_brown|dark)_(eyes|hair)$"
                  r"|^(monochrome|greyscale|comic|manga|multiple_views|border|black_border|white_border|speech_bubble|text|"
                  r"english_text|japanese_text|translated|sound_effects|onomatopoeia|artist_name|signature|watermark|censored|"
                  r"mosaic_censoring|bar_censor|halftone|screentone|sketch|lineart|1girl|1boy|solo|hetero)$")


# ---------------- コマの検出 ----------------
def detect(gray, min_frac=0.1):
    """コマの枠線（細くまっすぐな黒い線）でページを縦横に分けていく（ギロチン分割）。
    枠線＝その範囲の幅（高さ）の 75% 以上が黒い、厚さ 12px 以下の帯。斜めの枠・L 字のコマ・枠なしは --boxes で手で指定する"""
    H, W = gray.shape
    dark = gray < 70
    light = gray > 230

    TH = 0.75

    def lines(prof, n):
        out, i = [], 0
        while i < n:
            if prof[i] > TH:
                j = i
                while j < n and prof[j] > TH:
                    j += 1
                # 太さ 12px 以下で、すぐ外側は黒くない（髪や服の縁ではない）
                if j - i <= 12 and (i < 3 or prof[i - 3] < 0.45) and (j + 2 >= n or prof[j + 2] < 0.45):
                    out.append((i, j))
                i = j
            else:
                i += 1
        return out

    def split(x0, y0, x1, y1, depth=0):
        w, h = x1 - x0, y1 - y0
        if depth > 8:
            return [(x0, y0, x1, y1)]
        best = None
        for axis in ("h", "v"):
            prof = dark[y0:y1, x0:x1].mean(1 if axis == "h" else 0)
            n = h if axis == "h" else w
            lim = (H if axis == "h" else W) * min_frac
            for i, j in lines(prof, n):
                if i < lim or n - j < lim:
                    continue
                score = min(i, n - j)
                if best is None or score > best[0]:
                    best = (score, axis, i, j)
        if best is None:
            return [(x0, y0, x1, y1)]
        _, axis, i, j = best
        if axis == "h":
            return split(x0, y0, x1, y0 + i, depth + 1) + split(x0, y0 + j, x1, y1, depth + 1)
        return split(x0, y0, x0 + i, y1, depth + 1) + split(x0 + j, y0, x1, y1, depth + 1)

    boxes = []
    for x0, y0, x1, y1 in split(0, 0, W, H):
        # 縁に残った余白と枠線を削る（最大 30px まで。中身の白いシャツや黒髪は削らない）
        for _ in range(30):
            if light[y0, x0:x1].mean() > 0.95 or dark[y0, x0:x1].mean() > 0.6: y0 += 1
            else: break
        for _ in range(30):
            if light[y1 - 1, x0:x1].mean() > 0.95 or dark[y1 - 1, x0:x1].mean() > 0.6: y1 -= 1
            else: break
        for _ in range(30):
            if light[y0:y1, x0].mean() > 0.95 or dark[y0:y1, x0].mean() > 0.6: x0 += 1
            else: break
        for _ in range(30):
            if light[y0:y1, x1 - 1].mean() > 0.95 or dark[y0:y1, x1 - 1].mean() > 0.6: x1 -= 1
            else: break
        if (x1 - x0) > W * min_frac and (y1 - y0) > H * min_frac * 0.8:
            boxes.append((x0, y0, x1, y1))
    # 右綴じの読む順（上の段から、同じ段は右から）
    boxes.sort(key=lambda b: (round(b[1] / (H * 0.08)), -b[0]))
    return boxes


def preview(page, boxes, dst):
    im = page.copy(); dr = ImageDraw.Draw(im); f = ImageFont.truetype(FONT, max(24, page.width // 25))
    for i, (x0, y0, x1, y1) in enumerate(boxes, 1):
        dr.rectangle((x0, y0, x1, y1), outline="red", width=4)
        dr.text((x0 + 10, y0 + 6), str(i), font=f, fill="red", stroke_width=3, stroke_fill="white")
    im.save(dst, quality=88)


# ---------------- タグ付け ----------------
_sess = None


def wd14(img, thr=0.35):
    global _sess, _tags
    import onnxruntime as ort
    if _sess is None:
        prov = ["CPUExecutionProvider"]   # CUDA 版は cuDNN が無く警告が出るので CPU（1 コマ数秒）
        _sess = ort.InferenceSession(str(TAGGER / "model.onnx"), providers=prov)
        with open(TAGGER / "selected_tags.csv", encoding="utf-8") as f:
            _tags = [(r["name"], int(r["category"])) for r in csv.DictReader(f)]
    w, h = img.size; s = max(w, h)
    c = Image.new("RGB", (s, s), "white"); c.paste(img, ((s - w) // 2, (s - h) // 2))
    x = np.asarray(c.resize((448, 448), Image.BICUBIC), dtype=np.float32)[:, :, ::-1][None, ...]
    p = _sess.run(None, {_sess.get_inputs()[0].name: x})[0][0]
    out = [(n, q) for (n, cat), q in zip(_tags, p) if cat == 0 and q >= thr and not DROP.search(n)]
    out.sort(key=lambda t: -t[1])
    return [n.replace("_", " ") for n, _ in out]


# ---------------- ComfyUI ----------------
def post(g):
    req = urllib.request.Request(COMFY + "/prompt", data=json.dumps({"prompt": g, "client_id": str(uuid.uuid4())}).encode(),
                                 headers={"Content-Type": "application/json"})
    return json.loads(urllib.request.urlopen(req).read())["prompt_id"]


def wait(pid, timeout=900):
    t0 = time.time()
    while time.time() - t0 < timeout:
        h = json.loads(urllib.request.urlopen(f"{COMFY}/history/{pid}").read())
        if pid in h:
            e = h[pid]
            if e["status"].get("status_str") == "error":
                raise RuntimeError(json.dumps(e["status"].get("messages", []), ensure_ascii=False)[:800])
            if e.get("outputs"):
                x = [i for o in e["outputs"].values() for i in o.get("images", []) if i.get("type") == "output"][0]
                return ROOT / "output" / x["subfolder"] / x["filename"]
        time.sleep(2)
    raise TimeoutError(pid)


def graph(ref, w, h, pos, neg, loras, seed, denoise, anytest, prefix):
    g = {"5": {"class_type": "UNETLoader", "inputs": {"unet_name": "novaAnimeAM_v40.safetensors", "weight_dtype": "default"}},
         "7": {"class_type": "CLIPLoader", "inputs": {"clip_name": "qwen_3_06b_base.safetensors", "type": "stable_diffusion", "device": "default"}},
         "8": {"class_type": "VAELoader", "inputs": {"vae_name": "qwen_image_vae.safetensors"}},
         "9": {"class_type": "CLIPTextEncode", "inputs": {"clip": ["7", 0], "text": pos}},
         "10": {"class_type": "CLIPTextEncode", "inputs": {"clip": ["7", 0], "text": neg}},
         "20": {"class_type": "LoadImage", "inputs": {"image": ref}},
         "21": {"class_type": "ImageScale", "inputs": {"image": ["20", 0], "upscale_method": "lanczos", "width": w, "height": h, "crop": "disabled"}},
         "22": {"class_type": "VAEEncode", "inputs": {"pixels": ["21", 0], "vae": ["8", 0]}},
         "13": {"class_type": "VAEDecode", "inputs": {"samples": ["12", 0], "vae": ["8", 0]}},
         "14": {"class_type": "SaveImage", "inputs": {"images": ["13", 0], "filename_prefix": prefix}}}
    prev = ["5", 0]
    for i, (n, s) in enumerate(loras):
        g[f"6{i}"] = {"class_type": "LoraLoaderModelOnly", "inputs": {"model": prev, "lora_name": n, "strength_model": s}}
        prev = [f"6{i}", 0]
    if anytest > 0:
        g["30"] = {"class_type": "ModelPatchLoader", "inputs": {"name": "anima-lllite-any-test-like-v2.safetensors"}}
        g["31"] = {"class_type": "AnimaLLLiteApply", "inputs": {"model": prev, "model_patch": ["30", 0], "image": ["21", 0],
                                                                "strength": anytest, "start_percent": 0.0, "end_percent": 0.6}}
        prev = ["31", 0]
    g["12"] = {"class_type": "KSampler", "inputs": {"model": prev, "positive": ["9", 0], "negative": ["10", 0], "latent_image": ["22", 0],
                                                    "seed": seed, "steps": 30, "cfg": 4.0, "sampler_name": "er_sde", "scheduler": "simple",
                                                    "denoise": denoise}}
    return g


def gen_size(w, h, scale, max_area):
    s = min(scale, (max_area / (w * h)) ** 0.5)
    return max(512, round(w * s / 16) * 16), max(512, round(h * s / 16) * 16)


def main():
    ap = argparse.ArgumentParser(description="漫画ページのコマを切り出して約 3 倍で描き直す")
    ap.add_argument("page")
    ap.add_argument("--detect", action="store_true", help="コマの検出結果（番号つき）を出すだけ")
    ap.add_argument("--boxes", help='手で枠を指定: "x0,y0,x1,y1;x0,y0,x1,y1"（ページの画素）')
    ap.add_argument("--only", help="描き直すコマの番号（例 1,3）")
    ap.add_argument("--char", default="haruka", help="キャラの固定タグ: " + " / ".join(CHARS) + " / または直接タグを書く")
    ap.add_argument("--add", default="", help="全コマに足すタグ")
    ap.add_argument("--color", action="store_true", help="カラー（既定は白黒）")
    ap.add_argument("--loras", default=LORAS, help='"名前:強さ,名前:強さ"')
    ap.add_argument("--scale", type=float, default=3.0)
    ap.add_argument("--max-area", type=float, default=1.45e6, help="生成の最大画素数（大きすぎると崩れる）")
    ap.add_argument("--denoise", type=float, default=0.35)
    ap.add_argument("--anytest", type=float, default=0.6)
    ap.add_argument("--seeds", default="221001", help="カンマ区切りで複数")
    ap.add_argument("--out")
    a = ap.parse_args()

    src = Path(a.page)
    page = Image.open(src).convert("RGB")
    out = Path(a.out) if a.out else src.parent / f"{src.stem}_panels"; out.mkdir(parents=True, exist_ok=True)
    if a.boxes:
        boxes = [tuple(int(v) for v in b.split(",")) for b in a.boxes.split(";") if b.strip()]
    else:
        boxes = detect(np.asarray(page.convert("L")).astype(int))
    preview(page, boxes, out / "_検出.jpg")
    print(f"コマ {len(boxes)} 個:", "  ".join(f"{i}={b}" for i, b in enumerate(boxes, 1)), flush=True)
    print("確認画像:", out / "_検出.jpg", flush=True)
    if a.detect:
        return

    only = {int(v) for v in a.only.split(",")} if a.only else None
    loras = [(n.strip(), float(s)) for n, s in (x.rsplit(":", 1) for x in a.loras.split(",") if x.strip())]
    char = CHARS.get(a.char, a.char)
    head = ("" if a.color else "monochrome, greyscale, ") + (char + ", " if char else "")
    neg = NEG + (NEG_COLOR if a.color else NEG_MONO)
    seeds = [int(s) for s in a.seeds.split(",")]
    log = []
    done = []
    for i, box in enumerate(boxes, 1):
        if only and i not in only:
            continue
        crop = page.crop(box); crop.save(out / f"{i:02d}_crop.png")
        w, h = gen_size(crop.width, crop.height, a.scale, a.max_area)
        tags = wd14(crop)
        pos = head + ", ".join(tags) + (", " + a.add if a.add else "") + ", " + LINE
        ref = f"panel_upscale_{src.stem}_{i:02d}.png"
        crop.save(ROOT / "input" / ref)
        log.append(f"[{i:02d}] 枠 {box} → {w}×{h}\n  {pos}")
        for k, s in enumerate(seeds, 1):
            dst = out / (f"{i:02d}.png" if len(seeds) == 1 else f"{i:02d}_{k}.png")
            shutil.copy2(wait(post(graph(ref, w, h, pos, neg, loras, s, a.denoise, a.anytest, f"panel_upscale/{src.stem}_{i:02d}"))), dst)
            done.append((i, dst))
            print(f"{i:02d} {w}×{h} → {dst.name}", flush=True)
    (out / "_prompts.txt").write_text(f"ネガ: {neg}\nLoRA: {loras}  denoise {a.denoise}  anytest {a.anytest}\n\n" + "\n".join(log), encoding="utf-8")
    if done:                                                  # 切り出しと描き直しを並べた一覧
        f = ImageFont.truetype(FONT, 18); cw = 360; rows = []
        for i, dst in done:
            c = Image.open(out / f"{i:02d}_crop.png"); r = Image.open(dst)
            hh = round(cw * c.height / c.width); rows.append((f"{dst.stem}", c.resize((cw, hh)), r.convert("RGB").resize((cw, hh))))
        sh = Image.new("RGB", (cw * 2 + 30, sum(r[1].height + 28 for r in rows)), "white"); dr = ImageDraw.Draw(sh); y = 0
        for name, c, r in rows:
            sh.paste(c, (0, y + 28)); sh.paste(r, (cw + 20, y + 28))
            dr.text((4, y + 4), f"{name}  左: 切り出し / 右: 描き直し", font=f, fill="red"); y += c.height + 28
        sh.save(out / "_一覧.jpg", quality=86)
    print("DONE", out, flush=True)


if __name__ == "__main__":
    main()
