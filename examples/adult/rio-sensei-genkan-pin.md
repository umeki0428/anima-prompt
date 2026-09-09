# 例: 玄関で押し倒されるリオ(頭側床からのアオリ)

**指示(日本語):** ラフどおり。黒=男性、赤=女性。青い目の矢印がカメラ。夜の玄関で男性がリオを押し倒す。家具なし。女性は男性を見る。

**組み立てメモ:**
- 初稿は `from below` + リオ既定制服が「下から見た立ちリオ」の定番に引かれ、上の人物がもう1人のリオになった。男性タグが後ろすぎた。失敗は [failures.md](../../references/failures.md)。
- 人数は先頭で `1girl, 1boy`。先生の `faceless male, long bangs` をリオの長髪・ハロより前に書く。効かなかったので `(faceless male:1.5)`。
- カメラは頭側の床から扉方向。股の間からスカートを見上げる構図ではない。自然文で「between the legs ではない」と書く。
- 夜の玄関。奥に閉まった扉だけ。家具・植木はネガ。グラデ空背景は足さない(扉と喧嘩する)。
- 視線は `looking at another`。ネガに `looking at viewer, 2girls, straddling, upskirt`。
- `explicit` / `newest` / `colored` / `anime coloring` は未指定。接頭辞は `masterpiece, best quality, score_7, safe` のみ。

**状態:** 【未検証】(2girls化は実生成で確認 2026-09-09。修正稿は未再生成)

**スキル入力(日本語):**

```
リオと先生で。先生はアニメ版センセイで、顔は出さない。前髪は長い。夜の玄関。家具は出さない。1枚絵。漫画のコマ割りにしない。

【構図指示】
人数と配置: 1女1男の2人だけ。女性は仰向けで床。頭が画面下手前、足は奥の扉へ。男性(1boy)がその上に覆いかぶさる。上に乗っているのは男。女は1人。
ポーズ: 男性は両腕を女性の頭の横の床について支え、前傾して押し倒している。女性は両肩が床。
表情・視線: 女性は驚き気味。視線は上の男性を見る。カメラは見ない。男性の顔は出さない。
カメラ: 頭側の床すれすれ。わずかにアオリ。頭から足・扉を見る。股の間から見上げない。手前は頭と男性の両手と後頭部。
切り取り: 奥行き方向に全身。
背景・小道具: 手前=土間の床。中層=二人。奥=閉まった玄関扉だけ。靴箱・植木・棚はなし。
光: 夜。暗い。人物に弱い暖色。昼の均一光にしない。
色・空気感: 夜の玄関。押し倒した直後。
動き: 倒した余勢。上体がまだ前に乗っている。
不明瞭: 効果音は描かない
```

**推奨設定:** `896×1152`。`er_sde`、CFG 4〜5、30〜50ステップ。

**ポジティブ:**

```
masterpiece, best quality, score_7, safe, 1girl, 1boy, sensei (blue archive the animation), (faceless male:1.5), long bangs, rio (blue archive), blue archive, very long hair, black hair, blunt bangs, hair behind ear, red eyes, ringed eyes, white pupils, hairclip, millennium science school logo, halo, black halo, large breasts, white turtleneck sweater, black jacket, id card, black skirt, pleated skirt, black pantyhose, thigh holster, black high heels, lying, on back, on floor, leaning forward, height difference, blush, surprised, looking at another, from below, night, dim lighting, warm lighting, indoors, door, doorway

One man and one woman only. Low angle from the genkan floor at their heads, looking along their bodies toward the closed front door, not from between anyone's legs. Rio lies on her back and looks up at him, not at the camera. Sensei is male, faceless, on top of her; the back of his head and shoulders fill the near foreground as he pushes her down, both hands planted on the floor beside her head. Night genkan: dark floor, a closed door far away, no furniture and no plants.
```

**ネガティブ:**

```
worst quality, low quality, score_1, score_2, score_3, artist name, blurry, jpeg artifacts, chromatic aberration, 2girls, multiple girls, yuri, straddling, girl on top, upskirt, looking at viewer, standing, sitting, furniture, plant, potted plant, cabinet, shelf, table, chair, houseplant, daylight, sunlight, white background, simple background, gradient background, comic, multiple panels, 4koma, monochrome, greyscale, scenery, outdoors, photorealistic, 3d, extra limbs, bad hands, watermark, signature, text, logo
```
