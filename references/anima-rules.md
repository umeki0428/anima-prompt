# Anima 固有の書式ルール

出典の凡例: 【公式】= Hugging Face 公式README / docs.comfy.org 由来。【未検証】= 第三者記事由来で、このプロジェクトの実生成では未確認。

## 出力の3層構造(このプロジェクトの標準形)

プロンプトは常に次の3層で組み立てる:

1. **固定ブロック** — 接頭辞とネガティブ(下記「固定ブロック」節)。毎回ほぼ同じ。
2. **タグ行** — Danbooru形式で主題・属性を確定(人数、キャラ、外見、服装、表情、画風)。
3. **自然文** — 英語2文以上で構図・空間関係・雰囲気を補足。

タグと自然文の分担: **タグ=「何を描くか」、自然文=「どこに・どう配置するか」**。ハイブリッドが最良バランスという報告【未検証】(https://diffusiondoodles.substack.com/p/anima-light-fast-and-slightly-unruly)。自然文だと表記が揺れる語彙は [vocab.md](vocab.md) を参照してタグで書く。

## 固定ブロック

**接頭辞(anima-base v1.0 用)【公式】:**

```
masterpiece, best quality, score_7, safe,
```

**anima-aesthetic v1.1 用【公式】:** クオリティタグ・`score_*` は**付けない**(品質最適化済みのため)。`safe, ` 等のレーティングタグのみ。

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

## タグの書式【公式】

- **小文字**、アンダースコアではなく**スペース**(例: `long hair`)。例外: `score_*` のみアンダースコア。
- Danbooru と Gelbooru でタグが異なる場合は **Gelbooru 版を優先**。
- タグの並び順:

```
[quality/meta/year/safety] [1girl/1boy/1other等] [キャラ名] [作品名] [@絵師] [一般タグ]
```

各セクション内の順序は自由。

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
- 純自然文なら**最低2文**、描写は多めが良い【公式】。
- **キャラ名を出したら続けて外見を描写する**。複数キャラでは必須(名前だけだと特徴が混ざる)【公式】。
- 複数キャラは「キャラごとに名前→外見」をまとめ、位置関係(left/right/behind等)を自然文で明示する【未検証】。

## 長さ・NG構文

- 全体で**2〜3段落・15行未満**が最適。長すぎると追従性・品質が低下【未検証】(https://diffusiondoodles.substack.com/p/anima-light-fast-and-slightly-unruly)。
- **縛りすぎるプロンプトには反発する**傾向。自由度を残す【未検証】(同上)。
- 同義タグの積み増し(tag overloading)は避ける【未検証】(同上)。
- **JSON/YAML形式は非推奨**。複雑になると破綻し、品質面の利点なし【未検証】(同上)。
- **文字描画は1〜2単語まで**。複雑なタイポグラフィ不可【公式】(https://docs.comfy.org/tutorials/image/anima/anima)。入れる場合は自然文中で引用符で囲む(例: `a sign that says "OPEN"`)【未検証】。
- 異なる概念は**互いにブレンドされやすい**(服の色がキャラ間で入れ替わる等)。要素を絞る【未検証】(https://techtactician.com/anima-comfyui-quick-local-setup-guide/)。

## 漫画ページ(コマ割り)

詳細と見本は [manga-page.md](manga-page.md)。通常の3層ではなく、品質 → 容姿 → 配置 → コマ説明の4段にする。`4koma` は均等な縦積みになるので、不揃いのページでは使わない。

## 日本語指示 → プロンプト変換の手順

1. **主題を確定**: 人数(`1girl`/`2girls`/`1boy`/`1other`)、キャラ名・作品名(既存キャラなら小文字タグで)
2. **外見・服装・表情・ポーズ**を Danbooru タグに変換([vocab.md](vocab.md) を参照)
3. **背景・構図・ライティング**は自然文で補足(空間関係はタグより自然文が得意)。エロさだけ足す光・色・表情・湯気は [atmosphere.md](atmosphere.md)。漫画ページは [manga-page.md](manga-page.md) の4段構成にする
4. **画風指定**があれば前方に配置(`Studio Ghibli style` 等、または `@絵師名`。[styles.md](styles.md) 参照)
5. 接頭辞と年代タグ(新しい絵柄なら `newest`)を付与。aesthetic ならクオリティ/score タグなし
6. ネガティブは基本形+目的別追加
7. 全体を**15行未満・2〜3段落以内**に収める。細部を縛りすぎない

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
- https://docs.comfy.org/tutorials/image/anima/anima 【公式】
- https://diffusiondoodles.substack.com/p/anima-light-fast-and-slightly-unruly
- https://techtactician.com/anima-comfyui-quick-local-setup-guide/
