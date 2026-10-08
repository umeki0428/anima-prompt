# -*- coding: utf-8 -*-
"""NovelAI の画像 API を Python から使う（2026-10-08 に検証。使い方と注意は同じフォルダの README.md）。

トークンは環境変数 NOVELAI_TOKEN から読む（プロセスに無ければ Windows のユーザー環境変数＝レジストリから）。
トークンをファイル・ワークフロー・チャットに書かない。

  import sys; sys.path.insert(0, r"C:\\Git\\anima-prompt\\novelai")
  import nai_api as A
  A.generate(base, neg, [(人物プロンプト, 人物ネガ, x, y), ...], 832, 1216, seed, "out.png")      # 生成（x, y は 0〜1、左上が 0,0）
  A.img2img(base, neg, "元.png", 0.55, seed, "out.png")                                            # img2img
  A.infill(base, neg, "元.png", "マスク.png", seed, "out.png")                                      # インペイント（マスクは白が描き直す所）
  A.augment("declutter", "元.png", "out.png")                                                       # Director Tools
  A.anlas()                                                                                         # 残りの Anlas
"""
import base64
import io
import json
import os
import time
import urllib.error
import urllib.request
import zipfile
from pathlib import Path

from PIL import Image

HOST = "https://image.novelai.net"   # api.novelai.net は 400 を返す（2026-10 時点）
MODEL = "nai-diffusion-5-full"        # V5 Full。V5 Curated は nai-diffusion-5-curated、V4.5 は nai-diffusion-4-5-full
INPAINT_MODEL = "nai-diffusion-5-full-inpainting"

# 品質タグとネガの初期セット。API では Web 版のように自動で足されないので、こちらで足す（2026-10-08 比較で目が丁寧・少し大人っぽくなった）。
# Web 版の初期セット（UC Preset「強い」）から、コマ割りとぶつかる multiple views / negative space / blank page と halftone / screentone は外した
QUALITY = ", very aesthetic, masterpiece, no text"
UC_PRESET = ("lowres, artistic error, film grain, scan artifacts, worst quality, bad quality, jpeg artifacts, very displeasing, "
             "chromatic aberration, dithering, logo, too many watermarks, @_@, mismatched pupils, glowing eyes, bad anatomy, ")


def token():
    t = os.environ.get("NOVELAI_TOKEN")
    if not t:
        import winreg
        t = winreg.QueryValueEx(winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Environment"), "NOVELAI_TOKEN")[0]
    return t.strip()


def _post(path, payload, timeout=300):
    req = urllib.request.Request(HOST + path, data=json.dumps(payload).encode() if payload is not None else None,
                                 headers={"Authorization": "Bearer " + token(), "Content-Type": "application/json",
                                          "User-Agent": "Mozilla/5.0", "Accept": "*/*"})
    for k in range(4):
        try:
            return urllib.request.urlopen(req, timeout=timeout).read()
        except urllib.error.HTTPError as e:
            msg = e.read()[:300]
            if e.code == 429 and k < 3:          # 同時実行の制限。少し待ってやり直す
                time.sleep(10); continue
            raise RuntimeError(f"{e.code} {msg}")


def _save_zip(data, dst):
    z = zipfile.ZipFile(io.BytesIO(data))
    Path(dst).parent.mkdir(parents=True, exist_ok=True)
    Path(dst).write_bytes(z.read(z.namelist()[0]))
    return Path(dst)


def b64(img):
    """パス・PIL 画像のどちらでも PNG の base64 にする"""
    im = img if isinstance(img, Image.Image) else Image.open(img)
    buf = io.BytesIO(); im.convert("RGB").save(buf, "PNG")
    return base64.b64encode(buf.getvalue()).decode()


def anlas():
    d = json.loads(_post("/user/subscription", None))["trainingStepsLeft"]
    return d["fixedTrainingStepsLeft"] + d["purchasedTrainingSteps"]


def generate(base, neg, chars, w, h, seed, dst, steps=28, scale=5.0, quality=True, uc_preset=0, extra=None, action="generate", model=None,
             sampler="k_euler", schedule="karras"):   # euler が標準（2026-10-08 ユーザー指定。線と陰影がくっきり）
    """chars: [(人物プロンプト, 人物ネガ, x, y)]。人物プロンプト 1 つがほぼ 1 コマになる（漫画ページの配置に使う）。
    action: generate / img2img（extra に image, strength, noise）/ infill（model を ...-inpainting、extra に image, mask）
    quality=True で base の末尾に QUALITY、neg の先頭に UC_PRESET を足す（False で素のまま）"""
    if quality:
        base = base.rstrip(", ") + QUALITY
        neg = UC_PRESET + neg
    use_coords = bool(chars)
    p = {"params_version": 3, "width": w, "height": h, "scale": scale, "sampler": sampler, "steps": steps, "seed": seed,
         "n_samples": 1, "ucPreset": uc_preset, "qualityToggle": quality, "autoSmea": False, "dynamic_thresholding": False,
         "controlnet_strength": 1, "legacy": False, "add_original_image": True, "cfg_rescale": 0, "noise_schedule": schedule,
         "legacy_v3_extend": False, "skip_cfg_above_sigma": None, "use_coords": use_coords, "legacy_uc": False,
         "normalize_reference_strength_multiple": True, "negative_prompt": neg,
         "characterPrompts": [{"prompt": c, "uc": u, "center": {"x": x, "y": y}, "enabled": True} for c, u, x, y in chars],
         "v4_prompt": {"caption": {"base_caption": base, "char_captions": [{"char_caption": c, "centers": [{"x": x, "y": y}]} for c, u, x, y in chars]},
                       "use_coords": use_coords, "use_order": True},
         "v4_negative_prompt": {"caption": {"base_caption": neg, "char_captions": [{"char_caption": u, "centers": [{"x": x, "y": y}]} for c, u, x, y in chars]},
                                "legacy_uc": False}}
    if extra:
        p.update(extra)
    data = _post("/ai/generate-image", {"input": base, "model": model or MODEL, "action": action, "parameters": p})
    return _save_zip(data, dst)


def img2img(base, neg, image, strength, seed, dst, chars=(), noise=0.0, **kw):
    im = image if isinstance(image, Image.Image) else Image.open(image)
    return generate(base, neg, list(chars), im.width, im.height, seed, dst, action="img2img",
                    extra={"image": b64(im), "strength": strength, "noise": noise, "color_correct": False}, **kw)


def infill(base, neg, image, mask, seed, dst, chars=(), strength=0.7, **kw):
    """マスクは元画像と同じ大きさ、黒地に白が描き直す所。マスクの端がコマの内側にあるとそこに枠線を描くことがある"""
    im = image if isinstance(image, Image.Image) else Image.open(image)
    return generate(base, neg, list(chars), im.width, im.height, seed, dst, action="infill", model=INPAINT_MODEL,
                    extra={"image": b64(im), "mask": b64(mask), "strength": strength, "noise": 0, "add_original_image": True}, **kw)


def augment(tool, image, dst, prompt=None, defry=0):
    """Director Tools: declutter（フキダシ・文字消し）/ colorize / lineart / sketch / emotion（prompt "happy;;" など）/ bg-removal"""
    im = image if isinstance(image, Image.Image) else Image.open(image)
    p = {"req_type": tool, "image": b64(im), "width": im.width, "height": im.height}
    if prompt is not None:
        p["prompt"] = prompt
    if tool in ("colorize", "emotion"):
        p["defry"] = defry
    return _save_zip(_post("/ai/augment-image", p), dst)
