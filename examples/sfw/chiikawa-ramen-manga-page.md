# 例: ちいかわ×モモンガ・ラーメン屋(漫画1ページ)

**指示(日本語):** manga-page の書き方で、添付したちいかわ風ページを再現。空腹のちいかわとモモンガが赤い暖簾のラーメン屋に入り、二郎系のチャーシュー麺を食べて終わる。

**参考画像:** [chiikawa-ramen-manga-page.jpg](../../references-image/chiikawa-ramen-manga-page.jpg)

**組み立てメモ:** 漫画ページなので通常の3層ではなく [manga-page.md](../../references/manga-page.md) の画風 → Character → Panel 文章。`characters/` に定義がないので Character で容姿を文章定義し、各 Panel では同じ名前 `Chiikawa` / `Momonga` を使う。原画はフルカラー(白・ピンク・赤・黄・薄青)なので `black and white manga page` 等は付けない。`4koma` は使わない。セリフ・吹き出し・擬音は入れず後入れ。コマが多いので潰れたら位置句を厚くするか、1コマ1枚で組む。

**ポジティブ:**

```
manga style,
dynamic panel layout,

Character one:
(Chiikawa), a tiny round white hamster-like mascot,
a large round white head,
small black oval eyes,
light blue inner ears,
a small light blue patch on the forehead,
a small round white body with stubby arms and legs,
no clothes,

Character two:
(Momonga), a tiny round light-pink flying-squirrel mascot,
two short petal-shaped tufts on top of the head,
small black dot eyes,
oval pink blush marks on both cheeks,
a small round pink body with stubby arms and legs,
no clothes,

Panel 1:
small square panel in the top left,
close-up of Momonga filling most of the frame,
Momonga laughs with closed curved eyes and an open mouth,
one stubby hand is raised,
pink blush marks on the cheeks,
plain white background,

Panel 2:
small vertical panel in the top center,
full body of Chiikawa standing in the middle of the panel,
Chiikawa shouts with a wide open mouth and pink blush on the cheeks,
short vertical motion lines beside the body,
plain white background,

Panel 3:
vertical panel in the top right,
only the top of Chiikawa's head peeks in from the bottom of the frame,
Chiikawa looks upward with a weak unwell expression,
wavy dizziness lines along the right edge,
plain white background with a lot of empty space,

Panel 4:
small panel in the upper middle left,
an oval inset of Chiikawa's face in the lower left,
Chiikawa looks puzzled with small black eyes and pink blush,
a fragment of a shop entrance with a bright red noren curtain sits on the right,
plain white background,

Panel 5:
horizontal panel in the upper middle right,
a shop doorway with a bright red noren curtain split into flaps,
each flap has a simple white mountain-shaped mark,
pale blue glass under the curtain,
Chiikawa is seen from behind on the right, a round white body with light blue shading, looking toward the shop,
plain white background,

Panel 6:
large vertical panel on the middle left,
medium close-up of Chiikawa from the chest up,
Chiikawa looks determined and raises one stubby finger,
yellow radial speed lines and a pale blue glow behind the head,
a bright red counter runs along the bottom of the panel,

Panel 7:
horizontal panel on the middle right,
Momonga and Chiikawa sit behind a high bright-red ramen counter,
Momonga is on the left looking curious,
Chiikawa is on the right leaning over the front edge of the counter and looking down,
medium shot from slightly above,
plain white background above the red counter,

Panel 8:
horizontal panel below that on the middle right,
close-up of Chiikawa from the chest up,
Chiikawa looks down to the side with both stubby paws raised near the chest,
light blue inner ears and a light blue patch on the forehead,
plain white background,

Panel 9:
equal-width vertical panel in the bottom right,
Momonga sits at the bright red counter looking up excitedly with an open mouth and blushing cheeks,
small seasoning jars sit on the counter,
a stubby hand holds out a small white ticket,
Chiikawa is partly visible at the edge of the frame,
plain white background above the counter,

Panel 10:
equal-width vertical panel in the bottom center,
close-up of a ramen bowl on a small saucer,
thick noodles in dark broth,
large slices of chashu pork, a mound of minced garlic, a square pat of butter, and sheets of nori,
steam rising from the bowl,
plain white background,

Panel 11:
equal-width vertical panel in the bottom left,
Momonga and Chiikawa sit at the bright red counter hunched over two steaming ramen bowls,
Momonga on the left buries its face in the bowl,
Chiikawa on the right slurps noodles,
two small glasses of water sit on the counter,
a tiny end mark in the bottom-left corner.
```

**後入れ台詞:**

- 腹が減りすぎてちょっと具合が悪いんだよォー
- なんだァココ
- ラーメンだァ〜？
- そりゃもうアッッッのアッッッの腹にたまるうまいもんくれよッ
- お好みございますか
- ハフムシャッと食べるんだからサッ!!
- ふたつとも硬め濃いめ脂めで
- チャーシュー麺 ニンニクどっちゃり バターのせ
- スパッ… 血液が塩味を帯びそうだッ / ハグ…ハグ…

**ネガティブ:**

```
worst quality, low quality, score_1, score_2, score_3, artist name, blurry, jpeg artifacts, chromatic aberration, 4koma, 3koma, 2koma, equal panels, stacked panels, photorealistic, 3d, extra limbs, bad hands, watermark, text, logo
```

**推奨設定:** 1024×1536 または 768×1152、`er_sde`、CFG 4〜5、30〜50ステップ。コマが混ざったら各 Panel 先頭の位置句を `(large vertical panel on the middle left:1.5)` のように上げる。それでも潰れるなら1コマ1枚で生成して後で組む。

**状態:** 【未検証】(机上の変換例。実生成での確認後、結果と設定を追記する)
