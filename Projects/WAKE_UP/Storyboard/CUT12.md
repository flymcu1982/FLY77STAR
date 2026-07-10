# CUT12 — WAKE UP（SE77NTH.）

Studio OS標準制作ワークフロー Version 1(詳細: GitHub `AI_WORKFLOW_V1.md`)で生成。Story Bible改訂版(2026-07-10)に基づく新規カット。

## 生成前チェック

- Character Bible: [[10_Characters/MIU|MIU]]・[[10_Characters/AYA|AYA]]・[[10_Characters/NANA|NANA]]のビジュアル設定を確認
- Costume Bible: 3人の私服はいずれも [[11_Costume_Bible/_Index|Costume Bible]] に未登録
- Universe Rule: [[10_Characters/FLY77STAR_Universe|FLY77STAR Universe]] 「キャラクターは時間を生きる」— 本作は[[10_Characters/FLY77STAR_Universe|FLY77STAR Universe]] Chapter1の第一章として「続く」形で終わる構成であり矛盾なし
- Production Bible: 実在の渋谷の地名の範囲内での夜景描写に留める
- 矛盾: あり(既知) — 3人分の私服が未登録

## リレー実行ログ

```
🎬 CINE — 演出・カメラ・演技方針
3人が帰路を歩き続ける。MIUだけが一度だけ後ろを振り返り、それから前を向い
て歩き出す。街の夜景が遠ざかるように引いていくエンディングショット。
状態: 完了

🎭 SOUL — 感情・セリフ・心理描写
今夜の出来事は解決しないまま、それでも日常は続いていく。切なさと次への
予感が同居する余韻。
状態: 完了

📷 CUT — 絵コンテ・構図・プロンプト
3人の後ろ姿→MIUの最後の振り返り→街の夜景へ引いていくクレーンアップの
3段構図。画像/動画Promptへ変換。
状態: 完了

🛡 MASTER — Character Bible / Costume Bible / Universe Rule / Production Bible照合
3人のビジュアルはCharacter Bibleと一致。Chapter1の「続く」構成とUniverse
Ruleとの整合を確認。衣装は未登録(上記参照)。
状態: 完了
```

## シーンタイトル

エンディング

## 時間

3:00〜3:19 目安（BPM 95.7、楽曲末尾まで）

## 場所

渋谷、帰り道

## 出演者

MIU、AYA、NANA

## 演技

3人が並んで歩き続ける。MIUが一度だけ後ろを振り返り、小さく息をついてから前を向き、AYA・NANAと歩調を合わせる。

## セリフ

なし

## カメラ

3人の後ろ姿を追うミディアム → MIUの振り返りのクローズアップ → 街全体を俯瞰するクレーンアップで夜景へ引いていく

## 照明

渋谷の夜景全体、ネオンと街灯が遠くまで広がる。3人のシルエットが小さくなっていく

## 感情

解決しないまま続いていく日常への切なさと、次への静かな予感。「物語は次回へ続く」

## 画像生成Prompt

```
Three East Asian Japanese young women (MIU, AYA, NANA) walking away
from camera down a Shibuya street at night, MIU glancing back once
before facing forward again, camera slowly craning up and back to
reveal the wide glowing cityscape as the group becomes small in frame,
bittersweet anticipatory mood, cinematic wide ending shot, Soul ID
locked for consistency, 35mm film grain
```

## 動画Prompt

```
Camera follows three women from behind as they walk down the street,
MIU glances back once, then camera cranes upward and pulls back to a
wide view of the glowing Shibuya night skyline as they grow small in
frame, 8-10 seconds, ambient city hum fading with the music outro
```

## 編集指示

CUT11のMIUのセリフの余韻から直接繋ぐ。楽曲アウトロ(BPM95.7)に合わせてフェードアウト。エンドカードで「物語は次回へ続く」を示す静止テロップを想定(Palmier側で追加)。

## 4者レビュー

```
🎬 CINE「クレーンアップでの引きは楽曲アウトロと尺を合わせる調整が必要。」
🎭 SOUL「セリフなしで『続く』余韻を作れた。次章への感情の橋渡しとして機能する。」
📷 CUT「俯瞰の夜景生成は情報量が多く、Palmier側でのテロップ配置スペースを確保しておきたい。」
🛡 MASTER「Chapter1の『続く』構成とUniverse Ruleとの矛盾なし。全12カット、Character Bibleとの矛盾は衣装未登録のみ。」
```
