# 例: リオ・引き戸を開ける(上大ゴマ+下左右)

**指示(日本語):** 上3分の2の大ゴマ、下は左右同じ大きさの2コマ。男性はブルーアーカイブの先生。シャツに白い飛沫はかけない。フルカラー。セリフ・♡・擬音は入れない。キャラは `blue archive, rio \(blue archive\)`。服装は制服。

**組み立てメモ:** 漫画ページは [manga-page.md](../../references/manga-page.md)。画風は `manga style, dynamic panel layout` にフルカラーの `anime coloring, colored` を足す。`2koma` は使わない。Character one はリオのキャラタグと制服。Character two は `sensei \(blue archive\)`。ゲームの先生は顔なしになりやすいので `faceless male` は付けない(下左が顔アップのため)。飛沫は書かない。

**ポジティブ:**

```
manga style,
dynamic panel layout,
anime coloring,
colored,

Character one:
blue archive,
rio \(blue archive\),
white turtleneck sweater, black jacket, id card, black skirt, pleated skirt, black pantyhose, thigh holster, black high heels,

Character two:
blue archive,
sensei \(blue archive\),
grey suit, white shirt, black necktie, id card,

Panel 1:
large full-width panel occupying the top two-thirds of the page,
an indoor hallway with a sliding door and a plain wall,
wide shot,
on the left Sensei is shown in profile facing right, sweating, body tensed as if caught by surprise,
on the right Rio has just pulled open the sliding door and stands in the doorway,
Rio wears her school uniform,
her uniform is clean with no stains,
Rio looks toward Sensei with a startled expression,
Sensei looks toward Rio with wide eyes,

Panel 2:
equal-size square panel in the bottom left,
close-up profile of Sensei's face,
his eyes are wide and his expression is blank and stunned,
sweat on his skin,
solid black background with white radial shock lines behind his head,

Panel 3:
equal-size square panel in the bottom right,
close-up of Rio's face looking slightly to the left,
her eyes are wide and her mouth is slightly open in surprise,
solid black background with white radial shock lines behind her head.
```

**ネガティブ:**

```
monochrome, greyscale, black and white, faceless male, text, speech bubble, heart
```

**推奨設定:** 1024×1536 または 768×1152、`er_sde`、CFG 4〜5、30〜50ステップ。

**状態:** 【未検証】(机上の変換例。実生成での確認後、結果と設定を追記する)

上コマだけを1枚絵にする版は [rio-sensei-door-single.md](rio-sensei-door-single.md)。
