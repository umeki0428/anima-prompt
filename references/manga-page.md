# Anima 漫画ページのプロンプト

通常の1枚絵は [anima-rules.md](anima-rules.md) の3層(固定ブロック・タグ行・自然文)を使う。  
**漫画ページ**はこのファイルの4段構成にする。`<think>` は付けない。

## 4段構成

1. **品質タグ**
2. **登場人物の容姿のタグ**
3. **何コマ・どんな配置か**(サイズ差はここで書く。枚数の縦積みは書かない)
4. **コマ毎の状況説明**(ラベル付き。位置→カメラ→中身の順)

段のあいだは空行で分ける。

## 1. 品質タグ

anima-base の接頭辞に、レーティングとフルカラー指定を足す。

```
masterpiece, best quality, score_7, [safe|sensitive|explicit], newest,
```

フルカラーは `anime coloring` を品質段か配置段に入れる。  
`colored` も可。`shoujo manga style` / `shounen manga style` / `monochrome` / `greyscale` はモノクロ化するので使わない。

## 2. 容姿タグ

人数 → キャラ名 → 作品名 → 外見。複数人はキャラごとにまとめる。ComfyUI では括弧を `\(` `\)` でエスケープする。

```
1girl, darkness \(konosuba\), kono subarashii sekai ni shukufuku wo!, blonde hair, long hair, ponytail, blue eyes, large breasts,
1boy, short hair, black hair,
```

表情・拘束・濡れなど、ページ全体で共通する状態もここに置いてよい。コマ固有の動作は4段目へ。

## 3. 配置タグ(何コマか)

ページだと宣言し、**各コマの位置と大きさ**だけを書く。均等グリッドにしたいとき以外は `4koma` / `2koma` / `3koma` を使わない。

| 欲しいページ | ポジに書く | ネガに書く |
|---|---|---|
| 不揃い(ワイド+縦割り+大ゴマ等) | `comic page, multiple panels, panel layout, anime coloring` + 位置の英語 | `4koma, 3koma, 2koma, equal panels, stacked panels, grid layout` |
| 右が大ゴマ・左上が小コマ(L字) | 上に加えて `irregular manga layout, L-shaped page, thick black gutters, border, large vertical panel occupying the entire right side of the page, smaller rectangular panel in the upper left corner, the large panel wrapping under the small panel` | 同上 |
| 均等な4コマ縦積み | `4koma` | (縦積み回避タグは入れない) |

使ってはいけない表現: `four stacked panels`、`two panels` だけの指定、`2-panel manga layout`(上下均等の帯になる)。

`multiple views` は三面図なので配置段に使わない。ネガへ。

## 4. コマ毎の状況説明

1行1コマ。先頭ラベルで位置を固定してから、カメラ、ポーズ、表情、動作を列挙する。

```
right large panel: [カメラ], [全身/バストアップ], [拘束・ポーズ], [相手の動作], [状態],
upper left panel: close-up of [誰] face only, [表情], [視線], [カメラ],
```

ラベル例: `right large panel:` / `upper left panel:` / `top full-width panel:` / `bottom splash panel:` / `middle left vertical panel:`

吹き出し文字は1〜2単語まで。長い台詞は後入れ。

## ネガティブ(漫画ページ用)

基本形に、均等コマ・モノクロ・文字を足す。

```
worst quality, low quality, score_1, score_2, score_3, artist name, blurry, jpeg artifacts, chromatic aberration, 4koma, 3koma, 2koma, equal panels, stacked panels, grid layout, monochrome, greyscale, photorealistic, 3d, extra limbs, bad hands, extra fingers, multiple views, watermark, text, logo
```

## 設定

| 項目 | 値 |
|---|---|
| 解像度 | 1024×1536 または 768×1152(縦長ページ) |
| サンプラー | `er_sde` |
| CFG | 4〜5 |
| ステップ | 30〜50 |

配置が効かないときは、3段目の位置指定を `(large vertical panel occupying the entire right side of the page:1.5)` のように上げる。それでも潰れるなら1コマ1枚で生成して後で組む。

## 見本: 右大ゴマ + 左上アップ(L字)

```
masterpiece, best quality, score_7, explicit, newest,

1girl, darkness \(konosuba\), kono subarashii sekai ni shukufuku wo!, blonde hair, long hair, ponytail, orange-tipped hair, red hair clips, blue eyes, large breasts, blush, open mouth, sweat,
1boy, short hair, black hair,

comic page, multiple panels, panel layout, anime coloring, irregular manga layout, L-shaped page, thick black gutters, border,
large vertical panel occupying the entire right side of the page, smaller rectangular panel in the upper left corner, the large panel wrapping under the small panel,

right large panel: full body of Darkness, wrists bound together above her head, arms stretched up, body arched, legs spread, the boy's hand between her thighs fingering her roughly, vigorous fingering, pussy juice, trembling, kneeling or sitting, long blonde hair messy, heavy blush, from slightly in front,

upper left panel: close-up of Darkness's face only, moaning, open mouth, teary eyes, heavy blush, sweaty, ahegao, looking up, from slightly above
```

差分の足し方: 2段目のキャラタグを差し替え、4段目の動作だけ書き換える。3段目のL字配置はそのまま使う。

## 失敗

- `4koma` や `four stacked panels` → 同じ大きさの縦積み。[failures.md](failures.md)
- 配置を自然文の長文だけに頼る → コマが混ざる。位置は3段目の短い句で固定する。
