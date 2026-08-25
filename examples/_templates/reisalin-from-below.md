# 例: ライザ・地面から見上げ(既定衣装・服は着たまま)

**指示(日本語):** キャラクターシートはやめる。ライザの既定衣装を着たまま、参考画像と同じポーズとアングル。地面から真上に見上げるカウボーイショット。両手を肩の高さまで上げ、肘を曲げて胸元の服を掴む。服は脱がない。下着姿や白シャツ開きにはしない。

**組み立てメモ:** `characters/reisalin.md` の固定タグ・既定衣装・既定画風をそのまま使用。差分はポーズとカメラだけ(`standing, arms up, looking at viewer, from below, cowboy shot`)。参考画像の白シャツ・Tバック・ニーハイは使わない。`undressing` / `open shirt` / `clothes pull` は服が消えるので付けない。ローアングルで短パンが消えないよう `(red shorts:1.8), (short shorts:1.8)` と自然文で裾が見えると書く。タグ順は 固定タグ → 衣装 → ポーズ/表情 → 背景 → カメラ → 画風。

**ポジティブ:**

```
masterpiece, best quality, score_7, safe, 1girl, solo, reisalin stout, atelier (series), brown hair, short hair, brown eyes, hairclip, large breasts, white headwear, beret, (short shorts:1.8), (red shorts:1.8), brown gloves, bare shoulders, cleavage, navel, collarbone, thick thighs, standing, arms up, blush, looking at viewer, from below, cowboy shot, outdoors, cloudy sky, anime coloring

Reisalin Stout has short brown hair with a hairclip and brown eyes. She stands over the camera fully dressed in her usual clothes: a white beret, red short shorts, and brown gloves, with bare shoulders, collarbone, and navel visible. Both arms are raised to shoulder height with elbows bent, her gloved hands gripping the front of her clothes at the chest without pulling them off. She looks down at the viewer with a light blush. The camera is at ground level looking straight up, framing her from the upper thighs to her head against a dark overcast sky. The red shorts stay on and their hems stay visible above her thick thighs. No feet or shoes in frame. Clothes stay opaque.
```

**ネガティブ:**

```
worst quality, low quality, score_1, score_2, score_3, artist name, blurry, jpeg artifacts, chromatic aberration, nsfw, explicit, sensitive, nude, undressing, open shirt, white shirt, lab coat, thighhighs, panties, panty lines, cameltoe, upskirt, clothes removed, character sheet, multiple views, 2girls, extra limbs, bad anatomy, shoes, feet, close-up face only, portrait crop, text, watermark, signature, photorealistic, 3d
```

**推奨設定:** 3:4、`er_sde`、CFG 4〜5、30〜50ステップ。

**状態:** 【未検証】(机上の変換例。実生成での確認後、結果と設定を追記する)
