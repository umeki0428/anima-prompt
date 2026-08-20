# 生成設定(サンプラー・CFG・ステップ・解像度)

## 公式推奨設定

| 項目 | 推奨値 |
|---|---|
| 解像度 | 512² 〜 1536² px(約1〜2MP が最適) |
| ステップ数 | 30〜50(40以上で最良品質) |
| CFG | 4〜5 |
| スケジューラ | simple(デフォルト)。SGM Uniform も可 |
| Turbo LoRA 使用時 | CFG 1、8〜12ステップ |

- CFG を 10 以上にすると**彩度過剰・輪郭のキツさ・白飛び**が発生する。低めが綺麗。
- 解像度はやや低めの方が品質が安定する傾向。アスペクト比は 1:1 / 3:4 / 4:5 / 16:9 が無難。ComfyUI公式例は 1152×896。

## サンプラーの使い分け(公式の説明)

| サンプラー | 特徴 |
|---|---|
| `er_sde` | **デフォルト推奨**。ニュートラルな絵柄、フラットな塗り、シャープな線。結果が安定 |
| `euler_a` (euler ancestral) | 柔らかく細い線。やや2.5D寄りになることがある。キャラアート・イラスト向き |
| `dpmpp_2m_sde_gpu` | er_sde 系の絵柄だがバリエーションが豊か。創造的だが複雑なプロンプトでは不安定 |
| `euler` | er_sde よりやや創造的な基本サンプラー |

- ClownShaker などの特殊サンプラーは相性が悪いという報告あり。標準の KSampler で良い。

## img2img の denoise 目安

| 用途 | denoise |
|---|---|
| text-to-image | 1.0 |
| 微修正 | 0.5〜0.6 |
| 元画像をベースに大きく変える | 0.75〜0.85 |

## 運用のコツ

- Anima は出力のばらつきが大きい設計。**1回で決めず、seed・サンプラー・プロンプトを変えて複数回生成**するのが前提。
- 安定重視なら `er_sde`、アイデア出しなら `dpmpp_2m_sde_gpu` でガチャを回し、当たり構図を er_sde や img2img で仕上げる、という流れが実用的。

## 出典

- https://huggingface.co/circlestone-labs/Anima
- https://docs.comfy.org/tutorials/image/anima/anima
- https://techtactician.com/anima-comfyui-quick-local-setup-guide/
- https://diffusiondoodles.substack.com/p/anima-light-fast-and-slightly-unruly
- https://comfyui.nomadoor.net/en/basic-workflows/anima/
