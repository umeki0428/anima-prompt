# 色・表情・雰囲気でエロさを出す

行為や衣装を増やさず、**光の色・表情・空気(湯気)**でエロさを足すときの参照。書式の3層は [anima-rules.md](anima-rules.md)。語彙のタグ化は [vocab.md](vocab.md)。

出典の凡例: 【実生成】= このプロジェクトの生成で確認。【未検証】= 手順として使っているが、再検証待ち。

## 原則

- **タグ=光源・表情の種類、自然文=向き・色・湿度。** 背景・構図・ライティングは自然文が得意([anima-rules.md](anima-rules.md))。
- 一度に足すのは **色1系統 + 湯気か霧のどちらか**。光源を混ぜると色が割れる【未検証】。
- エロの土台は **部屋を暗くして光を1〜2個に減らす**。昼の均一光だと普通のイラストに戻る【未検証】。
- 試す順: **①色付きの dim light → ②湯気 → ③リムライト**。全部同時に足さない。
- 白シャツ／白タートル + `steaming body` は透けやすい。透け禁止なら `steam, haze` だけにする【実生成・2026-08-20】。

## レーティング

雰囲気だけで行為なしなら `safe` を外して **`sensitive`**。行為があるなら `nsfw` / `explicit`。`safe` のままだとエロ寄りの光と表情が弱まる。

ネガに `nsfw, explicit, sensitive` を入れると雰囲気ごと消える。エロ目的では入れない。

## 光の方向(自然文が本命)

| 日本語 | 自然文の例 | 印象 |
|---|---|---|
| 斜め前 | `soft light from the upper right` | 汎用。構図のカメラと揃えると安定 |
| 横 | `side light from the right` | 顔と胸の起伏 |
| 逆光 | タグ `backlight` + `rim light` | 輪郭だけ光る。色気が出やすい |
| 下から | `light from below` | ローアングルと相性。やりすぎ注意 |
| 一点 | `a single lamp beside the bed` | ホテル／夜部屋 |
| 窓 | `moonlight through a window` | 夜の室内 |

カメラが右上俯瞰なら、**主光も右上**か、**逆側のリムだけ**の二択。両方強く書くと光源が分裂する。

## 光の質

| 欲しい感じ | タグ | メモ |
|---|---|---|
| 夜の部屋 | `dim lighting` | エロの土台 |
| 柔らかい | `soft lighting` | 肌がきれい。甘め |
| 硬い | `dramatic lighting` | コントラスト。大人っぽい |
| 映画風 | `cinematic lighting` | 色指定と併用しすぎない |
| 空気を光らせる | `volumetric lighting` | 湯気・霧とセット |

## 光の色

タグか自然文の**片方で十分**。主光を白く書くと色が消える。**主光は色付き、リムは1色だけ。**

| 色 | タグ例 | 雰囲気 |
|---|---|---|
| 紫 | `purple lighting` | ネオン、夜。効きが強く画面全体が紫に染まりやすい【実生成・2026-08-21】 |
| マゼンタ／ピンク | `pink lighting, magenta lighting` | 媚びた夜、ホテル |
| 暖色 | `warm lighting, orange lighting` | ランプ、肌が寄る。紫の代替に使いやすい |
| 青 | `blue lighting, moonlight` | 冷静、夜窓 |
| 赤 | `red lighting` | 強い。風俗・非常灯になりやすい |
| ミックス | 2色まで | 例: 右が紫、左が弱いピンク |

紫が強すぎるときの退避:

- ポジから `purple lighting` / `purple background` を外す
- 背景は `dark background` の無彩色グラデ
- 光は `warm lighting, rim light` か、リムの自然文だけ
- ネガに `purple, purple lighting, purple background`

## 湯気・空気

光の色とは別レイヤー。湯気を強くすると濡れ透けに寄る。

| 欲しいもの | タグ | 注意 |
|---|---|---|
| 部屋の霧 | `steam, haze` | 背景のもや。透けより安全 |
| 肌から湯気 | `steaming body` | 熱さは出るが服が透ける【実生成・2026-08-20】 |
| 光の筋 | `volumetric lighting, light particles` | 夜部屋と相性良い |
| 煙 | `smoke` | タバコ／舞台になりやすい |

透け禁止の自然文例:

```
A faint haze of steam hangs in the dim room, catching the light without making her clothes see-through.
```

ネガ(透け抑制):

```
see-through, see-through shirt, see-through clothes, wet clothes, wet shirt, translucent
```

## 表情

行為なしでエロく見せるときの核。あへがおは指示があるときだけ。

| 日本語 | 使うタグ | メモ |
|---|---|---|
| とろけ顔 | `half-closed eyes, open mouth, blush` | 自然文で `melted, dazed` を足す |
| 息が荒い | `heavy breathing` | 口を開けたままになりやすい |
| 赤面 | `blush` | `heavy blush` は自然文 |
| 汗 | `sweat` | 肌側。服を濡らす指定は透けに繋がる |
| こっちを見る | `looking at viewer` | ローアングルなら `looking down` も併用 |
| ハート演出 | `heart` | ハート瞳・画面のハート増殖が起きやすい。不要なら外す |

自然文例:

```
Her expression is melted and dazed: half-lidded eyes, a loosely open mouth, heavy breathing, and a heavy blush. Sweat beads on her face and collarbone.
```

あへがおを避けるネガ: `ahegao, tongue out`

## 貼り付けセット

キャラ・衣装・ポーズのタグのあとに足す。画風タグの直前が扱いやすい。

**1. 紫の夜部屋(効きが強い。染め注意)**

```
dim lighting, purple lighting, rim light, steam, haze, volumetric lighting
```

```
Dim purple light falls from the upper right, with a thin magenta rim along her shoulder and collarbone. A faint haze of steam hangs in the air and catches the light, keeping the room humid and erotic, while her clothes stay opaque.
```

**2. ピンク／マゼンタ(ホテル寄り)**

```
dim lighting, pink lighting, magenta lighting, rim light, steam, haze
```

```
Soft pink-magenta light falls from the upper right. Steam drifts through the dim air and catches the light on her skin, without making her clothes see-through.
```

**3. 無彩色背景 + 暖色リム(紫を避けたいとき)**

```
dim lighting, warm lighting, rim light, steam, haze, volumetric lighting, dark background, simple background, gradient background
```

```
The background is a dark charcoal gradient, not purple. Soft warm light from below and behind puts a thin rim along her body. A faint haze of steam hangs in the air. Clothes stay opaque.
```

**4. ホテルのランプ**

```
dim lighting, warm lighting, lamp
```

```
A single warm lamp beside the bed lights her from the side. The rest of the room stays dark, with a thin haze in the air.
```

## 構図との干渉(雰囲気以外だが一緒に起きやすい)

- **ローアングルでスカートが消える:** スカートタグに重み(`(black skirt:1.8), (pleated skirt:1.8)`)、自然文で裾が見えると書く。ネガに `skirt removed, no skirt`。`from below` の重みを上げすぎない【実生成・2026-08-21】。
- **パンツライン:** ネガに `panty lines, cameltoe, panties`。自然文で `no panty lines`【実生成・2026-08-21】。
- **下からのライトアップ:** `from below` 構図と `light from below` は相性が良いが、スカートとパンツラインも強調される。

失敗の詳細は [failures.md](failures.md)。
