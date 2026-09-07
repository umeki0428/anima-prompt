# 例: ゆい×ユウジの口淫ページ(参考ページの再現・エロ)

**指示(日本語):** 添付した漫画ページのコマ割りとシーンを、ゆい×ユウジで再現する。上ワイド → 下は左列に小コマ2段 + 右に縦長大ゴマ。ゆいは仰向けでユウジに口淫されて乱れている。フルカラー。

**参考ページの読み取り:** [captions/manga-page-cunnilingus-reference.md](../../captions/manga-page-cunnilingus-reference.md)

**組み立てメモ:**
- 書式は [manga-page.md](../../references/manga-page.md) の 画風 → Character → Panel 文章。`4koma` は使わない。
- 参考ページはフルカラーなので、冒頭の画風ブロックを白黒からカラーに差し替えた(`full color manga page, colored, anime coloring`、`screentones` は外す)。白黒で試すときは標準ブロックに戻す。
- ゆい: `characters/yui.md` の固定タグ(茶髪ポニテ・茶目・medium-large breasts)は維持。衣装は参考ページに合わせて **白Tシャツ + 黒キャミの肩紐 + 下は裸(bottomless)** に全部置き換え。既定のデニムショートは混ぜない(ネガに `denim shorts`)。
- ユウジ: `characters/yuji.md` の既定(faceless male・前髪で目を隠す・黒Tシャツ)をそのまま。参考は白Tだが、ゆいの白Tと混ざるのを避けるため黒のまま。Panel 3 の顔アップも「前髪で目が隠れ、鼻と口と顎だけ」と書いて faceless を守る。
- 2人の外見は混ぜない: ゆい=茶髪ポニテ、ユウジ=短い黒髪、で先に分ける。
- 吹き出しは位置だけ確保し、台詞は後入れ(文字は1〜2単語までのルール)。
- Panel 2/3 は「左列に上下2段」、Panel 4 は「下右の縦長大ゴマ」と位置句を厚めに書く。左列が1つに潰れたら下の「検証用の差し替え」を試す。

**ポジティブ:**

```
manga style,
full color manga page,
colored,
anime coloring,
professional Japanese manga,
clean detailed line art,
soft cel shading,
dynamic panel layout,
explicit,

Character one:
(Yui), a young Japanese woman in her early twenties,
brown hair tied in a ponytail,
brown eyes,
medium-large breasts,
wearing a loose white t-shirt,
a black camisole strap visible at her collar,
bottomless, her lower body completely bare,
heavy blush, sweat and tears on her face,

Character two:
(Yuji), a young Japanese man in his twenties,
short black hair with bangs,
his eyes hidden behind his bangs, faceless,
wearing a black t-shirt,

Panel 1:
top full-width panel, very large, taking up almost the upper half of the page,
Yui lies on her back on a white rumpled bed with her head on the right side and her raised spread legs on the left,
Yuji is between her thighs with his face pressed into her crotch, licking her pussy,
his hand grips the inside of her thigh,
her white t-shirt has ridden up to show her belly,
she squeezes her eyes shut with tears, a heavy blush and an open mouth,
high-angle shot from above the bed,
white bedsheets fill the background,
a speech bubble in the upper right corner,

Panel 2:
middle left small panel, the upper panel of the left column below the top panel,
close shot from above of Yui's lower body,
her thighs lifted and spread wide, Yuji's head buried between them as he licks her pussy,
pussy juice and saliva glisten on her skin,
her blushing face is visible in the lower corner and her hand clutches the bedsheet,

Panel 3:
bottom left small panel, the lower panel of the left column,
close-up of Yuji's face,
his bangs cover his eyes and only his nose, mouth and chin are visible,
he wipes his wet mouth with the back of his hand,
fluid glistens on his chin,
dark shadowed background,

Panel 4:
large vertical panel on the lower right side, spanning from below the top panel to the bottom of the page,
Yui lies on her back seen from above,
her face in the upper part of the panel with half-closed teary brown eyes, a heavy blush, an open mouth and heavy breathing, warm breath visible in the air,
her white t-shirt covers her breasts while her legs are spread bare,
at the bottom of the panel Yuji's head is between her thighs, licking her pussy,
pussy juice glistens,
a speech bubble in the upper left corner.
```

**ネガティブ:**

```
worst quality, low quality, score_1, score_2, score_3, artist name, blurry, jpeg artifacts, chromatic aberration, 4koma, 3koma, 2koma, equal panels, stacked panels, grid layout, monochrome, greyscale, screentones, photorealistic, 3d, extra limbs, bad hands, extra fingers, multiple views, watermark, logo, signature, denim shorts, panties
```

文字化けした文字が出るときはネガに `text` を足す(吹き出しごと消えることがある)。

**設定メモ:** 縦長ページ `1024×1536` または `768×1152`。サンプラー `er_sde`、CFG 4〜5、30〜50ステップ。seed を変えて複数回。

## 検証用の差し替え

**A. 白黒版(標準ブロックに戻す):** 冒頭を [manga-page.md](../../references/manga-page.md) の `manga style, black and white manga page, professional Japanese manga, clean detailed line art, high quality screentones, dynamic panel layout,` に戻し、`explicit` は残す。ネガから `monochrome, greyscale, screentones` を外す。Character の `anime coloring` 相当は無し。

**B. 左列の小コマ2つが1つに潰れるとき:** Panel 2/3 の位置句を次に差し替える。

```
Panel 2:
small panel in the middle left,
...

Panel 3:
small panel in the bottom left, stacked under Panel 2,
...

Panel 4:
large vertical panel on the right side, next to the two small left panels,
...
```

それでも潰れるなら Panel 3(ユウジの顔アップ)を削って3コマにし、左列を1枚の縦コマにする。

**C. ゆいを既定衣装(タンクトップ)で:** Character one の `wearing a loose white t-shirt, a black camisole strap visible at her collar` を `wearing a loose oversized tank top with wide armholes, a black camisole strap visible` に置き換える。`bottomless` とネガの `denim shorts` はそのまま。

**D. 位置が安定したら次に試す差分:** 吹き出し内の文字(`"NO..."` のように1語を引用符で)、Panel 3 の背景を暗くしたまま Panel 1/4 の光を `dim lighting, warm lighting` にする([atmosphere.md](../../references/atmosphere.md))。

**状態:** 【未検証】(机上の変換例。実生成での確認後、結果と設定を追記する)
