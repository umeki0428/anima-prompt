# -*- coding: utf-8 -*-
"""NovelAI で作った PNG に入っている設定（プロンプト・人物の位置・ネガ・シード・サンプラー）を読み出して、
フォルダごとに _プロンプト.md に書き出す。Web 版に貼り直すときや、あとで見返すとき用。
  python nai_prompts.py "C:\\AI\\作品\\ane-ntr\\novelai"        （下のフォルダも全部）
NovelAI の PNG でないもの（ComfyUI の描き直しなど）は飛ばす。"""
import json
import sys
from pathlib import Path

from PIL import Image

sys.stdout.reconfigure(encoding="utf-8")


def read(p):
    try:
        im = Image.open(p)
        if im.info.get("Software") != "NovelAI" and "NovelAI" not in str(im.info.get("Source", "")):
            return None
        return json.loads(im.info["Comment"])
    except Exception:
        return None


def block(name, c):
    v4 = c.get("v4_prompt", {}).get("caption", {})
    n4 = c.get("v4_negative_prompt", {}).get("caption", {})
    out = [f"## {name}", "",
           f"- モデル: {c.get('model_name', '')} / {c.get('request_type', '')}　サイズ {c.get('width')}×{c.get('height')}　"
           f"シード {c.get('seed')}　サンプラー {c.get('sampler')}　steps {c.get('steps')}　CFG {c.get('scale')}", "",
           "**ベースプロンプト**", "```", v4.get("base_caption", c.get("prompt", "")), "```", "",
           "**除外したい要素（ネガ）**", "```", n4.get("base_caption", c.get("uc", "")), "```"]
    chars = v4.get("char_captions", [])
    negs = n4.get("char_captions", [])
    for i, ch in enumerate(chars):
        pos = ch.get("centers", [{}])[0]
        out += ["", f"**キャラクター {i + 1}**（位置 x={pos.get('x')}, y={pos.get('y')}）", "```", ch.get("char_caption", ""), "```"]
        if i < len(negs) and negs[i].get("char_caption"):
            out += [f"キャラクター {i + 1} のネガ: `{negs[i]['char_caption']}`"]
    return out + [""]


def main(root):
    root = Path(root)
    dirs = sorted({p.parent for p in root.rglob("*.png")})
    for d in dirs:
        lines = []
        for p in sorted(d.glob("*.png")):
            c = read(p)
            if c:
                lines += block(p.name, c)
        if lines:
            (d / "_プロンプト.md").write_text(f"# {d.name} の NovelAI 設定（PNG から読み出し）\n\n" + "\n".join(lines), encoding="utf-8")
            print(d / "_プロンプト.md", flush=True)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else ".")
