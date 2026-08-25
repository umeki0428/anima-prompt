# 例: ライザ・地面から見上げ(既定衣装・雰囲気だけエロ)

**指示(日本語):** 前稿のポーズ・衣装・カメラはそのまま。服は着たまま。背景と雰囲気だけエロくする。行為・脱衣・とろけ顔は足さない。

**組み立てメモ:** `characters/reisalin.md` の固定タグ・既定衣装を維持。差分は雰囲気だけ。[atmosphere.md](../../references/atmosphere.md) の「無彩色背景 + 暖色リム」。`safe` を外して `sensitive`。ネガから `nsfw, explicit, sensitive` を外す。昼空は雰囲気を殺すので `outdoors, cloudy sky` を外し、ネガへ。紫は使わない。`steaming body` は透けるので `steam, haze` のみ。タグ順は 固定タグ → 衣装 → ポーズ/表情 → ライティング → カメラ → 画風。

**ポジティブ:**

```
masterpiece, best quality, score_7, sensitive, 1girl, solo, reisalin stout, atelier (series), brown hair, short hair, brown eyes, hairclip, large breasts, white headwear, beret, (short shorts:1.8), (red shorts:1.8), brown gloves, bare shoulders, cleavage, navel, collarbone, thick thighs, standing, arms up, blush, looking at viewer, dim lighting, warm lighting, rim light, steam, haze, volumetric lighting, from below, cowboy shot, simple background, gradient background, dark background, anime coloring

Reisalin Stout has short brown hair with a hairclip and brown eyes. She stands over the camera fully dressed in her usual clothes: a white beret, red short shorts, and brown gloves, with bare shoulders, collarbone, and navel visible. Both arms are raised to shoulder height with elbows bent, her gloved hands gripping the front of her clothes at the chest without pulling them off. She looks down at the viewer with a light blush.

The camera is at ground level looking straight up, framing her from the upper thighs to her head. The background is a dark charcoal gradient, not purple. Soft warm light from below and behind puts a thin rim along her thighs, hips, and collarbone. A faint haze of steam hangs in the air. The red shorts stay on and their hems stay visible. Clothes stay opaque, with no panty lines. No feet or shoes in frame.
```

**ネガティブ:**

```
worst quality, low quality, score_1, score_2, score_3, artist name, blurry, jpeg artifacts, chromatic aberration, nude, undressing, open shirt, white shirt, lab coat, thighhighs, panties, panty lines, cameltoe, upskirt, clothes removed, character sheet, multiple views, 2girls, extra limbs, bad anatomy, shoes, feet, close-up face only, portrait crop, outdoors, scenery, cloudy sky, purple, purple background, purple lighting, see-through, see-through clothes, wet clothes, steaming body, text, watermark, signature, photorealistic, 3d
```

**推奨設定:** 3:4、`er_sde`、CFG 4〜5、30〜50ステップ。

**状態:** 【未検証】(机上の変換例。実生成での確認後、結果と設定を追記する)
