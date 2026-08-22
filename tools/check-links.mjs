#!/usr/bin/env node
// リポジトリ内 Markdown の相対リンク整合性チェック。
//
// このリポジトリは相互参照で成り立つナレッジベースなので、リンク切れ(link rot)が
// 最大の壊れやすさになる。外部URLはネットワーク依存で不安定なため検証対象外とし、
// リポジトリ内の相対リンクだけを対象に、参照先ファイル(と可能なら見出しアンカー)の
// 存在を確認する。誤検知を避けるため、対象は Markdown のインラインリンク `](target)` のみ。
//
// 使い方: node tools/check-links.mjs
// 全リンクが解決すれば exit 0、1件でも切れていれば exit 1。

import { readFileSync, readdirSync, statSync, existsSync } from "node:fs";
import { join, dirname, resolve, relative } from "node:path";
import { fileURLToPath } from "node:url";

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), "..");

// アクティブな検証対象から除外するトップレベルディレクトリ/ファイル。
const IGNORE_DIRS = new Set([".git", "node_modules", "_archive"]);

function walk(dir) {
  const out = [];
  for (const entry of readdirSync(dir)) {
    const full = join(dir, entry);
    const rel = relative(ROOT, full);
    if (IGNORE_DIRS.has(entry) || IGNORE_DIRS.has(rel)) continue;
    const st = statSync(full);
    if (st.isDirectory()) out.push(...walk(full));
    else if (entry.endsWith(".md")) out.push(full);
  }
  return out;
}

// インラインリンク `[text](target)` の target を抽出する(画像 `![]()` も含む)。
// コードスパン内は誤検知が多いので、行頭が ``` のコードフェンス内は除外する。
function extractLinks(content) {
  const links = [];
  const lines = content.split(/\r?\n/);
  let inFence = false;
  const linkRe = /\]\(\s*([^)\s]+)(?:\s+"[^"]*")?\s*\)/g;
  lines.forEach((line, i) => {
    const fence = line.match(/^\s*(```|~~~)/);
    if (fence) {
      inFence = !inFence;
      return;
    }
    if (inFence) return;
    let m;
    while ((m = linkRe.exec(line)) !== null) {
      links.push({ target: m[1], line: i + 1 });
    }
  });
  return links;
}

function isExternal(target) {
  return /^(https?:|mailto:|tel:|#|data:)/i.test(target);
}

function headingSlugs(mdPath) {
  const slugs = new Set();
  const content = readFileSync(mdPath, "utf8");
  for (const line of content.split(/\r?\n/)) {
    const h = line.match(/^#{1,6}\s+(.*)$/);
    if (!h) continue;
    const slug = h[1]
      .trim()
      .toLowerCase()
      .replace(/[^\w\s\u3000-\u9fff\u3040-\u30ff-]/g, "")
      .replace(/\s+/g, "-");
    slugs.add(slug);
  }
  return slugs;
}

const files = walk(ROOT);
let broken = 0;
let checked = 0;

for (const file of files) {
  const content = readFileSync(file, "utf8");
  const links = extractLinks(content);
  for (const { target, line } of links) {
    if (isExternal(target)) continue;
    checked++;
    const [pathPart, anchor] = target.split("#");
    const resolved = pathPart
      ? resolve(dirname(file), pathPart)
      : file; // 同一ファイル内アンカー
    if (!existsSync(resolved)) {
      console.error(
        `BROKEN  ${relative(ROOT, file)}:${line}  ->  ${target}  (ファイルが存在しない)`
      );
      broken++;
      continue;
    }
    if (anchor && resolved.endsWith(".md")) {
      const slugs = headingSlugs(resolved);
      const wanted = anchor
        .toLowerCase()
        .replace(/[^\w\s\u3000-\u9fff\u3040-\u30ff-]/g, "")
        .replace(/\s+/g, "-");
      if (!slugs.has(wanted)) {
        console.error(
          `BROKEN  ${relative(ROOT, file)}:${line}  ->  ${target}  (見出しアンカーが見つからない)`
        );
        broken++;
      }
    }
  }
}

console.log(
  `\nMarkdown 相対リンク検査: ${files.length} ファイル / ${checked} リンクを確認`
);
if (broken > 0) {
  console.error(`結果: ${broken} 件のリンク切れを検出`);
  process.exit(1);
}
console.log("結果: リンク切れなし ✓");
