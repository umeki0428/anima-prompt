# 例: 玄関で押し倒されるリオ(頭側床からのアオリ)

**指示(日本語):** ラフどおり。黒=男性、赤=女性。青い目の矢印がカメラ。玄関で男性が女性を押し倒した直後。女性はリオ。

**組み立てメモ:**
- 1枚絵のハイブリッド。容姿は `characters/rio.md` の固定タグ＋既定衣装をそのまま。自然文に髪・瞳・ヘイロー・クリップを再掲しない。
- 男性は直前までの指定を踏襲: `sensei (blue archive the animation), faceless male, long bangs`。顔は出さない。
- カメラは頭側の床すれすれから、足と閉まった扉のほうを見る。`from below` + 自然文 `low angle`。タグ `from behind` は使わない(横顔並列になる)。
- 頭が手前で大きく、胴と脚は奥へ小さくなる。手前=頭と男性の両手、中層=覆いかぶさる上体、奥=脚と玄関扉。
- 「パタン」は効果音なので出さない。ネガに `text`。
- 背景は玄関(場所の指示あり)。グラデや `simple background` は足さない。
- `explicit` / `newest` / `colored` / `anime coloring` は未指定。接頭辞は `masterpiece, best quality, score_7, safe` のみ。
- 視線は彼を見る。ネガに `looking at viewer`。立ち絵化防止でネガに `standing`。

**状態:** 【未検証】(机上の変換。実生成後に結果を追記する)

**スキル入力(日本語):**

```
リオと先生で。先生はアニメ版センセイで、顔は出さない。前髪は長い。1枚絵。漫画のコマ割りにしない。

【構図指示】
人数と配置: 2人。女性は仰向けで床に倒されている。頭が画面下手前で大きく、足は画面上奥へ小さく伸びる。男性はその上に覆いかぶさり、頭も手前、背中は奥の扉へ向かう。男性のほうが大きい。
ポーズ: 男性は両腕を女性の頭の横の床について上体を支え、前傾して覆いかぶさる。押し倒した直後で、まだ体重が乗っている。女性は両肩が床につき、膝は奥でわずかに曲がっていてよい。
表情・視線: 女性は眉が上がり、驚き。視線は上の男性へ。男性の顔は出さない。
カメラ: 頭側の床すれすれ。わずかにアオリ。頭から足・扉の方向を見る。パースは強く、手前の頭と手が大きい。
切り取り: 全身が奥行き方向に入る。足元は奥で小さいが見える。
背景・小道具: 手前=床と頭、男性の両手。中層=二人の胴。奥=閉まった玄関扉。玄関の土間。部屋の奥側は見せない。
光: 室内。扉側から弱い光が落ちてもよい。均一な昼光にはしない。
色・空気感: 玄関の室内。押し倒した直後の勢い。
動き: 倒した余勢が残っている。上体がまだ前に乗っている。
不明瞭: 効果音「パタン」は描かない
```

**推奨設定:** `896×1152`(縦長、頭が下・扉が上)。`er_sde`、CFG 4〜5、30〜50ステップ。

**ポジティブ:**

```
masterpiece, best quality, score_7, safe, 1girl, rio (blue archive), blue archive, very long hair, black hair, blunt bangs, hair behind ear, red eyes, ringed eyes, white pupils, hairclip, millennium science school logo, halo, black halo, large breasts, white turtleneck sweater, black jacket, id card, black skirt, pleated skirt, black pantyhose, thigh holster, black high heels, 1boy, sensei (blue archive the animation), faceless male, long bangs, lying, on back, on floor, leaning forward, height difference, blush, surprised, looking at another, from below, indoors, door, doorway

Low angle from the genkan floor at their heads, looking along their bodies toward the closed front door. Rio lies on her back, head nearest the camera and feet receding toward the door. Sensei is on top of her and larger; his head is also in the near foreground and his back stretches toward the door. He has just pushed her down and plants both hands on the floor beside her head. Strong perspective: heads and his hands large in front, the door small at the far end. No on-screen text.
```

**ネガティブ:**

```
worst quality, low quality, score_1, score_2, score_3, artist name, blurry, jpeg artifacts, chromatic aberration, looking at viewer, standing, sitting, from behind, white background, simple background, gradient background, comic, multiple panels, 4koma, monochrome, greyscale, scenery, outdoors, photorealistic, 3d, extra limbs, bad hands, watermark, signature, text, logo
```
