# 生成設定(サンプラー・CFG・ステップ・解像度)

凡例: 【公式】= Hugging Face 公式README / docs.comfy.org 由来。【未検証】= 第三者記事由来で、このプロジェクトの実生成では未確認。

## 推奨設定【公式】

| 項目 | 推奨値 |
|---|---|
| 解像度 | 512² 〜 1536² px |
| ステップ数 | 30〜50 |
| CFG | 4〜5 |
| Turbo LoRA 使用時 | CFG 1、8〜12ステップ |

- スケジューラは simple(デフォルト)。SGM Uniform も可【未検証】(https://techtactician.com/anima-comfyui-quick-local-setup-guide/)。
- CFG 10以上で彩度過剰・輪郭のキツさ・白飛び【未検証】(https://diffusiondoodles.substack.com/p/anima-light-fast-and-slightly-unruly)。
- 最適画素数は1〜2MP、低めの方が安定。アスペクト比 1:1 / 3:4 / 4:5 / 16:9 が無難【未検証】(同上)。ComfyUI公式サンプルは 1152×896【公式】。

- VRAM 6〜8GB のGPUで動作可能(モデル+テキストエンコーダ+VAE込み)【未検証】(https://techtactician.com/anima-comfyui-quick-local-setup-guide/)。

## サンプラーの使い分け【公式】

| サンプラー | 特徴 |
|---|---|
| `er_sde` | **デフォルト推奨**。ニュートラル、フラットな塗り、シャープな線 |
| `euler_a` | 柔らかく細い線。やや2.5D寄りになることがある |
| `dpmpp_2m_sde_gpu` | er_sde系の絵柄でバリエーション豊か |
| `euler` | er_sde よりやや創造的な基本サンプラー |

- ClownShaker 等の特殊サンプラーは相性が悪い報告。標準 KSampler で良い【未検証】(https://diffusiondoodles.substack.com/p/anima-light-fast-and-slightly-unruly)。

## img2img の denoise 目安

構図固定の用途と元画像の種類別の使い分けは [img2img.md](img2img.md)。以下は外部記事の目安【未検証】。

| 用途 | denoise |
|---|---|
| text-to-image | 1.0 |
| 微修正 | 0.5〜0.6 |
| 元画像から大きく変える | 0.75〜0.85 |

出典: https://techtactician.com/anima-comfyui-quick-local-setup-guide/

## 運用のコツ【未検証】

- 1回で決めず、seed・サンプラー・プロンプトを変えて複数回生成する。
- 安定重視は `er_sde`、アイデア出しは `dpmpp_2m_sde_gpu` で回し、当たりを er_sde / img2img で仕上げる。

## 出典

- https://huggingface.co/circlestone-labs/Anima 【公式】
- https://docs.comfy.org/tutorials/image/anima/anima 【公式】
- https://techtactician.com/anima-comfyui-quick-local-setup-guide/
- https://diffusiondoodles.substack.com/p/anima-light-fast-and-slightly-unruly
- https://comfyui.nomadoor.net/en/basic-workflows/anima/
