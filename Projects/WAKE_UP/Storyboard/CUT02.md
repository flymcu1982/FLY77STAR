# CUT02 — WAKE UP（SE77NTH.）

Studio OS標準制作ワークフロー Version 1(詳細: GitHub `AI_WORKFLOW_V1.md`)で生成。Story Bible改訂版(2026-07-10)に基づく。旧コンセプト(夜の路地→POP DINERへ)は廃止。

## 生成前チェック

- Character Bible: [[10_Characters/MIU|MIU]]・[[10_Characters/AYA|AYA]]のビジュアル設定を確認
- Costume Bible: MIU・AYAの私服はいずれも [[11_Costume_Bible/_Index|Costume Bible]] に未登録
- Universe Rule: [[10_Characters/FLY77STAR_Universe|FLY77STAR Universe]] 「キャラクターは時間を生きる」— 矛盾なし
- Production Bible: GitHub `PRODUCTION_BIBLE.md` のAI Production Policy(架空ブランドの明記)を確認。実在の渋谷の地名は使うが、店舗・看板は架空表記とする
- 矛盾: あり(既知) — MIU・AYAの私服が未登録。仮の私服想定で進行

## リレー実行ログ

```
🎬 CINE — 演出・カメラ・照明・演技方針
CUT01の続き。MIUが待つ場所へAYAが駆け寄ってくる構図。人混みの奥からAYAが
フレームインし、MIUが振り返って気づくまでをワンカットで繋ぐ。
状態: 完了

🎭 SOUL — 感情・セリフ・心理描写
待ち合わせ相手を見つけた安心感と高揚感。二人だけの軽い掛け合い、セリフは
短く一言のみ。
状態: 完了

📷 CUT — 絵コンテ・構図・プロンプト
人混み奥からのAYAの登場→MIUが振り返る→二人が向き合う3段構図。画像/動画
Promptへ変換。
状態: 完了

🛡 MASTER — Character Bible / Costume Bible / Universe Rule / Production Bible照合
MIU・AYAのビジュアルはCharacter Bibleと一致。衣装は未登録(上記参照)。CUT01
からの時間軸(BPM95.7)の連続性を確認。
状態: 完了
```

## シーンタイトル

AYA到着

## 時間

0:08〜0:18 目安（BPM 95.7）

## 場所

渋谷スクランブル交差点付近、夜（CUT01と同一エリア）

## 出演者

MIU、AYA

## 演技

MIUが振り返る。AYAが人混みを縫って小走りで駆け寄り、軽く手を上げて合流。二人で顔を見合わせ小さく笑う。

## セリフ

AYA「(小声で)待った？」

## カメラ

人混み奥からAYAが手前へ抜けてくるトラッキング → MIUが振り返る反応ショット → 二人を横並びで捉えるミディアム

## 照明

CUT01と同系統のネオン夜景。AYAが近づくにつれ、背後の光が徐々にソフトフォーカスへ

## 感情

待ち合わせ相手を見つけた安心感と高揚感。夜がここから動き出す予感

## 画像生成Prompt

```
Night street scene in Shibuya, East Asian Japanese young woman (AYA)
walking quickly through a crowd toward camera, center-parted straight
dark brown hair, nude-toned lips, silver accessories, raising a hand in
greeting, East Asian Japanese young woman (MIU) turning to look at her
with a small smile, long light brown wavy hair with white hairband,
neon signage bokeh in background, warm anticipatory mood, cinematic
medium shot, Soul ID locked for consistency, 35mm film grain
```

## 動画Prompt

```
Tracking shot following AYA as she weaves through the crowd toward MIU,
MIU turns and reacts with a smile, 6-7 seconds, natural crowd motion in
background, neon bokeh, ambient city noise, ends on two-shot
```

## 編集指示

CUT01のMIUの視線誘導から直接繋ぐ。AYAのセリフ「待った？」でCUT03(3人集合)への流れを作る。

## 4者レビュー

```
🎬 CINE「人混みからの合流はCUT01の視線誘導と自然に繋がった。」
🎭 SOUL「二人の関係性の温度感はまだ薄め。セリフのトーンで補強したい。」
📷 CUT「AYAのトラッキングは背景の人流生成が鍵になりそう。」
🛡 MASTER「Character Bibleとの整合はOK。Costume Bible登録は残課題のまま。」
```
