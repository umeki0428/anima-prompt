# 例: 室内フローリングで押し倒されるリオ

**指示(日本語):** 頭側床カメラのまま。靴削除。女性は股を開き、その間に男性。頭側の床が長いので短く切る。背景の暖色グラデをすこし暗く。女性は横を向く。腰浮き対策で構図が崩壊したので戻す。

**組み立てメモ:**
- `(on floor:1.8)` + 自然文 hips rest on the floor が真上俯瞰になり、`on back` が男性にも付いて上下が逆さ、腰が胴から外れた。接地を画面に描かせない。
- 構図は頭側床カメラ＋男性が上に戻す。`spread legs` / `pleated skirt` / `leaning forward` を戻す。`on floor` は重みなし。
- 腰浮きは「床との隙間を見せる」ではなく、脚を奥へ伸ばす。ネガ `m legs, arched back, ass up` は残す。
- 横向きは顔だけ `looking to the side`。ネガの `looking at another` は外す。ネガに `from above`（真上俯瞰止め）。
- ジャケット・ID・ホルスター・靴なし。男性は白シャツ。とろけ顔・双方赤面・`from below` 禁止は維持。
- `explicit` / `newest` / `colored` / `anime coloring` は未指定。接頭辞は `masterpiece, best quality, score_7, safe` のみ。

**状態:** 2girls化・股下アオリ化・腰浮き・真上俯瞰で解剖崩壊は実生成で確認 2026-09-09。頭側カメラ復帰稿は未再生成。

**スキル入力(日本語):**

```
リオと先生で。先生はアニメ版センセイで、顔は出さない。前髪は長い。白いシャツ。リオはジャケット・身分証・太ももホルスター・靴なし。股を開いて、その間に男性。女性は顔だけ横を向く。床はフローリングで、頭の下は短く切る。背景は室内の少し暗い暖かいグラデ。家具なし。1枚絵。

【構図指示】
人数と配置: 1女1男だけ。女性は仰向けで下。頭が下手前、すぐ外でフレームを切る。男性は同じ向きで上に覆いかぶさり、胴が太腿の間に入る。
ポーズ: 男性の両手は女性の頭の横の床。胸が女性の上。女性の脚は奥の床へ伸びる。股は開く。
表情・視線: 女性は半目で、すこしとろけている。顔は横向き。カメラは見ない。男性も赤面。顔は出さない。
カメラ: 頭側の床すれすれ。体に沿って足方向を見る。真上から見下ろさない。股の間から見上げない。
切り取り: 頭の下の床は短い。長いフローリングの余白は出さない。
背景・小道具: 手前=短いフローリング。中層=二人。奥=少し暗い暖かい室内グラデ。扉・家具なし。
光: 人物は弱い暖色。背景は一段暗い暖色。紫にしない。
色・空気感: 室内。暗いめの暖色グラデ。
動き: 倒した余勢。
不明瞭: なし
```

**推奨設定:** `896×1152`。`er_sde`、CFG 4〜5、30〜50ステップ。余白が残るならもう一段寄る。構図がまた抽選で外れるなら、頭側カメラで当たっていた前の絵を元に img2img 0.3〜0.5。

**ポジティブ:**

```
masterpiece, best quality, score_7, safe, 1girl, 1boy, sensei (blue archive the animation), (faceless male:1.5), long bangs, white shirt, collared shirt, rio (blue archive), blue archive, very long hair, black hair, blunt bangs, hair behind ear, red eyes, ringed eyes, white pupils, hairclip, millennium science school logo, halo, black halo, large breasts, white turtleneck sweater, black skirt, pleated skirt, black pantyhose, lying, on back, on floor, wooden floor, barefoot, spread legs, pinned down, leaning forward, height difference, blush, half-closed eyes, looking to the side, dim lighting, warm lighting, simple background, gradient background, dark background

Ground-level camera at her head, looking along her body toward her feet, cropped tight just past her head. He is on top of her, covering her, both hands on the floor beside her head; her face is turned to the side and her legs extend along the floor into the distance with his body between her thighs. Darker warm orange-to-brown indoor gradient, no furniture, no door.
```

**ネガティブ:**

```
worst quality, low quality, score_1, score_2, score_3, artist name, blurry, jpeg artifacts, chromatic aberration, from above, from below, between legs, upskirt, legs up, legs in the air, m legs, arched back, ass up, all fours, kneeling, looking at viewer, upside-down, inverted, standing, closed legs, 2girls, multiple girls, yuri, straddling, girl on top, closed eyes, ahegao, tongue out, sitting, shoes, high heels, black jacket, id card, thigh holster, t-shirt, door, open door, backlight, furniture, plant, potted plant, cabinet, shelf, table, chair, houseplant, purple lighting, purple background, white background, scenery, outdoors, comic, multiple panels, 4koma, monochrome, greyscale, photorealistic, 3d, extra limbs, bad hands, watermark, signature, text, logo
```
