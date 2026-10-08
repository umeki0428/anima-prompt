# NovelAI で漫画ページを作る（2026-10-08 検証）

NovelAI V5 は **1 回の生成でコマ割りされた漫画 1 ページ**を出せる。人物プロンプト（Character Prompts）を画面上の位置に置くと、1 つがほぼ 1 コマになる。
自作 LoRA は使えないので、**構図・コマ割り・演出は NovelAI、顔と絵柄は ComfyUI（キャラ LoRA の img2img）**で分担する。

## 準備
- 契約: Opus（tier 3）。**832×1216 と同じ面積まで・28 steps 以下・1 枚ずつなら Anlas 0**。1088×960 や 1024×1024 は Anlas がかかった（8 枚で 48）
- トークン: NovelAI の Account Settings →「Get Persistent API Token」→ Windows の**ユーザー環境変数 `NOVELAI_TOKEN`** に登録（Windows キー →「環境変数」→ ユーザー環境変数 → 新規）。`nai_api.py` はプロセスに無ければレジストリから読むので、アプリの再起動は不要
- トークンをファイル・ワークフロー・チャットに書かない
- 使い方: `nai_api.py` の先頭のコメント

## API の要点
| 機能 | 呼び方 | Opus の Anlas |
|---|---|---|
| 生成（位置指定） | `generate(base, neg, chars, w, h, seed, dst)` | 0 |
| img2img | `img2img(base, neg, 元, strength, seed, dst)` | 0 |
| インペイント | `infill(base, neg, 元, マスク, seed, dst)`（V5 inpainting） | 0 |
| Director Tools | `augment("declutter" / "colorize" / "lineart" / "sketch" / "emotion", 元, dst)` | 0 |
| Vibe Transfer・精密参照 | **V5 は非対応**（Web 版も参照を入れると V4.5 に切り替わる）。V4.5 で `director_reference_*` / `reference_image_multiple`。同時には使えない | 精密参照 5／枚、vibe 変換 2 |

- エンドポイントは `image.novelai.net`（`api.novelai.net` は 400）。モデル名 `nai-diffusion-5-full`
- 人物の位置は `v4_prompt.caption.char_captions[].centers` に 0〜1 の x, y。V5 は自由配置、V4.5 は 5×5 のマス目
- V4.5 は日本語プロンプトを理解しない。V5 は日本語も通るが、**日本語の「白黒」だけではカラーになる** → ベースに英語で `monochrome, greyscale, manga, comic`、ネガに `color`
- 出力 PNG の `Comment` に送ったパラメータが全部入る（同じ配置で出し直せる）

## ページの作り方（効いたこと）
- **ベース**: 人数タグ・白黒・場所・`thin lineart, clean lineart, soft shading`。人物プロンプトには `girl` / `boy`（数字なし）
- **1 コマ 1 人物プロンプト**。大ゴマに 2 人入れるときは 2 つのプロンプトを近くに置く（融合して 1 コマになる）
- 見せたいコマを大きく: 中央付近に置き、ほかは端に寄せる。均等に置かない
- **アングルは英文で具体的に**: 例「Seen from the side: the penis lies horizontally, coming in from the right edge, and its tip pushes against the pussy at the left side of the panel. One thigh fills the top edge and the other the bottom edge.」
- **似たコマは見た目の違いを書き分ける**（先端だけ・まだ閉じている ↔ 根元しか見えない・広がる・汁が飛ぶ）。さらに**人物ごとのネガに相手のコマの要素**（`inserted` ↔ `glans, not inserted`）。書き分けないと同じ絵がコピーされる
- キャラの固定タグ（髪型・服・男の髪色）は**全部の人物プロンプトに**入れる。入れないと男が金髪になる
- 胸: `hanging breasts` で巨大化 → ネガに `huge breasts, gigantic breasts`
- 使わない: `eyes in shadow`（目に黒い帯が入る）
- 再現できたページ: 引きとアップの組み合わせ、大ゴマ＋下段 2、5 要素の複雑なページ。**できないこと: 枠なしのコマ・コマをまたぐ重なり**（普通の枠つきになる）→ クリスタで重ねる
- **コマごとに 1 枚ずつ出すと CG っぽくなる**（アップが引きに、背景が細かく、汗や震えが減る）。1 ページで出すほうが漫画になる

## そのあと（ComfyUI 側）
1. **ページ丸ごと img2img**（キャラ LoRA）: 白黒は denoise 0.5 で構図そのまま顔だけそろう。0.65 で小物が変わり始める
   - カラーにするなら NovelAI で最初からカラー（ベース `full color`、ネガ `monochrome, greyscale`）→ 0.5。白黒ページからだと 0.85＋anytest が要り中身が変わる
2. **コマを切り出して約 3 倍で描き直す**: `novelai/panel_upscale.py`（anytest 0.6＋denoise 0.35、WD14 でコマごとにタグ。`--detect` で枠の自動検出を確認、斜めの枠・L 字・はめ込みは検出できないので `--boxes` で手で指定）。832×1216 のページの 1 コマは印刷には 3 倍ほど足りない
3. 他のコマの人物がかぶっていたら: はみ出しの演出ならクリスタで上に重ねる。消すなら ComfyUI の SetLatentNoiseMask インペイント denoise 0.85（NovelAI のインペイントはコマの端を白／灰で塗りつぶして失敗した）
4. フキダシの文字が入った画像を渡すときは先に `augment("declutter")`（跡が残らない。Qwen-Edit より確実）

## Director Tools の結果
- declutter: フキダシと文字が跡なく消える
- colorize: 白黒ページに自然な色
- lineart / sketch: 線画・ラフ化（anytest の参考に使える）
- emotion: **ページ中の全員の表情が変わる**（男まで照れ顔）→ コマを切り出してから使う

## 品質タグ・サンプラー・絵師タグ（2026-10-08 追記）
- API は品質タグとネガの初期セットを自動で足さない（Web 版はブラウザ側で足している）→ `generate(quality=True)`（既定）で `QUALITY` と `UC_PRESET` を足す。目が丁寧になり少し大人っぽくなる
- サンプラーは **euler を標準**にした（ユーザー指定）。euler / dpm++2m は線と陰影がくっきり・カラーでは色が落ち着く。euler_a（Web 既定）は柔らかく、カラーだと肌のピンクが強い。dpm++sde 系は柔らかく幼く見える
- 絵師タグはベースの先頭に `artist:名前`（Danbooru のローマ字）。**タグ候補 API（/ai/generate-image/suggest-tags）にはアニメ・漫画の絵師は出ない**（西洋画家だけ）ので、使えるかは生成して確かめる。5 ページ目で 11 人を試し、どじろー（dojirou）・ナポ（napo）は大きく変わり、大島あき（ooshima aki）・オクモト悠太（okumoto yuuta）・西沢みずき（nishizawa mizuki）は少し変わった。ほかはほぼ変化なし（ローマ字が違うか、学習されていない）
- **結論（ユーザー判断）: 絵師タグは使わない**。絵柄は変わるが本人の絵柄には程遠い。顔と絵柄はキャラ LoRA の img2img でそろえる
- **プロンプトの見返し**: NovelAI の PNG には送った設定が全部入っている。`python novelai/nai_prompts.py <フォルダ>` で、フォルダごとに `_プロンプト.md`（ベース・ネガ・キャラクターごとの文と位置・シード・サンプラー）を書き出す。Web 版に貼り直すときもこれを使う
