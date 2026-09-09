# 失敗事例集(外れた出力 → 原因 → 直し方)

実生成で意図と違う出力になった事例をここに蓄積する。同じ失敗を繰り返さないための一次資料。

記入フォーマット:

```
## <短いタイトル> (YYYY-MM-DD)

- **指示(日本語)**: 何を作ろうとしたか
- **使ったプロンプト**: (ポジ/ネガ、設定も変えていれば記載)
- **外れた出力**: どうなったか
- **原因(推定)**: なぜそうなったか
- **直し方**: 効いた修正。確定なら vocab.md / anima-rules.md / styles.md にも反映し、ここからリンクする
```

---

## `4koma` で均等な縦積みになる (2026-08-21)

- **指示(日本語)**: Anima でフルカラーの漫画ページ。コマは大きさ・配置を変えて物語を進める(脱ぐ → 押し倒す → 耳にかける → 口淫)
- **使ったプロンプト**: タグに `comic, 4koma, colored, border`。自然文は `A full-color manga page with four stacked panels` で上から順に4シーンを列挙
- **外れた出力**: 同じ大きさのコマが上から下へ単調に4段並ぶ(いわゆる4コマ漫画)
- **原因(推定)**: Danbooru の `4koma` は均等サイズの縦積み(または2×2)を指す。自然文の `four stacked panels` も同じ意味を補強した。不揃いの漫画ページ(ワイド+縦割り+スプラッシュ)とは別概念
- **直し方**: ポジから `4koma` を外す。ネガに `4koma, 2koma, 3koma` を入れる。枚数の縦積みは書かず、各 Panel の先頭で位置と大きさを文章指定する。書式は [manga-page.md](manga-page.md)。語彙は [vocab.md](vocab.md) の構図節

## 紫照明で画面が紫に染まる (2026-08-21)

- **指示(日本語)**: ローアングルの脱ぎかけ。色と湯気でエロくしたい。背景は紫グラデでもよい
- **使ったプロンプト**: ポジに `purple lighting, purple background, dim lighting, rim light, steam`
- **外れた出力**: 肌・服・背景まで全体が紫に寄る
- **原因(推定)**: `purple lighting` と `purple background` が重なり、主光まで紫になる
- **直し方**: `purple lighting` と `purple background` を同時に使わない。背景色は場面で選ぶ。無彩色でよいなら `dark background` + 暖色光。紫グラデが欲しいなら色は自然文、人物光は `warm lighting`、ネガに `purple lighting`。手順は [atmosphere.md](atmosphere.md)

## steaming body で服が透ける (2026-08-20)

- **指示(日本語)**: 汗で服が湿っているが、透けさせない
- **使ったプロンプト**: ポジに `sweat, steaming body, steam`。白シャツまたは白タートル
- **外れた出力**: 服が半透明になり、下着や体の線が見える
- **原因(推定)**: `steaming body` と白衣が濡れ透けに解釈される
- **直し方**: `steaming body` を外し `steam, haze` だけにする。自然文で `clothes stay opaque`。ネガに `see-through, see-through shirt, wet clothes`。[atmosphere.md](atmosphere.md)

## ローアングルでスカートが消える (2026-08-21)

- **指示(日本語)**: 下からのカウボーイショット。スカートは残す
- **使ったプロンプト**: `from below, cowboy shot, black skirt, pleated skirt, black pantyhose`
- **外れた出力**: スカートがなくなり、タイツだけの下半身になる
- **原因(推定)**: ローアングルが裾をフレーム外にし、タイツがボトムとして優先される
- **直し方**: `(black skirt:1.8), (pleated skirt:1.8)`。自然文で裾が見えると書く。ネガに `skirt removed, no skirt`。`from below` の重みは上げすぎない

## パンツラインが出る (2026-08-21)

- **指示(日本語)**: タイツは残すが、パンツのラインは不要
- **使ったプロンプト**: `black pantyhose` + ローアングル。ネガにライン指定なし
- **外れた出力**: スカート／タイツ越しにパンツラインが見える
- **原因(推定)**: 下からの光とタイツが輪郭を強調する
- **直し方**: ネガに `panty lines, cameltoe, panties`。自然文で `no panty lines`。[vocab.md](vocab.md) の照明節

## 服の中の手が生地の外に出る (2026-08-21)

- **指示(日本語)**: 背後の男性がタンクトップの中に手を入れて胸を揉む。手は生地の下
- **使ったプロンプト**: タグに `1boy, groping, breast grab, hands in clothes, oversized clothes`。自然文に `massaging her breasts` / `palms on her breasts` / `wrists show at the side openings`。カメラ `three-quarter view, cowboy shot`
- **外れた出力**: 男性の手がタンクトップの外側に乗り、服の上から揉む構図になる
- **原因(推定)**:
  1. `groping` / `breast grab` / 「胸を揉む」は学習上ほぼ服の上。`hands in clothes` も外手データが多い
  2. `1boy` + 背後 + 腕は「後ろから服の上で抱える」定番に寄る
  3. 胸の正面(`three-quarter` + `cowboy shot`)だと手が胸の手前レイヤーに合成される
  4. `oversized` とアームホール強調は、隙間から指が見えて外側に見える
  5. 手・胸・服を別物として書くとブレンドで手が一番前に来る
- **直し方**: 言い回しでは直らない。`groping` / `breast grab` / `hands in clothes` は使わない。この系統は 2026-08-22 に打ち切り。後続の「縛りすぎて崩壊」「裾から単発も失敗」を見よ

## 服の中の手を縛りすぎて構図が崩壊する (2026-08-21)

- **指示(日本語)**: 同上。手が外に出るのを止める
- **使ったプロンプト**: `from side`、自然文で no fingers / vanish into armholes / hand-shaped bulges。ネガに `groping, breast grab, hands on breasts`
- **外れた出力**: 人物も服も読めない、わけのわからない画像
- **原因(推定)**: 手を描くなと胸を揉んでいるを同時に要求し、男性を隠した。Animaは矛盾する空間指示で破綻しやすい
- **直し方**: `hug from behind` で背後の男性を明示。男性は短い茶髪など、相手と混ぜない外見。カメラは正面寄り。手の指示は1文。**裾から入れる単発も失敗し、この系統は打ち切り**(2026-08-22)。Anima単発では再現しない。言い回しを変えて再挑戦しない。必要な場合のみ、女性単独を出してから腕を inpaint する

## タンクトップ裾から手を入れる単発も失敗 (2026-08-22)

- **指示(日本語)**: 女の子座り、背後の男性がタンクトップの裾をたくし上げて中から乳首を触る
- **使ったプロンプト**: `hug from behind` + 自然文 `He pulls the hem of her tank top upward and slides both hands in from the bottom`
- **外れた出力**: 意図どおりにならない(服の上、破綻、または別構図)。ユーザーがこの系統を打ち切り
- **原因(推定)**: 「不透明な服の内側の手」と「乳首愛撫が見える」は同時に描きにくい。`hug from behind` は2人の配置には効くが、手を生地の下へは送らない
- **直し方**: 単発プロンプトでは扱わない。記録のみ。[vocab.md](vocab.md) の「服の中の手」

## 紫グラデがシーン全体を染める (2026-08-21)

- **指示(日本語)**: リオの下アングル。背景は紫のグラデーション
- **使ったプロンプト**: ポジに `simple background, gradient background, purple background`
- **外れた出力**: 背景だけでなく照明・肌まで紫に寄る
- **原因(推定)**: `purple background` がライティングとブレンドされる。Anima は異なる概念を混ぜやすい
- **直し方**: 肌まで染めたくないなら `purple background` を照明と同時に使わない。背景色は場面で選ぶ。チャコールが欲しいなら `dark background` + 自然文で charcoal。黒紫グラデが欲しいならタグは `simple background, gradient background, dark background`、色は自然文、人物光は `warm lighting`、ネガに `purple lighting`。色が弱いときだけ `purple background` を足す。[atmosphere.md](atmosphere.md) / [vocab.md](vocab.md)

## white shirt がTシャツになる (2026-08-21)

- **指示(日本語)**: 山田が白いシャツ(ボタン付き)を着て、マンション玄関の扉隙間から見える
- **使ったプロンプト**: ポジに `white shirt`。ネガに `t-shirt` なし
- **外れた出力**: 白シャツがTシャツになった
- **原因(推定)**: `white shirt` 単体はTシャツにもブレンドされやすい
- **直し方**: ポジに `collared shirt` を併記し、ネガに `t-shirt` を入れる。自然文は `button-up collared shirt` と書く。`open shirt` は全開になりやすいので使わない。語彙は [vocab.md](vocab.md) の衣装節

## カーディガンの肩落ちが効かず普通に着てしまう (2026-09-01)

- **指示(日本語)**: オーバーサイズのカーディガンを前を開けたまま両肩から落とし、二の腕に引っかける(脱ぎはしない)
- **使ったプロンプト**: ポジに `grey cardigan, open cardigan, off shoulder, bare shoulders, sleeves past wrists`。自然文で `worn open and pulled down off both shoulders, hanging around her upper arms with her hands still through the long sleeves`。ネガに `undressing, unworn cardigan`
- **外れた出力**: 前は開いているが、肩に普通に羽織っただけ。肩・鎖骨は襟に隠れて出ない
- **原因(推定)**: `off shoulder` は「オフショルダー設計の服」に強く紐づき、羽織りを下げる動作にはならない。下にシャツを着ていると `bare shoulders` の行き先がなくなる
- **直し方**: 肩を見せたいなら**服自体をオフショルダー設計にする**(`off-shoulder shirt` 等)のが確実。羽織りを落とす方向なら `(off shoulder:1.6)` + `jacket on shoulders` を併記し、自然文でも「素肌の肩と鎖骨が見える」と結果を書く。両肩より**片肩だけ**の方が通りやすい

## half-closed eyes が閉眼になる (2026-09-01)

- **指示(日本語)**: 半開きの目でニヤついた表情
- **使ったプロンプト**: `half-closed eyes, grin, fang, blush`
- **外れた出力**: 目が完全に閉じた笑顔(>_< 系)になり、瞳が見えない
- **原因(推定)**: `grin` / `fang` の笑顔と `half-closed eyes` が合成され、閉眼笑いの定番に寄る
- **直し方**: ネガに `closed eyes` を必ず入れる。自然文で `her pink eyes stay open and visible` と書く。それでも閉じるなら `(half-closed eyes:1.3)` か `narrowed eyes` に置換

## `front view` でも上から見下ろす構図になる (2026-09-03)

- **指示(日本語)**: 白背景で、人物を真正面から全身表示する
- **使ったプロンプト**: ポジに `front view, full body, symmetrical, centered`。自然文に `Perfectly front-facing`。実際のネガティブは品質・実写・背景抑制だけで、カメラ角度の否定は未投入
- **外れた出力**: 身体は正面を向いたが、カメラが頭上にあり、頭と胸が大きく足が小さい見下ろし構図になった
- **原因(推定)**: `front view` は人物の向きを指定するが、カメラの仰俯角は固定しない。縦長キャンバスの全身構図で遠近感が強まり、見下ろしへ寄った
- **直し方**: ポジに `upright posture` を足し、自然文で `The camera is level and directly in front of her, with no upward or downward tilt and minimal perspective distortion.` と明示する。ネガに `from above, high-angle view, overhead view, bird's-eye view, looking up, leaning forward, foreshortening` を実際に投入する。修正後の効果は【未検証】

## 舌キスなのに顔が出ない (2026-09-04)

- **指示(日本語)**: リオとユウジの舌キス。顔が見える
- **使ったプロンプト**: ユウジ側に既定の `faceless male` が残っている
- **外れた出力**: 男性の顔が潰れる、または舌キスにならない
- **原因(推定)**: `faceless male` は顔を描かない指定。舌キスと矛盾する
- **直し方**: 顔が必要な指示では `faceless male` を外し、ネガへ入れる。[yuji.md](../characters/yuji.md)

## 指のはずがディルド／両手とも胸 (2026-09-04)

- **指示(日本語)**: 膝の上で舌キス。片手は胸、もう片手の指先でタイツ越しにクリトリス。ディルドなし
- **使ったプロンプト**: 玩具や挿入を書かないつもりでも、股間の膨らみや両手胸に寄る
- **外れた出力**: ディルド、双方の胸を両手で掴む、挿入に読まれる
- **原因(推定)**: 股間の接触は玩具・挿入の定番に寄る。両手は両方とも胸にブレンドされやすい
- **直し方**: 自然文で left / right を固定し `index fingertip` と書く。ネガに `dildo, sex toy, vibrator, strap-on, object insertion, penis, two hands on breasts`。破れたタイツの上から触るのは可(服の中の手とは別)。見本は [rio-yuji-bed-kiss.md](../examples/adult/rio-yuji-bed-kiss.md)

## グリーンバックとエロ雰囲気を同時に取る (2026-09-04)

- **指示(日本語)**: 切り抜き用のグリーンバックのまま、暗い部屋の色気も出す
- **外れた出力**: クロマキーになって雰囲気が出ない、または色面が消える
- **原因(推定)**: `green background` は切り抜き用。dim / 湯気 / 色グラデとは目的が違う
- **直し方**: 切り抜きが目的ならグリーンバックだけ。雰囲気が目的なら場面に合った色面グラデにする。部屋が不要ならベッド面だけ残す。[atmosphere.md](atmosphere.md)

## 画像→変換で指示にない背景タグが混入する (2026-09-07)

- **指示(日本語)**: 漫画コマから変換した【構図指示】。「奥層=室内の壁、額装の絵、全層シャープ」
- **使ったプロンプト**: スキルが `Beige to light gray gradient background, simple background, gradient background, blurry background` と `indoors, framed picture on the wall` を同居させて出力
- **外れた出力**: 生成前に発見。矛盾するため背景がブレンドし、額や壁が消えるか灰グラデ化する
- **原因(推定)**: 過去例(リオ下アングルの `simple background, gradient background`)の癖が、指示にない場面にも持ち込まれた
- **直し方**: 指示に無い背景タグは足さない。[anima-rules.md](anima-rules.md) 自然文のルールに追記

## 3層を無視して全文自然文で出力 (2026-09-07)

- **指示(日本語)**: 同上
- **使ったプロンプト**: タグ行なし、すべて自然文
- **外れた出力**: 生成はできたが、`sweatdrop`, `facing another`, `half-lidded eyes` などタグで確定すべき語彙が自然文任せになった
- **原因(推定)**: 【構図指示】が文章形式なので、スキルがそのまま英訳した
- **直し方**: SKILL.md の3層は必須。自然文形式の入力でもタグ行を先に立てる。[anima-rules.md](anima-rules.md) に追記

## 向き合う2人が正面向き(並列)に化ける (2026-09-07)

- **指示(日本語)**: 男性の背中越しに、困っている女性を見る
- **使ったプロンプト**: 自然文 `She looks at him` / `body facing slightly left`。タグは `1girl, 1boy` のみ
- **外れた出力**: 女性の体と視線がカメラに向き、男性と並列に立つ正面構図
- **原因(推定)**: 「彼を見ている」が生成時に `looking at viewer` に均された。学習データの正面・中央の引力に自然文の弱い指定が負けた
- **直し方**: タグ `facing another, eye contact, talking` で関係を固定し、ネガに `looking at viewer`。カメラは撮影用語の自然文。検証済み → [composition.md](composition.md)、最終稿 [counter-ots-cinematic.md](../examples/sfw/counter-ots-cinematic.md)

## 押し倒しが2人のリオになる (2026-09-09)

- **指示(日本語)**: 夜の玄関。頭側の床から、男性がリオを押し倒しているところを見る
- **使ったプロンプト**: リオの固定タグ＋既定制服が先、`1boy, sensei..., faceless male` が後ろ。`from below, lying, on back`。ネガに `2girls` なし
- **外れた出力**: 上に乗っているのもリオ(スカート・タイツ・ヒールの下アングル)。床の人物もリオでカメラ目線。昼の玄関に家具と植木
- **原因(推定)**: `from below` + リオ既定制服が「下から見た立ちリオ」の定番に引かれ、1boy がもう1人の女になった。長髪ハロ持ちを先に書くと混ざる。[vocab.md](vocab.md) の「2人の外見が混ざる」
- **直し方**: 先頭で `1girl, 1boy`。`faceless male, long bangs` をリオの容姿より前に。ネガに `2girls, straddling, upskirt, looking at viewer, furniture, plant`。自然文で one man and one woman / 股の間から見上げない / 夜の玄関に扉だけで家具なし。見本は [rio-sensei-genkan-pin.md](../examples/adult/rio-sensei-genkan-pin.md)

## 押し倒しが股下アオリ＋脚上げ逆さになる (2026-09-09)

- **指示(日本語)**: 頭側の床から、男性がリオの上に覆いかぶさって押し倒しているところを見る
- **使ったプロンプト**: 修正稿。`from below` + 自然文 `Low angle` + `not from between anyone's legs`
- **外れた出力**: 男性が脚を開いて立つ。カメラが股の間。リオは頭が下で脚が天井方向に伸び、押し倒しになっていない
- **原因(推定)**: Danbooru の `from below` は「立っている人を下から見る」。頭側床カメラとは別物。否定の自然文より定番構図が強い
- **直し方**: ポジから `from below` を外しネガへ。男性は立つタグを使わず、同じ向きで上に寝て覆いかぶさる。脚は床に沿って扉へ(宙に上げない)。カメラは自然文だけ `ground-level at their heads, looking along the floor toward the closed door`。ネガに `from below, between legs, legs up, standing, spread legs, upside-down, open door`。見本は [rio-sensei-genkan-pin.md](../examples/adult/rio-sensei-genkan-pin.md)

## 仰向け開脚で腰と尻が床から浮く (2026-09-09)

- **指示(日本語)**: 股を開いて男性の胴が太腿の間。尻は床につける。女性は横を向く
- **使ったプロンプト**: 1回目 `spread legs, pleated skirt, on floor` + 自然文 hips flush / no gap / not M-shape。ネガ `m legs, arched back`
- **外れた出力**: 膝が立ったM字。スカートが腰で広がり、尻と床の間に隙間。1回目の直し後も再発
- **原因(推定)**: `spread legs` + `pleated skirt` が膝立て開脚の定番。ポジ自然文の否定形(`no gap`, `not M-shape`)が浮きを呼ぶ。[anima-rules.md](anima-rules.md) の否定形禁止
- **直し方(失敗)**: `spread legs` と `pleated skirt` を外し `(on floor:1.8)` + hips rest on the floor。次項で崩壊

## 押し倒しが真上俯瞰で上下逆さ・腰が外れる (2026-09-09)

- **指示(日本語)**: 頭側床カメラ。尻は床。女性は横を向く
- **使ったプロンプト**: `(on floor:1.8)`、`spread legs` なし。自然文 hips rest on the floor / thighs lie open on the floor。`looking to the side`
- **外れた出力**: 真上から見た床。男性が仰向けで下、女性が上。胴は正面、腰だけ別角度で途切れる。スカートが短いレザーに化ける
- **原因(推定)**: 頭側カメラでは腰と床の接地を正面に描けない。接地を強制すると俯瞰か骨盤ねじれになる。`on back` が二人に付き、男性が下になる。`on floor` の重みが床俯瞰を勝たせる
- **直し方(失敗)**: 頭側カメラに戻しても、男性の胴で腰が切れ脚が肩の後ろに回る。次項でPOVへ切替

## 頭側床カメラの押し倒しで脚が肩の後ろに浮く (2026-09-09)

- **指示(日本語)**: 頭側の床から男性が覆いかぶさる。腰は切らない。のち男性POVへ変更
- **使ったプロンプト**: `1girl, 1boy` + `spread legs, pinned down, leaning forward`。自然文 ground-level at her head / he is on top / legs extend along the floor
- **外れた出力**: 頭は下手前で当たるが、脚が男性の肩の後ろに現れ腰が途切れて浮く
- **原因(推定)**: 頭側カメラでは男性の胴が女性の腰と同じ奥行きに重なる。脚は肩の向こう側に回され、床から浮いて見える。言い換えでは解けない
- **直し方(失敗)**: 自然文で sleeves at the bottom of the frame としたため、頭が下・脚が上のまま。次項

## 男性POVが頭下・脚上の逆さになる (2026-09-09)

- **指示(日本語)**: 男性目線のPOV。顔を見下ろす
- **使ったプロンプト**: `pov, from above`。自然文 white shirt sleeves at the bottom of the frame / legs open toward the bottom。ネガに `looking at viewer`
- **外れた出力**: 頭が画面下、脚が画面上。手元は下端。腰は床から浮いて見える
- **原因(推定)**: 手は頭の横なので、袖を画面下に置くと頭も下になる。頭側カメラの奥行きが残る。POVの視線をネガにしていた
- **直し方**: 頭は画面の上、足は下。袖と手は画面の上前景。`looking at viewer`。ネガに `upside-down, inverted, looking to the side, from below`。見本は [rio-sensei-genkan-pin.md](../examples/adult/rio-sensei-genkan-pin.md)

## タートルめくりが首で止まる (2026-09-09)

- **指示(日本語)**: 服を手首まで全部持ち上げる。ブラなし。胸はすこし垂れて揺れる
- **使ったプロンプト**: `white turtleneck sweater, undressing, clothes lift, sweater lift`。自然文 bunched around her arms and partially covering her face / pink bra fully visible
- **外れた出力**: セーターが首元に残る。ブラが見える
- **原因(推定)**: `white turtleneck sweater` は着衣の襟を首に描く。顔に布がかかる指定も襟を首へ戻す
- **直し方(失敗)**: リフト重みでも `clothes lift` が裾上げになり、胴にタートル／タンクトップが残った。次項

## タートルめくりが着衣の裾上げになる (2026-09-09)

- **指示(日本語)**: 服を胴から外す。スクールロゴは付けない
- **使ったプロンプト**: `white turtleneck sweater, (clothes lift:1.8), (sweater lift:1.8), millennium science school logo`
- **外れた出力**: 手首にセーター、胴は白いタートルタンクトップ。胸にミレニアム風ロゴと文字
- **原因(推定)**: Danbooru の `clothes lift` は裾を上げて着衣のままへそを出す。着衣タグとスクールロゴが服のプリントになる
- **直し方**: `clothes lift` / `sweater lift` / `white turtleneck sweater` / `millennium science school logo` を外す。`undressing, removing sweater, unworn sweater, topless`。ネガ `turtleneck, tank top, crop top, logo, print`。見本は [rio-sweater-lift-bed.md](../examples/adult/rio-sweater-lift-bed.md)
