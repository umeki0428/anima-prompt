# 例: カウンター越しのナンパ、オーバーショルダー+アオリ(検証済み)

**指示(日本語):** レジカウンター越しに男性が女性に話しかけ、女性が困っている。男性の背中越しに女性を見る、やや下から、手前の男性はボケ。

**組み立てメモ:** 撮影用語の検証 C 案(タグ行+撮影用語の自然文)。LoRA なし、汎用キャラ。検証の全体は [../../references/composition.md](../../references/composition.md)。

**ポジティブ:**

```
masterpiece, best quality, score_7, safe,
1girl, 1boy, facing another, eye contact, talking, counter, from behind, from below, upper body, sweatdrop, furrowed brow, indoors

Over-the-shoulder shot from behind the man. Low angle, slightly below the woman's eye level. Medium close-up on the woman behind the counter, the man's head and shoulder large and out of focus in the lower left foreground. She looks at him with a troubled expression, sweat on her cheek. Shallow depth of field.
```

**ネガティブ:**

```
worst quality, low quality, score_1, score_2, score_3, artist name, blurry, jpeg artifacts, chromatic aberration, looking at viewer
```

**結果:** 2枚とも OTS・アオリ(天井照明とカウンター縁が見える)・手前ボケ・女性の視線が男性向き、を満たす。1枚は女性の顔が男性の肩で半分隠れる遮蔽構図。

**状態:** 検証済み 2026-09-07(txt2img、seed 固定、er_sde)
