# Anima プロンプト作成スキル

日本語の指示から ComfyUI + Anima 用のプロンプト(英語)を作る。説明は日本語で行う。

## 出力の型(3層)
1. **固定ブロック** — 接頭辞とネガティブ。モデル(base / aesthetic)で切り替える。
2. **タグ行** — Danbooru形式で主題・属性・画風を確定。
3. **自然文** — 英語2文以上で構図・空間関係・雰囲気を補足。容姿は書かない。

漫画ページだけ例外。`references/manga-page.md` の構成(画風 → Character → Panel文章)を使う。

## 容姿は一度だけ(再掲禁止)

髪・瞳・ヘイロー・髪飾りなどの**アイデンティティは、プロンプト内で一度だけ書く**。自然文の先頭にも末尾にも繰り返さない。

- **1枚絵:** 容姿はタグ行だけ。自然文は構図・空間・雰囲気。`Rio has thigh-length...` のような既定自然文は貼らない。見本は [character-pose-change.md](examples/_templates/character-pose-change.md)
- **漫画ページ:** 容姿は Character ブロックだけ。各 Panel は名前＋動作／カメラ／表情／背景。髪・瞳・ヘイロー・クリップを繰り返さない
- **例外:** タグ行に容姿がまだないときだけ、自然文で「名前の直後に外見」。見本は [two-girls-back-to-back.md](examples/_templates/two-girls-back-to-back.md)
- **複数キャラの混ざり防止:** 自然文で容姿を再掲せず、タグで外見差を先に書く

## 場面別の参照先
- 書式・タグ順・固定ブロック・変換手順・NG構文 → `references/anima-rules.md`(必読)
- 漫画ページ(複数コマ) → `references/manga-page.md`。画風行 → Character one/two → Panel毎に位置と状況を文章で書く。通常の3層は使わない
- キャラ名を指定されたとき → `characters/<名前>.md` を読む。1枚絵では固定タグ・既定衣装をそのまま使い、差分だけタグ行と自然文に足す(自然文に容姿は足さない)。漫画ページでは固定タグ・既定衣装・既定自然文を Character ブロックの文章に一度だけ展開し、各 Panel では同じ名前と動作だけ使う
- 画風・絵師タグ → `references/styles.md` / サンプラー・CFG等 → `references/settings.md`
- 色・光・表情・湯気でエロさを出す → `references/atmosphere.md`。**背景の配色は場面ごとに変える**(チャコール固定・紫回避固定にしない)
- 語彙のタグ化 → `references/vocab.md` / 失敗事例と対処 → `references/failures.md`
- 形式の見本 → `examples/_templates/`、検証済み例と生成記録 → `examples/sfw/` / `examples/adult/`
- `captions/` は参考画像の逆キャプション置き場(examples/ の素材)。生成記録は examples/ に保存する。

## 運用ルール
- 生成結果の報告を受けたら、外れた点を `references/failures.md` に追記し、タグ置換で解決した語彙は `references/vocab.md` にも反映する。
- 実生成で確認できた項目は【未検証】を外し、確認日を書く。
