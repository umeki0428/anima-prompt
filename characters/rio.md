# リオ (rio / tsukatsuki rio)

呼び方: 「リオ」「rio」「調月リオ」「tsukatsuki rio」と指示されたらこのファイルを使う

Danbooru/Gelbooru の本体タグは `rio (blue archive)`。`tsukatsuki rio` はエイリアスなので使わない。作品名は `blue archive`。Gelbooru 表記(スペース区切り)を優先。

## 固定タグ(毎回そのまま使う・順番も維持)

1girl, rio (blue archive), blue archive, very long hair, black hair, blunt bangs, hair behind ear, red eyes, ringed eyes, white pupils, hairclip, millennium science school logo, halo, black halo, large breasts

## 既定の衣装(衣装の指示がなければ使う。別衣装を指示されたら全部削除して置き換える)

white turtleneck sweater, black jacket, id card, black skirt, pleated skirt, black pantyhose, thigh holster, black high heels

## 任意タグ(指示があれば付ける)

- 小物: tablet pc(よく持つ。指示があれば)
- 画風: 指定がなければ付けない。`anime coloring` はユーザーが入れてほしいと言ったときだけ。[anima-rules.md](../references/anima-rules.md) の「入れないタグ」

## 公式衣装差分(指示されたら既定衣装を全部削除して、下の行に置き換える)

キャラタグ `rio (blue archive)` は残す。差分タグは追加する。identity の髪・目・ヘイローはそのまま(武装とドレスだけ髪型タグを足す)。

### 既定(セミナー制服)

white turtleneck sweater, black jacket, id card, black skirt, pleated skirt, black pantyhose, thigh holster, black high heels

### 武装 / 臨戦 (`rio (armed) (blue archive)`)

エイリアス: `rio (battle) (blue archive)` / `rio (bodysuit) (blue archive)`。6th PV・鋼鉄大陸の潜入スーツ。

official alternate costume, official alternate hairstyle, ponytail, black bodysuit, skin tight, headgear, black gloves, thigh holster

### 冬服 (`rio (winter) (blue archive)`)

ゲーム内 NPC 立ち絵。投稿が少なく、コート＋タートルが中心。

official alternate costume, black coat, coat, white turtleneck sweater, turtleneck, black gloves

### クリスマスドレス (`rio (christmas dress) (blue archive)`)

エイリアス: `rio (dress) (blue archive)`。5周年キービジュアル。

official alternate costume, official alternate hairstyle, hair bun, black dress, dress, jewelry, necklace, bare shoulders

## 既定の自然文(漫画の Character ブロック専用)

漫画ページの Character ブロックに**一度だけ**展開する。1枚絵の自然文には貼らない(容姿は固定タグだけで足りる)。

Rio has thigh-length straight black hair with blunt bangs, one side tucked behind her ear and a Millennium logo hairclip. Her red eyes are ringed with white pupils, and a black metallic halo floats above her head.

## 例(プロンプト全文)

| 内容 | ファイル | 状態 |
|---|---|---|
| 下アングル・上着を脱ぎかけ・太もも切り | [rio-jacket-from-below.md](../examples/_templates/rio-jacket-from-below.md) | ユーザー最終稿(2026-08-21)。`sensitive` |
| ベッドで舌キス(ユウジ) | [rio-yuji-bed-kiss.md](../examples/adult/rio-yuji-bed-kiss.md) | ユーザー最終稿(2026-09-04)。`explicit`。別衣装 |
| キス4コマを1コマ1枚(先生) | [kiss-4panel-separate.md](../examples/adult/kiss-4panel-separate.md) | 【未検証】。既定制服の襟元。先生は faceless。`explicit` 等は未指定のため未使用 |
| 室内で押し倒し(先生) | [rio-sensei-genkan-pin.md](../examples/adult/rio-sensei-genkan-pin.md) | POVが頭下・脚上になったのを確認 2026-09-09。顔上・足下稿は未再生成 |
| ベッドでタートルをめくる | [rio-sweater-lift-bed.md](../examples/adult/rio-sweater-lift-bed.md) | 胸中央稿は未再生成。表情は差し替え表 |
| ベッドで胸を揉む（胸フォーカス） | [rio-breast-groping-bed.md](../examples/adult/rio-breast-groping-bed.md) | 【未検証】。露出した胸の上。ロゴなし |
| ベッドで後ろから揉みながらキス | [rio-behind-kiss-groping-bed.md](../examples/adult/rio-behind-kiss-groping-bed.md) | 母乳は milking 文が原因。ロゴなし |
| モノクロ胸フォーカスで掴む | [rio-mono-breast-grab.md](../examples/adult/rio-mono-breast-grab.md) | 【未検証】。前傾・肩上げ・指先でこりこり |
| オフィス机で後ろから揉む | [rio-office-desk-groping.md](../examples/adult/rio-office-desk-groping.md) | 【未検証】。横構図・モノクロ。吹き出しなし |
| 下から後ろセックス | [rio-behind-sex-from-below.md](../examples/adult/rio-behind-sex-from-below.md) | 【未検証】。女性をリオに置換。色黒顔なし男性 |
| 武装 / 臨戦 | [rio-armed.md](../examples/_templates/rio-armed.md) | 【未検証】立ち絵 |
| 冬服 | [rio-winter.md](../examples/_templates/rio-winter.md) | 【未検証】立ち絵 |
| クリスマスドレス | [rio-christmas-dress.md](../examples/_templates/rio-christmas-dress.md) | 【未検証】立ち絵 |

## 注意

- identity はキャラ名+作品名+髪・目・ヘイロー・髪飾り。服装は既定衣装側。別衣装を指示されたら既定衣装だけ差し替える
- 1枚絵の自然文に固定タグの容姿や既定自然文を再掲しない。漫画なら Character ブロックに一度だけ展開し、各 Panel では名前と動作だけ使う
- 公式衣装差分ではキャラタグ `rio (blue archive)` に差分タグを足し、使わない衣装はネガへ(制服とボディスーツ等が混ざる)
- `long hair` と `very long hair` は同義積み増しになるので、太腿丈の `very long hair` のみ使う
- `bright pupils` は `white pupils` と近いので固定には入れない。効きが弱いときだけ足す
- `hair ornament` は `hairclip` の親タグ相当。固定は `hairclip` + `millennium science school logo`
- 既定衣装と別衣装を混在させない(概念ブレンドで崩れる)
- レーティング既定は接頭辞の `safe`。`explicit` / `sensitive` / `nsfw` はユーザーが入れてほしいと言ったときだけ。下アングル最終稿だけ当時の指示で `sensitive`(そのときネガに `sensitive` を入れない)
- 太ももから下が見えない指示なら `black high heels` を外し `cowboy shot`。ネガに `shoes, high heels, feet`
- 下アングル+undressing でスカートが消えるときは `(black skirt:1.8), (pleated skirt:1.8), miniskirt`
- `purple background` はシーン全体を染める。暗い背景は `dark background` + 自然文で charcoal。語彙は [vocab.md](../references/vocab.md)、失敗は [failures.md](../references/failures.md)
- タグ順は 固定タグ → 衣装 → ポーズ/表情 → カメラ → 画風
