# 例: キス4コマを1コマ1枚で再現

**指示(日本語):** 添付した縦4段のキス漫画を、上から1コマずつ別画像として生成する。フルカラー。漫画ページとしては出さない。

**参考の読み取り:** [../../captions/kiss-4panel-reference.md](../../captions/kiss-4panel-reference.md)

**組み立てメモ:**
- 1コマ=1枚の簡潔なハイブリッド。`4koma` も Panel 文章も使わない。ネガに `comic, multiple panels, 4koma`。
- キャラ名指定なし。容姿はタグ行だけ(紫の長髪 vs 茶の短髪で混ぜない)。自然文は左右・カメラ・切り取り・空気だけ。
- 背景は参考どおり無地のオフホワイト。暗い部屋や紫照明は足さない。
- よだれ・汗・湯気はタグ。とろけ顔は `half-closed eyes, open mouth, blush`。あへがおは指示がないのでネガへ。
- 吹き出しの「…」は出さない(ネガに `text`)。
- 1〜3は横顔キスなのでネガに `looking at viewer`。4だけ正面。
- 舌キス用に顔は出す。`faceless male` はネガへ。

**状態:** 【未検証】(机上の変換。実生成後に結果を追記する)

---

## 1枚目(最上段): 横顔のキス開始

【構図指示】
人数と配置: 2人。横顔のクローズアップ。女性が画面左半分、男性が画面右半分。顔が中央で接する。胸から上がフレーム。男性の頭の方がやや大きい。
ポーズ: 男性は右から上体を前傾し、顔を下げて女性に覆い被さるようにキス。右手で女性の顎から左頬を包む。女性は顔を上に向け、左手を顔の近くまで上げている。
表情・視線: 女性は目を閉じ、頬に赤み。男性も目を閉じてキス。視線は互いに相手の顔。
カメラ: ほぼ水平。真横からの横顔。クローズアップ。パース誇張なし。
切り取り: 胸から下は画面外。頭頂はフレーム内。
背景・小道具: 手前=なし。中層=二人の顔と肩。奥=無地のオフホワイト。ボケなし。
光: 柔らかい均一な暖色。影は弱い。
色・空気感: 暖色。赤面のピンク。親密。
動き: 男性が覆い被さるキスの瞬間。
不明瞭: コマ枠 / 白い腕防具の細部

**推奨設定:** `1152×896`(横長)。`er_sde`、CFG 4〜5、30〜50ステップ。

**ポジティブ:**

```
masterpiece, best quality, explicit, newest, colored, anime coloring, 1girl, long hair, purple hair, purple eyes, blunt bangs, gauntlets, 1boy, short hair, brown hair, messy hair, brown shirt, kissing, closed eyes, blush, profile, close-up, upper body, hand on another's face, facing another, simple background, white background, warm lighting

Profile close-up at eye level. The man on the right leans down over the woman on the left. His right hand cups her jaw. Tight crop from the chest up.
```

**ネガティブ:**

```
worst quality, low quality, score_1, score_2, score_3, artist name, blurry, jpeg artifacts, chromatic aberration, looking at viewer, comic, multiple panels, 4koma, monochrome, greyscale, saliva trail, ahegao, faceless male, scenery, indoor, furniture, photorealistic, 3d, extra limbs, bad hands, watermark, signature, text, logo
```

---

## 2枚目: 濃いキス

【構図指示】
人数と配置: 2人。1枚目より顔に寄った横顔。女性左、男性右。顔が画面の大半。
ポーズ: 男性は右手で女性の頬を強く包み、顔を引き寄せる。女性は頭がわずかに後ろへ倒れる。キスは口が開いたまま密着。
表情・視線: 女性は半目、焦点が甘い。頬の赤みが1枚目より強い。額と頬に汗。男性は目を細めてキス。
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
masterpiece, best quality, explicit, newest, colored, anime coloring, 1girl, long hair, purple hair, purple eyes, blunt bangs, gauntlets, 1boy, short hair, brown hair, messy hair, brown shirt, kissing, saliva, saliva trail, sweat, blush, half-closed eyes, profile, close-up, hand on another's face, facing another, simple background, white background, warm lighting, steam, haze

Tighter profile close-up on their faces. The man on the right presses his hand to her cheek and pulls her in. The kiss is wet, with a thin saliva thread at their lips. Soft warm light and a faint haze of steam.
```

**ネガティブ:**

```
worst quality, low quality, score_1, score_2, score_3, artist name, blurry, jpeg artifacts, chromatic aberration, looking at viewer, closed eyes, comic, multiple panels, 4koma, monochrome, greyscale, ahegao, faceless male, scenery, indoor, furniture, photorealistic, 3d, extra limbs, bad hands, watermark, signature, text, logo
```

---

## 3枚目: 口元の極寄り

【構図指示】
人数と配置: 2人の口と顎だけ。横長の極寄り。上に女性の口、下に男性の口、または左右に割れた横顔の下半分。唇が画面中央。
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
masterpiece, best quality, explicit, newest, colored, anime coloring, 1girl, long hair, purple hair, 1boy, short hair, brown hair, messy hair, kissing, saliva, saliva trail, drooling, sweat, blush, extreme close-up, profile, steam, haze, simple background, white background, warm lighting

Extreme close-up on their mouths only, cropped horizontally. Their lips have just parted, a thick saliva string stretching between them. Warm breath and steam around the mouths. Eyes and forehead stay out of frame.
```

**ネガティブ:**

```
worst quality, low quality, score_1, score_2, score_3, artist name, blurry, jpeg artifacts, chromatic aberration, looking at viewer, full body, upper body, comic, multiple panels, 4koma, monochrome, greyscale, ahegao, faceless male, scenery, indoor, furniture, photorealistic, 3d, extra limbs, bad hands, watermark, signature, text, logo
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
masterpiece, best quality, explicit, newest, colored, anime coloring, 1girl, long hair, purple hair, purple eyes, blunt bangs, 1boy, short hair, brown hair, looking at viewer, half-closed eyes, open mouth, blush, sweat, saliva, drooling, steam, haze, close-up, hands on another's face, simple background, white background, warm lighting

Frontal close-up of her face only. His hands cup both her cheeks from the sides, thumbs on her cheeks. Her expression is melted and dazed, unfocused half-lidded eyes, a heavy blush, sweat, and a saliva drop on her lower lip. A faint haze of steam around her head. No speech bubble.
```

**ネガティブ:**

```
worst quality, low quality, score_1, score_2, score_3, artist name, blurry, jpeg artifacts, chromatic aberration, closed eyes, ahegao, tongue out, comic, multiple panels, 4koma, monochrome, greyscale, faceless male, scenery, indoor, furniture, photorealistic, 3d, extra limbs, bad hands, extra fingers, watermark, signature, text, logo
```
