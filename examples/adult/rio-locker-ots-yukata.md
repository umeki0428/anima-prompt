# 例: ロッカー部屋で浴衣の男性を見るリオ（後ろ姿OTS）

**指示(日本語):** 添付画像の構図を再現。女性はリオ。男性は短髪・顔なし・太め・年齢差。

**組み立てメモ:**
- カメラは手前の女性の背中越し。タグ `from behind` だけだと横並びになるので、自然文 `Over-the-shoulder shot from behind the girl`。
- 容姿はリオ固定。スクールロゴなし。既定制服（後ろ姿なので黒ジャケット）。ポニテは元絵用なので付けない。
- 男性は指定どおり `short hair, faceless male, fat man, age difference`。浴衣は男性だけ。自然文 He wears a yukata。
- 部屋はロッカーとベッド。モノクロ漫画に合わせ `monochrome, greyscale, screentones`。吹き出しは文字化けするので付けない。
- `explicit` / `newest` / `colored` / `anime coloring` は未指定。
- 構図が外れるなら参考画像で img2img 0.55〜0.7。

**状態:** 【未検証】

**スキル入力(日本語):**

```
リオと男性で。添付の構図。リオは手前で背中を見せ、部屋の奥のベッドに座る男性を見る。男性は短髪、顔なし、太め、年齢差、浴衣。左にロッカー。モノクロ。吹き出しなし。1枚絵。

【構図指示】
人数と配置: 1女1男。女性が手前・背中。男性が右奥のベッドに座る。
ポーズ: 女性は立って男性の方を向く。男性はベッドに座り、こちら（女性）を向く。
表情・視線: 女性の顔はほぼ見えない。男性は顔なし。カメラは見ない。
カメラ: 女性の背中越しのオーバーショルダー。横並びの二人組にしない。
切り取り: 女性は頭から腰。男性は座った全身が収まる。
背景・小道具: 左に金属ロッカー。奥にベッド。吹き出しなし。
光: 指定なし。スクリーントーン。
色・空気感: モノクロ漫画。
動き: 部屋に入って男性を見ている。
不明瞭: なし
```

**推奨設定:** `896×1152`。`er_sde`、CFG 4〜5、30〜50ステップ。外れるなら参考画像 img2img 0.55〜0.7。

**ポジティブ:**

```
masterpiece, best quality, score_7, safe, 1girl, 1boy, (faceless male:1.5), short hair, fat man, age difference, rio (blue archive), blue archive, very long hair, black hair, blunt bangs, hair behind ear, red eyes, ringed eyes, white pupils, hairclip, halo, black halo, large breasts, white turtleneck sweater, black jacket, id card, black skirt, pleated skirt, black pantyhose, from behind, facing another, indoors, locker, bed, yukata, sitting, standing, monochrome, greyscale, screentones

Over-the-shoulder shot from behind the girl. She stands in the foreground with her back to the camera, looking at him. A fat faceless man with short hair sits on the bed in a yukata, facing her. Metal lockers on the left, beds in the room. No speech bubbles.
```

**ネガティブ:**

```
worst quality, low quality, score_1, score_2, score_3, artist name, blurry, jpeg artifacts, chromatic aberration, looking at viewer, from front, ponytail, 2girls, multiple girls, girl on top, speech bubble, japanese text, text, comic, multiple panels, 4koma, colored, millennium science school logo, logo, extra limbs, bad hands, watermark, signature, photorealistic, 3d
```
