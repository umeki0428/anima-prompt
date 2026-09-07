# しずか (shizukamimizukaws)

LoRAトリガー: `shizukamimizukaws`
呼び方: 「しずか」と指示されたらこのファイルを使う

## 固定タグ(毎回そのまま使う・順番も維持)

short hair, multicolored hair, black hair, blue eyes, bright pupils, mole under eye, large breasts

## 既定の衣装(衣装の指示がなければ使う。別衣装を指示されたら全部削除して置き換える)

yellow headband, light blue t-shirt, bunny print, blue denim skirt, red backpack

## 任意タグ(指示があれば付ける)

- 文字描写: u.s.a text, text under bunny, red text(LoRA学習由来。不要なら付けない)
- 画風: anime coloring, anime screencap(既定ON。別画風の指示があれば外す)

## 注意

- 1枚絵の自然文に固定タグの容姿を再掲しない。漫画なら Character ブロックに一度だけ展開し、各 Panel では名前と動作だけ使う
- 元のLoRAキャプションにあった `multicolor hair` は `multicolored hair` が正式タグなので修正済み
- 既定衣装と別衣装を混在させない(概念ブレンドで崩れる)
- タグ順は 品質/レーティング → 1girl, solo → トリガー → 固定タグ → 衣装 → ポーズ/表情 → 背景 → カメラ → 画風 の順(`references/anima-rules.md` の公式順に準拠)
