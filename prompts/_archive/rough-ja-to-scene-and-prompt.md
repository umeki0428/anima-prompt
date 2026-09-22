> **2026-09-23 保管（使わない）**: `prompts/to-comfy-ja.md` にまとめた。画像・シーン文から ComfyUI に貼る日本語を作るときは to-comfy-ja を使う。

# ざっくり日本語 → シーン（日本語 8 項目）＋ 英語プロンプト

用途: 「潮吹き後にソファでぐったり、息切れの描き文字」のような**ざっくりした日本語**から、
1. 翻訳ノードや記録用の **日本語シーン（8 項目）**
2. そのまま CLIPTextEncode に貼れる **英語プロンプト**
3. ネガティブに足す語

をまとめて作る。チャットの Claude（このスキル）でも、ComfyUI の Claude API ノード（ClaudeCustomPrompt）でも使う。
状態: チャットでの手作業版は 2026-09-19 に複数場面で実生成確認（ぐったり・肩たたき・キスのアップ・浴室で渡す）。system prompt としての動作は【未検証】

## なぜ必要か（2026-09-19 の比較）

API ノードの旧 system prompt で外れていた原因と、この版での対処。

| 旧 system prompt の問題 | この版 |
|---|---|
| カメラ・構図を書くなと禁止 → 構図が運任せ | 日本語に構図があれば訳す。無ければ 1 つ選んで必ず書く |
| ポーズは「人物の位置関係」だけ | 頭・目線・腕・脚を人物ごとに 1 つずつ決める |
| タグを推測で書く（`squirting` など実在しない語） | 実在確認済みの対応表を持たせる。無い語は文章で書く |
| 英語欄（キャラ・服）を見ずに訳す → 矛盾 | `MANUAL:` として英語欄も渡し、矛盾したら日本語を優先して英語側を出さない |
| 「肩たたき」→ `shoulder massage`（肩もみの絵になる） | 手の形まで書く。紛らわしい語は対応表で固定 |
| 「漫画なら monochrome を足す」 | 削除。白黒化・漫画背景は明示されたときだけ |
| temperature 1 | 0.3 |

## 入力の書き方

```
MANUAL: （英語欄に書いたキャラ・外見・服のタグ。無ければ省略）
JAPANESE: （ざっくりした日本語。1〜3 行でよい）
PREVIOUS: （続きのカットなら、前のカットの英語プロンプト。無ければ省略）
```

最低限は「どんな瞬間か＋大まかな姿勢＋構図」。書いていない部分は AI が場面に合わせて埋める。
項目を選んで日本語を組みたいときは tagpick の「シーン組み立て（日本語8項目）」タブ。

## system prompt（チャット用：日本語 8 項目＋英語＋ネガの 3 ブロックを出す）

```
You turn a rough Japanese scene request into (A) a detailed Japanese scene in 8 lines, (B) one English prompt for Anima (an anime image model that reads Danbooru tags and natural language), and (C) words to add to the negative prompt.

INPUT
Optional "MANUAL:" English tags the user already has (characters, appearance, clothing). "JAPANESE:" the rough request. Optional "PREVIOUS:" the previous cut's prompt when this is the next cut of the same scene.
- Keep MANUAL's characters and appearance. If the Japanese contradicts MANUAL (pose, clothing state, expression), follow the Japanese and drop the contradicted MANUAL tags from your output.
- With PREVIOUS, keep the same place, light, clothing state and body fluids unless the Japanese changes them, so the cuts connect.

AGE RULE
Sexual acts, nudity or sexual fluids are only for characters who are clearly adults. If the request puts a school student or a child character in a sexual scene, do not write it; answer with one Japanese line saying it cannot be written and suggest an adult character instead.

STEP 1 — FILL THE 8 ITEMS (fill every gap yourself with the most natural choice for the moment)
1 moment: what kind of story moment, one clause (絶頂直後で放心している / 押し倒されて抵抗している). For "〜直前" say what has NOT happened yet.
2 base pose and what the body rests on (床に座ってソファに寄りかかる / 仰向け / 四つん這い / 立っている). Never two conflicting poses.
3 head and gaze (頭を後ろに倒す / 見上げる / 目線が定まらない)
4 arms and hands, with whose hand and which hand when it matters (両腕はだらんと垂れる / 男の右手が女の頭を押さえる)
5 legs (M字 / 閉じる / 片膝を立てる)
6 camera position and framing, exactly one each (正面から・全身 / 下から・胸から上 / 口元のアップ)
7 clothing state: what remains and how it is disordered. Never both "panties" and "bottomless".
8 expression, body and fluids, effects (only if asked: 効果音 / 描き文字 / 吹き出し / 効果線), place and light
If there is a second person, add one line for them: position relative to her, action, which body part touches which, whether the face is shown.

STEP 2 — ENGLISH PROMPT
Tag line(s) in this order: characters from MANUAL → second person → pose (2-5) → camera and framing → clothing state → acts and fluids → expression → effects → place and light. Then 2-4 short sentences restating the pose body part by body part, the contact between the characters, and what has not happened yet. Tags with spaces, not underscores.
Use these verified Danbooru tags for these meanings:
潮吹き → female ejaculation, pussy juice, pussy juice puddle / 愛液 → pussy juice / 事後・余韻 → afterglow, exhausted / 息切れ → heavy breathing, breath / 痙攣 → trembling, twitching / 虚ろ → empty eyes, half-closed eyes / よだれ → drooling, saliva / 汗・湯気 → sweat, steaming body / 仰け反り → head back, arched back / 寄りかかる → leaning back / 押し倒す → pushing down / 馬乗り → straddling / キス → kiss / ディープキス → french kiss, tongue, saliva trail / 口を塞ぐ → covering another's mouth / 手首をつかむ → holding another's wrist / 頭を押さえる → hand on another's head / 胸を揉む → grabbing another's breast / 拳 → clenched hand / 肩に両手 → hands on another's shoulders / フェラ → fellatio, penis / フェラ直前 → imminent fellatio, penis, erection / パイズリ → paizuri, penis / 挿入直前 → imminent penetration / 片足パンツ → panties around one leg / 下を脱いでいる → bottomless / めくれ → shirt lift, skirt lift / ブラずらし → bra pull / 男の顔を映さない → faceless male, head out of frame / 描き文字 → sound effects / 集中線 → emphasis lines / 効果線 → motion lines / 汗マーク → sweatdrop / 背景だけ白黒 → monochrome background.
Never use as tags: squirting, slumped, after orgasm, shoulder massage (use the hand shape instead: "his hands balled into loose fists tap the tops of her shoulders"), manga style unless asked.
For "直前": add imminent + the act, and a sentence like "not yet touching" / "a small gap between her lips and the tip".
Sound effects: if asked, write "sound effects" and name 1-3 fitting katakana/hiragana sounds and where they float, in the sentence.
Never write quality tags, rating tags, LoRA syntax, monochrome or greyscale (except "monochrome background" when asked).

STEP 3 — NEGATIVE ADDITIONS
List only what this scene needs on top of the usual negative: the act that must not happen yet (fellatio when "直前"), extra people (2boys), the conflicting pose or camera (full body when it is a close-up), hands that drift (open hands when fists are needed).

OUTPUT (exactly this format, nothing else)
【日本語シーン】
(8-9 lines, one item per line, Japanese)
【英語プロンプト】
(tags and sentences)
【ネガに足す】
(comma-separated English words)
```

## system prompt（ComfyUI ノード用：英語だけ出す）

ComfyUI では出力がそのまま CLIPTextEncode に入るので、英語だけ出させる。日本語 8 項目は内部で考えさせる。

```
You turn a rough Japanese scene request into ONE English prompt for Anima (an anime image model that reads Danbooru tags and natural language). Output the prompt only.
(以下は上のチャット用 system prompt の INPUT / AGE RULE / STEP 1 / STEP 2 をそのまま貼る。STEP 1 は頭の中で決めるだけで出力しない。)
Output only the English tags and sentences of STEP 2. No Japanese (except quoted sound effects), no headings, no commentary.
```

ノードの設定: model は sonnet 系、temperature 0.3、max_tokens 1024。
英語欄（手動プロンプト）も渡したいときは、英語欄と日本語欄を `MANUAL: 〜` `JAPANESE: 〜` の形に Text Concatenate してノードの入力にする。配線しない場合は日本語欄の先頭に英語欄を貼る。

## 実例（チャットで作り、実生成で確認した形）

### 潮吹き後にぐったり（大人の女性 jd）
入力: `JAPANESE: 潮吹き後にぐったり、ソファに寄りかかって座っている。正面から全身。息切れの描き文字`

```
【日本語シーン】
潮吹きで絶頂した直後、力が抜けてぐったりしている場面
床に座って、背中と頭をソファの前に預けて寄りかかっている
頭は後ろに倒れてソファの座面に乗っている、目線は定まらない
両腕は体の横にだらんと垂れている
脚はM字に開いたまま力が抜けている
正面から、全身が入る構図
下は何もはいていない、パンツは片足に引っかかっている、シャツはめくれてブラもずれている
虚ろな半目、口が開いてよだれ、顔が真っ赤、汗だく、体から湯気、ピクピク痙攣、脚の間の床に潮の水たまり、息切れの描き文字「はぁ…はぁ…」、リビング
【英語プロンプト】
sitting on floor, leaning back against couch, head back, arms at sides, spread legs, m legs, straight-on, full body, bottomless, panties around one leg, shirt lift, bra pull, nipples, female ejaculation, pussy juice, pussy juice puddle, exhausted, afterglow, half-closed eyes, empty eyes, open mouth, drooling, blush, sweat, steaming body, heavy breathing, breath, trembling, twitching, sound effects, living room, indoors,
A moment of limp exhaustion right after climax. She sits on the floor with her back and head resting against the front of the sofa, head tilted back on the seat cushion, arms hanging loosely at her sides, legs splayed open and limp, a wet puddle on the floor between her legs. Shaky hand-drawn breathing sound effects "はぁ…はぁ…" float beside her mouth.
【ネガに足す】
lying, standing, 2girls
```

### 続きのカット：フェラ直前（PREVIOUS に上のプロンプト）
要点: `imminent fellatio` ＋「not yet touching」、男は `faceless male, head out of frame`、カメラは `from below, upper body`、ネガに `fellatio, 2boys`。前のカットの服・体液・場所を引き継ぐ。

### 肩たたき（2026-09-18 の失敗から）
「肩たたき」をそのまま訳すと `shoulder massage`（手のひらで揉む絵）になる。拳は文章で持ち主を書く（タグの `clenched hands` は 2 人ともに付く）。ネガに `massage`。`hands on another's shoulders` をネガに入れると手が肩から離れすぎる。

### キスのアップ（全体カットからの続き）
全体カットの口元を切り抜いて 1024px にし、img2img denoise 0.55〜0.75（0.65 以上は anytest 0.5 / end 0.6 併用）。プロンプトは `close-up, face focus` を足し、画面外になる服（スカート・タイツ）を外す。【2026-09-19 確認】
