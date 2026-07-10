# CUT01 — WAKE UP（SE77NTH.）

Studio OS標準制作ワークフロー Version 1(詳細: GitHub `AI_WORKFLOW_V1.md`)で生成。Story Bible改訂版(2026-07-10)に基づく。旧コンセプト(閉店ーFLY77STAR. CLOSET)は廃止。

## 生成前チェック

- Character Bible: [[10_Characters/MIU|MIU]]のビジュアル設定を確認
- Costume Bible: MIUの私服は [[11_Costume_Bible/_Index|Costume Bible]] に未登録
- Universe Rule: [[10_Characters/FLY77STAR_Universe|FLY77STAR Universe]] 「キャラクターは時間を生きる」— 矛盾なし
- Production Bible: GitHub `PRODUCTION_BIBLE.md` のAI Production Policy(架空ブランドの明記)を確認。実在の渋谷の地名は使うが、店舗・看板は架空表記とする
- 矛盾: あり(既知) — MIUの私服が未登録。仮の私服想定で進行

## リレー実行ログ

```
🎬 CINE — 演出・カメラ・照明・演技方針
渋谷の夜、雑踏の中にMIUが一人佇む構図。俯瞰から下降するワイド〜クレーン風の
導入ショットで街の熱量を見せ、最後にMIUへ寄る。
状態: 完了

🎭 SOUL — 感情・セリフ・心理描写
「これから何かが始まる予感」。まだ何も起きていない、けれど普段と違う夜だという
気配。セリフなし。
状態: 完了

📷 CUT — 絵コンテ・構図・プロンプト
俯瞰→ワイド→MIUへの寄りの3段構図。画像/動画Promptへ変換。
状態: 完了

🛡 MASTER — Character Bible / Costume Bible / Universe Rule / Production Bible照合
MIUのビジュアルはCharacter Bibleと一致。衣装は未登録(上記参照)。渋谷の実在感と
架空店舗表記のバランスはProduction Bibleのポリシーに沿う。
状態: 完了
```

## シーンタイトル

渋谷

## 時間

0:00〜0:08 目安（BPM 95.7）

## 場所

渋谷スクランブル交差点付近、夜

## 出演者

MIU

## 演技

雑踏の中、一人で待つ。周囲を軽く見渡し、スマホを一瞬確認してからしまう。

## セリフ

なし

## カメラ

俯瞰のワイド(交差点全体) → 緩やかな降下 → MIUへのミディアムショット

## 照明

ネオンサイン・電光掲示板の光が入り混じる、彩度の高い夜の光。MIU周辺だけやや落ち着いたトーン

## 感情

これから何かが始まる予感。普段通りの夜のはずが、どこか浮ついている

## 画像生成Prompt

```
Wide establishing shot descending into Shibuya scramble crossing at night,
East Asian Japanese young woman (MIU) standing alone amid the crowd, long
light brown loose wavy hair with white hairband, glossy warm-toned lips,
gold accessories, neon signage and digital billboards reflecting on wet
pavement, vibrant saturated night colors, cinematic wide angle transitioning
to medium shot, anticipatory mood, Soul ID locked for consistency, 35mm
film grain
```

## 動画Prompt

```
Slow descending crane shot from wide overhead view of the crossing down to
a medium shot of MIU standing still amid moving crowd, 6-7 seconds, subtle
parallax, neon flicker, ambient city noise
```

## 編集指示

MVの導入カット。BPM95.7のイントロ頭からスタート。CUT02(AYA到着)への繋ぎはMIUの視線誘導(画面外を見る)からのカット。

## 4者レビュー

```
🎬 CINE「渋谷の熱量を最初に見せられた。次CUTでAYA登場のタイミングを揃えたい。」
🎭 SOUL「MIUの『予感』はまだ薄め。表情のニュアンスをCUT02以降で積み上げたい。」
📷 CUT「俯瞰からの降下は生成時にカメラパスの分割が必要になりそう。」
🛡 MASTER「Character Bible・Universe Ruleとの整合はOK。Costume Bible登録は残課題のまま。」
```
