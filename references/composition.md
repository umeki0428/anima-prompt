# 構図・カメラの制御(検証結果と使い分け)

漫画的な構図(オーバーショルダー、アオリ、遮蔽、ボケ)を Anima で出すための知見。語彙表は [vocab.md](vocab.md) の構図節、失敗は [failures.md](failures.md)。

## 結論(2026-09-07 実生成)

**撮影用語の自然文は Danbooru タグより強く効く。ただしカメラ高さだけはタグ必須。**

| 要素 | 効く書き方 | 備考 |
|---|---|---|
| オーバーショルダー(手前に相手の背中・肩) | 自然文 `Over-the-shoulder shot from behind the man` | タグ `from behind` 単体は「男性の横顔で並列」にしかならない |
| 手前ボケ・被写界深度 | 自然文 `shallow depth of field`, `out of focus in the foreground` | タグ側に相当語がなく、自然文でしか出せない |
| カメラ高さ(アオリ) | タグ `from below` **+** 自然文 `low angle` の二重指定 | どちらか片方では出ない。タグのみ→水平、自然文のみ→水平〜やや俯瞰 |
| 2人が向き合う | タグ `facing another, eye contact` | `looking at him` は生成時に `looking at viewer` に均されて正面化する |
| 手前人物による顔の遮蔽 | `out of focus foreground` があると誘発される | 意図的に出す方法は未確定 |

分担の整理: **ショット種別・ボケ・レンズ = 自然文(撮影用語)/ カメラ高さ・人数・視線関係 = タグ**。「タグで確定+自然文で寄せる」の3層の型は、構図についてもこの検証で裏付けられた。

副産物: 自然文があると無指定要素(髪色など)の抽選が狭まる(タグのみでは髪色がランダム、自然文ありで茶髪に収束)。

## 検証記録(2026-09-07)

txt2img、seed 固定、LoRA なし、場面「カウンター越しに男性が女性に話しかけ、女性が困っている」。各2枚。

| 判定項目 | A タグのみ | B 撮影用語のみ | C 両方 |
|---|---|---|---|
| 男性が手前・大きく・背中側 | △ 横顔で並列 | ○ 完全なOTS | ○ |
| 女性の体・視線が男性向き | ○ | ○ | ○ |
| カメラ高さ(やや下から) | × 水平 | × 水平〜やや俯瞰 | ○ 天井照明・カウンター縁が見えるアオリ |
| 被写界深度(手前ボケ) | × | ○ 強い | ○ |

A: `1girl, 1boy, facing another, eye contact, talking, counter, from behind, upper body, sweatdrop, furrowed brow, indoors`
B: `Over-the-shoulder shot from behind the man. Low angle, slightly below the woman's eye level. Medium close-up on the woman behind the counter, the man's head and shoulder large and out of focus in the lower left foreground. She looks at him with a troubled expression, sweat on her cheek. Shallow depth of field.`
C: A のタグ行 + B の自然文。最終稿は [../examples/sfw/counter-ots-cinematic.md](../examples/sfw/counter-ots-cinematic.md)

## 正面化(デフォルト構図への引力)への対処

学習データの大半が正面・中央・水平なので、弱い指示は必ず正面に均される。

1. `facing another, eye contact, talking` で2人の関係をタグ固定(カメラは自動的に第三者視点になる)
2. ネガに `looking at viewer`
3. 自然文で「カメラは誰の肩越しに、どの高さから」を撮影用語で書く
4. それでも正面に戻るなら、プロンプトでの抽選をやめて img2img で構図を固定する → [img2img.md](img2img.md)

## Danbooru 構図タグの効き方の予測

Danbooru の構図タグは「描かれた結果」に事後的に付くもので、カメラ指示として付いていない。付与基準が明確なタグ(`from below`, `close-up`, `from behind`)は安定し、曖昧なタグ(`foreshortening`, `dynamic pose`, `dynamic angle`)は効きが弱い【未検証】。効くかどうかは Danbooru 側の付与ルールの明確さでおおむね予測できる。

## 次の検証候補

- `extreme close-up on the lips`(漫画中央コマ級の寄り)— 通ると予想
- `tilted camera` / `dutch angle` の自然文版 — 高さと同様、単独では弱いと予想
- `rack focus`, `bokeh` 単独
- `head out of frame`, `feet out of frame`(漫画的トリミング)
- 遮蔽を意図的に出す書き方(`partially hidden behind his shoulder` 等)

## 参考(外部・未検証)

- edmondyip「Mastering SDXL Prompts: Lens Perspective」(Animagine で焦点距離・アングルを同条件比較) https://edmondyip.substack.com/p/mastering-sdxl-prompts-1-advanced
- 月ヶ瀬そら「構図・アングル・ポーズ系タグリスト(約900)」(NovelAI 検証、Danbooru 語彙) https://note.com/sora_tsukigase/n/n9500741037fd
- 本当に漫画的な構図(強いパース・複数人の奥行き)は SDXL 系では ControlNet が定石。Anima は ControlNet 未整備のため、[img2img.md](img2img.md) の手段で代替する。
