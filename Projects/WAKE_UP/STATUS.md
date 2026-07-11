# Status

Production Start: 2026-07-10 / 現在フェーズ: **Production Phase 2**(2026-07-11、Character Master / Location Master仕様策定 → 画像生成エンジン方針修正)

## Story Bible改訂(2026-07-10)

旧コンセプト(31カット、MIU単独の閉店→POP DINER夢オチ)を廃止し、渋谷を舞台にしたAYA/MIU/NANA3人+KAI+HINAの群像劇(12カット、SE77NTH.第一章)に差し替え。詳細はObsidian Vault `06_Projects/WAKE_UP/Overview.md` を参照。

## Storyboard進捗(Studio OS標準ワークフロー Version 1、`AI_WORKFLOW_V1.md`)

全12カット中、Storyboard/Script/Image Prompt/Video Prompt/Reviewが揃ったCUT数: 12/12(新Story Bibleで全カット制作完了。画像/動画生成は未着手)

Panel Storyboard(Step 3.5、映画レベル絵コンテ)進捗: 12/12(CUT01〜12全てで`CUT<番号>_絵コンテ.md`を作成済み。2026-07-10、CUT01での試作を経てFLY77STAR標準フォーマットとして正式採用)

Director Notes(Step 3.6、重要Panelのみ、Studio OS v1.2)進捗:
- [x] CUT01 Panel03(主人公初登場/静止の発見)
- [x] CUT02 Panel01(主人公初登場、AYA)
- [x] CUT03 Panel01(主人公初登場、NANA)・Panel04(象徴カット、3人集結)
- [x] CUT04 Panel01(感情変化、CUT03→CUT04の感情のバトン)
- [x] CUT05 Panel01(伏線、違和感の始まり)
- [x] CUT06 Panel01(世界観説明、ダイナーへの境界)
- [x] CUT07 Panel02(主人公初登場、KAI=コックとしてのみ登場)
- [x] CUT08 Panel04(象徴カット、現実ではない空気の完成)
- [x] CUT09 Panel01(象徴カット、WAKE UP=覚醒の体現)
- [x] CUT10 Panel02(伏線、KAIとの現実でのすれ違い)
- [x] CUT11 Panel01(主人公初登場、HINA)
- [x] CUT12 Panel04(ラストカット、次回への余韻)

## Scene構成

- **Scene1**(CUT01〜04): 渋谷の夜、3人集合〜歩き出す
- **Scene2**(CUT05〜08): 「現実からパラレルワールドへの入口」— 制作完了(2026-07-11)。詳細: [[Storyboard/Scene2_Review|Scene2 Review]]
- **Scene3**(CUT09〜12): 「夢から現実へ」— 制作完了(2026-07-11)。詳細: [[Storyboard/Scene3_Review|Scene3 Review]]

全12カット、Panel Storyboard・Director Notes(重要Panel12件)が出揃い、Storyboard工程が完了。

- [x] CUT01 — 渋谷
- [x] CUT02 — AYA到着
- [x] CUT03 — 3人集合
- [x] CUT04 — 歩き出す
- [x] CUT05 — ダイナー発見
- [x] CUT06 — 店内
- [x] CUT07 — KAI登場
- [x] CUT08 — パラレル終了
- [x] CUT09 — 現実
- [x] CUT10 — KAIとすれ違う
- [x] CUT11 — HINA登場
- [x] CUT12 — エンディング

## Production Phase 1(2026-07-11)

- [x] Image Asset List作成(全12CUT・51Panel、Character Master 5点・Location Master 5点を含む)。実体: `Prompt/IMAGE_ASSET_LIST.md`
- [x] Asset ID付与(命名規則: `CUT<番号>_P<パネル>_<種別><連番>`)
- [x] 撮影優先順位整理(画像生成順・動画生成順)。実体: `Prompt/IMAGE_ASSET_LIST.md`内
- [x] EDIT_PLAN作成(Timeline/BGM/SE/Transition/Camera Motion/Dialogue Sync/Color Plan)。実体: `Edit/EDIT_PLAN.md`

**Phase 1完了時点のブロッカー**: Character Master Reference(5キャラクター)・Costume Bible(全キャラクター衣装)・Dialogue音声、いずれも未着手/未登録。Phase 2(実際の画像生成)着手前に要対応。

## Production Phase 2(2026-07-11)

Character Master Reference仕様策定完了。真正面/左右45°/横顔/全身/表情差分(6種)を全キャラクターで統一フォーマット化。

### 制作方針修正(2026-07-11)

画像生成エンジンを **Higgsfield / Nano Banana → Higgsfield / GPT Image** へ変更。Nano BananaはProductionフローから除外。Soul 2(Higgsfield Soul 2.0)はProduction標準では使用せず、Character Masterにも使用しない(アーティスト写真・ファッションカット・SNSビジュアル・雰囲気重視の一枚絵・コンセプトアートに限定使用)。詳細: `IMAGE_GENERATION_POLICY.md`(リポジトリルート、新設)。Decision Log記録: Obsidian Vault `03_Company/Decisions/2026-07-11_画像生成エンジン方針変更.md`。

5点のCharacter Masterファイル(`Reference/CHAR_*_MASTER.md`)は本方針に合わせて更新済み(タイトル・Lock Prompt・一貫性アンカーの各セクションからSoul ID/Soul 2表記を除去し、GPT Image前提の記述に統一)。Studio OS(`AI_WORKFLOW_V1.md`)のバージョン番号(v1.2)は変更していない。

**既知の残課題**: `Storyboard/CUT<番号>.md`・`CUT<番号>_絵コンテ.md`・Director Notes・`Edit/EDIT_PLAN.md`内に残る"Soul ID locked for consistency"等の表記は、本方針変更時点では遡及的に修正していない(Discovery Log記録済み)。

- [x] CHAR_MIU_MASTER01 — `Reference/CHAR_MIU_MASTER.md`
- [x] CHAR_AYA_MASTER01 — `Reference/CHAR_AYA_MASTER.md`
- [x] CHAR_NANA_MASTER01 — `Reference/CHAR_NANA_MASTER.md`
- [x] CHAR_KAI_MASTER01 — `Reference/CHAR_KAI_MASTER.md`(MA-1期、"East Asian Japanese"必須明記)
- [x] CHAR_HINA_MASTER01 — `Reference/CHAR_HINA_MASTER.md`

Location Master(ロケーション基準)仕様策定完了。

- [x] LOC_CROSSING01(渋谷スクランブル交差点) — `Reference/LOC_CROSSING_MASTER.md`
- [x] LOC_STREET01(大通り〜路地) — `Reference/LOC_STREET_MASTER.md`
- [x] LOC_DINER_EXT01(POP DINER外観) — `Reference/LOC_DINER_EXT_MASTER.md`
- [x] LOC_DINER_INT01(POP DINER内装、CUT08崩壊VFXバリエーション含む) — `Reference/LOC_DINER_INT_MASTER.md`
- [x] LOC_SIDEWALK01(帰り道、CUT09空き区画〜CUT12夜景まで) — `Reference/LOC_SIDEWALK_MASTER.md`

**衣装は全キャラクターCostume Bible未登録のため、生成の一貫性維持のみを目的とした中立的な仮描写を採用(創作上の衣装デザイン決定ではない)。正式デザイン確定後、各Character Masterファイルの更新とCostume Bible登録が必要。**

## 後工程

- [x] Image Asset List / Asset ID / 撮影優先順位 / EDIT_PLAN作成(Production Phase 1)
- [x] Character Master / Location Master仕様策定(Production Phase 2)
- [ ] Character Master / Location Masterの実画像生成(Higgsfield + GPT Image)
- [ ] CUT素材配置(画像/動画生成)
- [ ] Palmier編集
- [ ] QC
- [ ] Export
