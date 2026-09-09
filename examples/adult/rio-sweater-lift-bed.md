# 例: ベッドでタートルを手首までめくるリオ

**指示(日本語):** ミレニアムサイエンススクールのロゴは不要。服を着たままになっているのをやめ、胸は出す。手首まで全部持ち上げる。ブラなし。胸の揺れはなし。

**組み立てメモ:**
- `clothes lift` / `sweater lift` は裾上げ＝着衣のままへそ出し。外す。
- `white turtleneck sweater` も着衣として胴に残るのでポジから外す。服は自然文で手首に束ねた白いセーターだけ。タグは `undressing, removing sweater, unworn sweater, topless`。
- `millennium science school logo` は削除。ネガ `logo, text, print`。クリップとハロは残す。
- ブラなし。ネガ `bra, tank top, crop top, turtleneck`。
- 胸の揺れはなし。`bouncing breasts` を外しネガへ。`hanging breasts` もネガ。`motion blur` も外す。
- 胸は `medium breasts`。男性は手だけ。
- `explicit` / `newest` / `colored` / `anime coloring` は未指定。接頭辞は `masterpiece, best quality, score_7, safe` のみ。

**状態:** 裾上げでタンクトップ着衣＋胸ロゴは実生成で確認 2026-09-09。脱衣稿は未再生成。

**スキル入力(日本語):**

```
リオで。ミレニアムサイエンススクールのロゴは付けない。白いセーターは胴から外して手首に束ねる。ブラなし。胸は揺らさない。仰向け、両手を上げている。頭の上から見下ろす。ベッドのシーツは少しだけ。背景はぼかしたチャコールから深いプラムのグラデ。1枚絵。

【構図指示】
人数と配置: 女性1人。男性の手だけが手首の服をつかむ。全身の男性は出さない。
ポーズ: 仰向け。両腕は頭の上。セーターは胴になく、手首にだけ束ねる。胸は出ている。
表情・視線: 驚きと照れ。赤面。カメラを見る。
カメラ: 頭の上から急なハイアングル。ダッチアングル。上半身近景。
切り取り: 上半身。
背景・小道具: 下にシーツが少し。奥はぼかしたチャコール〜深いプラム。部屋のディテールなし。
光: 上からの弱い暖色。
色・空気感: 暗い室内。
動き: 服を脱がせる途中。胸は揺らさない。
不明瞭: なし
```

**推奨設定:** `896×1152`。`er_sde`、CFG 4〜5、30〜50ステップ。

**ポジティブ:**

```
masterpiece, best quality, score_7, safe, 1girl, rio (blue archive), blue archive, very long hair, black hair, blunt bangs, hair behind ear, red eyes, ringed eyes, white pupils, hairclip, halo, black halo, medium breasts, undressing, removing sweater, unworn sweater, topless, arms up, bare shoulders, lying, on back, surprised, embarrassed, blush, looking at viewer, from above, dutch angle, upper body, close-up, bed sheet, gradient background, blurry background, depth of field, soft lighting, dim lighting

Steep high-angle shot from above her head. A white sweater is off her torso and bunched only at her wrists on her raised arms. A man's hands grip that bunched fabric, mid-motion, lifting it toward the top of the frame. A small stretch of bed sheet under her; soft charcoal-to-deep-plum gradient, blurred, no room details.
```

**ネガティブ:**

```
worst quality, low quality, score_1, score_2, score_3, artist name, blurry, jpeg artifacts, chromatic aberration, millennium science school logo, logo, text, print, clothes writing, bra, pink bra, underwear, turtleneck, tank top, crop top, shirt, fully clothed, covered chest, clothes lift, sweater lift, bouncing breasts, hanging breasts, from below, closed eyes, extra limbs, bad hands, watermark, signature, photorealistic, 3d
```
