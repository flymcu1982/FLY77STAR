# CUT01 — WAKE UP（SE77NTH.）

Studio OS標準制作ワークフロー Version 1(詳細: GitHub `AI_WORKFLOW_V1.md`)で生成。2026-07-10、Production Start(Pre Production)。本番CUTとして確定。

## 生成前チェック

- Character Bible: MIU([[10_Characters/MIU|MIU]])のビジュアル・性格設定を確認
- Costume Bible: MIUの「FLY77STAR. CLOSET」店員衣装は [[11_Costume_Bible/_Index|Costume Bible]] に未登録
- Universe Rule: [[10_Characters/FLY77STAR_Universe|FLY77STAR Universe]] 「キャラクターは時間を生きる」— CUT01時点のMIUは現行era、矛盾なし
- Production Bible: GitHub `PRODUCTION_BIBLE.md` のAI Production Policy(架空ブランドの明記)を確認
- 矛盾: あり(軽微) — MIUの店員衣装が未登録のため、本CUTでは仮の私服+エプロン想定で進行。正式デザインが決まり次第、[[11_Costume_Bible/_Index|Costume Bible]] への登録と本CUTの差し替えが必要

## リレー実行ログ

```
🎬 CINE — 演出・カメラ・照明・演技方針
「FLY77STAR. CLOSET」閉店後、MIU単独のシーンを設計。Limp Bizkit "Take a Look
Around"の潜入トーンを踏襲し、ワイド→手元クローズ→ワイドの緩やかなドリーインと、
店内灯を一つずつ落とす照明を指定。
状態: 完了

🎭 SOUL — 感情・セリフ・心理描写
感情の核を「日常への疲労の奥にある、まだ諦めていない憧れ」に設定。後半のPOP
DINERパートへの伏線として機能させる。セリフは無し(ノンバーバル)と判断。
状態: 完了

📷 CUT — 絵コンテ・構図・プロンプト
CINE/SOULの出力を構図(ワイド→クローズ→ワイド)に変換し、画像生成Prompt・動画
Promptへ落とし込んだ。
状態: 完了

🛡 MASTER — Character Bible / Costume Bible / Universe Rule / Production Bible照合
MIUのビジュアルはCharacter Bibleと一致。衣装はCostume Bible未登録(上記「生成前
チェック」参照、仮置きで進行)。Universe Rule・Production Bibleとの矛盾なし。
状態: 完了
```

## シーンタイトル

閉店 — FLY77STAR. CLOSET

## 時間

0:00〜0:06 目安（イントロ帯、BPM 95.7）

## 場所

アパレル店「FLY77STAR. CLOSET」店内、閉店後

## 出演者

MIU

## 演技

疲れを滲ませながらも、閉店作業を淡々とこなす。ふと手を止め、窓の外を一瞬だけ見つめる。

## セリフ

なし（ノンバーバル。BPM同期のイントロ帯に割り当て）

## カメラ

ワイドショット → 手元のクローズアップ → ワイドへ戻る、緩やかなドリーイン

## 照明

店内灯を一つずつ落としていく。最終カットはネオン看板の光のみが残る、寒色系。

## 感情

日常への疲労の奥にある、まだ諦めていない憧れ（後半のPOP DINERパートへの伏線）

## 画像生成Prompt

```
Wide shot, East Asian Japanese young woman (MIU), long light brown loose wavy hair
with white hairband, glossy warm-toned lips, gold accessories, closing an apparel
shop alone at night, shop sign reads "FLY77STAR. CLOSET" (fictional brand), retail
interior with clothing racks, warm shop lights turning off one by one, cool blue
dusk light from outside window, cinematic wide angle, contemplative tired mood,
Soul ID locked for consistency, 35mm film grain
```

## 動画Prompt

```
Slow dolly-in from wide shot to close-up on hands folding clothes, then pull back
to wide as the final light switches off, neon sign glow remains, ambient night
city sound, 5-6 seconds, subtle handheld drift, light-off timed to BPM 95.7 downbeat
```

## 編集指示

イントロのBPM頭に照明が落ちるタイミングを同期させる。次CUT（POP DINERへの移動、または眠りに落ちる描写）への繋ぎは暗転からのクロスフェードを想定。

## 4者レビュー

```
🎬 CINE「導入演出は完成しました。潜入トーンはCUT02以降でも踏襲したい。」
🎭 SOUL「今回はノンバーバルが正解。次のCUTで内面がもう少し見える表情が欲しい。」
📷 CUT「画像生成向けの構図は調整可能。衣装確定後にプロンプトの再調整が必要。」
🛡 MASTER「Character Bible・Universe Ruleとの整合はOK。Costume Bible登録が残課題。」
```
