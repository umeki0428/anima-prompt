# 例: やまだ・両手を肩の高さで手のひら上(じゃーん)

**指示(日本語):** やまだで添付ポーズを再現。服装は `tayama-altoutfit1`(青ジャケット・黒シャツイン・短パン)。髪は下ろしたストレート。正面向きで太ももから上。肘は胴に近づけ、両前腕を外向きに上げ、手のひらを肩の高さで上向きに開く。頭は向かって左(本人の右)に少し傾け、目は閉じた笑顔、口は大きく開いた喜びのGrin。背景は真っ黒。

**組み立てメモ:** 既定の白シャツ／ドレス／`folded ponytail` は全部削除し、別衣装・別髪型に置き換える。服装キャプションのうちタバコ・喫煙・ポケットの手・`looking at viewer` はじゃーんポーズと衝突するので使わない。髪キャプションの黒レザージャケットは別衣装(`tayamaoutfit`)なので混ぜない。`open clothes` はシャツまで開くので `open jacket` のみ。`long hair` と `medium hair` は重ねず `medium hair`。`ringed eyes` はリオ混入の可能性が高いので付けない。Anima は SDXL LoRA 非互換のため `<lora:...>` と括弧重みの品質タグは入れない。画風は指定どおり `anime coloring`。1枚ソロなので外見はタグだけ。自然文はジャケットが開いていること、シャツがインであること、肘と手の高さ。タグ順は 品質/レーティング → 1girl, solo → トリガー → 髪/目 → 衣装 → ポーズ/表情 → 背景 → カメラ → 画風。

**ポジティブ:**

```
masterpiece, best quality, score_7, safe, 1girl, solo, yamada, bangs, sidelocks, medium hair, straight hair, red hair, red eyes, earrings, black choker, black shirt, shirt tucked in, shorts, belt, blue jacket, open jacket, alternate costume, standing, palms up, open hands, closed eyes, open mouth, :d, head tilt, facing viewer, cowboy shot, simple background, black background, anime coloring

She stands facing the viewer in a cowboy shot from the upper thighs up. The blue jacket hangs open, and the black shirt stays tucked into the shorts. Her elbows stay tucked close to her torso while both forearms lift slightly outward, holding her open palms up at shoulder height with fingers splayed in an excited ta-da greeting. Her head tilts a little to her right, her eyes are closed in happy curves, and her mouth is wide open in a joyful grin. The background is a flat black void, with no feet or shoes in frame.
```

**ネガティブ:**

```
worst quality, low quality, score_1, score_2, score_3, artist name, blurry, jpeg artifacts, chromatic aberration, bad anatomy, extra limbs, bad hands, waving, v, peace sign, arms above head, hand in pocket, cigarette, smoking, folded ponytail, brown hair, white shirt, dress, white skirt, pantyhose, leather jacket, black jacket, shoes, boots, feet, close-up face only, portrait crop, nsfw, explicit, sensitive
```

**推奨設定:** 3:4、`er_sde`、CFG 4〜5、30〜50ステップ。

**状態:** 【未検証】(机上の変換例。実生成での確認後、結果と設定を追記する)
