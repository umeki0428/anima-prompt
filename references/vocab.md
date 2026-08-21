# タグで書くべき語彙集

自然文で書くと表記が揺れたり無視されたりするため、**Danbooruタグで書くべき語彙**をここに蓄積する。
実生成で「自然文では揺れた/タグなら安定した」と確認できたものを追記していく。

記入フォーマット:

```
| 日本語 | 使うタグ | メモ(自然文での揺れ方など) | 確認日 |
```

## 髪型

| 日本語 | 使うタグ | メモ | 確認日 |
|---|---|---|---|
| (未記入) | | | |

## 衣装

| 日本語 | 使うタグ | メモ | 確認日 |
|---|---|---|---|
| 上着を脱いでいる途中 | `undressing, removing jacket` | 脱ぎ終わりは `unworn jacket`。肩に残るだけなら `jacket on shoulders`。【未検証】 | |
| スカートを残す(下アングル) | `(black skirt:1.8), (pleated skirt:1.8), miniskirt` | 下アングル+undressing だとスカートが消える。自然文でも hem is visible / not removed と書く。重みは SDXLより高め(公式) | 2026-08-21 |

## ポーズ・視線

| 日本語 | 使うタグ | メモ | 確認日 |
|---|---|---|---|
| 軽い赤面 | blush | 自然文で faint blush。照れなら `embarrassed` も足す。【未検証】 | |
| 半目 | half-closed eyes | 自然文は half-lidded eyes。最終稿で使用 | 2026-08-21 |
| 汗・湯気 | `sweat, steam, haze` | 顔の汗と空気中の湯気。最終稿で使用 | 2026-08-21 |

## 小物・持ち物

| 日本語 | 使うタグ | メモ | 確認日 |
|---|---|---|---|
| (未記入) | | | |

## 構図・カメラ

| 日本語 | 使うタグ | メモ | 確認日 |
|---|---|---|---|
| 下から見上げ | from below | 【未検証】 | |
| 上から見下ろし | from above | 【未検証】 | |
| 斜め構図 | dutch angle | 【未検証】 | |
| 顔アップ | close-up | 【未検証】 | |
| バストアップ | upper body | 【未検証】 | |
| 太ももまで | cowboy shot | 【未検証】 | |
| 太ももから下は切る | cowboy shot | 靴・足元タグは外す。ネガに `shoes, high heels, feet`。【未検証】 | |
| 全身 | full body | 【未検証】 | |
| 横顔 | profile | 【未検証】 | |
| 後ろ姿 | from behind | 【未検証】 | |
| こっち目線 | looking at viewer | 【未検証】 | |
| 視線外し | looking away | 【未検証】 | |
| 不揃いの漫画ページ | `comic page, multiple panels, panel layout` | `4koma` は均等な縦積みになる(2026-08-21)。サイズ差は配置タグで位置を書く。書式は [manga-page.md](manga-page.md)。ネガに `4koma, 2koma, 3koma` | 2026-08-21 |
| 均等4コマ | `4koma` | 同じ大きさのコマが上から下(または2×2)。動的なページには使わない | 2026-08-21 |
| フルカラー漫画 | `colored` | `shoujo manga style` / `shounen manga style` / `monochrome` / `greyscale` はモノクロ化するのでフルカラーではネガへ | 【未検証】 |
| 紫のグラデーション背景 | (使わない) | シーン全体が紫に染まる。暗い背景は下の行 | 2026-08-21 |
| 暗いチャコールグラデ | `simple background, gradient background, dark background` | 自然文で dark charcoal gradient, not purple。ネガに `purple background, outdoors, scenery, cloudy sky` | 2026-08-21 |
| 暖色リム | `dim lighting, warm lighting, rim light, volumetric lighting` | 下と後ろからの薄いリム。紫と混ぜない | 2026-08-21 |
