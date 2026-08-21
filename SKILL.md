# Anima プロンプト作成スキル

日本語の指示から ComfyUI + Anima 用のプロンプト(英語)を作る。説明は日本語で行う。

## 出力の型(3層)
1. **固定ブロック** — 接頭辞とネガティブ。モデル(base / aesthetic)で切り替える。
2. **タグ行** — Danbooru形式で主題・属性・画風を確定。
3. **自然文** — 英語2文以上で構図・空間関係・雰囲気を補足。

漫画ページだけ例外。`references/manga-page.md` の4段(品質・容姿・配置・コマ説明)を使う。

## 場面別の参照先
- 書式・タグ順・固定ブロック・変換手順・NG構文 → `references/anima-rules.md`(必読)
- 漫画ページ(複数コマ) → `references/manga-page.md`。品質タグ → 容姿タグ → 配置タグ → コマ毎の状況説明の4段。通常の3層は使わない
- キャラ名を指定されたとき → `characters/<名前>.md` を読み、固定タグ・既定衣装をそのまま使う。ユーザーの指示はポーズ・表情・構図・カメラ・背景など差分だけなので、差分をタグ行と自然文に変換して組み合わせる
- 画風・絵師タグ → `references/styles.md` / サンプラー・CFG等 → `references/settings.md`
- 語彙のタグ化 → `references/vocab.md` / 失敗事例と対処 → `references/failures.md`
- 形式の見本 → `examples/_templates/`、検証済み例と生成記録 → `examples/sfw/`
- `captions/` は参考画像の逆キャプション置き場(examples/ の素材)。生成記録は examples/ に保存する。

## 運用ルール
- 生成結果の報告を受けたら、外れた点を `references/failures.md` に追記し、タグ置換で解決した語彙は `references/vocab.md` にも反映する。
- 実生成で確認できた項目は【未検証】を外し、確認日を書く。
