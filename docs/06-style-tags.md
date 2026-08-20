# 画風(アートスタイル)タグの効き方

同一seed・同一設定で108種の画風プロンプトを比較した日本語検証記事
([おーら氏の note 記事](https://note.com/ai_0049/n/n74ccab5370e0))のまとめ。

検証時のベースプロンプト:

```
masterpiece, best quality, score_7, safe, [スタイル挿入], 1girl, solo, outerwear, skirt
```

## 強く効いたスタイル(トップ10)

| スタイル | 効果 |
|---|---|
| `Studio Ghibli style` | 素朴な顔立ち、抑えた色数、柔らかい線 |
| `Pixar style` | 丸みのある顔、3DCG風グラデーション塗り |
| `Spider-Verse style` | マゼンタ×シアンのハーフトーン処理 |
| `Akira Toriyama style` | 太めの線、原色配色、鳥山明風の顔 |
| `Arknights style` | 白銀髪・エルフ耳などゲーム系デザイン |
| `Art Nouveau style` | 唐草模様、アーチフレーム、金の縁取り |
| `Vaporwave style` | ネオンピンク×パープル、90年代カルチャー |
| `Gothic style` | レザー・チョーカー・装飾フレームの耽美系 |
| `Golden Age Comic style` | 白黒ハーフトーンの印刷コミック質感 |
| `Pencil style` | 鉛筆画特有の粗い輪郭と淡さ |

## 効きが弱い・無効なスタイル

- `cel shading style`, `flat color illustration` — Animaのデフォルト絵柄に埋もれて変化なし
- `chibi style`, `mecha anime style` — **体型変形やオブジェクト追加を要求するタグは反応が弱い**(chibi は `(chibi:2)` のような強い重み付けが必要)
- `ink wash painting style` — 「painting」だけが解釈され水墨画にならない
- `steampunk / dieselpunk / solarpunk / biopunk` — どれも同じ「近未来風」出力に収束
- NSFW系 — `safe` タグ+ネガティブで完全無効化

## 効くタグの傾向(法則)

**強く効く:**
- 色彩とモチーフの**両方**に紐づくタグ(art nouveau, vaporwave, psychedelic art)
- モノクロ・ハーフトーン変換系(golden age comic, charcoal drawing, マンガ系)
- 固有の視覚的記号を持つ固有名詞系(Spider-Verse, Ghibli, Akira Toriyama)

**弱い:**
- アニメの基本塗りを指すタグ(cel shading, flat color)
- 体型変形・オブジェクト追加を要求するタグ(chibi, magical girl)
- 抽象度の高い複合語(steampunk系, dystopian concept art)

## 実在絵師スタイルの利用

- `@絵師名` 形式(@必須)。約6万スタイルが学習済み。
- スタイル指定はプロンプト**前方**に置く。

## 出典

- https://note.com/ai_0049/n/n74ccab5370e0
- https://huggingface.co/circlestone-labs/Anima
