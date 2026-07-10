# CUT08 — WAKE UP（SE77NTH.）

Studio OS標準制作ワークフロー Version 1(詳細: GitHub `AI_WORKFLOW_V1.md`)で生成。Story Bible改訂版(2026-07-10)に基づく新規カット。

## 生成前チェック

- Character Bible: [[10_Characters/MIU|MIU]]・[[10_Characters/AYA|AYA]]・[[10_Characters/NANA|NANA]]・[[10_Characters/KAI|KAI]]のビジュアル設定を確認
- Costume Bible: 4人分の衣装はいずれも [[11_Costume_Bible/_Index|Costume Bible]] に未登録
- Universe Rule: [[10_Characters/FLY77STAR_Universe|FLY77STAR Universe]] 「キャラクターは時間を生きる」— パラレル世界の解消は物語構造上の演出であり矛盾なし
- Production Bible: 架空店舗の消失演出も架空表記ポリシーの範囲内
- 矛盾: あり(既知) — 4人分の衣装が未登録

## リレー実行ログ

```
🎬 CINE — 演出・カメラ・照明・演技方針
店内の光がゆっくり明滅し、輪郭が滲み始める。KAIの姿が最初にぼやけ、店内
全体が光の粒子のように解けていく。
状態: 完了

🎭 SOUL — 感情・セリフ・心理描写
夢から覚める直前の浮遊感と焦り。3人はまだ状況を飲み込めていない。
状態: 完了

📷 CUT — 絵コンテ・構図・プロンプト
光の明滅→KAIの輪郭が滲む→店内全体がホワイトアウトする3段構図。画像/動画
Promptへ変換。
状態: 完了

🛡 MASTER — Character Bible / Costume Bible / Universe Rule / Production Bible照合
KAI・3人のビジュアルはCharacter Bibleと一致(解け始める演出のため輪郭のみ
崩す)。パラレル世界の解消はUniverse Ruleと矛盾なし。
状態: 完了
```

## シーンタイトル

パラレル終了

## 時間

1:45〜2:00 目安（BPM 95.7）

## 場所

「POP DINER」店内（架空店舗、消失していく空間）

## 出演者

MIU、AYA、NANA、KAI

## 演技

3人が異変に気づき顔を見合わせる。KAIは動じず微笑んだまま、輪郭が光に溶けていく。3人は思わず手を伸ばすが届かない。

## セリフ

MIU「え……？」

## カメラ

店内の明滅を捉えるワイド → KAIの輪郭が滲むクローズアップ → 店内全体がホワイトアウトするワイド

## 照明

暖色ネオンが不規則に明滅し、徐々に純白の光へ飽和していく

## 感情

夢から覚める直前の浮遊感と焦り。掴みたいものが手からすり抜ける感覚

## 画像生成Prompt

```
Dreamlike diner interior beginning to dissolve into flickering light,
East Asian Japanese young man (KAI) smiling calmly as his silhouette
softens and blurs into particles of warm light, three East Asian
Japanese young women (MIU, AYA, NANA) reaching out with startled
expressions, warm neon flickering into overexposed white, cinematic
dissolve composition, Soul ID locked for consistency, 35mm film grain
```

## 動画Prompt

```
Warm interior lighting flickers irregularly, KAI's outline softens and
dissolves into light particles as three women reach toward him, scene
whites out gradually, 6-7 seconds, rising ambient tone fading to
silence at the whiteout
```

## 編集指示

CUT07のKAIの一言から直接繋ぐ。ホワイトアウトのピークでCUT09(現実)へハードカット。

## 4者レビュー

```
🎬 CINE「明滅からホワイトアウトへの流れでパラレル世界の終わりを明確に示せた。」
🎭 SOUL「MIUの『え……？』一言に3人分の戸惑いを凝縮できた。」
📷 CUT「輪郭が溶けるエフェクトは生成モデルによって品質差が出やすい、要検証。」
🛡 MASTER「Universe Ruleとの矛盾なし。ホワイトアウトからCUT09への接続を確認。」
```
