# 漫画ページのプロンプト

通常の1枚絵は [anima-rules.md](anima-rules.md) の3層(固定ブロック・タグ行・自然文)を使う。  
**漫画ページ**はこのファイルの書式にする。`<think>` は付けない。

この書式は、**コマ位置を文章で指定する**タイプのLoRA向け。各コマの中身はタグ羅列より文章で書く。

## 構成

1. **冒頭の画風**
2. **Character one / Character two**(既存キャラは作品名+キャラタグ。服装は制服)
3. **Panel 1 / Panel 2 / ...**(位置 + 状況を文章で)

段のあいだは空行で分ける。

```
manga style,
dynamic panel layout,

Character one:
...

Character two:
...

Panel 1:
...

Panel 2:
...

Panel 3:
...
```

## 1. 冒頭の画風

毎回このブロックから始める。

```
manga style,
dynamic panel layout,
```

**使わない**(今後付けない):

```
black and white manga page,
professional Japanese manga,
clean detailed line art,
high quality screentones,
```

`4koma` / `2koma` / `3koma` は均等な縦積みになるので、不揃いのページでは使わない。[failures.md](failures.md)

## 2. 人物設定(Character)

既存キャラは容姿の長文に展開しない。作品名とキャラタグを書き、服装は制服(既定衣装)にする。ComfyUI では括弧を `\(` `\)` でエスケープする。

```
Character one:
blue archive,
rio \(blue archive\),
white turtleneck sweater, black jacket, id card, black skirt, pleated skirt, black pantyhose, thigh holster, black high heels,
```

各 Panel では同じ名前 `Rio` を使う。

```
Panel 1:
Rio is standing...

Panel 2:
close-up of Rio...
```

オリジナルキャラだけ、名前と容姿を文章で定義する。

```
Character one:
(Yuki), 22-year-old Japanese woman,
long straight black hair,
thin eyebrows,
large almond-shaped eyes,
small nose,
wearing a white blouse and black skirt,
```

複数人は `Character two:` を続ける。このLoRAだけでは複数コマの同一人物維持に限界があるので、既存キャラはタグ、オリジナルは冒頭の容姿定義を厚くする。

## 3. コマ(Panel)

タグ列挙ではなく、次を文章で書く。

- 人物が何をしている
- どこにいる
- カメラ位置
- 表情
- 背景

先頭でコマの位置と大きさを指定する。このLoRAは、まさにこの「コマ位置の文章指定」を学習している。

### 位置指定の例

上ワイド → 中段左右の縦割り → 下の大ゴマ:

```
Panel 1:
top full-width panel,
...

Panel 2:
middle left vertical panel,
...

Panel 3:
middle right vertical panel,
...

Panel 4:
bottom large full-width panel,
...
```

上段左右の縦コマ + 下の横長:

```
Panel 1:
equal-width vertical panel in the top left,
...

Panel 2:
equal-width vertical panel in the top right,
...

Panel 3:
bottom large full-width cinematic panel,
...
```

上の大ゴマ + 下左右の同じ大きさのコマ:

```
Panel 1:
large full-width panel occupying the top two-thirds of the page,
...

Panel 2:
equal-size square panel in the bottom left,
...

Panel 3:
equal-size square panel in the bottom right,
...
```

左上の小コマ + 右の縦長大ゴマ + 下の横長:

```
Panel 1:
small panel in the top left,
...

Panel 2:
large vertical panel on the right side,
...

Panel 3:
bottom full-width cinematic panel,
...
```

ほかの位置句: `top full-width panel` / `middle left vertical panel` / `middle right vertical panel` / `bottom large full-width panel` / `bottom splash panel`

使ってはいけない表現: `four stacked panels`、`two panels` だけの指定、`2-panel manga layout`(上下均等の帯になる)。

セリフ・吹き出し・♡・ハートマーク・擬音は入れない。文字は後入れ。

## 見本: 駅の夜(シンプルな2人・オリジナル)

```
manga style,
dynamic panel layout,

Character one:
(Yuki), a 22-year-old Japanese woman,
long straight black hair,
large expressive eyes,
wearing a white blouse and black skirt,

Character two:
a 24-year-old Japanese man,
short black hair,
wearing a casual jacket,

Panel 1:
top full-width panel,
the woman is standing at a train station at night,
looking nervously toward the man,
medium shot,
city lights visible in the background,

Panel 2:
middle left vertical panel,
close-up of the woman's face,
she looks away with a slight blush,
dramatic shading,

Panel 3:
middle right vertical panel,
the man looks at her from the side,
side profile composition,

Panel 4:
bottom large full-width panel,
the woman walks away while looking back over her shoulder,
emotional cinematic composition,
dramatic night atmosphere.
```

名前を付けた版では、Panel 内を `Yuki is standing at a train station at night` のようにする。

## 見本: リオ・深夜のオフィス(キャラタグ+制服)

Character one は作品名+キャラタグと制服のみ。容姿の長文は書かない。テンプレ全文は [rio-night-office-manga.md](../examples/_templates/rio-night-office-manga.md)。

```
manga style,
dynamic panel layout,

Character one:
blue archive,
rio \(blue archive\),
white turtleneck sweater, black jacket, id card, black skirt, pleated skirt, black pantyhose, thigh holster, black high heels,

Panel 1:
top full-width panel,
Rio is standing beside the floor-to-ceiling windows of a high-rise office at night,
looking down at the glowing city far below,
wide cinematic shot from slightly behind and to the side,
her expression is calm and distant,
the dark office interior and city lights fill the background,
```

ベッドのキス3コマは [rio-bed-kiss-manga.md](../examples/adult/rio-bed-kiss-manga.md)。  
顔アップ縦2段は [rio-face-closeup-manga.md](../examples/adult/rio-face-closeup-manga.md)。  
上大ゴマ+下左右は [rio-door-walkin-manga.md](../examples/adult/rio-door-walkin-manga.md)。

## 設定

| 項目 | 値 |
|---|---|
| 解像度 | 1024×1536 または 768×1152(縦長ページ) |
| サンプラー | `er_sde` |
| CFG | 4〜5 |
| ステップ | 30〜50 |

コマが潰れるときは、各 Panel 先頭の位置句を厚くする。それでも混ざるなら1コマ1枚で生成して後で組む。

## 失敗

- 既存キャラの髪・目・ヘイローを長文で書き直す → キャラタグと食い違う。`blue archive, rio \(blue archive\)` を使い、容姿はタグに任せる
- コマの動作・場所・カメラをタグだけ羅列する → 中身が薄くなる。Panel は文章で書く
- 各 Panel で名前を変える → 人物がコマ間で入れ替わる。同じ名前を使う
- `4koma` や `four stacked panels` → 同じ大きさの縦積み。[failures.md](failures.md)
- `black and white manga page` / `professional Japanese manga` / `clean detailed line art` / `high quality screentones` を付ける
- セリフ・吹き出し・♡・擬音を入れる → 文字が崩れる。コマには表情と動作だけ書く
