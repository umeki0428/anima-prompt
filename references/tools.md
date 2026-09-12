# 手元ツールと ComfyUI ワークフロー(2026-09-13 時点)

プロンプト作成の前後で使うローカルツールの置き場。中身の詳細は各フォルダの README。

## タグ整理・辞典

| ツール | 場所 | 用途 |
|---|---|---|
| **tagpick** | `C:\AI\tagpick\start_tagpick.bat` → http://127.0.0.1:7870 | 画像/貼り付けプロンプト → WD14 タグをジャンル別・日本語付きチェックボックスに展開。キャラ差し替え(女性/男性プリセット)、絵柄タグ除外、アセット(タグ束)合体、自分用辞典 `mydict.md`、プロンプト大辞典 14万語の日本語検索 |
| **シチュエーション帳** | https://claude.ai/code/artifact/c3158c1d-51b9-45e6-bb75-ffff27bab2ce | 状況プロンプト 122 種(前戯/女性責め/行為/男乳首責め/NTR/拒絶)。札クリックでコピー、＋で合体。キャラ・場所は含まないので [characters/](../characters/) とアセットで重ねる |

tagpick の日本語訳は `C:\AI\studio-magami\sd-webui-prompt-dictionary\data\` の辞書を実行時に読む(個人利用のみ・コピー不可)。

## 前処理(ComfyUI API バッチ)

| ツール | 場所 | 用途 |
|---|---|---|
| **remove_text_batch.py** | `C:\AI\comfy-batch\` | フォルダ内の画像からセリフ・フキダシ・描き文字を Qwen-Image-Edit-2511 で一括除去。出力 `_cleaned\`。構図・ポーズ素材向け(絵柄は微妙に変わるので絵柄LoRAの素材には使わない) |
| **tag_images.py** | `C:\AI\hgk-lora-v1\`(lora リポジトリ `scripts/tag_images_wd14.py` にも同じもの) | wd-eva02-large-v3 で一括キャプション。`--keep_style` / `--extra_remove` / `--boost_tags` |

## ComfyUI ワークフロー(`user/default/workflows/`)

| ファイル | 用途 |
|---|---|
| `copita-compare-qwen-edit` / `copita-compare-sdxl-img2img` | Copita 用の比較画像(実写化)。SDXL 版は bigLust で NSFW も通る |
| `colorize-qwen-edit` / `colorize-sdxl-anytest` | 白黒 → カラー。色は positive に具体的に書く |
| `cleanup-text-qwen-masked` | マスクした文字部分だけ Qwen 出力に置換(効果線を1pxも変えない) |
| `anima-style-dataset-gen` | SDXL + Dynamic Prompts(`wildcards/styleds/`)で学習素材を量産。着衣/NSFW 比率は `{6::…|4::…}` |
| `room-style-match-anima` | 別モデル/写真の背景を depth LLLite 付き img2img で nova v4 の絵柄に揃える |
| `room-add-characters-inpaint-anima` | マスク範囲を crop&stitch で 1024px に拡大して人物を描き足す。引きの構図で人物を精細にする手段 → [composition.md](composition.md) |

## Qwen-Image-Edit のプロンプト注意

- 否定文が苦手。「speed lines は残せ」と書くと**集中線が描き足される**。消したいものだけ短く書き、残すものは列挙しない(`Erase all Japanese text and heart marks. Leave every other part untouched.`)
- `sound effects` は効果線と解釈される。文字を指すなら `sound effect lettering`
- 名詞を書くとそれを描く。negative にも効果線系の語は入れない
