# Status

Production Start: 2026-07-10 / 現在フェーズ: **Production Phase 5(Pilot Production)**(2026-07-11、Production Baseline確定・社長承認済み)

**⚠️ Legacy notice(2026-07-16)**: 本ファイル以下のCUT01〜12構成は、2026-07-16受領のFLY77STAR CANON(`/CANON_FLY77STAR_20260716_final.md`)とは異なる物語構成(旧12カット、渋谷スクランブル交差点開始)。Director判断確定までLegacy扱い。詳細: `HANDOFF.md`、`Storyboard/00_LEGACY_STRUCTURE_NOTICE.md`。

## 🟡 HOLD: CANON準拠 Scene 1(オープニング) — 制作コスト対効果により停止(2026-07-21)

**Director Decision(2026-07-21)**: Scene 1の新規生成作業を停止。理由: C1 Visual Canon参照ファイル連携に追加対応が必要/再生成のクレジット消費・作業時間がWAKE UP完成優先方針に見合わない/最優先目標は新規オープニングの追求ではなくWAKE UP全体の完成。

- Panel 2/3/4の追加生成: **停止**(未QCジョブ `f8f04d2e`/`48fd75f3` は放置、投入済みクレジットのみで打ち切り)
- Seedance 2.0ワンカット生成: **不実行**
- 保存(再開候補): Production Package(`WAKE_UP_CANON_SCENE01_PRODUCTION_PACKAGE.md`)/Panel 1採用画像(job `29955416`)/Storyboard一式/Decision Log
- **再開条件**: ①C1参照画像を確実に直接アップロードできる環境の整備、または②低コストでVisual Canonを維持できる生成手段の確認
- Decision Log: `Obsidian_Vault/03_Company/Decisions/2026-07-21_WAKE_UP_Scene1生成停止_HOLD.md`
- 以後は既存C1素材またはLegacy素材を使用し、次の未完成工程へ戻る

以下は停止時点までの記録(保存)。

## CANON準拠 Scene 1(オープニング)Storyboard完成(2026-07-21)

CANON(§6 ACT01 SHIBUYA_NIGHT Panel 1-2)準拠の新オープニングを制作。夜の渋谷上空→降下→クラブ入口→AYA・MIU・NANA登場までのワンカット風構成(4パネル、約20秒、BPM95.7)。Legacy CUT01〜12は無変更。

- [x] `Storyboard/WAKE_UP_CANON_SCENE01_OPENING.md`(ショット構成/演出意図/画像・動画Prompt/制作注意点)
- [x] `Storyboard/WAKE_UP_CANON_SCENE01_OPENING_絵コンテ.md`(Panel Storyboard)
- [x] `Storyboard/WAKE_UP_CANON_SCENE01_PANEL04_クラブ出口3人_DirectorNotes.md`(重要Panel: 主人公初登場)
- [x] **Director承認(2026-07-21)**: ①クラブ外観=正式店名なし・LOC_CLUB_EXT01のまま・判読不能ネオン ②衣装=仮衣装で進行(識別性必須: MIU白系インナー/AYA最暗ダークトーン/NANA軽いシルエット/全員ノーロゴ) ③総尺=20秒仮ロック(5秒×4セグメント、微調整は編集工程)。Decision Log: `Obsidian_Vault/03_Company/Decisions/2026-07-21_WAKE_UP_CANON_Scene1承認.md`
- [x] `Storyboard/WAKE_UP_CANON_SCENE01_PRODUCTION_PACKAGE.md`(生成実行用: GPT Image最終プロンプト/Higgsfield投入コピペ版/Palmier接続メモ短縮版/Panel3→4接続QC)
- [x] **Director指示(2026-07-21)**: 生成実行をClaude Codeへ再委任(Production Policy v1.3の例外)。進行順Panel 1→2→3→4固定、優先順位=①位置関係②シルエット差③明度差④顔の安定⑤細部アクセサリー、Seg4はQC通過後のみ動画化、修正は各工程最大2回
- [x] Panel 1 生成ジョブ投入成功(Higgsfield Soul Cinema/soul_cinematic、16:9 2k、job: `29955416-64a1-4ac4-a5a1-a455bbc1e7f5`)
- [ ] **🚨 ブロッカー(2026-07-21)**: 結果確認ツール(job_display / show_generations)が「MCP tool call requires approval」でブロック。生成結果の受領・QCが不能のため、最優先ルールv1.2に従いPanel 2以降へ進まず停止。FLY77STAR U.の対応待ち(MCPツール承認 or Higgsfield側での結果確認)。Discovery Log: `Obsidian_Vault/02_Discovery_Log/2026-07/2026-07-21_Higgsfield_MCP承認ゲート_2026-07-21.md`
- [x] **Panel 1 Image QC通過(2026-07-21)**: Directorが結果画像をチャット貼付→Claude CodeがQC実施。藍色プリダーン・判読不能看板・実在ランドマーク無しを確認。中央下の大通りを降下パスとして採用。※結果確認ツールのブロックは継続中だが「Director貼付→QC」の運用ループで回避
- [x] Panel 2 生成ジョブ投入(job: `8ff32def-e06a-41c4-8299-ff2c4b3cfb3e`)
- [x] Panel 3 生成ジョブ投入(job: `2ded7c35-c381-4163-8abe-5f0b194cc5c1`)
- [x] **Director指示(2026-07-21)**: Panel 1画像をスタートフレームに、降下→クラブ入口までを自然につなぐワンカット設計 → Seedance 2.0のstart_image+end_image方式で設計(start=Panel 1 job / end=Panel 3 job、15秒・1080p・16:9・音声なし、Panel 2はimage_referencesで中間アンカー)。破綻時は承認済み3セグメント分割案(Seg1〜3個別+Palmier接続)へフォールバック、修正上限各2回
- [x] Panel 2・Panel 3 Take1 Image QC実施(2026-07-21、Director貼付画像): **Panel 2=不通過**(左上ネオンに判読可能な漢字様文字/大通り→路地の流れ弱い)、**Panel 3=条件付き**(ドア面ポスターの擬似文字・紋章風図形/3人分の余白不足/仕様のドア隙間暖色光漏れ無し→Panel 4の暖色逆光設計が不成立)
- [x] Panel 2 修正1回目投入(job: `f8f04d2e-9b18-4b61-a79a-e34fbf785a51`、ノーテキスト強化+大通り→路地の接続+奥に暖色の気配)
- [x] Panel 3 修正1回目投入(job: `48fd75f3-bcd2-4e96-b5d7-32ae3d0efa91`、ポスター全除去+暖色光漏れ+3人分の余白+引きフレーミング)
- [x] **Director指示(2026-07-21)**: C1画像(FLY77STAR NIGHT CLUB正面・SE77NTH CROSSING・77タワーを含むネオン密度の高い雨上がり夜景)を**Scene 1最優先Visual Canon**に指定。既生成のPanel 2/3(Take1・修正1回目 job `f8f04d2e`/`48fd75f3`)は構図検証用に格下げ、世界観・色味・建築の参照には不使用。新Panel 2/3はC1参照で「既存C1世界の中に追加する」方針(構図とカメラ位置のみ変更)。Panel 2=地上8〜12mの斜め降下視点・路地奥にクラブ入口方向、Panel 3=入口8〜10m後方の正面水平構図・3人全身の前景スペース・文字/ロゴ/ポスター完全排除で抽象ネオンラインのみ
- [ ] **ブロッカー**: C1がチャットインライン貼付のため実ファイル未着(uploads未反映)。参照付き生成にはファイル添付での再送が必要(Director依頼中)
- [ ] C1受領→media_upload→C1参照付きPanel 2/3生成(新仕様Take1)→Director貼付QC→ワンカット投入判断
- [ ] ワンカット動画投入(Panel 3 QC通過後、Seedance 2.0)
- [ ] Panel 4(3ショット)起点画像生成→QC通過後のみSeg4動画化
- [ ] Image QC(Panel 4は位置関係・シルエット・色差の固定を顔の作り込みより優先)
- [ ] 採用画像のみHiggsfieldで動画化(Seg1〜4)
- [ ] Palmier編集(接続メモ短縮版参照、イントロ実尺との微調整)

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

## Panel04 本番制作(2026-07-11)

Panel04の720pテイクは本セッション外(社長⇄ChatGPT/GPT Image/Higgsfield)で承認済み(Character/Composition/Lighting/Story/Emotion全て✅)。Production Policy Version 1.1により、Panel04以降はAI社員(Claude Code)が厳格運用サイクル(1テーク生成→停止→Director Review→明示的GOで次へ、5項目自己チェック、承認後のみ記録・コミット)のもとで本番生成を実行する。

社長より共有されたPanel04.mdの原文には、実在ブランド名(QFRONT/STARBUCKS)・Story Bible構成(ACT2「Night Walk」)・Panel Storyboard(旧「スマホを見る」との不一致)・衣装記述・ファイルパスの5点で既存プロダクション成果物との不整合を確認。生成実行を保留し社長確認を仰いだ結果、**Director Decision(2026-07-11)により全5点が解決**:

1. 実在ブランド名 → 一般表現(Iconic scramble crossing buildings等)へ差し替え
2. Story Bible → 最新版(Production Bible運用中のもの)を優先。Vault側への全文統合は別途対応
3. Panel Storyboard → 「静止していた時間が動き始める」を正式採用(`CUT01_絵コンテ.md`更新済み、旧案は「旧案(参考・廃止)」として保持)
4. Costume → Panel03と完全同一(`casual dark top with simple jeans or skirt, no visible logos or brand marks`)へ修正
5. File Path → 実在パスへ修正

`Storyboard/WAKE_UP_CUT01_PANEL04_静止時間動き出し_PRODUCTION_PACKAGE.md`をDirector Decision反映版に更新。コミット・push後、720P Pilot Generationへ進行予定。

- [x] Director Decision(5点)反映
- [x] `CUT01_絵コンテ.md` Panel4更新
- [x] `WAKE_UP_CUT01_PANEL04_静止時間動き出し_PRODUCTION_PACKAGE.md`修正版作成
- [x] 技術検証タスク: `generate_video`含むHiggsfield MCP生成系ツールがこの環境では実行不可能と確定
- [x] **Production Policy Version 1.3: AI社員による生成実行の例外(v1.1〜v1.2)を撤回。生成実行はDirector/GPT Image運用側へ復帰**
- [ ] **保留中**: DirectorよりPanel04の5点(実在ブランド名/Story Bible/Panel Storyboard/Costume/File Path)について「未解決のまま」との指示があったが、上記の通り本セッション内で既にDirector Decisionとして解決・コミット済み(`b72ea77`)。矛盾があるためDirectorへ確認依頼中。回答を待ってからProduction Package再作成に着手
- [ ] 720P Pilot Generation(Director/GPT Image運用側が実施)
- [ ] 4K Production Generation(承認後)

**2026-07-12追記**: 別件のCUT05→CUT06 Director Decision(下記参照)は、このPanel04の5点を解決するものではない。Panel04の矛盾は本追記時点でも未解決のまま。

## CUT05→CUT06(POP DINERへの接近シーン)Director Decision(2026-07-12)

POP DINERへ向かう追加の歩行テイクは削除。入口を通り過ぎてから戻るように見える動線は不採用(歩行シーンが過剰になるため、該当テイクは本編に使用しない)。次の正式な展開は、CUT06 Panel1(AYAがPOP DINERのドアを開けるシーン、旧「誰の視点かは限定しない」から視点をAYAへ固定)から開始する。前後の接続は編集(Palmier)で補完する。

- [x] `Storyboard/CUT05_絵コンテ.md`: Panel3→4以降に歩行・接近の追加テイクを挟まない旨を追記
- [x] `Storyboard/CUT06_絵コンテ.md`: Panel1のパネル構成表・本文をAYA視点固定へ更新(旧案は「旧案(参考・廃止)」として保持)
- [x] `Storyboard/CUT06_Panel01_DirectorNotes.md`: 役者への演技指示をAYA視点固定へ更新
- [x] Decision Log・Discovery Log記録
- [x] `Obsidian_Vault/08_Studio_OS/Rules/テイク修正上限ルール.md`(同一テイク修正上限2回)を適用ルールとして明記

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
