# -*- coding: utf-8 -*-
"""ページ組み立て（2026-10-08）。page.json に書いた「土台のページ・コマの位置・コマの素材・セリフ」から、
  3_絵柄/page.png（絵だけ）と 4_仮文字/page_仮.png（仮の吹き出し・描き文字入り）を作る。
コマを差し替えたら page.json を書き換えて、もう一度実行するだけ。

  python page_compose.py <ページのフォルダ>            例: ...\\novelai\\pages\\D03
  python page_compose.py <ページのフォルダ> --grid     座標を読むための 50px 方眼つきの土台を _grid.png に出す

page.json（座標はすべて土台のページの画素。出力は scale 倍）:
{
  "base": "1_ネーム/xxx.png",          土台（余白・背景・コマの外の絵はここから）
  "scale": 2.5,                         出力の倍率
  "frame_width": 3,                     枠線の太さ（土台の画素）。0 で枠を引かない
  "panels": [                           上に貼るコマ（読む順でなくてよい）
    {"id": "右大", "box": [x0, y0, x1, y1], "src": "3_絵柄/右大.png", "fit": "stretch", "frame": true, "inset": 0}
  ],                                    fit: stretch（枠に合わせて伸ばす）/ cover（はみ出しを切る）
  "texts": [                            仮のセリフ。\\n で改行（縦書きは右の行から）
    {"text": "ほら。\\n自分で", "x": 600, "y": 120, "size": 14, "kind": "normal", "tail": [560, 220]}
  ],                                    kind: normal（丸）/ weak（ヨレヨレ＋グレー）/ thought（雲）/ shout（トゲ）/ none（文字だけ）
  "sfx": [{"text": "パサッ", "x": 650, "y": 120, "size": 30, "angle": -10}]   描き文字（白フチの太字）
}"""
import json
import math
import random
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageOps

sys.stdout.reconfigure(encoding="utf-8")
FONT_TEXT = r"C:\Windows\Fonts\yumin.ttf"          # セリフ（明朝）
FONT_SFX = r"C:\Windows\Fonts\YuGothB.ttc"         # 描き文字（太ゴシック）
ROT = set("ー―…～〜「」『』（）()-—")              # 縦書きで 90 度回す文字
SMALL = set("、。")


# ---------------- 縦書き ----------------
def vsize(lines, fs):
    return len(lines) * fs * 1.3, max((len(l) for l in lines), default=1) * fs


def draw_vtext(img, cx, cy, lines, fs, font, fill=0):
    d = ImageDraw.Draw(img)
    f = ImageFont.truetype(font, fs)
    tw, th = vsize(lines, fs)
    x = cx + tw / 2 - fs * 1.3 / 2
    for line in lines:
        y = cy - th / 2
        for ch in line:
            if ch in SMALL:
                d.text((x + fs * 0.32, y + fs * 0.1), ch, font=f, fill=fill, anchor="mm")
            elif ch in ROT:
                t = Image.new("LA", (fs * 2, fs * 2), (255, 0))
                ImageDraw.Draw(t).text((fs, fs), ch, font=f, fill=(fill, 255), anchor="mm")
                t = t.rotate(-90)
                img.paste(t.convert("L"), (int(x - fs), int(y + fs / 2 - fs)), t.split()[1])
            else:
                d.text((x, y + fs / 2), ch, font=f, fill=fill, anchor="mm")
            y += fs
        x -= fs * 1.3


# ---------------- 吹き出し ----------------
def ellipse_pts(cx, cy, rx, ry, n=72, jitter=0.0, seed=0):
    rnd = random.Random(seed)
    pts = []
    for i in range(n):
        a = 2 * math.pi * i / n
        k = 1 + (rnd.uniform(-jitter, jitter) if jitter else 0)
        pts.append((cx + rx * k * math.cos(a), cy + ry * k * math.sin(a)))
    return pts


def tail_poly(cx, cy, rx, ry, tx, ty, w):
    a = math.atan2(ty - cy, tx - cx)
    bx, by = cx + rx * 0.8 * math.cos(a), cy + ry * 0.8 * math.sin(a)
    nx, ny = -math.sin(a) * w, math.cos(a) * w
    return [(bx + nx, by + ny), (tx, ty), (bx - nx, by - ny)]


def bubble(img, t, s):
    lines = t["text"].split("\n")
    fs = int(t.get("size", 14) * s)
    cx, cy = t["x"] * s, t["y"] * s
    tw, th = vsize(lines, fs)
    rx, ry = tw / 2 + fs * 0.9, th / 2 + fs * 0.9
    kind = t.get("kind", "normal")
    lw = max(2, int(1.2 * s))
    d = ImageDraw.Draw(img)
    tail = t.get("tail")
    if kind == "normal":
        if tail:
            d.polygon(tail_poly(cx, cy, rx, ry, tail[0] * s, tail[1] * s, fs * 0.35), fill=255, outline=0, width=lw)
        d.ellipse((cx - rx, cy - ry, cx + rx, cy + ry), fill=255, outline=0, width=lw)
        if tail:   # しっぽの付け根の線を消す
            d.polygon(tail_poly(cx, cy, rx * 0.97, ry * 0.97, tail[0] * s, tail[1] * s, fs * 0.33), fill=255)
            d.line(tail_poly(cx, cy, rx, ry, tail[0] * s, tail[1] * s, fs * 0.35), fill=0, width=lw)
    elif kind == "weak":
        pts = ellipse_pts(cx, cy, rx, ry, n=90, jitter=0.035, seed=int(cx + cy))
        if tail:
            tp = tail_poly(cx, cy, rx, ry, tail[0] * s, tail[1] * s, fs * 0.3)
            d.polygon(tp, fill=228, outline=0, width=max(1, lw // 2))
        d.polygon(pts, fill=228)
        d.line(pts + [pts[0]], fill=0, width=max(1, lw // 2), joint="curve")
        if tail:
            d.polygon(tail_poly(cx, cy, rx * 0.96, ry * 0.96, tail[0] * s, tail[1] * s, fs * 0.28), fill=228)
    elif kind == "thought":
        for (px, py) in ellipse_pts(cx, cy, rx * 0.92, ry * 0.92, n=14):
            r = fs * 0.75
            d.ellipse((px - r, py - r, px + r, py + r), fill=255, outline=0, width=lw)
        d.ellipse((cx - rx * 0.92, cy - ry * 0.92, cx + rx * 0.92, cy + ry * 0.92), fill=255)
        if tail:
            for k, r in ((0.35, fs * 0.35), (0.65, fs * 0.22)):
                px, py = cx + (tail[0] * s - cx) * (0.6 + k * 0.6), cy + (tail[1] * s - cy) * (0.6 + k * 0.6)
                d.ellipse((px - r, py - r, px + r, py + r), fill=255, outline=0, width=lw)
    elif kind == "shout":
        pts = []
        n = 22
        for i in range(n * 2):
            a = math.pi * i / n
            k = 1.25 if i % 2 == 0 else 0.92
            pts.append((cx + rx * k * math.cos(a), cy + ry * k * math.sin(a)))
        d.polygon(pts, fill=255, outline=0, width=lw)
    draw_vtext(img, cx, cy, lines, fs, FONT_TEXT, 0)


def sfx(img, t, s):
    fs = int(t.get("size", 30) * s)
    lines = t["text"].split("\n")
    tw, th = vsize(lines, fs)
    pad = fs
    layer = Image.new("L", (int(tw + pad * 2), int(th + pad * 2)), 255)
    mask = Image.new("L", layer.size, 0)
    draw_vtext(mask, layer.width / 2, layer.height / 2, lines, fs, FONT_SFX, 255)
    edge = mask.filter(ImageFilter.MaxFilter(int(fs * 0.18) // 2 * 2 + 1))     # 白フチ
    comp = Image.new("RGBA", layer.size, (0, 0, 0, 0))
    comp.alpha_composite(Image.merge("RGBA", (Image.new("L", layer.size, 255),) * 3 + (edge,)))
    comp.alpha_composite(Image.merge("RGBA", (Image.new("L", layer.size, 0),) * 3 + (mask,)))
    comp = comp.rotate(t.get("angle", 0), expand=True, resample=Image.BICUBIC)
    x, y = int(t["x"] * s - comp.width / 2), int(t["y"] * s - comp.height / 2)
    base = img.convert("RGBA"); base.alpha_composite(comp, (x, y))
    img.paste(base.convert("L"))


# ---------------- 組み立て ----------------
def compose(folder):
    folder = Path(folder)
    cfg = json.loads((folder / "page.json").read_text(encoding="utf-8"))
    s = cfg.get("scale", 2.5)
    base = Image.open(folder / cfg["base"]).convert("L")
    W, H = round(base.width * s), round(base.height * s)
    page = base.resize((W, H), Image.LANCZOS)
    d = ImageDraw.Draw(page)
    fw = int(cfg.get("frame_width", 3) * s)
    for p in cfg.get("panels", []):
        x0, y0, x1, y1 = [round(v * s) for v in p["box"]]
        ins = round(p.get("inset", 0) * s)
        w, h = x1 - x0 - ins * 2, y1 - y0 - ins * 2
        im = Image.open(folder / p["src"]).convert("L")
        im = ImageOps.fit(im, (w, h), Image.LANCZOS) if p.get("fit") == "cover" else im.resize((w, h), Image.LANCZOS)
        page.paste(im, (x0 + ins, y0 + ins))
        if p.get("frame", True) and fw:
            d.rectangle((x0, y0, x1, y1), outline=0, width=fw)
    out3 = folder / "3_絵柄"; out3.mkdir(exist_ok=True)
    page.save(out3 / "page.png")
    for t in cfg.get("texts", []):
        if t.get("kind", "normal") == "none":
            draw_vtext(page, t["x"] * s, t["y"] * s, t["text"].split("\n"), int(t.get("size", 14) * s), FONT_TEXT, 0)
        else:
            bubble(page, t, s)
    for t in cfg.get("sfx", []):
        sfx(page, t, s)
    out4 = folder / "4_仮文字"; out4.mkdir(exist_ok=True)
    page.save(out4 / "page_仮.png")
    page.resize((W // 3, H // 3), Image.LANCZOS).save(out4 / "page_仮_小.jpg", quality=85)
    print(out3 / "page.png", "/", out4 / "page_仮.png", f"{W}×{H}", flush=True)


def grid(folder):
    folder = Path(folder)
    cfg = json.loads((folder / "page.json").read_text(encoding="utf-8"))
    im = Image.open(folder / cfg["base"]).convert("RGB"); d = ImageDraw.Draw(im)
    f = ImageFont.truetype(FONT_SFX, 12)
    for x in range(0, im.width, 50):
        d.line((x, 0, x, im.height), fill=(255, 0, 0) if x % 100 == 0 else (255, 170, 170), width=1)
        if x % 100 == 0: d.text((x + 2, 2), str(x), font=f, fill=(255, 0, 0))
    for y in range(0, im.height, 50):
        d.line((0, y, im.width, y), fill=(255, 0, 0) if y % 100 == 0 else (255, 170, 170), width=1)
        if y % 100 == 0: d.text((2, y + 2), str(y), font=f, fill=(255, 0, 0))
    im.save(folder / "_grid.png"); print(folder / "_grid.png")


if __name__ == "__main__":
    (grid if "--grid" in sys.argv else compose)(sys.argv[1])
