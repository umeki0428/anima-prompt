# ライザ / ライザリン・シュタウト (reisalin stout)

呼び方: 「ライザ」「ライザリン」「reisalin」「reisalin stout」「ryza」と指示されたらこのファイルを使う

Danbooru/Gelbooru の本体タグは `reisalin stout`。作品名はユーザー指定どおり `atelier (series)`。Gelbooru 表記(スペース区切り、括弧のエスケープなし)を優先。`atelier \(series\)` は使わない。

## 固定タグ(毎回そのまま使う・順番も維持)

1girl, reisalin stout, atelier (series), brown hair, short hair, brown eyes, hairclip, large breasts

## 既定の衣装(衣装の指示がなければ使う。別衣装を指示されたら全部削除して置き換える)

white headwear, beret, short shorts, red shorts, brown gloves, bare shoulders, cleavage, navel, collarbone, thick thighs

## 任意タグ(指示があれば付ける)

- 画風: anime coloring(既定ON。別画風の指示があれば外す)

## 既定の自然文(容姿の補足。タグと併用)

Reisalin Stout has short brown hair with a hairclip and brown eyes. She wears a white beret, red short shorts, and brown gloves, with bare shoulders, collarbone, and navel visible.

## 例(プロンプト全文)

| 内容 | ファイル | 状態 |
|---|---|---|
| 地面から見上げ・既定衣装のまま | [reisalin-from-below.md](../examples/_templates/reisalin-from-below.md) | 【未検証】 |

## 注意

- identity はキャラ名+作品名+髪・目・髪飾り・胸。服装と露出は既定衣装側。別衣装を指示されたら既定衣装だけ差し替える
- `thighs` と `thick thighs` は同義積み増しになるので、体型は `thick thighs` のみ使う
- `white headwear` と `beret` は色と種類の併用。崩れたら `white beret` に畳む
- `short shorts` と `red shorts` は形状と色の併用。既定衣装と別ボトムを混在させない
- ローアングルでは短パンが消えやすい。`(red shorts:1.8), (short shorts:1.8)` と自然文で裾が見えると書く
- 既定衣装と別衣装を混在させない(概念ブレンドで崩れる)
- レーティング既定は `safe`
- タグ順は 固定タグ → 衣装 → ポーズ/表情 → カメラ → 画風
