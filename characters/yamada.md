# やまだ (yamada)

LoRAトリガー: 学習元は `yamada_yanisuu-mdfdver`(Anima は SDXL LoRA 非互換。プロンプトには入れず、キャラ名タグは `yamada`)
呼び方: 「やまだ」「yamada」「tayama」と指示されたらこのファイルを使う

## 固定タグ(毎回そのまま使う・順番も維持)

bangs, folded ponytail, brown hair, red hair, red eyes

## 既定の衣装(衣装の指示がなければ使う。別衣装を指示されたら全部削除して置き換える)

choker, black choker, white shirt, dress, white skirt, belt, leather, pantyhose, boots

## 衣装差分(指示されたら既定衣装を全部削除して、下の行に置き換える)

### 田山アルト (`tayama-altoutfit1`)

alternate costume, black choker, black shirt, shirt tucked in, shorts, belt, blue jacket, open jacket

全身なら `black footwear` を足す。クロップ外なら足さない。

## 別髪型(指示されたら `folded ponytail` を外し、下を足す。`bangs` と目の色は残す)

medium hair, straight hair, sidelocks, earrings

単色の赤髪にする指示なら `brown hair` も外す。`long hair` は `medium hair` と重ねない。

## 任意タグ(指示があれば付ける)

- 人数: `1girl`(ソロ想定。複数人指示があれば人数タグを差し替える)
- 画風: 指定がなければ付けない。別画風の指示があれば `references/styles.md` に従う

## 注意

- 元タグの `masterpiece, best quality` はキャラ固定ではなく、プロンプト接頭辞(anima-base)へ置く。aesthetic では付けない
- `brown hair` と `red hair` の併記は二色髪(茶×赤)として扱う。単色にしたい指示があれば片方だけ残す
- `dress` と `white shirt` / `white skirt` の併記は概念ブレンドしやすい。別衣装指定時は既定衣装を全部削除する
- `choker` と `black choker` は一般タグ+色指定の併用。不要なら `black choker` のみでも可
- `leather` は素材タグで部位が曖昧。崩れたら `leather belt` や `leather boots` など部位を限定する
- 既定衣装と別衣装を混在させない(概念ブレンドで崩れる)
- `tayama-altoutfit1` と `tayamaoutfit`(黒レザー)は別衣装。同時に使わない
- `open clothes` はシャツまで開く。青ジャケットを開くだけなら `open jacket`
- タグ順は トリガー/キャラ名 → 固定タグ → 衣装 → ポーズ/表情 → カメラ → 画風 の順
- 太ももから下が見えない指示なら `boots` / `black footwear` を外し `cowboy shot`。ネガに `shoes, boots, feet`

## 例(プロンプト全文)

| 内容 | ファイル | 状態 |
|---|---|---|
| 胸の前で手のひらこちら・口タバコ・真顔・白背景 | [yamada-tada-pose.md](../examples/_templates/yamada-tada-pose.md) | 【未検証】 |
