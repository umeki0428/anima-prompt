# ネガティブプロンプト

## 公式推奨ネガティブ(基本形)

```
worst quality, low quality, score_1, score_2, score_3, artist name, blurry, jpeg artifacts, chromatic aberration
```

- `artist name` は画像内に絵師のサイン・名前が描き込まれるのを防ぐ。
- anima-aesthetic 使用時も score 系ネガティブはそのまま使ってよい(ポジティブ側の score タグのみ非推奨)。

## よく追加される要素

用途に応じて基本形に追記する:

| 目的 | タグ例 |
|---|---|
| 解剖学的破綻の抑制 | `bad anatomy, extra limbs, bad hands` |
| 透かし・文字の抑制 | `watermark, signature, text, logo, twitter username` |
| 実写・3D化の防止 | `photorealistic, 3d, cgi` |
| 背景が寂しいときの逆用 | `simple background`(ポジティブに背景描写がある場合) |
| 画風の締まり | `muddy colors, thick lineart, painterly`(狙いの画風に応じて) |
| 構図制御 | `close-up face only, portrait crop`(顔アップを避けたいとき) |

## NSFW 制御

- ポジティブに `safe`、ネガティブに `nsfw, explicit, sensitive` を入れると、NSFW系タグを混ぜてもほぼ完全に無効化できる(108スタイル検証でも確認済み)。

## 実例(検証記事で使われた構成)

```
worst quality, low quality, score_1, score_2, score_3, artist name, blurry, bad anatomy, extra limbs, watermark, signature, jpeg artifacts, simple background
```

## 出典

- https://huggingface.co/circlestone-labs/Anima
- https://note.com/ai_0049/n/n74ccab5370e0
- https://comfyui.nomadoor.net/en/basic-workflows/anima/
