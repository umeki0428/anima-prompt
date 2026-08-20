# 画師・スタイルタグの効き方

凡例: 【公式】= Hugging Face 公式README由来。【未検証】= 第三者記事由来で、このプロジェクトの実生成では未確認。

## 絵師(アーティスト)タグの書式【公式】

- **必ず `@` を先頭に付ける**(例: `@nnn yryr`)。@なしでは効果が非常に弱い。
- 小文字・スペース区切り(タグ書式は [anima-rules.md](anima-rules.md) 参照)。
- 画像内への絵師サイン描き込みを防ぐため、ネガティブに `artist name` を入れる。
- スタイル・絵師参照は**プロンプト前方**に置くと効きやすい【未検証】(https://diffusiondoodles.substack.com/p/anima-light-fast-and-slightly-unruly)。
- 学習データには約6万の絵師スタイルが含まれ、Anima Style Explorer で検索可能【未検証】(同上)。

出典: https://huggingface.co/circlestone-labs/Anima

## 画風タグの検証結果(108スタイル比較)【未検証・外部検証】

同一seed・同一設定での比較検証(https://note.com/ai_0049/n/n74ccab5370e0)より。
ベース: `masterpiece, best quality, score_7, safe, [スタイル], 1girl, solo, outerwear, skirt`

### 強く効いた(推奨強度: そのままで可)

| スタイル | 効果 |
|---|---|
| `Studio Ghibli style` | 素朴な顔立ち、抑えた色数、柔らかい線 |
| `Pixar style` | 丸みのある顔、3DCG風グラデーション塗り |
| `Spider-Verse style` | マゼンタ×シアンのハーフトーン処理 |
| `Akira Toriyama style` | 太めの線、原色配色 |
| `Arknights style` | ゲーム系キャラデザイン(白銀髪・エルフ耳等) |
| `Art Nouveau style` | 唐草模様、アーチフレーム、金の縁取り |
| `Vaporwave style` | ネオンピンク×パープル、90年代カルチャー |
| `Gothic style` | レザー・チョーカー・装飾フレームの耽美系 |
| `Golden Age Comic style` | 白黒ハーフトーンの印刷コミック質感 |
| `Pencil style` | 鉛筆画の粗い輪郭と淡さ |

### 弱い・無反応(推奨強度: 重み付け必須 or 使用回避)

- `cel shading style`, `flat color illustration` — デフォルト絵柄に埋もれて**無効**
- `chibi style`, `mecha anime style` — 体型変形系は反応が弱い。chibi は `(chibi:2)` 級の強い重みが必要【公式】(重み付けの必要性はHF READMEにも記載)
- `ink wash painting style` — 「painting」だけ解釈され水墨画にならない
- `steampunk / dieselpunk / solarpunk / biopunk` — 全て同じ「近未来風」に収束
- NSFW系 — `safe` + ネガティブで完全無効化

### 効き方の法則

**強く効く**: ①色彩とモチーフ両方に紐づく(art nouveau, vaporwave)、②モノクロ・ハーフトーン変換系(golden age comic, charcoal)、③固有の視覚的記号を持つ固有名詞(Spider-Verse, Ghibli, Akira Toriyama)。

**弱い**: ①アニメの基本塗りを指す(cel shading, flat color)、②体型変形・オブジェクト追加を要求(chibi, magical girl)、③抽象度の高い複合語(steampunk系, dystopian concept art)。

## このプロジェクトでの検証記録

(実生成で確認したら、ここに「タグ → 結果 → 推奨強度」を追記して【未検証】を外す)

## 出典

- https://huggingface.co/circlestone-labs/Anima 【公式】
- https://note.com/ai_0049/n/n74ccab5370e0
- https://diffusiondoodles.substack.com/p/anima-light-fast-and-slightly-unruly
