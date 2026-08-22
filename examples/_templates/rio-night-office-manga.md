# 例: リオ・深夜のオフィス(漫画1ページ)

**指示(日本語):** リオのプロンプトで、何か1ページの漫画ページを作る。

**組み立てメモ:** 漫画ページは [manga-page.md](../../references/manga-page.md)。画風は `manga style, dynamic panel layout` のみ。Character one は `blue archive, rio \(blue archive\)` と制服。容姿の長文は書かない。各 Panel では同じ名前 `Rio` を使う。コマは上ワイド → 中段左右の縦割り → 下の大ゴマ。

**ポジティブ:**

```
manga style,
dynamic panel layout,

Character one:
blue archive,
rio \(blue archive\),
white turtleneck sweater, black jacket, id card, black skirt, pleated skirt, black pantyhose, thigh holster, black high heels,

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
her eyes catch a faint screen glow,
dramatic shading around her cheeks,

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
dramatic night atmosphere with long shadows.
```

**推奨設定:** 1024×1536 または 768×1152、`er_sde`、CFG 4〜5、30〜50ステップ。

**状態:** 【未検証】(机上の変換例。実生成での確認後、結果と設定を追記する)
