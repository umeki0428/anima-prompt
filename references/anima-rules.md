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
- **文字描画は1〜2単語まで**。複雑なタイポグラフィ不可【公式】(https://docs.comfy.org/tutorials/image/anima/anima)。
- 異なる概念は**互いにブレンドされやすい**(服の色がキャラ間で入れ替わる等)。要素を絞る【未検証】(https://techtactician.com/anima-comfyui-quick-local-setup-guide/)。

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
