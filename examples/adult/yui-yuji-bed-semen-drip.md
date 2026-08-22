# 例: ゆい×ユウジ・ベッドで精液を垂らす1コマ(モノクロ漫画)

**指示(日本語):** ゆいとユウジで添付のモノクロ漫画コマを再現。ゆいは全裸でベッドに仰向け、脚を大きく開いたM字。ユウジは顔なしで右手と足元だけ見え、指から白い粘液をゆいの股間へ垂らしている。高コントラストの白黒漫画。

**組み立てメモ:** 1枚絵なので通常の3層。漫画ページ書式は使わない。`characters/yui.md` / `characters/yuji.md` の固定タグはそのまま。画像は全裸なので既定衣装は削除して `nude` に置き換える(混在させない)。元絵の蝶ヘアアクセはゆいの固定容姿ではないので付けない。ユウジは `faceless male` のまま、手と脚先だけ。レーティングは行為ありなので `explicit`(`safe` は外す)。画風はモノクロ漫画なので `anime coloring` は外し `monochrome, greyscale, manga`。吹き出しの長い台詞は後入れ(文字は1〜2単語まで)。

**ポジティブ:**

```
masterpiece, best quality, score_7, explicit, newest,

1girl, yui, medium-large breasts, brown hair, brown eyes, ponytail, nude, lying, on back, on bed, pillow, spread legs, navel, pussy, blush, sweat, half-closed eyes, open mouth, teary eyes,
1boy, yuji, faceless male, black hair, short hair, bangs, hair over eyes, male hand,
semen, dripping, after sex, pussy juice, bed, from above, full body, monochrome, greyscale, manga, high contrast, screentones

Yui, a girl with a brown ponytail, brown eyes, and medium-large breasts, lies naked on her back across a rumpled bed, head on a pillow, one hand near her head, legs spread wide, her body angled toward the viewer. Her half-lidded eyes are teary, her cheeks heavily blushed, her mouth slightly open, sweat beading on glistening skin. Yuji, a faceless young Japanese man in his twenties with short black hair and bangs hiding his eyes, appears only as a right hand hovering over her lower abdomen and a glimpse of his lower leg; a thick white string of semen stretches from his fingers down onto her wet pussy. High-contrast black-and-white manga lighting, deep shadows and stark highlights, simple bedroom background.
```

**ネガティブ:**

```
worst quality, low quality, score_1, score_2, score_3, artist name, blurry, jpeg artifacts, chromatic aberration, bad anatomy, extra limbs, bad hands, extra fingers, photorealistic, 3d, cgi, colored, anime coloring, clothes, clothed, panties, watermark, signature, text, logo
```

**設定メモ:** 横長 `1536×1024` または `1152×768`(体が横に伸びる構図)。サンプラー `er_sde`、CFG 4〜5、30〜50ステップ。色が乗ったらネガの `colored, anime coloring` を維持し、ポジの `monochrome, greyscale` に `(monochrome:1.5)` を足す。服が残るならネガの `clothes, clothed` を確認。手と精液の糸が崩れたら seed を回す。

**状態:** 【未検証】(机上の変換例。実生成での確認後、結果と設定を追記する)
