# 例: 室内フローリングで押し倒されるリオ

**指示(日本語):** 頭側床カメラのまま。靴削除。女性は股を開き、その間に男性。頭側の床が長いので短く切る。背景の暖色グラデをすこし暗く。尻がまだ浮く。女性は横を向く。

**組み立てメモ:**
- `black high heels` を外す。ネガに `shoes, high heels`。脚は見えるので `feet` はネガに入れない。`barefoot` をタグへ。
- 腰浮き1回目の直し(自然文で flush + ネガ `m legs`)は実生成でも失敗。原因は `spread legs` + `pleated skirt` と、ポジ自然文の否定形(`no gap` / `not M-shape`)。
- 2回目: `spread legs` と `pleated skirt` を外す。`black skirt` は残す。`(on floor:1.8)`。自然文は肯定だけ。太腿は床の上で開く、と書く。
- 女性は横向き。`looking to the side`。`looking at another` は外す(頭側カメラで正面顔になる)。
- 頭の下の床が長い → 自然文で頭のすぐ外で切る。
- 背景は暖色のまま一段暗く。`dark background` + 自然文 dark warm orange-to-brown。人物光は `warm lighting`。
- ジャケット・ID・ホルスターなし。男性は白シャツ。とろけ顔・双方赤面・`from below` 禁止は維持。
- `explicit` / `newest` / `colored` / `anime coloring` は未指定。接頭辞は `masterpiece, best quality, score_7, safe` のみ。

**状態:** 2girls化・股下アオリ化・仰向け開脚の腰浮き(自然文接地でも再発)は実生成で確認 2026-09-09。横向き＋タグ外し稿は未再生成。

**スキル入力(日本語):**

```
リオと先生で。先生はアニメ版センセイで、顔は出さない。前髪は長い。白いシャツ。リオはジャケット・身分証・太ももホルスター・靴なし。股を開いて、その間に男性。女性は横を向く。床はフローリングで、頭の下は短く切る。背景は室内の少し暗い暖かいグラデ。家具なし。1枚絵。

【構図指示】
人数と配置: 1女1男だけ。女性は仰向け。頭が下手前、すぐ外でフレームを切る。長い空き床は出さない。足は床に着いたまま、股を開いて奥へ。男性は同じ向きで上に覆いかぶさり、胴が太腿の間に入る。立っていない。
ポーズ: 男性の両手は女性の頭の横の床。胸が女性の上。低く覆いかぶさる。女性の腰と尻の体重は床。太腿は床の上で開く。スカートは床に沿う。
表情・視線: 女性は半目で、すこしとろけている。顔は横向き。カメラは見ない。男性も赤面。顔は出さない。
カメラ: 頭側の床すれすれ。体に沿って奥を見る。股の間からカメラで見上げない。頭の直後で切る。
切り取り: 頭の下の床は短い。長いフローリングの余白は出さない。
背景・小道具: 手前=短いフローリング。中層=二人。奥=少し暗い暖かい室内グラデ。扉・家具なし。
光: 人物は弱い暖色。背景は一段暗い暖色。紫にしない。
色・空気感: 室内。暗いめの暖色グラデ。
動き: 倒した余勢。
不明瞭: なし
```

**推奨設定:** `896×1152`。`er_sde`、CFG 4〜5、30〜50ステップ。余白が残るならもう一段寄る。

**ポジティブ:**

```
masterpiece, best quality, score_7, safe, 1girl, 1boy, sensei (blue archive the animation), (faceless male:1.5), long bangs, white shirt, collared shirt, rio (blue archive), blue archive, very long hair, black hair, blunt bangs, hair behind ear, red eyes, ringed eyes, white pupils, hairclip, millennium science school logo, halo, black halo, large breasts, white turtleneck sweater, black skirt, black pantyhose, lying, on back, (on floor:1.8), wooden floor, barefoot, pinned down, height difference, blush, half-closed eyes, looking to the side, dim lighting, warm lighting, simple background, gradient background, dark background

Ground-level camera at their heads, looking along their bodies, cropped tight just past her head. She lies on her back with her head turned to the side; her hips rest on the floor and her thighs lie open on the floor with his body between them. He lies low over her in the same direction, both hands on the floor beside her head, both blushing. Darker warm orange-to-brown indoor gradient, no furniture, no door.
```

**ネガティブ:**

```
worst quality, low quality, score_1, score_2, score_3, artist name, blurry, jpeg artifacts, chromatic aberration, from below, between legs, upskirt, legs up, legs in the air, m legs, arched back, ass up, all fours, kneeling, looking at viewer, looking at another, upside-down, inverted, standing, closed legs, 2girls, multiple girls, yuri, straddling, girl on top, closed eyes, ahegao, tongue out, sitting, shoes, high heels, black jacket, id card, thigh holster, t-shirt, door, open door, backlight, furniture, plant, potted plant, cabinet, shelf, table, chair, houseplant, purple lighting, purple background, white background, scenery, outdoors, comic, multiple panels, 4koma, monochrome, greyscale, photorealistic, 3d, extra limbs, bad hands, watermark, signature, text, logo
```
