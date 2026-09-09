# 例: 室内フローリングで押し倒されるリオ

**指示(日本語):** ラフの頭側床カメラのまま。ジャケット・身分証・太ももホルスターは削除。男性は白シャツ。床はフローリング。背景は室内の暖かい色グラデ。家具なし。男性も赤面。女性はすこしとろけ顔。男性を見る。

**組み立てメモ:**
- リオ既定から `black jacket, id card, thigh holster` を削除。残すのはタートル・スカート・タイツ・ヒール。ネガに外した3点。
- 先生は `white shirt, collared shirt`。ネガに `t-shirt`。白タートルと混ざるので自然文で誰が何を着るかだけ書く(容姿は書かない)。
- 床は `wooden floor`。背景は部屋の暖色グラデ。タグ `simple background, gradient background`、色名は自然文。人物光は `warm lighting`。ネガに `purple lighting, furniture, door`。
- `from below` は使わない(股下アオリ化)。カメラは自然文。
- とろけ顔は `half-closed eyes, blush` + 自然文で slightly melted。あへがおはネガ。驚きタグは外す。
- `blush` は二人。自然文で both。
- `explicit` / `newest` / `colored` / `anime coloring` は未指定。接頭辞は `masterpiece, best quality, score_7, safe` のみ。

**状態:** 2girls化・股下アオリ化は実生成で確認 2026-09-09。衣装・床・グラデ差し替え稿は未再生成。

**スキル入力(日本語):**

```
リオと先生で。先生はアニメ版センセイで、顔は出さない。前髪は長い。白いシャツ。リオはジャケット・身分証・太ももホルスターなし。床はフローリング。背景は室内の暖かい色のグラデ。家具なし。1枚絵。

【構図指示】
人数と配置: 1女1男だけ。女性は仰向け。頭が下手前、足はフローリングに着いたまま奥へ。脚は宙に上げない。男性は同じ向きで上に覆いかぶさる。立っていない。
ポーズ: 男性の両手は女性の頭の横の床。胸が女性の上。押し倒した直後。
表情・視線: 女性は半目で、すこしとろけている。視線は上の男性。カメラは見ない。男性も赤面。顔は出さない。
カメラ: 頭側の床すれすれ。体に沿って奥を見る。股の間から見上げない。
切り取り: 奥行き方向に全身。
背景・小道具: 手前=フローリング。中層=二人。奥=暖かい色の室内グラデ。扉・靴箱・植木・棚なし。
光: 人物は弱い暖色。背景色で肌を染めない。
色・空気感: 室内。暖かいグラデ。
動き: 倒した余勢。
不明瞭: なし
```

**推奨設定:** `896×1152`。`er_sde`、CFG 4〜5、30〜50ステップ。

**ポジティブ:**

```
masterpiece, best quality, score_7, safe, 1girl, 1boy, sensei (blue archive the animation), (faceless male:1.5), long bangs, white shirt, collared shirt, rio (blue archive), blue archive, very long hair, black hair, blunt bangs, hair behind ear, red eyes, ringed eyes, white pupils, hairclip, millennium science school logo, halo, black halo, large breasts, white turtleneck sweater, black skirt, pleated skirt, black pantyhose, black high heels, lying, on back, on floor, wooden floor, pinned down, leaning forward, height difference, blush, half-closed eyes, looking at another, warm lighting, simple background, gradient background

One man and one woman only. Ground-level camera at their heads, looking along the wooden flooring into the room. Rio lies on her back; her head is nearest the camera and her legs stay on the floor, stretching away, not in the air. She looks up at him, not at the camera, with a slightly melted, dazed expression. Sensei is male and faceless and is not standing; he lies over her in the same direction, both blushing, both hands planted on the floor beside her head as he pins her down. He wears a white button-up collared shirt. Only wooden flooring is under them. The background is a warm orange-to-amber indoor gradient with no furniture and no door.
```

**ネガティブ:**

```
worst quality, low quality, score_1, score_2, score_3, artist name, blurry, jpeg artifacts, chromatic aberration, from below, between legs, upskirt, legs up, legs in the air, upside-down, inverted, standing, spread legs, 2girls, multiple girls, yuri, straddling, girl on top, looking at viewer, closed eyes, ahegao, tongue out, sitting, black jacket, id card, thigh holster, t-shirt, door, open door, backlight, furniture, plant, potted plant, cabinet, shelf, table, chair, houseplant, purple lighting, purple background, white background, scenery, outdoors, comic, multiple panels, 4koma, monochrome, greyscale, photorealistic, 3d, extra limbs, bad hands, watermark, signature, text, logo
```
