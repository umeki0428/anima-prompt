# 例: やまだ×マンション玄関の扉隙間

**指示(日本語):** 山田のキャラクターで、シャツを着て色っぽい状態で息が切れている。軽い赤面。マンションの玄関の扉が開いた隙間から女性が見える構図。

**組み立てメモ:** `characters/yamada.md` の固定タグはそのまま使用。衣装は「シャツ」指定のため既定衣装を全部削除し `white shirt` のみに置き換え。色っぽい息切れは `sensitive` レーティング(接頭辞の `safe` は使わない)。扉の隙間・内外の位置関係はタグより自然文。参考画像の長髪・アホ毛・強い発汗は山田の固定タグおよび「軽い赤面」と矛盾するため入れない。

**ポジティブ:**

```
masterpiece, best quality, score_7, sensitive, 1girl, solo, yamada, bangs, folded ponytail, brown hair, red hair, red eyes, white shirt, blush, open mouth, panting, seductive, looking at viewer, doorway, open door, indoors, upper body

Yamada, a girl with bangs, a folded ponytail, brown and red hair, and red eyes, wears a white shirt and stands just inside an apartment entrance. She looks at the viewer through the narrow vertical gap of a slightly open door, lightly blushing and out of breath, her mouth slightly open in a sensual daze. The camera is in the outside hallway, framing her between the door and the doorframe, with a glimpse of the tiled genkan behind her.
```

**ネガティブ:**

```
worst quality, low quality, score_1, score_2, score_3, artist name, blurry, jpeg artifacts, chromatic aberration, simple background, nsfw, explicit
```

**設定メモ:** 縦構図が合いやすい(3:4 または 4:5)。サンプラーは `er_sde`、CFG 4〜5、30〜50ステップ。

**状態:** 【未検証】(机上の変換例。実生成での確認後、結果と設定を追記する)
