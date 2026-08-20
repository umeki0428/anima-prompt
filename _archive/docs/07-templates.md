# プロンプトテンプレート集

日本語の指示から Anima 用プロンプトを組み立てる際の雛形。

## 基本テンプレート(anima-base 用)

**ポジティブ:**

```
masterpiece, best quality, score_7, safe, [年代タグ], [画風/絵師タグ], [1girl/1boy/2girls等], [キャラ名], [作品名], [一般タグ: 外見・服装・表情・ポーズ・背景・構図]
```

**ネガティブ:**

```
worst quality, low quality, score_1, score_2, score_3, artist name, blurry, jpeg artifacts, chromatic aberration
```

## anima-aesthetic 用テンプレート

クオリティタグ・score タグをポジティブから外す:

```
safe, [年代タグ], [画風タグ], 1girl, [キャラ名], [作品名], [一般タグ]
```

ネガティブは基本形と同じでよい。

## ハイブリッドテンプレート(推奨)

```
masterpiece, best quality, safe, 1girl, silver hair, red eyes, school uniform, classroom, window seat

A girl with long silver hair and red eyes sits by the window in a sunlit classroom. She rests her chin on her hand, gazing outside with a gentle smile. Afternoon light casts soft shadows across her desk.
```

- 1行目: タグで主題・属性を確定
- 2行目以降: 自然言語で構図・空間関係・雰囲気を補足(最低2文)

## 複数キャラのテンプレート

キャラごとに「名前→外見」をまとめ、位置関係を自然言語で明示する:

```
masterpiece, best quality, safe, 2girls

Two girls stand back to back. On the left, Hanako has short black hair and wears a red kimono. On the right, Yuki has long blonde twintails and wears a blue school uniform. They are smiling at each other over their shoulders.
```

## 日本語指示 → プロンプト変換の手順

1. **主題を確定**: 人数(`1girl`/`2girls`/`1boy`/`1other`)、キャラ名・作品名(既存キャラなら小文字タグで)
2. **外見・服装・表情・ポーズ**を Danbooru タグに変換(小文字・スペース区切り)
3. **背景・構図・ライティング**は自然言語の文で補足(空間関係はタグより自然言語が得意)
4. **画風の指定**があれば前方に配置(`Studio Ghibli style` 等、または `@絵師名`)
5. 接頭辞(`masterpiece, best quality, score_7, safe,`)と年代タグ(新しい絵柄なら `newest`)を付与
6. ネガティブは基本形+目的別追加
7. 全体を**15行未満・2〜3段落以内**に収める。細部を縛りすぎない

## 変換例

**指示:** 「銀髪ロングの女の子が夜の街をひとりで歩いている。サイバーパンクっぽい雰囲気で」

**ポジティブ:**

```
masterpiece, best quality, score_7, safe, newest, cyberpunk, 1girl, solo, long hair, silver hair, walking, night, city, neon lights, from behind

A girl with long silver hair walks alone through a neon-lit city street at night. Glowing signs reflect on the wet pavement around her, and tall buildings tower into the dark sky.
```

**ネガティブ:**

```
worst quality, low quality, score_1, score_2, score_3, artist name, blurry, jpeg artifacts, chromatic aberration, watermark, signature, photorealistic, 3d
```

## 出典

- https://huggingface.co/circlestone-labs/Anima
- https://diffusiondoodles.substack.com/p/anima-light-fast-and-slightly-unruly
