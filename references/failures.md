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

## 紫グラデがシーン全体を染める (2026-08-21)

- **指示(日本語)**: リオの下アングル。背景は紫のグラデーション
- **使ったプロンプト**: ポジに `simple background, gradient background, purple background`
- **外れた出力**: 背景だけでなく照明・肌まで紫に寄る
- **原因(推定)**: `purple background` がライティングとブレンドされる。Anima は異なる概念を混ぜやすい
- **直し方**: `purple background` を外し `dark background` + 自然文で `dark charcoal gradient, not purple`。ライティングは `warm lighting, rim light`。ネガに `purple background`。語彙は [vocab.md](vocab.md) の構図節。最終稿は [rio-jacket-from-below.md](../examples/_templates/rio-jacket-from-below.md)
