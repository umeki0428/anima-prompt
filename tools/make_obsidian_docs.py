# -*- coding: utf-8 -*-
"""ComfyUI の現役ワークフローと system prompt を読み取り、Obsidian 用のノートを作り直す。

実物（ワークフローの JSON と system-prompts/*.txt）から毎回作るので、ノートと実物がずれない。
使い方:  tools\\update_docs.bat をダブルクリック（または python tools/make_obsidian_docs.py）
"""
import hashlib, json, re, sys, time
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
WF_ROOT = Path(r"C:\AI\ComfyUI_windows_portable\ComfyUI\user\default\workflows")
ACTIVE, ARCHIVE = WF_ROOT / "00_現役", WF_ROOT / "_保管"
SP_DIR = Path(r"C:\Git\anima-prompt\system-prompts")
VAULT = Path(r"C:\Users\apric\OneDrive\Documents\Obsidian Vault")
OUT = VAULT / "ComfyUI"
STATE = OUT / "_state.json"
AUTO = "> [!info] このノートは自動生成です。直接編集しても次の更新で上書きされます。メモは「メモ（手書き）」フォルダに書いてください。\n\n"


def md_name(s):
    return re.sub(r'[\\/:*?"<>|#^\[\]]', "_", s)


def read_wf(path):
    wf = json.loads(path.read_text(encoding="utf-8"))
    nodes = [n for n in wf.get("nodes", []) if isinstance(n, dict)]
    by_id = {n["id"]: n for n in nodes}
    links = {l[0]: l for l in wf.get("links", []) if isinstance(l, list)}

    def src_of(node, input_name):
        for i in node.get("inputs", []):
            if i.get("name") == input_name and i.get("link") in links:
                return by_id.get(links[i["link"]][1])
        return None

    info = {"name": path.stem, "path": str(path), "mtime": path.stat().st_mtime, "note": "", "note_title": "", "loras": [], "prompts": [], "claude": [],
            "neg": "", "manual": [], "save": [], "size": "", "features": [], "key_leak": '"sk-ant' in path.read_text(encoding="utf-8")}
    types = [n["type"] for n in nodes]
    for t, label in [("AnimaLLLiteApply", "anytest / LLLite（参考画像で構図を固定）"), ("FaceDetailer", "FaceDetailer（顔の描き直し）"), ("ImageCrop", "切り抜き"),
                     ("VAEEncode", "img2img（元画像から描き直し）")]:
        if t in types:
            info["features"].append(label)
    for n in nodes:
        t, wv, title = n["type"], n.get("widgets_values") or [], n.get("title") or ""
        if t in ("Note", "MarkdownNote") and "使い方" in title:
            info["note"], info["note_title"] = wv[0] if wv else "", title
        elif t == "LoraLoaderModelOnly" and wv:
            info["loras"].append((title, wv[0].replace(".safetensors", ""), wv[1], n.get("mode", 0) == 4))
        elif t == "ClaudeCustomPrompt":
            files, inline = [], None
            s = src_of(n, "system_prompt")
            stack = [s] if s else []
            while stack:
                x = stack.pop()
                if x["type"] == "AnimaLoadTextFile":
                    files.append(Path(x["widgets_values"][0]))
                elif x["type"] == "Text Concatenate":
                    stack += [y for y in (src_of(x, k) for k in ("text_d", "text_c", "text_b", "text_a")) if y]
                elif x.get("widgets_values"):
                    inline = x["widgets_values"][0]
            if not s:
                inline = wv[1] if len(wv) > 1 else ""
            info["claude"].append({"title": title, "bypass": n.get("mode", 0) == 4, "model": wv[0] if wv else "", "temp": wv[4] if len(wv) > 4 else "",
                                   "files": files, "inline": inline})
        elif t == "CLIPTextEncode" and ("Negative" in title or "ネガ" in title) and wv:
            info["neg"] = wv[0]
        elif t == "DF_DynamicPrompts_Text_Box" and wv and "システム" not in title:
            info["manual"].append((title, wv[0]))
        elif t == "SaveImage" and wv and n.get("mode", 0) == 0:
            info["save"].append(wv[0])
        elif t == "KSampler":
            lat = src_of(n, "latent_image")
            if lat and lat["type"] == "EmptyLatentImage":
                info["size"] = f'{lat["widgets_values"][0]}×{lat["widgets_values"][1]}'
    return info


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "ワークフロー").mkdir(exist_ok=True)
    (OUT / "システムプロンプト").mkdir(exist_ok=True)
    (OUT / "メモ（手書き）").mkdir(exist_ok=True)
    meta = json.loads((SP_DIR / "_meta.json").read_text(encoding="utf-8")) if (SP_DIR / "_meta.json").exists() else {}
    wfs = [read_wf(p) for p in sorted(ACTIVE.glob("*.json"))]
    sps = sorted(p for p in SP_DIR.glob("*.txt"))
    used_by = {p.name: [] for p in sps}
    warn = []

    # ---------------- ワークフローのノート
    for w in wfs:
        L = [AUTO, f"# {w['name']}\n", f"- ファイル: `{w['path']}`", f"- 最終更新: {time.strftime('%Y-%m-%d %H:%M', time.localtime(w['mtime']))}"]
        if w["features"]:
            L.append("- 仕組み: " + " / ".join(w["features"]))
        if w["size"]:
            L.append(f"- 画像サイズ（いま接続中）: {w['size']}")
        if w["save"]:
            L.append("- 保存先: " + ", ".join(f"`output\\{s}`" for s in w["save"]))
        L.append("\n## 使い方（ワークフロー内のノートと同じ）\n")
        if w["note"]:
            L.append(w["note"].replace("\n", "  \n"))
        else:
            L.append("**（使い方ノートがありません）**"); warn.append(f"[[{md_name(w['name'])}]] に「使い方」ノートがない")
        L.append("\n## 日本語翻訳ノードと system prompt\n")
        if not w["claude"]:
            L.append("翻訳ノードなし（日本語は使わない）。")
        for c in w["claude"]:
            L.append(f"### {c['title']}" + ("　（いまは OFF＝バイパス）" if c["bypass"] else ""))
            L.append(f"- model: `{c['model']}` / temperature: {c['temp']}")
            for f in c["files"]:
                if f.parent == SP_DIR:
                    used_by.setdefault(f.name, []).append(w["name"])
                    L.append(f"- system prompt: [[{md_name(f.stem)}]]")
                else:
                    L.append(f"- 追加で読むファイル: `{f}`")
            if c["inline"] and not c["files"]:
                L.append("- **system prompt がワークフローに直書きされています**（`system-prompts` フォルダに出すこと）")
                warn.append(f"[[{md_name(w['name'])}]] の「{c['title']}」は system prompt が直書き")
        L.append("\n## LoRA\n\n| 枠 | LoRA | 強さ | 状態 |\n|---|---|---|---|")
        for t, name, s, byp in w["loras"]:
            L.append(f"| {t} | `{name}` | {s} | {'OFF' if byp else 'ON'} |")
        for t, text in w["manual"]:
            L.append(f"\n## {t}\n\n```\n{text.strip()}\n```")
        if w["neg"]:
            L.append(f"\n## ネガティブ\n\n```\n{w['neg'].strip()}\n```")
        if w["key_leak"]:
            warn.append(f"[[{md_name(w['name'])}]] に API キーが平文で入っている")
        (OUT / "ワークフロー" / f"{md_name(w['name'])}.md").write_text("\n".join(L) + "\n", encoding="utf-8")

    # ---------------- system prompt のノート
    for p in sps:
        m = meta.get(p.name, {})
        text = p.read_text(encoding="utf-8")
        L = [AUTO, f"# {p.stem}\n", f"- ファイル: `{p}`（**直すときはこのテキストを編集**。保存すれば次の実行から反映）",
             f"- 最終更新: {time.strftime('%Y-%m-%d %H:%M', time.localtime(p.stat().st_mtime))} / {len(text)} 字",
             "- 使っているワークフロー: " + (", ".join(f"[[{md_name(x)}]]" for x in used_by.get(p.name, [])) or "**なし（未使用）**")]
        if not m:
            warn.append(f"[[{md_name(p.stem)}]] の説明が `_meta.json` にない")
        for k in ("役割", "既定の動き", "日本語の書き方"):
            L.append(f"\n## {k}\n\n{m.get(k, '（未記入。system-prompts/_meta.json に書く）')}")
        if m.get("入力例"):
            L.append(f"\n## 入力例（日本語）\n\n```\n{m['入力例']}\n```")
        L.append(f"\n## 本文\n\n````\n{text.strip()}\n````")
        (OUT / "システムプロンプト" / f"{md_name(p.stem)}.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    for name, users in used_by.items():
        if not users and name in {p.name for p in sps}:
            warn.append(f"[[{md_name(Path(name).stem)}]] はどの現役ワークフローからも使われていない（予備なら問題なし）")

    # ---------------- 変更履歴
    state = json.loads(STATE.read_text(encoding="utf-8")) if STATE.exists() else {}
    now = {**{"WF:" + w["name"]: hashlib.md5(Path(w["path"]).read_bytes()).hexdigest() for w in wfs},
           **{"SP:" + p.name: hashlib.md5(p.read_bytes()).hexdigest() for p in sps}}
    changes = [("追加" if k not in state else "変更", k) for k, v in now.items() if state.get(k) != v] + [("削除", k) for k in state if k not in now]
    log = OUT / "変更履歴.md"
    if changes:
        old = log.read_text(encoding="utf-8") if log.exists() else "# 変更履歴\n\n更新スクリプトを回したときに、前回から変わったファイルを記録します。理由は手で 1 行足してください。\n"
        head, _, rest = old.partition("\n## ")
        entry = f"## {time.strftime('%Y-%m-%d %H:%M')}\n" + "\n".join(f"- {a}: {k[3:]}（{'ワークフロー' if k.startswith('WF') else 'system prompt'}）" for a, k in changes) + "\n- 理由: \n\n"
        log.write_text(head.rstrip() + "\n\n" + entry + ("## " + rest if rest else ""), encoding="utf-8")
    STATE.write_text(json.dumps(now, ensure_ascii=False, indent=1), encoding="utf-8")

    # ---------------- 入口のノート
    n_arch = sum(1 for _ in ARCHIVE.rglob("*.json")) if ARCHIVE.exists() else 0
    L = [AUTO, "# ComfyUI の使い分け（入口）\n", f"最終更新: {time.strftime('%Y-%m-%d %H:%M')}\n",
         "## どれを使うか\n", "| ワークフロー | 仕組み | 日本語翻訳の system prompt | 保存先 |", "|---|---|---|---|"]
    for w in wfs:
        sp = ", ".join(f"[[{md_name(f.stem)}]]" for c in w["claude"] for f in c["files"] if f.parent == SP_DIR) or "（日本語なし）"
        L.append(f"| [[{md_name(w['name'])}]] | {' / '.join(w['features']) or '通常の生成'} | {sp} | {', '.join(w['save'])} |")
    L += ["\n## system prompt の一覧\n", "| ファイル | 役割 | 日本語の書き方 |", "|---|---|---|"]
    for p in sps:
        m = meta.get(p.name, {})
        L.append(f"| [[{md_name(p.stem)}]] | {m.get('役割', '（未記入）')} | {m.get('日本語の書き方', '（未記入）')} |")
    L += ["\n## 要確認\n", "\n".join(f"- {x}" for x in warn) if warn else "なし。",
          "\n## 増やすときのルール\n",
          "1. ワークフローは `workflows\\00_現役\\` にだけ置く。ファイル名は「番号_用途」。中に「使い方: …」という題のノートを必ず置く（何をするか・日本語の書き方）。",
          "2. system prompt はワークフローに直書きしない。`C:\\Git\\anima-prompt\\system-prompts\\` にテキストで置き、`_meta.json` に役割・日本語の書き方・入力例を書く。",
          "3. 使わなくなったものは `workflows\\_保管\\` に移す（消さない）。",
          "4. 変えたら `C:\\Git\\anima-prompt\\tools\\update_docs.bat` を実行 → このノート群が作り直され、[[変更履歴]] に記録される。理由を 1 行書く。",
          "5. API キーはワークフローに書かない（環境変数 `ANTHROPIC_API_KEY`）。",
          f"\n## 場所\n\n- 現役: `{ACTIVE}`\n- 保管: `{ARCHIVE}`（{n_arch} 本）\n- system prompt: `{SP_DIR}`\n- 手書きのメモ: このフォルダの「メモ（手書き）」（自動更新で消えない）"]
    (OUT / "00_入口（使い分け）.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"workflows {len(wfs)} / system prompts {len(sps)} / 変更 {len(changes)} / 要確認 {len(warn)}")
    for x in warn:
        print("  要確認:", x)


if __name__ == "__main__":
    main()
