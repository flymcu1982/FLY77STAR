# WAKE UP — 3人ダンスオープニング Generation Prompt設計

Production Package(設計フェーズ)。AI社員(Claude Code)はプロンプト設計のみを担当し、実際の生成実行はDirector/GPT Image運用側が行う(Production Policy Version 1.3準拠、`IMAGE_GENERATION_POLICY.md`)。

## 前提条件

- ツール: Higgsfield Cinema Studio 3.0 / 3.5
- 尺: 5.04秒
- テンポ: 約95.7 BPM
- 主体: MIU(中央)・AYA(左)・NANA(右)、POP DINER店内
- 手法: 3人のダイナー衣装シートをElementsとして使用(画像リファレンスアップロード方式ではない)
- **重要な前提の確認事項**: 2026-07-11の技術検証タスクにより、この実行環境からHiggsfield MCPの`models_explore`/`show_reference_elements`等への確実なアクセスは検証できていない(詳細: Discovery Log 2026-07-11)。今回のダイナー衣装シート(MIU/AYA/NANA)がElementsとして実際に登録済みかどうかは、本ドキュメント作成時点で確認していない。下記プロンプト中の `@MIU_Diner` 等はプレースホルダーであり、**生成前に実際のElement名への置き換えが必要**。

## Elements方式での設計方針(既知の学び)

Panel04開発時のDiscovery Log(2026-07-11)より: Higgsfield Elements(@-mention)経由の生成では「@-mention + 最小限テキスト」が最も精度が高く、テキストで容姿・衣装を説明し直すとむしろ崩れやすい。本プロンプトはこの学びに従い、**Elementsに任せられる情報(顔・衣装)は極力言葉で説明しない**方針で設計する。

---

## 1. 本命プロンプト(Cinema Studio用)

```
[主体]
Three idol members performing synchronized choreography inside a retro
American diner. @MIU_Diner centered, @AYA_Diner stage-left, @NANA_Diner
stage-right. Fixed positions held for the full duration — no swapping,
no drifting.

[ダンス]
Tight, sharp K-pop girl-group choreography. Unison isolations, grounded
stance, weight shifts locked to a strong downbeat. Restrained, confident
energy.

[カメラ]
Slight low angle, subtle handheld sway, slow continuous push-in toward
the group across the full shot.

[固定条件]
Duration 5.04s. Motion tempo locked to 95.7 BPM. Retro diner interior
background, warm neon lighting.

[禁止事項]
No cute idol expression, no peace signs, no explanatory hand gestures,
no static locked-off camera, no position swapping, no face or limb
distortion, no duplicated figures, no extra logos or text beyond the
Elements.
```

**設計意図(セクション対応)**:

| セクション | 目的 |
|---|---|
| 主体 | 3人の顔・立ち位置をElementsに委ね、位置だけを1回だけ明記(位置情報の重複記述はドリフトの原因になるため避けた) |
| ダンス | 「K-pop girl-group」「isolations」「grounded stance」という具体語で、可愛いアイドル寄り・抽象的すぎる指定の両方を回避 |
| カメラ | 「push-in」1つの動きに絞り、パン・ズーム・オービット等を同時指定しない(矛盾回避) |
| 固定条件 | 尺・BPMという機械的パラメータのみ。演出指示はここに混ぜない |
| 禁止事項 | 実際に起きた失敗パターン(J-POP寄り・説明ジェスチャー・固定カメラ・崩れ)に直接対応させた |

---

## 2. 最必要最小限であることの確認

- 各セクション1〜2文。装飾的な形容詞の重ね掛けをしていない(「指示を増やしすぎると崩れる」という既知の問題への対応)
- 衣装・髪型・表情の詳細記述は一切含めない(Elementsに委ねる)
- カメラ指示は「push-in」1種類のみ

---

## 3. セクション分け(再掲・確認用)

主体 / ダンス / カメラ / 固定条件 / 禁止事項 の5分割。本命プロンプトの `[ ]` 見出しと対応。

---

## 4. 矛盾チェック

- 「grounded stance(地に足がついた構え)」と「handheld sway(手持ちの微揺れ)」は主体とカメラで役割が分離しており矛盾しない(被写体は安定、カメラは軽く揺れる)
- 「push-in」1方向のみを指定し、オービット・パン・ズームアウト等の相反する動きを含めていない
- 「sharp isolations」と「no explanatory hand gestures」は同じ方向性(鋭く・説明的でない)で矛盾しない

---

## 5. 最重要文の説明

優先順位順:

1. **`Fixed positions held for the full duration — no swapping, no drifting.`**
   3人の顔と立ち位置維持が今回の最大要件。ここが崩れると他の全要素が無意味になるため最優先。
2. **`no explanatory hand gestures`**(禁止事項内)
   「抽象的なダンス指定で腕の説明ジェスチャーが増える」という既知の失敗に直接対応。これが無いと最も再現性高く失敗する。
3. **`Slight low angle, subtle handheld sway, slow continuous push-in`**
   「人物が背景に貼り付いたように見える」問題への対応。ただし1文にまとめ、複数のカメラ動作を並列指定しない。
4. **`Duration 5.04s. Motion tempo locked to 95.7 BPM.`**
   機械的パラメータで、プロンプトの「解釈」に依存しないため失敗リスクは相対的に低い。優先度は最後。

---

## 6. 失敗時の修正版(それぞれ変更点1つのみ)

### 修正版A(顔・立ち位置が崩れる場合)

**変更点**: カメラ指示を一切削除し、Elements依存度をさらに上げる。

```
[カメラ]
Static camera.
```

(他のセクションは本命プロンプトのまま。カメラ動作の記述量を減らすことで、Elements由来の顔・衣装情報への「予算」を確保する狙い)

### 修正版B(ダンスが説明ジェスチャーに寄る場合)

**変更点**: 「ダンス」セクションをさらに抑制的な表現に置き換える。

```
[ダンス]
Restrained micro-movements only. Weight shifts on the beat. No arm
choreography.
```

(他のセクションは本命プロンプトのまま)

### 修正版C(人物が背景に貼り付いたように見える場合)

**変更点**: 「push-in」を「orbit」に変更(動き自体の質を変える、複数動作の追加はしない)。

```
[カメラ]
Slight low angle, subtle handheld sway, slow orbit around the group.
```

(他のセクションは本命プロンプトのまま)

---

## 7. Seedance 2.0 / Kling 3.0への移植差分

**確認できていない前提**: `models_explore`(モデルカタログ確認)は2026-07-11の技術検証タスクの時点でこの環境から実行できていない(承認待ちでブロック、詳細はDiscovery Log参照)。以下はHiggsfield MCPツール自体の説明文(`generate_video`ツールの利用ガイド)から分かる範囲の一般的な差分であり、各モデルの正確なタグ構文・パラメータ名は未確認。**実際の移植時は、生成前にDirector側で構文を確認すること。**

| 項目 | Higgsfield Cinema Studio(本命) | Seedance 2.0 | Kling 3.0 |
|---|---|---|---|
| 位置づけ | Elements(@-mention)による顔・衣装の同一性担保が前提 | ツール説明上「identity」に強いモデルとされる。Elements的な@-mention機構を持つかは未確認 | ツール説明上「multi-shot/audio/motion transfer」向け。単一ショットの振付ダンスでは過剰スペックの可能性 |
| 移植時の主な差分 | 本ドキュメントの構成そのまま使用可 | @-mention構文が同一かどうか未確認 → 未確認の場合は顔参照を画像アップロード方式に切り替える必要がある可能性 | マルチショット機能を持つため、5秒single-shotの場合は機能を使わない設定が必要な可能性。turbo版(`kling3_0_turbo`)は「fast text-to-video/単一開始フレームアニメーション」向けとツールガイドに明記されており、こちらの方が今回の用途に近い可能性 |
| 変更不要な部分 | — | 「主体/ダンス/カメラ/固定条件/禁止事項」の5分割構造、禁止事項の内容(J-POP寄り回避・説明ジェスチャー回避・固定カメラ回避)はモデルに依存しない設計思想のため、そのまま流用可能 | 同左 |

---

## 関連

- Discovery Log: `Obsidian_Vault/02_Discovery_Log/2026-07/2026-07-11_WAKE_UP.md`(Elements方式の学び、MCP承認待ちブロッカー)
- `IMAGE_GENERATION_POLICY.md`(Production Policy Version 1.3)
- `Obsidian_Vault/08_Studio_OS/Rules/テイク修正上限ルール.md`(修正2回でボツ判断)
