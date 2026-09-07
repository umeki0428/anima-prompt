# システムプロンプト集

Claude / ローカルLLM に貼って使う「前工程」のプロンプト。出力は最終的に SKILL.md の3層プロンプトか、ComfyUI の CLIPTextEncode に流す。

| ファイル | 入力 | 出力 | 実行場所 | 状態 |
|---|---|---|---|---|
| [image-to-scene-ja.md](image-to-scene-ja.md) | 参考画像 | 日本語の構図指示【構図指示】 | Claude(チャット) | 実生成で確認 2026-09-07 |
| [scene-to-composition-ja.md](scene-to-composition-ja.md) | 短いシーン文(1〜3文) | 日本語の構図指示 + 別案2つ | Claude(チャット/Code) | 【未検証】 |
| [comfyui-scene-to-prompt.md](comfyui-scene-to-prompt.md) | 短いシーン文 | 英語プロンプト(タグ行+自然文) | ComfyUI の Ollama 等ノード | 【未検証】 |
| [shot-list.md](shot-list.md) | シーン文(数文) | 漫画1ページ分のショットリスト | Claude | 【未検証】 |

## つなぎ方

```
参考画像 ──(image-to-scene-ja)──┐
                                ├→ 【構図指示】 + 「〇〇で」 ──(SKILL.md)──→ 3層プロンプト → txt2img / img2img
シーン一文 ─(scene-to-composition-ja)┘

シーン一文 ─(comfyui-scene-to-prompt)→ Ollamaノード → String Concatenate(品質+キャラ固定+LLM出力) → CLIPTextEncode
```

- キャラ差し替え前提なので、どのプロンプトも**キャラの同一性(髪・目・顔・体型・衣装)は書かない**。キャラは `characters/` から SKILL.md 側が足す。
- 漫画コマを元にするときは吹き出し・効果音・コマ枠は「不明瞭:」に分離する(本文に混ぜない)。
- 構図が正面に化けたときの対処は [../references/composition.md](../references/composition.md)。
