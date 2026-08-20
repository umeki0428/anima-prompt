# タグベースのプロンプト構造(公式ルール)

## タグの並び順(公式推奨)

```
[quality/meta/year/safety タグ] [1girl/1boy/1other 等] [キャラ名] [作品名] [絵師タグ] [一般タグ]
```

各セクション内での順序は自由。

## タグの書式ルール

- **小文字**で書く。
- アンダースコアではなく**スペース**を使う(例: `long hair`、`long_hair` ではない)。
  - 例外: `score_7` などの **score タグのみアンダースコア**を使う。
- DanbooruとGelbooruでタグが異なる場合は **Gelbooru 版を優先**。
- キャラ名・作品名も小文字タグで書く(例: `oomuro sakurako, yuru yuri`)。

## クオリティタグ(2系統)

**人力スコア系:**
`masterpiece, best quality, good quality, normal quality, low quality, worst quality`

**審美モデルスコア系:**
`score_9` (最高) 〜 `score_1` (最低)

- どちらか一方でも、両方でも、無しでも良い。
- **anima-aesthetic 使用時はクオリティタグ不要、`score_*` は非推奨**(すでに品質最適化済みのため)。

## 年代タグ

- 特定年: `year 2025`, `year 2024`, ...
- 期間ラベル: `newest, recent, mid, early, old`
- 絵柄の時代感を制御できる(新しい絵柄が欲しければ `newest` や `year 2025`)。

## メタタグ

`highres, absurdres, anime screenshot, official art, jpeg artifacts` など。

## 安全性(レーティング)タグ

`safe, sensitive, nsfw, explicit`

- ポジティブに `safe` を入れ、ネガティブと併用すると NSFW をほぼ完全に抑制できる。

## 絵師(アーティスト)タグ

- **必ず `@` を先頭に付ける**。例: `@nnn yryr`
- `@` を付けないと効果が非常に弱くなる。
- スタイル・絵師参照は**プロンプトの前方**に置くと効きやすい。
- 学習データには約6万の絵師スタイルが含まれる(Anima Style Explorer で検索可能)。

## プロンプト重み付け

- `(tag:1.5)` 形式の重み付けは使えるが、**SDXLより高めの値が必要**(例: `(chibi:2)`)。

## 公式のフルタグ例

```
year 2025, newest, normal quality, score_5, highres, safe, 1girl, oomuro sakurako, yuru yuri, @nnn yryr, smile, brown hair, hat, solo, fur-trimmed gloves, open mouth, long hair, gift box, fang, skirt, red gloves, blunt bangs, gloves, one eye closed, shirt, brown eyes, santa costume, red hat, skin fang, white background, holding bag, fur trim, simple background, brown skirt, bag, gift bag, looking at viewer, santa hat, ;d, red shirt, box, gift, holding, red capelet, holding box, capelet
```

## 出典

- https://huggingface.co/circlestone-labs/Anima
