# 例: 室内フローリングで押し倒されるリオ

**指示(日本語):** 頭側床カメラでは腰がどうしても浮く／切れるので、男性目線のPOVに変える。靴なし。股を開いてその間に男性。女性は横を向く。背景は少し暗い暖かいグラデ。家具なし。

**組み立てメモ:**
- 頭側床カメラ＋覆いかぶさりは、男性の胴で腰が切れ、脚が肩の後ろに回る。接地の言い換えでは直らない。カメラを男性POVへ。
- 人数は `1girl` のみ。`1boy` / `sensei` / `faceless male` は第三人称の全身を呼ぶので外す。ネガに `1boy`。
- カメラは `pov, from above` + 自然文 `high angle` / first-person from his eyes。手前は白シャツの袖と手だけ。`hands` タグはキャラに付くので使わない。
- 衣装はタートル・黒スカート・タイツ。ジャケット・ID・ホルスター・靴なし。`barefoot`。
- 横向きは `looking to the side`。POVでも `looking at viewer` はネガ（顔を横に保つ）。
- `explicit` / `newest` / `colored` / `anime coloring` は未指定。接頭辞は `masterpiece, best quality, score_7, safe` のみ。

**状態:** 頭側床カメラの腰切れ・浮きは実生成で確認 2026-09-09。男性POV稿は未再生成。

**スキル入力(日本語):**

```
リオと先生で。男性目線のPOV。先生の顔は出さない。手前に白いシャツの手だけ。リオはジャケット・身分証・太ももホルスター・靴なし。仰向け。股を開いて、その間に男性。顔は横向き。床はフローリング。背景は室内の少し暗い暖かいグラデ。家具なし。1枚絵。

【構図指示】
人数と配置: 見えるのは女性1人。男性の全身は出さない。女性は仰向けで床。頭が画面の上寄り、脚が下。男性の両手だけ前景で、頭の横の床。
ポーズ: 女性は押し倒されている。股は開く。男性の胴は太腿の間だが、カメラは男性の目なので胴の全体は写さない。
表情・視線: 女性は半目で、すこしとろけている。顔は横向き。カメラ（男性）は正面では見ない。
カメラ: 男性の目線。上から見下ろすハイアングル。真上の真俯瞰にはしない。股の間から見上げない。
切り取り: 頭から太腿まで。男性の顔・頭は出さない。
背景・小道具: フローリング。奥は少し暗い暖かい室内グラデ。扉・家具なし。
光: 人物は弱い暖色。背景は一段暗い暖色。紫にしない。
色・空気感: 室内。暗いめの暖色グラデ。
動き: 倒した余勢。
不明瞭: なし
```

**推奨設定:** `896×1152`。`er_sde`、CFG 4〜5、30〜50ステップ。

**ポジティブ:**

```
masterpiece, best quality, score_7, safe, 1girl, rio (blue archive), blue archive, very long hair, black hair, blunt bangs, hair behind ear, red eyes, ringed eyes, white pupils, hairclip, millennium science school logo, halo, black halo, large breasts, white turtleneck sweater, black skirt, pleated skirt, black pantyhose, lying, on back, on floor, wooden floor, barefoot, spread legs, pinned down, pov, from above, blush, half-closed eyes, looking to the side, dim lighting, warm lighting, simple background, gradient background, dark background

Point-of-view shot from the man looking down at her, high angle from his eyes as he pins her. His hands in the foreground hold her wrists to the floor beside her head, white shirt sleeves at the bottom of the frame. Her face is turned to the side; her legs are open toward the bottom of the frame with his body between her thighs. Darker warm orange-to-brown indoor gradient, no furniture, no door.
```

**ネガティブ:**

```
worst quality, low quality, score_1, score_2, score_3, artist name, blurry, jpeg artifacts, chromatic aberration, 1boy, faceless male, from below, between legs, upskirt, legs up, legs in the air, m legs, arched back, ass up, all fours, kneeling, looking at viewer, upside-down, inverted, standing, closed legs, 2girls, multiple girls, yuri, straddling, girl on top, closed eyes, ahegao, tongue out, sitting, shoes, high heels, black jacket, id card, thigh holster, t-shirt, door, open door, backlight, furniture, plant, potted plant, cabinet, shelf, table, chair, houseplant, purple lighting, purple background, white background, scenery, outdoors, comic, multiple panels, 4koma, monochrome, greyscale, photorealistic, 3d, extra limbs, bad hands, watermark, signature, text, logo
```
