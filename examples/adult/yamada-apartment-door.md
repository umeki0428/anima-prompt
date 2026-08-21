# 例: やまだ×マンション玄関の扉隙間

**指示(日本語):** 山田がボタン付きの白シャツを着て、途中のボタンが外れ黒ブラが少し見える。すこし汗、ぎこちない笑顔、はぁはぁ、赤面。マンションの玄関の扉が開いた隙間から見える。

**組み立てメモ:** `characters/yamada.md` の固定タグはそのまま使用。衣装は既定を全部削除し、`collared shirt, white shirt, black bra, partially unbuttoned` に置き換え(`white shirt` 単体はTシャツ化する。failures.md 参照)。`open shirt` は全開になるので使わない。表情は `blush, sweat, awkward smile, open mouth, panting`。扉の隙間は自然文。レーティングは `sensitive`。

**ポジティブ:**

```
masterpiece, best quality, score_7, sensitive, 1girl, solo, yamada, bangs, folded ponytail, brown hair, red hair, red eyes, collared shirt, white shirt, black bra, partially unbuttoned, blush, sweat, awkward smile, open mouth, panting, looking at viewer, doorway, open door, upper body

Yamada, a girl with bangs, a folded ponytail, brown and red hair, and red eyes, wears a white button-up collared shirt. The middle buttons are undone, and a black bra is slightly visible. She looks at the viewer through the narrow vertical gap of a slightly open apartment door, blushing and lightly sweating, panting with an awkward smile. The camera is in the outside hallway, framing her between the door and the doorframe.
```

**ネガティブ:**

```
worst quality, low quality, score_1, score_2, score_3, artist name, blurry, jpeg artifacts, chromatic aberration, t-shirt, simple background, nsfw, explicit
```

**設定メモ:** 縦構図が合いやすい(3:4 または 4:5)。サンプラーは `er_sde`、CFG 4〜5、30〜50ステップ。

**状態:** 【未検証】(Tシャツ化は実生成で確認。ボタンシャツ化・ブラチラ見え・表情の追従は未確認)
