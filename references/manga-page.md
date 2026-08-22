# 漫画ページのプロンプト

通常の1枚絵は [anima-rules.md](anima-rules.md) の3層(固定ブロック・タグ行・自然文)を使う。  
**漫画ページ**はこのファイルの書式にする。`<think>` は付けない。

この書式は、**コマ位置を文章で指定する**タイプのLoRA向け。タグを羅列するより、人物と各コマを文章で書く。

## 構成

1. **冒頭の画風**
2. **Character one / Character two**(容姿を詳しく。名前を付ける)
3. **Panel 1 / Panel 2 / ...**(位置 + 状況を文章で)

段のあいだは空行で分ける。

```
manga style,
black and white manga page,
professional Japanese manga,
clean detailed line art,
high quality screentones,
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

Panel 4:
...
```

## 1. 冒頭の画風

毎回このブロックから始める。

```
manga style,
black and white manga page,
professional Japanese manga,
clean detailed line art,
high quality screentones,
dynamic panel layout,
```

`4koma` / `2koma` / `3koma` は均等な縦積みになるので、不揃いのページでは使わない。[failures.md](failures.md)

## 2. 人物設定(Character)

このLoRAだけでは、複数コマで完全に同じ人物を維持する能力に限界がある。  
最初に容姿をかなり詳しく定義し、各 Panel では同じ名前を使う。

```
Character one:
(Yuki), 22-year-old Japanese woman,
long straight black hair,
thin eyebrows,
large almond-shaped eyes,
small nose,
wearing a white blouse and black skirt,
```

既存キャラなら `characters/<名前>.md` の固定タグ・既定衣装・既定自然文を、この Character ブロックの文章に展開する。タグ行のまま貼らない。

複数人は `Character two:` を続ける。各 Panel では `(Yuki)` ではなく `Yuki` と呼ぶ。

```
Panel 1:
Yuki is standing...

Panel 2:
close-up of Yuki...

Panel 3:
Yuki turns her face...
```

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

吹き出し文字は1〜2単語まで。長い台詞は後入れ。

## 見本: 駅の夜(シンプルな2人)

```
manga style,
black and white manga page,
professional Japanese manga line art,
clean ink lines,
detailed screentones,
dramatic manga composition,

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
dramatic manga screentones,

Panel 3:
middle right vertical panel,
the man gently speaks to her,
side profile composition,

Panel 4:
bottom large full-width panel,
the woman walks away while looking back over her shoulder,
emotional cinematic composition,
dramatic night atmosphere.
```

名前を付けた版では、Panel 内を `Yuki is standing at a train station at night` のようにする。

## 見本: リオ・深夜のオフィス(キャラ固定)

リオの固定容姿を Character one に展開し、各 Panel で `Rio` を使う。`characters/rio.md` があるときはそこから展開する。テンプレ全文は [rio-night-office-manga.md](../examples/_templates/rio-night-office-manga.md)。

```
manga style,
black and white manga page,
professional Japanese manga,
clean detailed line art,
high quality screentones,
dynamic panel layout,

Character one:
(Rio), a young Japanese woman,
thigh-length straight black hair,
blunt bangs,
one side of her hair tucked behind her ear,
a Millennium science school logo hairclip,
large almond-shaped red eyes with ringed irises and white pupils,
a black metallic halo floating above her head,
large breasts,
wearing a white turtleneck sweater,
a black jacket with an ID card,
a black pleated skirt,
black pantyhose,
a thigh holster,
and black high heels,

Panel 1:
top full-width panel,
Rio is standing beside the floor-to-ceiling windows of a high-rise office at night,
looking down at the glowing city far below,
wide cinematic shot from slightly behind and to the side,
her expression is calm and distant,
the dark office interior and city lights fill the background,
```

## 設定

| 項目 | 値 |
|---|---|
| 解像度 | 1024×1536 または 768×1152(縦長ページ) |
| サンプラー | `er_sde` |
| CFG | 4〜5 |
| ステップ | 30〜50 |

コマが潰れるときは、各 Panel 先頭の位置句を厚くする。それでも混ざるなら1コマ1枚で生成して後で組む。

## 失敗

- 容姿や動作をタグだけ羅列する → コマの中身が薄くなる。Character と Panel は文章で書く
- 各 Panel で名前を変える / 容姿を省略する → 人物がコマ間で入れ替わる。冒頭で詳しく定義し、同じ名前を使う
- `4koma` や `four stacked panels` → 同じ大きさの縦積み。[failures.md](failures.md)
