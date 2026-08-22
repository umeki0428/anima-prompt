# 例: リオ・深夜のオフィス(漫画1ページ)

**指示(日本語):** リオのプロンプトで、何か1ページの漫画ページを作る。

**組み立てメモ:** 漫画ページは [manga-page.md](../../references/manga-page.md) の画風 → Character → Panel 文章。`characters/rio.md` があるときは固定タグ・既定衣装・既定自然文を Character one に展開する。各 Panel では同じ名前 `Rio` を使う。コマは上ワイド → 中段左右の縦割り → 下の大ゴマ。

**ポジティブ:**

```
manga style,
black and white manga page,
professional Japanese manga,
clean detailed line art,
high quality screentones,
dynamic panel layout,

Character one:
(Rio), a young Japanese woman,
thigh-length straight black hair,
blunt bangs,
one side of her hair tucked behind her ear,
a Millennium science school logo hairclip,
large almond-shaped red eyes with ringed irises and white pupils,
a black metallic halo floating above her head,
large breasts,
wearing a white turtleneck sweater,
a black jacket with an ID card,
a black pleated skirt,
black pantyhose,
a thigh holster,
and black high heels,

Panel 1:
top full-width panel,
Rio is standing beside the floor-to-ceiling windows of a high-rise office at night,
looking down at the glowing city far below,
wide cinematic shot from slightly behind and to the side,
her expression is calm and distant,
the dark office interior and city lights fill the background,

Panel 2:
middle left vertical panel,
close-up of Rio's face,
she looks down at a tablet in her hands with a slight frown,
her ringed red eyes catch a faint screen glow,
dramatic manga screentones around her cheeks and halo,

Panel 3:
middle right vertical panel,
Rio turns toward the office door while still holding the tablet,
medium shot from the side,
her face is composed but slightly tense,
empty desks and dim overhead lights sit behind her,

Panel 4:
bottom large full-width panel,
Rio walks away down a long empty corridor while looking back over her shoulder,
full-body shot from a low three-quarter angle,
her expression is lonely and unreadable,
dramatic night atmosphere with long shadows and detailed screentones.
```

**推奨設定:** 1024×1536 または 768×1152、`er_sde`、CFG 4〜5、30〜50ステップ。

**状態:** 【未検証】(机上の変換例。実生成での確認後、結果と設定を追記する)
