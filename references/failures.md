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
- **直し方**: ポジから `4koma` を外す。ネガに `4koma, 2koma, 3koma` を入れる。自然文では枚数の縦積みを書かず、配置とサイズだけ書く。書式は [manga-page.md](manga-page.md)。語彙は [vocab.md](vocab.md) の構図節

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
