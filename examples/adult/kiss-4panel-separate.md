# 例: キス4コマを1コマ1枚で再現(リオ×先生)

**指示(日本語):** 添付した縦4段のキス漫画を、上から1コマずつ別画像として生成する。フルカラー。漫画ページとしては出さない。キャラはリオと先生(アニメ版センセイ、faceless)。

**参考の読み取り:** [../../captions/kiss-4panel-reference.md](../../captions/kiss-4panel-reference.md)

**組み立てメモ:**
- 1コマ=1枚の簡潔なハイブリッド。`4koma` も Panel 文章も使わない。ネガに `comic, multiple panels, 4koma`。
- リオの容姿はユーザー指定の固定タグから `hairclip` を外す(指示)。ネガに `hairclip, hair ornament, millennium science school logo`。自然文に髪・瞳を再掲しない。`characters/rio.md` の既定自然文は貼らない。
- 先生はユーザー指定どおり `sensei (blue archive the animation), faceless male, long bangs`。キスでも `faceless male` は外さない(指定)。ネガへは移さない。
- 衣装指示なし。1〜2枚目(上半身)だけ既定のタートル＋ジャケット。スカート／タイツ／ヒールはフレーム外なので入れない。3〜4枚目は顔・口元なので衣装タグなし。
- 2人の外見差はタグで先に分ける(リオ=very long black hair、先生=faceless + long bangs)。
- 1枚目の背景は黒〜チャコールの夜グラデ(`simple background, gradient background, dark background` + 自然文)。色は自然文、人物光は `dim lighting, warm lighting`、ネガに `white background, purple lighting`。2〜4枚目は未指示のため白背景のまま。
- 1枚目は身長差で男性が上から(`height difference` + `from below` / `low angle`)、右手は手前で大きく、いきなりキスの勢い、目を閉じて受け入れる驚き、よだれ。
- よだれ・汗・湯気はタグ。とろけ顔は `half-closed eyes, open mouth, blush`。あへがおは指示がないのでネガへ。
- 吹き出しの「…」は出さない(ネガに `text`)。
- 1〜3は横顔キスなのでネガに `looking at viewer`。4だけ正面。
- `explicit` / `newest` / `colored` / `anime coloring` は未指定。接頭辞は `masterpiece, best quality, score_7, safe` のみ。

**状態:** 【未検証】(机上の変換。実生成後に結果を追記する)

---

## 1枚目(最上段): 横顔のキス開始

【構図指示】
人数と配置: 2人。横顔のクローズアップ。女性が画面左、男性が画面右。身長差があり男性の頭が一段高い。胸から上がフレーム。
ポーズ: 男性は右上から覆い被さるように前傾し、まだ前に突っ込んでいる途中でキス。右手はカメラに一番近く、顔より手前で大きく、女性の顎〜頬を包む。女性は顔を上に向け、上体は引かず受けている。
表情・視線: 女性は目を閉じている。眉がわずかに上がり、驚きが残るが口は合わせて受け入れている。頬に赤み。男性の顔は出さない。
カメラ: わずかにアオリ(女性の目線より少し下)。真横。クローズアップ。手前の手は顔より大きく、軽いパース。
切り取り: 胸から下は画面外。手前の手の手首から先はフレーム内。
背景・小道具: 手前=男性の右手。中層=二人の顔と肩。奥=黒〜チャコールの夜グラデ。部屋も家具もなし。
光: 暗い。人物だけ柔らかい暖色。背景は無彩色の黒。
色・空気感: 夜。赤面。口元の濡れ。
動き: いきなり距離を詰めた直後。上体がまだ前に進んでいる。
不明瞭: コマ枠

**推奨設定:** `1152×896`(横長)。`er_sde`、CFG 4〜5、30〜50ステップ。アオリが強すぎて顔だけになったら `from below` の重みは上げない。

**スキル入力(日本語):** 後段の SKILL.md にこのブロックを貼る。容姿の固定タグはスキル側が足す。

```
リオと先生で。先生はアニメ版センセイで、顔は出さない。前髪は長い。リオのヘアクリップは描かない。1枚絵。漫画のコマ割りにしない。

【構図指示】
人数と配置: 2人。横顔のクローズアップ。女性が画面左、男性が画面右。身長差があり、男性の頭が一段高い。胸から上がフレーム。
ポーズ: 男性は右上から覆い被さるように前傾し、まだ前へ突っ込んでいる途中でキス。右手はカメラに一番近く、顔より手前で大きく、女性の顎から頬を包む。女性は顔を上に向け、上体は引かず受けている。
表情・視線: 女性は目を閉じている。眉がわずかに上がり、驚きが残るが口は合わせて受け入れている。頬に赤み。口元に細いよだれの糸。男性の顔は出さない。
カメラ: わずかにアオリ(女性の目線より少し下)。真横。クローズアップ。手前の手は顔より大きく、軽いパース。
切り取り: 胸から下は画面外。手前の手の手首から先はフレーム内。
背景・小道具: 手前=男性の右手。中層=二人の顔と肩。奥=黒からチャコールの夜グラデ。部屋も家具もなし。
光: 暗い。人物だけ柔らかい暖色。背景は無彩色の黒。紫の照明は使わない。
色・空気感: 夜。赤面。口元の濡れ。生生しい。
動き: いきなり距離を詰めた直後。上体がまだ前に進んでいる。
不明瞭: なし
```

**ポジティブ:**

```
masterpiece, best quality, score_7, safe, 1girl, rio (blue archive), blue archive, very long hair, black hair, blunt bangs, hair behind ear, red eyes, ringed eyes, white pupils, white turtleneck sweater, black jacket, 1boy, sensei (blue archive the animation), faceless male, long bangs, height difference, kissing, saliva, saliva trail, drooling, closed eyes, blush, leaning forward, profile, close-up, upper body, from below, hand on another's face, facing another, simple background, gradient background, dark background, night, dim lighting, warm lighting

Low angle. Sensei is taller on the right and still lunging down from above into a sudden kiss. Rio on the left tilts her face up; a trace of surprise remains in her brows as she yields. His right hand is large in the foreground, closer to the camera than their faces, cupping her jaw. A thin saliva thread at their lips. Tight crop from the chest up. The background is a black-to-charcoal night gradient with nothing else in it.
```

**ネガティブ:**

```
worst quality, low quality, score_1, score_2, score_3, artist name, blurry, jpeg artifacts, chromatic aberration, looking at viewer, hairclip, hair ornament, millennium science school logo, white background, purple lighting, purple background, comic, multiple panels, 4koma, monochrome, greyscale, ahegao, scenery, indoor, furniture, black skirt, black pantyhose, black high heels, photorealistic, 3d, extra limbs, bad hands, watermark, signature, text, logo
```

---

## 2枚目: 濃いキス

【構図指示】
人数と配置: 2人。1枚目より顔に寄った横顔。女性左、男性右。顔が画面の大半。
ポーズ: 男性は右手で女性の頬を強く包み、顔を引き寄せる。女性は頭がわずかに後ろへ倒れる。キスは口が開いたまま密着。
表情・視線: 女性は半目、焦点が甘い。頬の赤みが1枚目より強い。額と頬に汗。男性の顔は出さない。
カメラ: ほぼ水平。真横。顔のクローズアップ。
切り取り: 肩から下は画面外。耳より後ろは切れてよい。
背景・小道具: 奥=無地のオフホワイト。
光: 柔らかい暖色。
色・空気感: 暖色。赤と汗の光沢。熱い。
動き: なし。密着の瞬間。
不明瞭: コマ枠 / 集中線の有無

**推奨設定:** `1152×896`。`er_sde`、CFG 4〜5、30〜50ステップ。

**ポジティブ:**

```
masterpiece, best quality, score_7, safe, 1girl, rio (blue archive), blue archive, very long hair, black hair, blunt bangs, hair behind ear, red eyes, ringed eyes, white pupils, white turtleneck sweater, black jacket, 1boy, sensei (blue archive the animation), faceless male, long bangs, kissing, saliva, saliva trail, sweat, blush, half-closed eyes, profile, close-up, hand on another's face, facing another, simple background, white background, warm lighting, steam, haze

Tighter profile close-up on their faces. Sensei on the right presses his hand to Rio's cheek and pulls her in. The kiss is wet, with a thin saliva thread at their lips. Soft warm light and a faint haze of steam.
```

**ネガティブ:**

```
worst quality, low quality, score_1, score_2, score_3, artist name, blurry, jpeg artifacts, chromatic aberration, looking at viewer, closed eyes, hairclip, hair ornament, millennium science school logo, comic, multiple panels, 4koma, monochrome, greyscale, ahegao, scenery, indoor, furniture, black skirt, black pantyhose, black high heels, photorealistic, 3d, extra limbs, bad hands, watermark, signature, text, logo
```

---

## 3枚目: 口元の極寄り

【構図指示】
人数と配置: 2人の口と顎だけ。横長の極寄り。左右に割れた横顔の下半分。唇が画面中央。
ポーズ: 唇がわずかに離れた直後。口はまだ開いている。
表情・視線: 目はフレーム外。口元によだれの白い糸。肌に汗。
カメラ: ほぼ水平。口元へのエクストリームクローズアップ。
切り取り: 鼻より上、喉より下は画面外。目・額・後頭部は出さない。
背景・小道具: 奥=無地のオフホワイト。口のまわりに小さな白い吐息。
光: 柔らかい暖色。口元の濡れにハイライト。
色・空気感: 暖色。濡れと熱。
動き: 唇が離れて糸が伸びている瞬間。
不明瞭: コマ枠 / 白い液の量(唾液)

**推奨設定:** `1344×768` または `1280×768`(横長)。`er_sde`、CFG 4〜5、30〜50ステップ。

**ポジティブ:**

```
masterpiece, best quality, score_7, safe, 1girl, rio (blue archive), blue archive, very long hair, black hair, 1boy, sensei (blue archive the animation), faceless male, long bangs, kissing, saliva, saliva trail, drooling, sweat, blush, extreme close-up, profile, steam, haze, simple background, white background, warm lighting

Extreme close-up on their mouths only, cropped horizontally. Their lips have just parted, a thick saliva string stretching between them. Warm breath and steam around the mouths. Eyes and forehead stay out of frame.
```

**ネガティブ:**

```
worst quality, low quality, score_1, score_2, score_3, artist name, blurry, jpeg artifacts, chromatic aberration, looking at viewer, full body, upper body, hairclip, hair ornament, millennium science school logo, comic, multiple panels, 4koma, monochrome, greyscale, ahegao, scenery, indoor, furniture, photorealistic, 3d, extra limbs, bad hands, watermark, signature, text, logo
```

---

## 4枚目(最下段): キスのあと正面

【構図指示】
人数と配置: 女性の顔が画面中央をほぼ埋める正面アップ。男性の顔は出ない。男性の両手の指だけが、顔の左右から頬を挟む。
ポーズ: 男性の親指が両頬の前、残りの指は顎の下〜横。女性は動かず、顔を正面に向けたまま。
表情・視線: 半目、焦点が合わない。口が小さく開く。下唇と顎によだれ。頬は強い赤面。額に汗。視線は正面やや下。
カメラ: ほぼ水平。顔のクローズアップ。正面。パース誇張なし。
切り取り: 首から下は画面外。両手の手首から先だけ。
背景・小道具: 奥=無地のオフホワイト。頭のまわりに湯気。
光: 柔らかい暖色。正面やや上。
色・空気感: 暖色。赤面が強い。とろけたあとの虚脱。
動き: なし。
不明瞭: 吹き出し「…」 / くらくら記号 / コマ枠

**推奨設定:** `896×1152`(縦長)。`er_sde`、CFG 4〜5、30〜50ステップ。

**ポジティブ:**

```
masterpiece, best quality, score_7, safe, 1girl, rio (blue archive), blue archive, very long hair, black hair, blunt bangs, hair behind ear, red eyes, ringed eyes, white pupils, 1boy, sensei (blue archive the animation), faceless male, long bangs, looking at viewer, half-closed eyes, open mouth, blush, sweat, saliva, drooling, steam, haze, close-up, hands on another's face, simple background, white background, warm lighting

Frontal close-up of Rio's face only. Sensei's hands cup both her cheeks from the sides, thumbs on her cheeks. Her expression is melted and dazed, unfocused half-lidded eyes, a heavy blush, sweat, and a saliva drop on her lower lip. A faint haze of steam around her head. No speech bubble.
```

**ネガティブ:**

```
worst quality, low quality, score_1, score_2, score_3, artist name, blurry, jpeg artifacts, chromatic aberration, closed eyes, ahegao, tongue out, hairclip, hair ornament, millennium science school logo, comic, multiple panels, 4koma, monochrome, greyscale, scenery, indoor, furniture, photorealistic, 3d, extra limbs, bad hands, extra fingers, watermark, signature, text, logo
```
