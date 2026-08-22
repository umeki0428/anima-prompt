# 失敗事例集(外れた出力 → 原因 → 直し方)

実生成で意図と違う出力になった事例をここに蓄積する。同じ失敗を繰り返さないための一次資料。

記入フォーマット:

```
## <短いタイトル> (YYYY-MM-DD)

- **指示(日本語)**: 何を作ろうとしたか
- **使ったプロンプト**: (ポジ/ネガ、設定も変えていれば記載)
- **外れた出力**: どうなったか
- **原因(推定)**: なぜそうなったか
- **直し方**: 効いた修正。確定なら vocab.md / anima-rules.md / styles.md にも反映し、ここからリンクする
```

---

## `4koma` で均等な縦積みになる (2026-08-21)

- **指示(日本語)**: Anima でフルカラーの漫画ページ。コマは大きさ・配置を変えて物語を進める(脱ぐ → 押し倒す → 耳にかける → 口淫)
- **使ったプロンプト**: タグに `comic, 4koma, colored, border`。自然文は `A full-color manga page with four stacked panels` で上から順に4シーンを列挙
- **外れた出力**: 同じ大きさのコマが上から下へ単調に4段並ぶ(いわゆる4コマ漫画)
- **原因(推定)**: Danbooru の `4koma` は均等サイズの縦積み(または2×2)を指す。自然文の `four stacked panels` も同じ意味を補強した。不揃いの漫画ページ(ワイド+縦割り+スプラッシュ)とは別概念
- **直し方**: ポジから `4koma` を外す。ネガに `4koma, 2koma, 3koma` を入れる。枚数の縦積みは書かず、各 Panel の先頭で位置と大きさを文章指定する。書式は [manga-page.md](manga-page.md)。語彙は [vocab.md](vocab.md) の構図節

## 紫照明で画面が紫に染まる (2026-08-21)

- **指示(日本語)**: ローアングルの脱ぎかけ。色と湯気でエロくしたい。背景は紫グラデでもよい
- **使ったプロンプト**: ポジに `purple lighting, purple background, dim lighting, rim light, steam`
- **外れた出力**: 肌・服・背景まで全体が紫に寄る
- **原因(推定)**: `purple lighting` と `purple background` が重なり、主光まで紫になる
- **直し方**: 両方外す。背景は `dark background` の無彩色。光は `warm lighting, rim light`。ネガに `purple, purple lighting, purple background`。手順は [atmosphere.md](atmosphere.md)

## steaming body で服が透ける (2026-08-20)

- **指示(日本語)**: 汗で服が湿っているが、透けさせない
- **使ったプロンプト**: ポジに `sweat, steaming body, steam`。白シャツまたは白タートル
- **外れた出力**: 服が半透明になり、下着や体の線が見える
- **原因(推定)**: `steaming body` と白衣が濡れ透けに解釈される
- **直し方**: `steaming body` を外し `steam, haze` だけにする。自然文で `clothes stay opaque`。ネガに `see-through, see-through shirt, wet clothes`。[atmosphere.md](atmosphere.md)

## ローアングルでスカートが消える (2026-08-21)

- **指示(日本語)**: 下からのカウボーイショット。スカートは残す
- **使ったプロンプト**: `from below, cowboy shot, black skirt, pleated skirt, black pantyhose`
- **外れた出力**: スカートがなくなり、タイツだけの下半身になる
- **原因(推定)**: ローアングルが裾をフレーム外にし、タイツがボトムとして優先される
- **直し方**: `(black skirt:1.8), (pleated skirt:1.8)`。自然文で裾が見えると書く。ネガに `skirt removed, no skirt`。`from below` の重みは上げすぎない

## パンツラインが出る (2026-08-21)

- **指示(日本語)**: タイツは残すが、パンツのラインは不要
- **使ったプロンプト**: `black pantyhose` + ローアングル。ネガにライン指定なし
- **外れた出力**: スカート／タイツ越しにパンツラインが見える
- **原因(推定)**: 下からの光とタイツが輪郭を強調する
- **直し方**: ネガに `panty lines, cameltoe, panties`。自然文で `no panty lines`。[vocab.md](vocab.md) の照明節

## 服の中の手が生地の外に出る (2026-08-21)

- **指示(日本語)**: 背後の男性がタンクトップの中に手を入れて胸を揉む。手は生地の下
- **使ったプロンプト**: タグに `1boy, groping, breast grab, hands in clothes, oversized clothes`。自然文に `massaging her breasts` / `palms on her breasts` / `wrists show at the side openings`。カメラ `three-quarter view, cowboy shot`
- **外れた出力**: 男性の手がタンクトップの外側に乗り、服の上から揉む構図になる
- **原因(推定)**:
  1. `groping` / `breast grab` / 「胸を揉む」は学習上ほぼ服の上。`hands in clothes` も外手データが多い
  2. `1boy` + 背後 + 腕は「後ろから服の上で抱える」定番に寄る
  3. 胸の正面(`three-quarter` + `cowboy shot`)だと手が胸の手前レイヤーに合成される
  4. `oversized` とアームホール強調は、隙間から指が見えて外側に見える
  5. 手・胸・服を別物として書くとブレンドで手が一番前に来る
- **直し方**: 言い回しでは直らない。`groping` / `breast grab` / `hands in clothes` は使わない。この系統は 2026-08-22 に打ち切り。後続の「縛りすぎて崩壊」「裾から単発も失敗」を見よ

## 服の中の手を縛りすぎて構図が崩壊する (2026-08-21)

- **指示(日本語)**: 同上。手が外に出るのを止める
- **使ったプロンプト**: `from side`、自然文で no fingers / vanish into armholes / hand-shaped bulges。ネガに `groping, breast grab, hands on breasts`
- **外れた出力**: 人物も服も読めない、わけのわからない画像
- **原因(推定)**: 手を描くなと胸を揉んでいるを同時に要求し、男性を隠した。Animaは矛盾する空間指示で破綻しやすい
- **直し方**: `hug from behind` で背後の男性を明示。男性は短い茶髪など、相手と混ぜない外見。カメラは正面寄り。手の指示は1文。**裾から入れる単発も失敗し、この系統は打ち切り**(2026-08-22)。Anima単発では再現しない。言い回しを変えて再挑戦しない。必要な場合のみ、女性単独を出してから腕を inpaint する

## タンクトップ裾から手を入れる単発も失敗 (2026-08-22)

- **指示(日本語)**: 女の子座り、背後の男性がタンクトップの裾をたくし上げて中から乳首を触る
- **使ったプロンプト**: `hug from behind` + 自然文 `He pulls the hem of her tank top upward and slides both hands in from the bottom`
- **外れた出力**: 意図どおりにならない(服の上、破綻、または別構図)。ユーザーがこの系統を打ち切り
- **原因(推定)**: 「不透明な服の内側の手」と「乳首愛撫が見える」は同時に描きにくい。`hug from behind` は2人の配置には効くが、手を生地の下へは送らない
- **直し方**: 単発プロンプトでは扱わない。記録のみ。[vocab.md](vocab.md) の「服の中の手」

## 紫グラデがシーン全体を染める (2026-08-21)

- **指示(日本語)**: リオの下アングル。背景は紫のグラデーション
- **使ったプロンプト**: ポジに `simple background, gradient background, purple background`
- **外れた出力**: 背景だけでなく照明・肌まで紫に寄る
- **原因(推定)**: `purple background` がライティングとブレンドされる。Anima は異なる概念を混ぜやすい
- **直し方**: `purple background` を外し `dark background` + 自然文で `dark charcoal gradient, not purple`。ライティングは `warm lighting, rim light`。ネガに `purple background`。語彙は [vocab.md](vocab.md) の構図節。最終稿は [rio-jacket-from-below.md](../examples/_templates/rio-jacket-from-below.md)

## white shirt がTシャツになる (2026-08-21)

- **指示(日本語)**: 山田が白いシャツ(ボタン付き)を着て、マンション玄関の扉隙間から見える
- **使ったプロンプト**: ポジに `white shirt`。ネガに `t-shirt` なし
- **外れた出力**: 白シャツがTシャツになった
- **原因(推定)**: `white shirt` 単体はTシャツにもブレンドされやすい
- **直し方**: ポジに `collared shirt` を併記し、ネガに `t-shirt` を入れる。自然文は `button-up collared shirt` と書く。`open shirt` は全開になりやすいので使わない。語彙は [vocab.md](vocab.md) の衣装節
