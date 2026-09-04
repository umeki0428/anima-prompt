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
| リオ武装/臨戦 | `rio (armed) (blue archive), official alternate costume, official alternate hairstyle, ponytail, black bodysuit, skin tight, headgear, black gloves, thigh holster` | エイリアス `battle` / `bodysuit`。既定制服は削除。例は [rio-armed.md](../examples/_templates/rio-armed.md) | 2026-08-21 |
| リオ冬服 | `rio (winter) (blue archive), official alternate costume, black coat, coat, white turtleneck sweater, turtleneck, black gloves` | NPC立ち絵。投稿が少ない。例は [rio-winter.md](../examples/_templates/rio-winter.md) | 2026-08-21 |
| リオクリスマスドレス | `rio (christmas dress) (blue archive), official alternate costume, official alternate hairstyle, hair bun, black dress, dress, jewelry, necklace, bare shoulders` | エイリアス `rio (dress)`。例は [rio-christmas-dress.md](../examples/_templates/rio-christmas-dress.md) | 2026-08-21 |
| ボタン付き白シャツ(Tシャツではない) | collared shirt, white shirt | `white shirt` 単体はTシャツ化しやすい。ネガに `t-shirt`。自然文は button-up collared shirt | 【未検証】 |
| 途中のボタンが外れている | partially unbuttoned | `unbuttoned` や `open shirt` は全開になりやすい。中央だけ外れていることは自然文で書く | 【未検証】 |
| 黒いブラが少し見える | black bra | チラ見えは自然文で slightly visible。`open shirt` は付けない | 【未検証】 |

## ポーズ・視線

| 日本語 | 使うタグ | メモ | 確認日 |
|---|---|---|---|
| とろけ顔 | half-closed eyes, open mouth, blush | 自然文で melted / dazed。あへがおは指示があるときだけ。詳細は [atmosphere.md](atmosphere.md) | 【未検証】 |
| 息が荒い | heavy breathing | | 【未検証】 |
| 汗 | sweat | 肌の汗。服を濡らす指定は透けに繋がる | 【未検証】 |
| 下を見る(ローアングル) | looking down | `looking at viewer` と併用しがち | 【未検証】 |
| 女の子座り | wariza, sitting, on floor | `seiza` や `hugging own knees` に寄る。ネガに `seiza` | 【未検証】 |
| 耳にかける | tucking hair, hair behind ear | ポーズを変えても指示がある限り残す。四つん這いと両立しにくい | 【未検証】 |
| 四つん這い | all fours | 膝立ちに戻るなら `(all fours:2)`。ネガに `sitting, standing` | 【未検証】 |
| 前かがみ | leaning forward | | 【未検証】 |
| 前かがみで胸が垂れる | hanging breasts | `leaning forward` / `all fours` とセット。白タートルでは透け注意 | 【未検証】 |
| 後ろから抱える | hug from behind | 2人の位置関係の固定用。服の中の手までは保証しない | 2026-08-21 |
| 舌を出す(あへがおなし) | tongue out, open mouth | ネガに `ahegao, rolling eyes` | 【未検証】 |
| 舌キス | kissing, tongue out | 顔が必要。`faceless male` は外してネガへ。よだれは下の行 | 2026-09-04 |
| よだれ | drooling, saliva, saliva trail | 舌キスとセット。量は自然文 | 2026-09-04 |
| 破れたタイツ越しの指 | torn pantyhose, white panties, wet panties | 自然文で index fingertip over the wet panties。服の中の手とは別(こちらは可)。ネガに `dildo, sex toy, intact pantyhose` | 2026-09-04 |
| 左右の手が別動作 | (タグにしない) | 自然文で left / right。ネガに `two hands on breasts` | 2026-09-04 |
| 疑似フェラ | penis / fellatio は使わない | `open mouth, tongue out` + `pov` で画面下に口。ネガに `penis, fellatio` | 【未検証】 |
| 軽い赤面 | blush | 自然文で faint blush。照れなら `embarrassed` も足す。【未検証】 | |
| 半目 | half-closed eyes | 自然文は half-lidded eyes。最終稿で使用 | 2026-08-21 |
| 汗・湯気 | `sweat, steam, haze` | 顔の汗と空気中の湯気。最終稿で使用 | 2026-08-21 |
| ぎこちない笑顔 | awkward smile | `forced smile` だと強要感が出る。はぁはぁと併用するなら `open mouth, panting` も付ける | 【未検証】 |
| はぁはぁしている | panting, open mouth | `panting` だけだと口が閉じることがある | 【未検証】 |
| 赤面 | blush | | 【未検証】 |
| すこし汗 | sweat | 強い発汗にしない。量は自然文で lightly | 【未検証】 |

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
| 不揃いの漫画ページ | 各 Panel 先頭で位置を文章指定(`top full-width panel` 等) | `4koma` は均等な縦積みになる(2026-08-21)。書式は [manga-page.md](manga-page.md)。タグ羅列より Panel 文章 | 2026-08-22 |
| 均等4コマ | `4koma` | 同じ大きさのコマが上から下(または2×2)。動的なページには使わない | 2026-08-21 |
| フルカラー漫画 | `colored` | `shoujo manga style` / `shounen manga style` / `monochrome` / `greyscale` はモノクロ化するのでフルカラーではネガへ | 【未検証】 |
| 扉の隙間から見るPOV | pov, doorway, open door | 縦の扉とドア枠で切り取ることは自然文。`peeking` は目だけになりやすいので使わない | 【未検証】 |
| 左下でインターホンを押す手 | (タグにしない) | `hands` を付けるとキャラ側に付く。自然文で bottom-left foreground, the viewer's hand presses a wall-mounted intercom | 【未検証】 |


## 照明・雰囲気

詳細な手順・貼り付けセットは [atmosphere.md](atmosphere.md)。

| 日本語 | 使うタグ | メモ | 確認日 |
|---|---|---|---|
| 暗い部屋 | dim lighting | エロ雰囲気の土台 | 【未検証】 |
| リムライト | rim light | 輪郭。色指定は自然文 | 【未検証】 |
| 逆光 | backlight | `rim light` とセットしやすい | 【未検証】 |
| 紫の光 | purple lighting | 画面全体が紫に染まりやすい。強すぎるときは外して `warm lighting` + ネガ `purple` | 2026-08-21 |
| ピンク／マゼンタの光 | pink lighting, magenta lighting | ホテル寄り | 【未検証】 |
| 暖色の光 | warm lighting | 人物側。色付き背景と分けるときにも使う | 2026-08-21 |
| ボリューム光 | volumetric lighting | 湯気・霧とセット | 【未検証】 |
| 部屋の湯気 | steam, haze | `steaming body` より透けにくい | 2026-08-20 |
| 肌から湯気 | steaming body | 白服が透けやすい。透け禁止なら使わない | 2026-08-20 |
| 暗い無彩色背景 | dark background | 無彩色の場面用。色付きグラデが欲しい場面では下の「色付きグラデ」 | 2026-08-21 |
| パンツライン抑制 | (ネガ) panty lines, cameltoe, panties | ローアングル＋タイツで出やすい | 2026-08-21 |
| 服の中の手 | **Anima単発では扱わない**(2026-08-22打ち切り) | `groping` / `breast grab` / `hands in clothes` は服の上。見えない手＋膨らみは構図崩壊。裾から入れる単発も失敗。inpaintのみ | 2026-08-22 |
| 2人の外見が混ざる | 男性は短い茶髪など、相手と違う外見を**タグで先に書く** | 長髪ハロ持ちと `1boy` を並べると顔が混ざる。自然文で容姿を再掲しない | 2026-08-21 |
| 色付きグラデ背景 | `simple background, gradient background, dark background` | **色は場面で変える。** 色名は自然文。`purple background` タグは肌まで染めやすいので、弱いときだけ足す。人物光は背景色と分ける(紫グラデなら光は `warm lighting`、ネガ `purple lighting`) | 2026-09-04 |
| 暗いチャコールグラデ | `simple background, gradient background, dark background` | 無彩色の場面。自然文で dark charcoal gradient。ネガに `purple background` は、その場面で紫が不要なときだけ | 2026-08-21 |
| ベッド面だけ(部屋なし) | on bed | 自然文で rumpled bed surface。ネガに `scenery, indoor, furniture, bedroom, headboard`。グリーンバックは切り抜き用で雰囲気とは別 | 2026-09-04 |
| 暖色リム | `dim lighting, warm lighting, rim light, volumetric lighting` | 人物側の光。色付き背景と重ねるときは照明色タグを背景色と同じにしない | 2026-08-21 |
