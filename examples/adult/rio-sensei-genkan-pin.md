# 例: 玄関で押し倒されるリオ(頭側の床から扉方向)

**指示(日本語):** ラフどおり。黒=男性、赤=女性。青い目の矢印がカメラ。夜の玄関で男性がリオを押し倒す。家具なし。女性は男性を見る。

**組み立てメモ:**
- `from below` は使わない。立ち人物を股下から見る定番になり、男が開脚して立ち、リオが脚を上げた逆さになる(2026-09-09)。[failures.md](../../references/failures.md) / [vocab.md](../../references/vocab.md)
- カメラは自然文だけ。床＝頭側、視線は体に沿って閉まった扉へ。
- 二人は同じ向き。頭が手前、足は床に着いたまま奥の扉へ。男性は立たず、上に覆いかぶさる。
- 人数は先頭で `1girl, 1boy`。`(faceless male:1.5), long bangs` をリオより前。
- 夜の玄関。閉まった扉だけ。家具・植木・開いた逆光の扉はネガ。
- 視線は `looking at another`。ネガに `looking at viewer`。
- `explicit` / `newest` / `colored` / `anime coloring` は未指定。接頭辞は `masterpiece, best quality, score_7, safe` のみ。

**状態:** 2girls化・股下アオリ化は実生成で確認 2026-09-09。この稿は未再生成。

**スキル入力(日本語):**

```
リオと先生で。先生はアニメ版センセイで、顔は出さない。前髪は長い。夜の玄関。家具は出さない。1枚絵。漫画のコマ割りにしない。

【構図指示】
人数と配置: 1女1男だけ。女性は仰向けで床に寝ている。頭が画面下手前、足は床に着いたまま画面上奥の扉へ伸びる。脚は宙に上げない。男性はその上に同じ向きで覆いかぶさる。立っていない。上に乗っているのは男。
ポーズ: 男性は両膝と両手が床側。両手は女性の頭の横の床。胸が女性の上に乗る。押し倒した直後。女性は肩と尻とかかとが床。
表情・視線: 女性は驚き。視線は上の男性。カメラは見ない。男性の顔は出さない。
カメラ: 頭側の床すれすれ。体に沿って扉を見る。股の間から見上げない。下からアオリのタグは使わない。手前は後頭部と両手、奥は足と扉。
切り取り: 奥行き方向に全身。
背景・小道具: 暗い土間。奥に閉まった玄関扉だけ。靴箱・植木・棚なし。扉は開けない。
光: 夜。暗い。人物に弱い暖色。逆光のシルエットにしない。
色・空気感: 夜の玄関。押し倒した直後。
動き: 倒した余勢。上体がまだ前に乗っている。
不明瞭: 効果音は描かない
```

**推奨設定:** `896×1152`。`er_sde`、CFG 4〜5、30〜50ステップ。

**ポジティブ:**

```
masterpiece, best quality, score_7, safe, 1girl, 1boy, sensei (blue archive the animation), (faceless male:1.5), long bangs, rio (blue archive), blue archive, very long hair, black hair, blunt bangs, hair behind ear, red eyes, ringed eyes, white pupils, hairclip, millennium science school logo, halo, black halo, large breasts, white turtleneck sweater, black jacket, id card, black skirt, pleated skirt, black pantyhose, thigh holster, black high heels, lying, on back, on floor, pinned down, leaning forward, height difference, blush, surprised, looking at another, night, dim lighting, warm lighting, indoors, door, doorway, closed door

One man and one woman only. Ground-level camera at their heads, looking along the floor toward the closed front door. Rio lies on her back on the genkan floor; her head is nearest the camera and her legs stay on the floor, stretching toward the door, not in the air. She looks up at him, not at the camera. Sensei is male and faceless and is not standing; he lies over her in the same direction, chest over her chest, the back of his head in the near foreground, both hands planted on the floor beside her head as he pins her down. Night genkan: dark floor, a closed door far away, no furniture, no plants, no open doorway backlight.
```

**ネガティブ:**

```
worst quality, low quality, score_1, score_2, score_3, artist name, blurry, jpeg artifacts, chromatic aberration, from below, between legs, upskirt, legs up, legs in the air, upside-down, inverted, standing, spread legs, 2girls, multiple girls, yuri, straddling, girl on top, looking at viewer, sitting, open door, backlight, furniture, plant, potted plant, cabinet, shelf, table, chair, houseplant, daylight, sunlight, white background, simple background, gradient background, comic, multiple panels, 4koma, monochrome, greyscale, scenery, outdoors, photorealistic, 3d, extra limbs, bad hands, watermark, signature, text, logo
```
