# CUT01 — WAKE UP（SE77NTH.）

AI社員ワークフロー試験運用(2026-07-10)。CINE→SOUL→CUT→MASTERのリレーで生成。完成度確認用ではなく、リレーが機能するかの確認が目的。

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

---

## リレー記録

| 担当 | 出力 |
|---|---|
| CINE(演出) | シーン設計・カメラ・照明・演技方針を決定 |
| SOUL(感情) | 感情の核とセリフ有無を決定(ノンバーバル判断) |
| CUT(絵コンテ) | 構図・画像生成Prompt・動画Promptに変換 |
| MASTER(確認) | Character Bible / 命名規則 / AI Production Policyと照合(下記) |

### MASTER確認結果

- MIUのビジュアル(ロング緩巻きライトブラウン+白ヘアバンド/グロスリップ/ゴールド系アクセ)は [[10_Characters/MIU]] の設定と一致 ✓
- 「FLY77STAR. CLOSET」表記は77ルール(77を埋め込み読まない)・末尾ドット規則に準拠 ✓
- 実在ブランドは使用せず、架空ブランドとして明記(AI Production Policy準拠) ✓
- ⚠️ MIUの「FLY77STAR. CLOSET」店員としての衣装は [[11_Costume_Bible]] に未登録。本CUTでは仮に私服+エプロン想定とし、正式デザインは別途Costume Bibleへ登録が必要
- CUT01時点でSE77NTH.の他メンバー(AYA/NANA)は未登場。[[06_Projects/WAKE_UP/Overview|WAKE UP概要]]の物語構成(閉店→POP DINERでの夢)と矛盾なし
