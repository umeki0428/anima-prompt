# Anima プロンプト作成スキル

日本語の指示から ComfyUI + Anima 用のプロンプト(英語)を作る。説明は日本語で行う。

## 出力の型(3層)

1. **固定ブロック** — 接頭辞とネガティブ。モデル(base / aesthetic)で切り替える。
2. **タグ行** — Danbooru形式で主題・属性・画風を確定。
3. **自然文** — 英語2文以上で構図・空間関係・雰囲気を補足。

## 場面別の参照先

- 書式・タグ順・固定ブロック・タグと自然文の分担・NG構文 → `references/anima-rules.md`(必読)
- 画風・絵師タグを指定するとき → `references/styles.md`
- サンプラー・CFG・解像度を聞かれたとき → `references/settings.md`
- 髪型・衣装・ポーズ等の語彙をタグ化するとき → `references/vocab.md`
- 生成結果が外れたとき・修正相談 → `references/failures.md`(対処後は追記する)
- 出力形式の見本 → `examples/sfw/`
- 生成に使ったプロンプトの記録 → `captions/` に保存する
