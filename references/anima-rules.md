# Anima 固有の書式ルール

出典の凡例: 【公式】= Hugging Face 公式README / docs.comfy.org 由来。【未検証】= 第三者記事由来で、このプロジェクトの実生成では未確認。

## 出力の基本形(このプロジェクトの標準形)

Anima は Danbooru 形式のタグ、自然言語キャプション、その混合で学習されている【公式】。このプロジェクトでは、単純な1枚絵は次の簡潔なハイブリッド形式を標準とする。

1. **固定ブロック** — 接頭辞とネガティブ(下記「固定ブロック」節)。
2. **タグ行** — 人数、キャラ、外見、服装、表情、構図、画風などの離散的な要素。
3. **短い自然文(必要な場合だけ)** — 服の重なり、人物間の位置関係、画面のどこまで写すかなど、タグだけでは曖昧な内容。

自然文が不要なら固定ブロック＋タグ行だけでよい。**タグで確定した内容を自然文で言い直さない。** たとえば `black hair, low twintails, blue eyes` と書いた後に、同じ髪と目を文章で再説明しない。公式はタグのランダムドロップアウト学習を明記しており、画像に関係するタグをすべて列挙する必要はない【公式】。

タグと自然文の分担は、**タグ=「何を描くか」、自然文=「タグでは表しにくい関係や状態」**。自然文だと表記が揺れる語彙は [vocab.md](vocab.md) を参照してタグにする。

## 固定ブロック

**接頭辞(anima-base v1.0 用)【公式】:**

```
masterpiece, best quality, score_7, safe,
```

**Anima-Aesthetic 用【公式】:** 品質タグは不要。`masterpiece, best quality` は残してもよいが、`score_*` はポジティブ・ネガティブとも使わないことが公式推奨。`safe, ` 等のレーティングタグは目的に合わせる。

**Anima-Turbo 用【公式】:** プロンプト形式は同じ。CFG 1、8〜12ステップを基本にする。

**ネガティブ基本形【公式】:**

```
worst quality, low quality, score_1, score_2, score_3, artist name, blurry, jpeg artifacts, chromatic aberration
```

目的別の追加(基本形に足す):

| 目的 | タグ |
|---|---|
| 解剖学的破綻の抑制【未検証】 | `bad anatomy, extra limbs, bad hands` |
| 透かし・文字の抑制【未検証】 | `watermark, signature, text, logo, twitter username` |
| 実写・3D化の防止【未検証】 | `photorealistic, 3d, cgi` |
| NSFW抑制【未検証・外部検証あり】 | ポジに `safe` + ネガに `nsfw, explicit, sensitive`(https://note.com/ai_0049/n/n74ccab5370e0) |
| 顔アップ回避(構図制御)【未検証】 | `close-up face only, portrait crop`(https://comfyui.nomadoor.net/en/basic-workflows/anima/) |
| 背景が寂しいときの逆用【未検証】 | ポジに背景描写がある場合、ネガに `simple background` |

出典: https://huggingface.co/circlestone-labs/Anima

ネガティブは基本形に、**今回起きやすい失敗だけ**を追加する。画面に出る理由がない服、身体部位、構図を網羅的に禁止しない。意図的な腰上構図で `cropped`、意図的な上半身構図で `out of frame` のような包括的な否定を入れると、ポジティブと競合するため避ける。必要なら `cropped head` のように失敗を限定する。

## タグの書式【公式】

- **小文字**、アンダースコアではなく**スペース**(例: `long hair`)。例外: `score_*` のみアンダースコア。
- Danbooru と Gelbooru でタグが異なる場合は **Gelbooru 版を優先**。
- タグの並び順:

```
[quality/meta/year/safety] [1girl/1boy/1other等] [キャラ名] [作品名] [@絵師] [一般タグ]
```

各セクション内の順序は自由。

## タグの量【公式】

- Anima はランダムなタグドロップアウトを使って学習されているため、関連タグをすべて入れる必要はない。
- 親子・同義タグを重ねない。例: `long hair` と `very long hair`、`skirt` と `pleated skirt` を必要なく併記しない。
- 1つの特徴は原則1回だけ指定する。タグ、自然文、ネガティブをまたいで同じ意味を反復しない。
- 強調したい特徴でも、まず通常タグで生成する。効かなかった場合だけ重み付けを試す。

## タグカテゴリ【公式】

- **クオリティ(人力)**: `masterpiece, best quality, good quality, normal quality, low quality, worst quality`
- **クオリティ(審美スコア)**: `score_9`(高)〜`score_1`(低)。人力/スコアは片方・両方・無しのいずれも可。
- **年代**: `year 2025` 等の特定年、または `newest, recent, mid, early, old`。新しい絵柄なら `newest`。
- **メタ**: `highres, absurdres, anime screenshot, official art` 等。
- **レーティング**: `safe, sensitive, nsfw, explicit`。
- **絵師**: `@絵師名`(@必須)。詳細と効き方は [styles.md](styles.md)。

**公式のフルタグ例【公式】:**

```
year 2025, newest, normal quality, score_5, highres, safe, 1girl, oomuro sakurako, yuru yuri, @nnn yryr, smile, brown hair, hat, solo, fur-trimmed gloves, open mouth, long hair, gift box, fang, skirt, red gloves, blunt bangs, gloves, one eye closed, shirt, brown eyes, santa costume, red hat, skin fang, white background, holding bag, fur trim, simple background, brown skirt, bag, gift bag, looking at viewer, santa hat, ;d, red shirt, box, gift, holding, red capelet, holding box, capelet
```

## 自然文のルール

- 英語の標準的な大文字化に従う(キャラ名・作品名は大文字始まり。タグとは逆)【公式】。
- **純自然文だけで作る場合**は最低2文を目安に、十分具体的に書く【公式】。
- タグとのハイブリッドでは最低文数を設けない。補足が1文で済むなら1文、不要なら自然文なしでよい。
- タグで指定済みの外見・衣装・表情・構図を文章で繰り返さない。
- 出したくない概念をポジティブ自然文へ書かない。`not gigantic`、`not elderly` のような否定は対象語を呼び込む可能性があるため、必要なら短いネガティブタグへ移す。
- **キャラ名を出したら続けて外見を描写する**。複数キャラでは必須(名前だけだと特徴が混ざる)【公式】。
- 複数キャラは「キャラごとに名前→外見」をまとめ、位置関係(left/right/behind等)を自然文で明示する【未検証】。
- **撮影用語が通る**。ショット種別(`over-the-shoulder shot`, `medium close-up`)と被写界深度(`shallow depth of field`, `out of focus foreground`)は Danbooru タグより強く効く。カメラ高さだけはタグ(`from below`)+自然文(`low angle`)の二重指定が必要。検証は [composition.md](composition.md)【実生成・2026-09-07】。
- **指示にない背景タグを足さない**。`simple background, gradient background, blurry background` は指示に無ければ入れない。室内描写と同居すると背景がブレンドして額や壁が消える【実生成・2026-09-07】。
- **出力は必ずタグ行と自然文を分ける**。全文自然文にしない(タグで確定できる語彙が揺れる)。

## 長さ・NG構文

- 単純な1人絵は**タグ1行＋自然文0〜2文**から始める。情報が不足した場合だけ追加する。
- 複雑な場面でも全体で**2〜3段落・15行未満**を上限の目安にする【未検証】(https://diffusiondoodles.substack.com/p/anima-light-fast-and-slightly-unruly)。
- **縛りすぎるプロンプトには反発する**傾向。自由度を残す【未検証】(同上)。
- 同義タグの積み増し(tag overloading)は避ける【未検証】(同上)。
- ポジティブで「Aではない」「Bほど大きくない」と否定形を重ねない。望む状態を直接書き、不要概念は必要最小限のネガティブへ置く。
- ネガティブへ思いつく失敗を網羅しない。ポジティブと競合する包括語や、今回の画面に無関係な衣装・身体部位は削る。
- **JSON/YAML形式は非推奨**。複雑になると破綻し、品質面の利点なし【未検証】(同上)。
- **文字描画は1〜2単語まで**。複雑なタイポグラフィ不可【公式】(https://docs.comfy.org/tutorials/image/anima/anima)。入れる場合は自然文中で引用符で囲む(例: `a sign that says "OPEN"`)【未検証】。
- 異なる概念は**互いにブレンドされやすい**(服の色がキャラ間で入れ替わる等)。要素を絞る【未検証】(https://techtactician.com/anima-comfyui-quick-local-setup-guide/)。
- **2人は外見を混ぜない。** 片方に長髪・ハロがあるなら、もう片方は短い別色の髪を自然文で先に書く【実生成・2026-08-21】。
- **服の内側の手**(タンクトップの脇・裾から入れて胸を触る等)は Anima 単発では再現できない。言い回しを変えて再挑戦しない。記録は [failures.md](failures.md)【実生成・2026-08-22】。
- Danbooru由来のタグは**アンダースコアをスペースに直し**、同義の積み増し(`skirt` + `black skirt` + `pleated skirt` など)は畳む。

## 漫画ページ(コマ割り)

詳細と見本は [manga-page.md](manga-page.md)。通常の簡潔なハイブリッド形式ではなく、画風行 → Character → Panel文章にする。コマ位置はタグ列挙ではなく文章で指定する。`4koma` は均等な縦積みになるので、不揃いのページでは使わない。

## 日本語指示 → プロンプト変換の手順

1. **主題を確定**: 人数(`1girl`/`2girls`/`1boy`/`1other`)、キャラ名・作品名(既存キャラなら小文字タグで)
2. **外見・服装・表情・ポーズ・基本構図**を、重複しない最小限の Danbooru タグに変換([vocab.md](vocab.md) を参照)
3. **服の重なり、空間関係、厳密なフレーミング**など、タグだけでは曖昧な点だけを短い自然文で補足する。単純な1枚絵では自然文を省略してよい。エロさだけ足す光・色・表情・湯気は [atmosphere.md](atmosphere.md)。漫画ページは [manga-page.md](manga-page.md) の Character / Panel 文章にする
4. **画風指定**があれば前方に配置(`Studio Ghibli style` 等、または `@絵師名`。[styles.md](styles.md) 参照)
5. 接頭辞と年代タグ(新しい絵柄なら `newest`)を付与。Aesthetic では `score_*` を外し、品質タグは省略または `masterpiece, best quality` だけにする
6. ネガティブは基本形に、今回起きやすい失敗だけを追加する。ポジティブと競合しないか確認する
7. 最後に重複監査を行う。同じ特徴がタグと自然文に二重指定されていたら、原則として自然文側を削る
8. 1枚絵はタグ1行＋自然文0〜2文から始める。漫画ページは [manga-page.md](manga-page.md) の Character / Panel 文章を優先する

## 重み付け【公式】

`(tag:1.5)` 形式は使えるが **SDXLより高い値が必要**(例: `(chibi:2)`)。

## 前提知識(要点のみ)

- Anima = CircleStone Labs × Comfy Org、2Bパラメータ、アニメ/イラスト特化。実写はサポート外【公式】。
- NVIDIA Cosmos系Transformer + Qwen-3 0.6Bテキストエンコーダ。自然言語理解と複数キャラの空間関係に強い【公式】。
- **SDXL用LoRA非互換**【未検証】。知識カットオフ2025年9月頃【未検証】(https://techtactician.com/anima-comfyui-quick-local-setup-guide/)。
- 出力ばらつきが大きい設計。**seed/サンプラーを変えた複数回生成が前提**【未検証】。
- 必要ファイル: diffusion model(`models/diffusion_models/`)、`qwen_3_06b_base.safetensors`(`models/text_encoders/`)、`qwen_image_vae.safetensors`(`models/vae/`)【公式】。詳細は `_archive/docs/01-anima-basics.md`。
- サンプラー・CFG等は [settings.md](settings.md)。

## 主な出典

- https://huggingface.co/circlestone-labs/Anima 【公式】
- https://huggingface.co/circlestone-labs/Anima/raw/main/README.md 【公式・プロンプト仕様とタグドロップアウト】
- https://docs.comfy.org/tutorials/image/anima/anima 【公式】
- https://diffusiondoodles.substack.com/p/anima-light-fast-and-slightly-unruly
- https://techtactician.com/anima-comfyui-quick-local-setup-guide/
