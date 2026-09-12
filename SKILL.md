# Anima プロンプト作成スキル

日本語の指示から ComfyUI + Anima 用のプロンプト(英語)を作る。説明は日本語で行う。

## 出力の基本形(簡潔なハイブリッド)
1. **固定ブロック** — 接頭辞とネガティブ。モデル(base / aesthetic / turbo)で切り替える。
2. **タグ行** — Danbooru形式で人数、外見、衣装、表情、構図などの離散的な要素を指定する。
3. **自然文(必要な場合だけ)** — 服の重なり、位置関係、画面内の範囲、カメラなど、タグだけでは曖昧な内容を短く補足する。容姿は書かない。

タグで指定済みの髪・目・衣装・構図を自然文で繰り返さない。ハイブリッド形式の自然文に最低文数はない。**純自然文だけで作る場合**は公式推奨どおり2文以上を目安にする。

自然文が不要な単純な1枚絵は、固定ブロック＋タグ行だけでもよい。漫画ページは例外として `references/manga-page.md` の構成(画風 → Character → Panel文章)を使う。

## 容姿は一度だけ(再掲禁止)

髪・瞳・ヘイロー・髪飾りなどの**アイデンティティは、プロンプト内で一度だけ書く**。自然文の先頭にも末尾にも繰り返さない。

- **1枚絵:** 容姿はタグ行だけ。自然文は構図・空間・雰囲気。`Rio has thigh-length...` のような既定自然文は貼らない。見本は [character-pose-change.md](examples/_templates/character-pose-change.md)
- **漫画ページ:** 容姿は Character ブロックだけ。各 Panel は名前＋動作／カメラ／表情／背景。髪・瞳・ヘイロー・クリップを繰り返さない
- **例外:** タグ行に容姿がまだないときだけ、自然文で「名前の直後に外見」。見本は [two-girls-back-to-back.md](examples/_templates/two-girls-back-to-back.md)
- **複数キャラの混ざり防止:** 自然文で容姿を再掲せず、タグで外見差を先に書く

## 場面別の参照先
- 書式・タグ順・固定ブロック・変換手順・NG構文 → `references/anima-rules.md`(必読)
- 漫画ページ(複数コマ) → `references/manga-page.md`。画風行 → Character one/two → Panel毎に位置と状況を文章で書く。通常のハイブリッド形式は使わない
- キャラ名を指定されたとき → `characters/<名前>.md` を読む。1枚絵では固定タグ・既定衣装をそのまま使い、差分だけタグ行と自然文に足す(自然文に容姿は足さない)。漫画ページでは固定タグ・既定衣装・既定自然文を Character ブロックの文章に一度だけ展開し、各 Panel では同じ名前と動作だけ使う
- 画風・絵師タグ → `references/styles.md` / サンプラー・CFG等 → `references/settings.md`
- 構図・カメラ(オーバーショルダー、アオリ、ボケ、正面化の対処) → `references/composition.md`。ショット種別・ボケは撮影用語の自然文、カメラ高さはタグ+自然文の二重指定
- プロンプトで構図が出ないとき、参考画像・ラフから構図を固定する → `references/img2img.md`
- 「画像から構図」「シーンから構図」「ショットリスト」と言われたら → `prompts/README.md` の呼び名表で該当ファイルを開き、そのプロンプトを実行する。出力の【構図指示】に続けて「〇〇で」とキャラ名があれば、そのままこのスキルで3層プロンプトまで作る。渡すシーン文の書き方は `prompts/scene-input-rules.md`
- 色・光・表情・湯気でエロさを出す → `references/atmosphere.md`。**背景の配色は場面ごとに変える**(チャコール固定・紫回避固定にしない)
- 語彙のタグ化 → `references/vocab.md` / 失敗事例と対処 → `references/failures.md`
- 手元ツール(tagpick / シチュエーション帳 / 一括文字消し / ComfyUI ワークフロー一覧) → `references/tools.md`。俯瞰・引きと人物の精細化は `references/composition.md` の 2026-09-13 節
- 形式の見本 → `examples/_templates/`、検証済み例と生成記録 → `examples/sfw/` / `examples/adult/`
- `captions/` は参考画像の逆キャプション置き場(examples/ の素材)。生成記録は examples/ に保存する。

## 運用ルール
- 生成結果の報告を受けたら、外れた点を `references/failures.md` に追記し、タグ置換で解決した語彙は `references/vocab.md` にも反映する。
- 実生成で確認できた項目は【未検証】を外し、確認日を書く。
