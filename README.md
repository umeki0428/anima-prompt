# anima-prompt

ComfyUI + Anima モデルで画像生成する際に、日本語の指示から画像生成用プロンプトを作成するためのナレッジベース。

## ドキュメント構成

| ファイル | 内容 |
|---|---|
| [docs/01-anima-basics.md](docs/01-anima-basics.md) | モデル概要・アーキテクチャ・バージョン・必要ファイル |
| [docs/02-tag-prompting.md](docs/02-tag-prompting.md) | タグの並び順・書式ルール・各種タグカテゴリ(公式ルール) |
| [docs/03-natural-language-hybrid.md](docs/03-natural-language-hybrid.md) | 自然言語プロンプトとハイブリッド(タグ+自然言語)の書き方 |
| [docs/04-generation-settings.md](docs/04-generation-settings.md) | サンプラー・CFG・ステップ数・解像度の推奨設定 |
| [docs/05-negative-prompts.md](docs/05-negative-prompts.md) | ネガティブプロンプトの基本形と目的別追加タグ |
| [docs/06-style-tags.md](docs/06-style-tags.md) | 画風タグの効き方(108スタイル検証の知見) |
| [docs/07-templates.md](docs/07-templates.md) | テンプレート集・日本語指示→プロンプト変換手順 |

## 使い方

Claude Code に日本語で描きたい内容を伝えると、上記ドキュメントのルールに従って Anima 用のポジティブ/ネガティブプロンプトを生成する(詳細は [CLAUDE.md](CLAUDE.md))。

生成結果に対する気づき(効いたタグ・効かなかったタグ等)は docs に追記して育てていく。
