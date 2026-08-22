# 例: ゆい×ユウジ・ベッドで指入れ(フルカラー)

**指示(日本語):** ゆいとユウジで添付構図を再現。服装は指定プロンプトから抽出(白タンクトップ＋黒キャミ、腰から下は裸、黒アイマスク)。フルカラー。仰向け、ユウジは指だけ見えて指入れ。暗い背景・弱い光・落ち着いた色。

**組み立てメモ:** 1枚絵なので通常の3層。`characters/yui.md` / `characters/yuji.md` の固定タグはそのまま。指定衣装があるので既定衣装は全部削除(デニム短パンや oversized タンクは混ぜない)。ユウジは指だけなので既定の黒Tシャツは付けない。`faceless male` は維持。レーティングは行為ありなので `explicit`。フルカラー指定のため `anime coloring` を付け、`monochrome` / `greyscale` はネガへ。アームホールからキャミが見える位置関係と「指だけ」は自然文。`two fingers` はジェスチャーに寄るのでタグにせず自然文。服の内側の手は対象外(今回は腰下の指入れ)。

**ポジティブ:**

```
masterpiece, best quality, score_7, explicit, newest,

1girl, yui, medium-large breasts, brown hair, brown eyes, ponytail, (blindfold:1.3), black blindfold, covered eyes, white tank top, sleeveless, bare arms, bare shoulders, wide armholes, black camisole, black strap visible, bottomless, lying, on back, on bed, spread legs, navel, pussy, pussy juice, blush,
1boy, yuji, faceless male, black hair, short hair, bangs, hair over eyes, male hand, fingering,
dim lighting, dark background, muted colors, from above, full body, anime coloring

Yui, a girl with a brown ponytail, brown eyes, and medium-large breasts, lies on her back on rumpled white sheets, a black blindfold covering her eyes. She wears a white sleeveless tank top with armholes cut wide and low, open down the sides of her chest; a black camisole underneath shows its strap on her shoulder and its fabric through the wide armhole, while from the waist down she is nude, legs spread, pussy wet with juice. Yuji, a faceless young Japanese man in his twenties with short black hair and bangs hiding his eyes, is not shown except for two fingers roughly fingering her. The room stays dark, with dim muted light and a dark background.
```

**ネガティブ:**

```
worst quality, low quality, score_1, score_2, score_3, artist name, blurry, jpeg artifacts, chromatic aberration, bad anatomy, extra limbs, bad hands, extra fingers, photorealistic, 3d, cgi, monochrome, greyscale, shorts, pants, panties, watermark, signature, text, logo
```

**設定メモ:** 横長 `1536×1024` または `1152×768`。サンプラー `er_sde`、CFG 4〜5、30〜50ステップ。短パンが残るならネガの `shorts, pants` を確認。ユウジの体が出るなら自然文の "not shown except for two fingers" を維持し seed を回す。アイマスクが外れるなら `(blindfold:1.5)` まで上げる。

**状態:** 【未検証】(机上の変換例。実生成での確認後、結果と設定を追記する)
