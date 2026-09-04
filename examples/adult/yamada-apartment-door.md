# 例: やまだ×マンション玄関の扉隙間

**指示(日本語):** 山田がボタン付きの白シャツを着て、途中のボタンが外れ黒ブラが少し見える。すこし汗、ぎこちない笑顔、はぁはぁ、赤面。添付構図どおり、外から少し開いた扉の隙間に彼女が見え、左下前景で手がインターホンを押している。

**組み立てメモ:** `characters/yamada.md` の固定タグはそのまま。容姿はタグ行だけにし、自然文は構図・空間(髪・瞳を再掲しない)。衣装・表情は前回どおり(`collared shirt, white shirt, black bra, partially unbuttoned` / `blush, sweat, awkward smile, open mouth, panting`)。構図差分は `pov` + 自然文(左下の手とインターホン、扉とドア枠の縦フレーム、玄関内側)。`hands` タグはキャラに付くので使わない。`peeking` は目だけになりやすいので使わない。

**ポジティブ:**

```
masterpiece, best quality, score_7, sensitive, 1girl, solo, yamada, bangs, folded ponytail, brown hair, red hair, red eyes, collared shirt, white shirt, black bra, partially unbuttoned, blush, sweat, awkward smile, open mouth, panting, looking at viewer, pov, doorway, open door, upper body

From a first-person view in the outside hallway, Yamada stands just inside the apartment and looks at the viewer through the narrow vertical gap of a barely open door. She wears a white button-up collared shirt with the middle buttons undone, a black bra slightly visible, blushing and lightly sweating, panting with an awkward smile. In the bottom-left foreground, a hand presses the button of a wall-mounted intercom; the door and doorframe crop her tightly, with a glimpse of the tiled genkan behind her.
```

**ネガティブ:**

```
worst quality, low quality, score_1, score_2, score_3, artist name, blurry, jpeg artifacts, chromatic aberration, t-shirt, simple background, nsfw, explicit, close-up face only, portrait crop
```

**設定メモ:** 縦構図が合いやすい(3:4 または 4:5)。サンプラーは `er_sde`、CFG 4〜5、30〜50ステップ。

**状態:** 【未検証】(Tシャツ化は実生成で確認。POV・インターホンの手・扉フレームの追従は未確認)
