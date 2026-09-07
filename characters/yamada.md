# やまだ (yamada)

LoRAトリガー: 未指定(キャラ名タグは `yamada`)
呼び方: 「やまだ」「yamada」と指示されたらこのファイルを使う

## 固定タグ(毎回そのまま使う・順番も維持)

bangs, folded ponytail, brown hair, red hair, red eyes

## 既定の衣装(衣装の指示がなければ使う。別衣装を指示されたら全部削除して置き換える)

choker, black choker, white shirt, dress, white skirt, belt, leather, pantyhose, boots

## 任意タグ(指示があれば付ける)

- 人数: `1girl`(ソロ想定。複数人指示があれば人数タグを差し替える)
- 画風: 指定がなければ付けない。別画風の指示があれば `references/styles.md` に従う

## 注意

- 元タグの `masterpiece, best quality` はキャラ固定ではなく、プロンプト接頭辞(Anima-Base)へ置く。Aesthetic では省略可能で、使う場合も `score_*` は付けない
- `brown hair` と `red hair` の併記は二色髪(茶×赤)として扱う。単色にしたい指示があれば片方だけ残す
- `dress` と `white shirt` / `white skirt` の併記は概念ブレンドしやすい。別衣装指定時は既定衣装を全部削除する
- `choker` と `black choker` は一般タグ+色指定の併用。不要なら `black choker` のみでも可
- `leather` は素材タグで部位が曖昧。崩れたら `leather belt` や `leather boots` など部位を限定する
- 既定衣装と別衣装を混在させない(概念ブレンドで崩れる)
- タグ順は トリガー/キャラ名 → 固定タグ → 衣装 → ポーズ/表情 → カメラ → 画風 の順
