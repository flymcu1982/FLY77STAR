# Status

Production Start: 2026-07-10 / 現在フェーズ: **Production Phase 5(Pilot Production)**(2026-07-11、Production Baseline確定・社長承認済み)

## Phase5: Pilot Production(2026-07-11)

対象: Scene01 / CUT01(Panel01〜03)。一括制作ではなく段階的に進める。

**Director Decision(2026-07-11、社長承認・Production Baseline確定)**:

| Panel | 役割 | 状態 |
|---|---|---|
| CUT01 Panel01 | Location Validation | Go(社長承認済み、生成待ち) |
| CUT01 Panel02 | Camera Validation | Go(Panel01に続き実施) |
| CUT01 Panel03 | **Golden Production Image**(基準画像) | 今後のProduction QC・Character QC・Costume QC・Director Approvalの基準として扱う |

詳細: `Storyboard/CUT01_Panel01_PILOT_PRODUCTION.md`(Director Decision反映済み)、`Prompt/DIRECTOR_APPROVAL_SHEET.md`。

- [x] Production Prompt最終確認(Character/Costume/Location/Storyboard/Director Notes整合レビュー、Panel01)
- [x] Production QC Checklist準備(Character/Costume/Location/Lighting/Composition/Emotion、Panel01)
- [x] Director Review Point整理(5項目、Director Approval Sheet更新)
- [x] Panel02進行のGo/Hold判定 → 社長承認によりPanel01→02→03と段階的に進行(Baseline確定)
- [x] 社長レビュー・採用決定(Baseline変更を含め承認済み)
- [ ] GPT Imageでの本番生成(Panel01: Location Validationから着手)
- [ ] Image QC実施(生成後)
- [ ] Director Approval

**経緯**: 当初CUT01 Panel01を「Golden Production Image」として提出したが、Panel01・Panel02がいずれも人物不在のカット(MIU初登場はPanel3)であることが判明し、社長確認事項として提出。2026-07-11、社長判断によりPanel01=Location Validation、Panel02=Camera Validation、Panel03=Golden Production Imageへ役割を再定義(Director Decisionとして承認・確定)。

## Panel03(Golden Production Image)Production Package(2026-07-11)

`Storyboard/CUT01_Panel03_PRODUCTION_PACKAGE.md`を作成。Character Master(MIU)・Costume Master(Costume Bible未登録のため技術的仮描写)・Location Master・Story Bible・Panel Storyboard・Director Notesを統合。

- [x] ① Final Production Prompt(統合完成版)
- [x] ② Negative Prompt
- [x] ③ Production QC Checklist(Character/Costume/Emotion/Lighting/Composition/Story、本Panel抽出版)
- [x] ④ Director Approval Checklist(10項目)
- [x] ⑤ Production Report(注意点・Panel04への引き継ぎ事項)
- [ ] 社長レビュー・採用決定
- [ ] GPT Imageでの本番生成(社長承認後)

**最大のリスク**: MIUの私服がCostume Bible未登録のまま。Golden Production Imageとして採用する場合、正式デザイン確定後に再生成が必要になる可能性がある(Director Approval Checklist項目4で明示)。

## Take 1 生成直前レビュー(2026-07-11)

`Storyboard/CUT01_Panel03_Take1.md`を作成。Production Packageを基に、Take 1本番生成直前のチェック用として再整理。2026-07-11、Director方針(超自然的に見えない自然な静止、ポーズを取らない偶然の発見感)を追加反映済み。

- [x] ① Final Production Prompt(コピー使用可の完成版)
- [x] ② Negative Prompt(避けるべき描写/AI破綻防止/Character Master不一致の3分類)
- [x] ③ Director Shooting Notes(最重要演出意図3項目)
- [x] ④ Take 1 Director Goal(必達5項目)
- [x] ⑤ Take 1採用基準(Director Approved条件、7項目)
- [x] **Take 1 Production Package: 社長承認済み(2026-07-11)**
- [ ] GPT ImageでのTake 1本番生成(社長 / GPT Image運用側で実施。AI社員は画像生成を行わない、Production Policy Version 1.0準拠)
- [ ] ① Take 1生成画像の受領
- [ ] ② Production QC Report
- [ ] ③ Director Review Summary
- [ ] ④ Take 2要否の判定

**今回はTake 1のみを対象とし、Take 2・Take 3の資料は社長承認があるまで作成しない。コミット・pushはTake 1のDirector Review完了後に実施する方針だったが、2026-07-11、社長の明示的指示によりProduction Package承認状態を先行してコミット・pushする。**

## Phase4のAI社員担当範囲(確定、2026-07-11、Phase5でも継続)

- Image QC(`Prompt/IMAGE_QC_CHECKLIST.md`、生成画像提供後に実施)
- Production Report(節目ごとに提出)
- Director Approval支援(`Prompt/DIRECTOR_APPROVAL_SHEET.md`でQC結果を整理。承認自体は社長が行う)

**AI社員は画像生成を行わない。** Studio OS(`AI_WORKFLOW_V1.md`)は引き続き無改修。既存成果物(CUT01.md/CUT01_絵コンテ.md/Location Master等)は変更せず、補助資料(`CUT01_Panel01_PILOT_PRODUCTION.md`)として追加した。

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

## Production Policy Version 1.0(2026-07-11)

制作方針を正式運用へ移行。AI社員(Claude Code含む)は「生成する担当」ではなく「最高品質の制作設計を行う担当」と再定義。詳細: GitHub `IMAGE_GENERATION_POLICY.md`、Decision Log: Obsidian Vault `03_Company/Decisions/2026-07-11_Production_Policy_v1.0.md`。

制作フロー: ①AI社員が設計 → ②社長レビュー → ③採用決定 → ④GPT Imageで本番画像生成 → ⑤採用画像のみHiggsfieldへ渡し動画生成 → ⑥Palmier編集 → ⑦QC → ⑧Export

Higgsfieldクレジットは「採用が決定した素材」にのみ使用。生成回数ではなく採用率を最優先する。

**Studio OS(`AI_WORKFLOW_V1.md`)のバージョン番号(v1.2)は変更していない。**

## Production Phase 3: 画像生成仕様書完成フェーズ(2026-07-11)

Phase3は「画像生成」ではなく「画像生成仕様書完成フェーズ」として運用。実際の画像生成実行は社長承認後の別工程。

- [x] ① Character Master最終確認 — 5ファイル(MIU/AYA/NANA/KAI/HINA)を通しでレビュー。構造・一貫性アンカー・GPT Image前提の記述・キャラクター間の混同なしを確認、設計完了と判定
- [x] Location Master(Phase2で仕様策定済み、5点)
- [x] Image Asset List / Asset ID / 撮影優先順位(Phase1で作成済み)
- [x] Image QC Checklist作成 — `Prompt/IMAGE_QC_CHECKLIST.md`(Character Masterとの一致/表情/衣装/背景/Story Bibleとの整合/Panel Storyboardとの一致の6項目)
- [ ] ② 社長レビュー(YU) — 本Phase3完了パッケージの承認待ち
- [ ] ③ 採用決定
- [ ] ④ GPT Imageで本番画像生成(社長承認後、Claude Codeは実行しない)
- [ ] ⑤ 採用画像のみHiggsfieldへ渡し動画生成
- [ ] ⑥ Palmier編集
- [ ] ⑦ QC(`Prompt/IMAGE_QC_CHECKLIST.md`使用)
- [ ] ⑧ Export

## 後工程

- [x] Image Asset List / Asset ID / 撮影優先順位 / EDIT_PLAN作成(Production Phase 1)
- [x] Character Master / Location Master仕様策定(Production Phase 2)
- [x] Character Master最終確認 / Image QC Checklist作成(Production Phase 3)
- [ ] 社長レビュー・採用決定
- [ ] 本番画像生成(承認後、Higgsfield + GPT Image)
- [ ] 動画生成(採用画像のみ、Higgsfield)
- [ ] Palmier編集
- [ ] QC
- [ ] Export
