# Anima モデルの基礎知識

## モデル概要

- **Anima** は CircleStone Labs と Comfy Org の共同開発による **2B(20億)パラメータ** のテキスト→画像生成モデル。
- **アニメ・イラスト・非フォトリアル系** に特化。リアル系(実写風)の描画は設計上サポート外。
- 学習データ: 数百万枚のアニメ系画像 + 約80万枚の非アニメ系アート画像。
- 知識カットオフ: **2025年9月** ごろ(比較的新しいキャラクターも再現可能)。

## アーキテクチャ

- ベースは **NVIDIA Cosmos 系の Transformer アーキテクチャ**(SDXL の U-Net とは別物)。
- テキストエンコーダ: **Qwen-3 0.6B** (`qwen_3_06b_base.safetensors`)
  - LLMベースのため **自然言語の理解力が高い**。Danbooruタグと自然言語の両方(および混在)を理解する。
  - CLIP時代のモデルより **複数キャラの空間関係の理解が得意**(マスクなしで複数キャラを描き分けやすい)。
- VAE: **Qwen Image VAE** (`qwen_image_vae.safetensors`)
- **SDXL用LoRAは使用不可**。Anima専用に学習されたLoRAが必要。

## モデルバージョン

| バージョン | 特徴 |
|---|---|
| `anima-base-v1.0` | 未調整のベースモデル。クオリティタグでの制御が前提 |
| `anima-aesthetic-v1.1` | 高品質画像のみでファインチューン済み。**通常はこちらを使う**。ポジティブにクオリティタグ不要、`score_*` タグは**使わない**ことを推奨 |
| Turbo LoRA | 8〜12ステップ・CFG 1 で高速生成(品質は若干低下) |

## ComfyUI での必要ファイル

| ファイル | 配置先 |
|---|---|
| `anima-base-v1.0.safetensors` 等(diffusion model) | `models/diffusion_models/` |
| `qwen_3_06b_base.safetensors` (text encoder) | `models/text_encoders/` |
| `qwen_image_vae.safetensors` (VAE) | `models/vae/` |

- 配布元: [circlestone-labs/Anima (Hugging Face)](https://huggingface.co/circlestone-labs/Anima)
- VRAM 6〜8GB のGPUで動作可能。

## モデルの性格・弱点

- プロンプト追従性は良好だが、Flux.2 や Qwen Image ほど厳密ではない。「大枠は合うが細部はブレる」。
- **縛りすぎるプロンプトには反発する**傾向がある。ある程度の自由度を残した方が良い結果になる。
- **文字描画は苦手**。入れるなら1〜2単語まで。複雑なタイポグラフィは不可。
- ベースモデルは構図がシンプルになりがち。
- 意図した絵を得るには seed・サンプラー・プロンプトを変えた**複数回生成が前提**の「やや気まぐれな」モデル。
- プロンプト内の異なる概念は**互いにブレンドされやすい**(概念混入に注意)。

## 出典

- https://huggingface.co/circlestone-labs/Anima
- https://docs.comfy.org/tutorials/image/anima/anima
- https://techtactician.com/anima-comfyui-quick-local-setup-guide/
- https://diffusiondoodles.substack.com/p/anima-light-fast-and-slightly-unruly
