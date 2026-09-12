# 日本語入力 → Qwen3.5-2B → Anima

`anima-japanese-iat-qwen35-2b.json` をComfyUIへドラッグ＆ドロップしてください。
「01 日本語で描きたい場面を書く」に日本語を入力し、実行します。
Qwenが英語のタグ行と必要最小限の補足文を作り、固定タグを付けてAnimaで生成します。
「05 実際に使う英語プロンプト」で生成された英語を確認できます。

## 初回準備

2026-09-11に確認したローカル環境:

- ComfyUI: `C:\AI\ComfyUI_windows_portable\ComfyUI`、v0.33.1。
- GPU: RTX 5070 Ti、VRAM 16GB。
- Anima、テキストエンコーダ、VAEは配置済み。JSONのファイル名は実際の配置に合わせています。
- **ComfyUI-IATは未導入、Qwen3.5-2Bの配置は未確認。現在のTransformersは4.57.1で、IATの必要条件5.2.0以上を満たしません。JSONの読み込みだけではまだ実行できません。**

1. ComfyUI Managerで `ComfyUI-IAT`（作者 Eric7758）をインストールします。
   公開元: https://github.com/Eric7758/ComfyUI-IAT
2. ComfyUIを停止し、同じPython環境にIATの依存関係を導入して再起動します。
   ポータブル版の場合は `C:\AI\ComfyUI_windows_portable\python_embeded\python.exe` を使います。
   IATは `transformers>=5.2.0` を要求します。現在の4.57.1からのメジャー更新になるため、既存環境を複製してから導入すると戻しやすくなります。今回はインストールや更新は実行していません。
3. Qwenは [Qwen/Qwen3.5-2B](https://huggingface.co/Qwen/Qwen3.5-2B) のHugging Face形式一式（重み・config・tokenizer等）を使用します。GGUFやAnima用 `qwen_3_06b_base.safetensors` とは別です。
   IATの既定の読み込み先は `ComfyUI/models/diffusion_models/Qwen3.5-2B/` です。
   手動で全ファイルを配置するか、IATの `config.yaml` にある `runtime.offline_only` を `false` にして再起動し、初回実行時に自動ダウンロードさせます。自動取得はModelScope優先、Hugging Faceがフォールバックです。既定configが `true` の場合、ファイル未配置のままでは取得されません。
4. JSONを読み込み、ノード02で `Qwen3.5-2B / cuda / SDPA` になっていることを確認します。

## 日常の操作

- ノード01: 日本語の場面説明。人物の外見や衣装もここへ書けます。
- ノード02: 日本語を英語プロンプトに変換。`custom_system_prompt` にAnima用の変換規則を設定済みなので、通常は変更不要です。カスタム指示が優先されるため、`enhancement_style` の選択だけを変えても出力方針は変わりません。
- ノード03: Base用の品質・安全タグ。初期値は `masterpiece, best quality, score_7, safe,`。
- ノード05: 最終英語の確認欄。
- ノード11: 幅896、高さ1152、1枚。16の倍数で変更します。
- ノード12: 30 steps、CFG 4.5、`er_sde / simple`。画像seedは毎回ランダム化。
- ノード14: `ComfyUI/output/Anima_JP_IAT/` へPNG保存。

翻訳seedは42固定、temperatureは0.2。絵だけ再抽選する場合はノード12のseedを変えます。同じ日本語・設定ならComfyUIの通常キャッシュにより文章は再生成されません。英語も作り直したい場合はノード02のseedを変えます。

Qwenの `keep_model_loaded=false` を設定しています。変換後にIATのモデルキャッシュを解放し、Animaが使えるVRAMを確保します。これは処理全体のピークVRAMを保証するものではありません。

変換はPrompt Enhancerのカスタム指示で1回にまとめています。英語出力を指定しているため、後段のTranslatorは不要です。プロジェクトの `SKILL.md` に合わせ、外見をタグ行に一度だけ記述し、自然文は構図や位置関係の補足に限定しています。2Bモデルが指示を必ず守る保証はないため、最初の数回はノード05で確認してください。

## 画像モデルを変更するとき

| バージョン | 固定タグとNegative | KSampler |
|---|---|---|
| Base v1.0 | JSONの初期設定 | 30 steps、CFG 4.5 |
| Aesthetic | ノード03と10から `score_*` を削除。品質タグは省略可能 | 30 steps、CFG 4〜5 |
| Turbo | 使用するモデルの説明に合わせる | 8〜12 steps、CFG 1 |

ノード06だけを切り替えても、品質タグやCFGは自動では変わりません。

## 確認範囲

- UI用workflow JSON形式（version 0.4）、ノードID・配線・型・widget値・循環の有無を検証。
- 稼働中ComfyUIの `/object_info` と標準ノード仕様・モデル選択肢を照合。
- IATのノード名・引数順・設定範囲は公開ソースのcommit `0647827c6ec3bd40a0c0235342d402231f1c7dd8` と照合。
- IAT/Qwenが未導入のため、実際の日本語変換・GPU推論・画像生成・ブラウザ上の読み込みは未検証です。
- 既存ワークフロー、モデル、Python依存関係は変更していません。

参照: [IATノード実装](https://github.com/Eric7758/ComfyUI-IAT/blob/0647827c6ec3bd40a0c0235342d402231f1c7dd8/py/nodes/qwen35_nodes.py)、[IATモデル読み込み実装](https://github.com/Eric7758/ComfyUI-IAT/blob/0647827c6ec3bd40a0c0235342d402231f1c7dd8/py/nodes/qwen35_runtime.py)、[Anima公式](https://huggingface.co/circlestone-labs/Anima)。
