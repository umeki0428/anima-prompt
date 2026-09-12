# 色・表情・雰囲気でエロさを出す

行為や衣装を増やさず、**光の色・表情・空気(湯気)**でエロさを足すときの参照。簡潔なハイブリッド書式は [anima-rules.md](anima-rules.md)。語彙のタグ化は [vocab.md](vocab.md)。

出典の凡例: 【実生成】= このプロジェクトの生成で確認。【未検証】= 手順として使っているが、再検証待ち。

## 原則

- **タグ=光源・表情の種類、自然文=向き・色・湿度。** 背景・構図・ライティングは自然文が得意([anima-rules.md](anima-rules.md))。
- 一度に足すのは **色1系統 + 湯気か霧のどちらか**。光源を混ぜると色が割れる【未検証】。
- エロの土台は **部屋を暗くして光を1〜2個に減らす**。昼の均一光だと普通のイラストに戻る【未検証】。
- 試す順: **①色付きの dim light → ②湯気 → ③リムライト**。全部同時に足さない。
- 白シャツ／白タートル + `steaming body` は透けやすい。透け禁止なら `steam, haze` だけにする【実生成・2026-08-20】。
- **背景の配色は場面に合わせる。** チャコール固定でも紫回避固定でもない。切り抜きならグリーンバック、夜の密着なら黒紫グラデ、などその場の空気で選ぶ【実生成・2026-09-04】。

## 背景の配色

色面の背景と、人物に当たる光は別物。同じ色を両方に書くと肌まで染まる。

| 欲しいもの | タグ | 色の書き方 |
|---|---|---|
| 色面のグラデ | `simple background, gradient background, dark background` | 色名は自然文(例: `black-to-dark-purple gradient`)。場面ごとに色を変える |
| 切り抜き | `green background` 等 | エロ雰囲気(dim / 湯気 / 色光)とは両立しにくい。切り抜きが目的のときだけ |
| 部屋・風景 | 背景タグ + 自然文 | 指示があるときだけ。ベッドの上だとわかれば部屋は不要 |

色付きグラデで肌を残す手順【実生成・2026-09-04】:

1. タグは `simple background, gradient background, dark background`
2. 色は自然文だけ書く。部屋や家具は書かない
3. 人物の光は背景色と分ける。紫グラデでも肌を染めないなら `warm lighting, rim light`、ネガに `purple lighting`
4. グラデが弱く色が出ないときだけ `purple background` 等の色タグを足す
5. ベッド面だけなら `on bed` + 自然文で rumpled bed surface。ネガに `scenery, indoor, furniture, bedroom, headboard`

グリーンバックは切り抜き用。雰囲気を足したい場面では使わない。

## レーティング

接頭辞の既定は `safe`。`sensitive` / `nsfw` / `explicit` は**ユーザーが入れてほしいと言ったときだけ**付ける。エロい指示でも勝手に `safe` を外したり差し替えたりしない。[anima-rules.md](anima-rules.md) の「入れないタグ」。

ネガに `nsfw, explicit, sensitive` を入れると雰囲気ごと消える。エロ目的でネガへは入れない(ポジへ足すのも指示があるときだけ)。

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
| 暖色 | `warm lighting, orange lighting` | ランプ、肌が寄る。色付き背景と分けるときにも使う |
| 青 | `blue lighting, moonlight` | 冷静、夜窓 |
| 赤 | `red lighting` | 強い。風俗・非常灯になりやすい |
| ミックス | 2色まで | 例: 右が紫、左が弱いピンク |

紫が肌まで染まったときの退避(場面が無彩色でよいとき):

- ポジから `purple lighting` / `purple background` を外す
- 光は `warm lighting, rim light`
- ネガに `purple lighting`
- 背景色がこの場面に必要なら、上の「背景の配色」どおり自然文で書き、照明タグとは重ねない

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

**3. チャコールグラデ + 暖色リム(無彩色の場面)**

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

**5. 黒紫グラデ + 暖色の人物光(夜の密着。部屋は出さない)**

```
dim lighting, warm lighting, rim light, steam, haze, on bed, simple background, gradient background, dark background
```

```
Only a rumpled bed surface is under them; there is no room or furniture. The background is a black-to-dark-purple gradient with nothing else in it. Soft warm light from the upper right, a thin rim on her shoulder, and a faint haze of steam.
```

ネガに `purple lighting, scenery, indoor, furniture, bedroom, headboard`。色が弱いときだけポジに `purple background`。見本は [rio-yuji-bed-kiss.md](../examples/adult/rio-yuji-bed-kiss.md)。

## 構図との干渉(雰囲気以外だが一緒に起きやすい)

- **ローアングルでスカートが消える:** スカートタグに重み(`(black skirt:1.8), (pleated skirt:1.8)`)、自然文で裾が見えると書く。ネガに `skirt removed, no skirt`。`from below` の重みを上げすぎない【実生成・2026-08-21】。
- **パンツライン:** ネガに `panty lines, cameltoe, panties`。自然文で `no panty lines`【実生成・2026-08-21】。
- **下からのライトアップ:** `from below` 構図と `light from below` は相性が良いが、スカートとパンツラインも強調される。
- **服の中の手:** タンクトップの脇・裾から手を入れて胸や乳首を触る構図は、言い回しを変えても Anima 単発では再現できず打ち切り(2026-08-22)。詳細は [failures.md](failures.md)。
- **タイツ越しの指:** 破れたタイツの上からクリトリスを指で触るのは可。服の内側に隠す手とは別【実生成・2026-09-04】。
- **左右の手が別動作:** 片手は胸、もう片手は股、などは自然文で left / right を固定。ネガに `two hands on breasts`【実生成・2026-09-04】。
- **舌キスと faceless:** 顔が見えるキスでは `faceless male` を外し、ネガへ入れる。[yuji.md](../characters/yuji.md)

失敗の詳細は [failures.md](failures.md)。
