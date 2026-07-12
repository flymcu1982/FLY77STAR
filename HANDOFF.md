# HANDOFF.md

現在の作業状態の引き継ぎ記録。Claude Code / Codex どちらが作業する場合も、着手前に本ファイルを確認すること。作業終了時は必ず本ファイルを更新してから次の担当に渡す。

最終更新: 2026-07-11(Claude Code)

## 現在のプロジェクト

WAKE UP(`Projects/WAKE_UP/`)

## 現在の工程

Production Phase 5。CUT01のPanel単位パイロット制作中。Production Policy Version 1.3準拠(`IMAGE_GENERATION_POLICY.md`)。

**技術検証タスクの結論(2026-07-11)**: `generate_video`(get_cost:trueの無課金見積りプリフライトを含む)も含め、Higgsfield MCP経由の生成系ツールはこの環境(managed remote execution environment)では承認待ちにより実行不可能と確定。Director判断により、**v1.1で導入した「AI社員による生成実行」の例外はv1.3で撤回**。生成実行はDirector/GPT Image運用側へ戻った。AI社員はProduction Package作成・QC・記録・Git管理を担当する原則に復帰。

**現在の状態(2026-07-11)**: Directorより「CUT01 Panel04のProduction Package再作成は、絵コンテ側の未解決5点(実在ブランド名/Story Bible版/Panel Storyboard整合/衣装記述矛盾/ファイルパス不一致)についてDirectorが判断した後に指示する」との指示があり、待機中。**⚠️留意**: この5点は、本セッション内で同日(2026-07-11)に一度「Director Decision」として解決済み・コミット済み(commit `b72ea77`、`Storyboard/CUT01_Panel04_PRODUCTION_PACKAGE.md`修正版・`CUT01_絵コンテ.md`更新・Decision Log記録)。最新のDirector指示はこれを「未解決のまま」としており、両者に矛盾があるためClaude Codeより確認依頼中(次に対応するAIは、Directorへこの矛盾を確認してから作業すること)。

## Production Baseline(Director Decision、2026-07-11)

| Panel | 役割 | 状態 |
|---|---|---|
| CUT01 Panel01 | Location Validation | Go(社長承認済み、未生成) |
| CUT01 Panel02 | Camera Validation | Go(未生成) |
| CUT01 Panel03 | **Golden Production Image**(基準画像) | Take1 Production Package社長承認済み(未生成) |
| CUT01 Panel04 | 本番制作(720pテイクを本セッション外で承認済み) | **生成実行はDirector側へ復帰(v1.3)。Production Package再作成はDirectorの5点再判断待ちで保留中(下記「現在の工程」の留意事項参照)** |

## 完了済み

- Character Master 5点(MIU/AYA/NANA/KAI/HINA)、Location Master 5点(いずれも設計のみ、生成画像なし)
- Image Asset List / Asset ID / 撮影優先順位 / Image QC Checklist / Director Approval Sheet
- CUT01 Panel01 Pilot Production(Location Validation)、Panel03 Production Package + Take1レビュー(Golden Production Image)
- MIU Diner Ver.・AYA Diner Ver.・NANA Diner Ver.・KAI Cook Ver.(衛生仕様修正版) — 衣装、Costume Bible未登録
- Panel04: 720pテイクが本セッション外(社長⇄ChatGPT/GPT Image/Higgsfield)で承認済み(Character/Composition/Lighting/Story/Emotionすべて問題なしと判断)
- Panel04.md原文と既存プロダクション成果物の不整合5点(実在ブランド名/Story Bible/Panel Storyboard/Costume/File Path)を検出し生成保留、Director Decision(2026-07-11)で全点解決。`Storyboard/CUT01_Panel04_PRODUCTION_PACKAGE.md`を修正版として更新、`CUT01_絵コンテ.md` Panel4も更新済み

## 重要決定

- HINAはソロアーティスト(SE77NTH.のメンバーではない)。**Character Bibleへの正式反映・Decision Log記録はまだ未実施(下記「次の作業」参照)**
- 通常の画像制作はGPT Imageを標準とする。Nano BananaはProductionフローから除外
- Soul 2(Higgsfield Soul 2.0)は雰囲気重視の限定用途のみ。Character Masterには使用しない
- **2026-07-11、Production Policy Version 1.1: WAKE UP Panel04以降、AI社員(Claude Code)がHiggsfield/GPT Imageでの本番生成を実行する運用へ変更。** ただし厳格運用サイクル必須(1テーク生成→自己チェック→改善提案→Director Review→明示的GOで次へ、承認後のみ記録・コミット)。Panel01〜03はこの変更の対象外(引き続き社長/GPT Image側が生成)
- **2026-07-11、Production Policy Version 1.3: 上記v1.1の例外を撤回。** 技術検証タスクで`generate_video`含むHiggsfield MCP生成系ツールがこの環境で実行不可能と確定したため、生成実行はDirector/GPT Image運用側へ戻った。AI社員はProduction Package作成・QC・記録・Git管理を担当する原則に復帰
- **2026-07-11、Studio OS v1.3: 「調査タスクと制作タスクの分離」を運用原則として正式採用(`AI_WORKFLOW_V1.md`)。** 調査タスク(MCP/API/Higgsfield/Git/外部サービス/モデル確認/権限確認)で技術的ブロッカーが発生した場合、制作タスク(Production Package/画像生成/動画生成/QC/Documentation)へ進まず、技術課題解決→Director報告→解決後に制作再開、の順を守る。Production EnvironmentをProductionより優先
- **2026-07-11、Production Policy Version 1.2: 「分からないまま進まない」を最優先原則として明文化。** MCP・外部サービス・APIで承認待ち・権限不足に遭遇した場合、推測・代替値では絶対に進めず、①何を実行しようとしたか②何がブロックされたか③何が分かっていて何が分からないか④Directorに何を確認してほしいか、の4点整理で必ず報告・停止する。同一Seedを取得できない場合はDirector Approved Pilotをbaselineとして4K生成する運用も新設。Panel04の720P Pilot Generation試行中に発生したHiggsfield MCP承認待ちブロッカーへの対応がこのルール制定の契機
- 実際の画像は原則として社長とChatGPT側で制作・採用する(Panel04以降のみ例外)
- AI社員は設計、文書化、QC、登録、レビューを担当する
- KAIコック衣装では指輪、時計、ブレスレットを外し、7ネックレスは制服内へ収納。両耳ダイヤスタッドを採用(Cook Ver.限定の承認済み仕様、通常Character Masterは上書きしない)
- MIU Golden Reference v1.0(Panel04開発より): 赤いハートネックレス/ブレスレット/フープピアス。CHAR_MIU_MASTER.mdへの反映要確認(下記「次の作業」)

## 次の作業

- **最優先**: Directorへ「Panel04絵コンテ5点は本セッション内で一度解決済み・コミット済み(commit `b72ea77`)」という矛盾を確認する。Directorの回答を待ってからPanel04 Production Packageの再作成に着手する(現時点では待機、無断で再作成しない)
- HINAをソロアーティストとしてCharacter Bibleへ正式反映する
- Decision Logへ決定を記録する
- Discovery Logの「HINA: SE77NTH. VOCAL」矛盾を解決済みに更新する
- 完成したCharacter MasterとCostume Masterを登録し、Image QCとDirector Approval Sheetを更新する
- Story Bible: ACT2「Night Walk」構成のObsidian Vault Story Bible(`06_Projects/WAKE_UP/Overview.md`)への統合(社長より全文共有があれば対応)

## 禁止事項

- 完成画像の再生成(Director承認済みのものを無断で作り直さない)
- 承認済み設定の変更
- HINAをSE77NTH.メンバーとして登録すること
- Studio OSの無断改修(`AI_WORKFLOW_V1.md`のバージョン番号、現行v1.3)
- 調査タスク(MCP/API/Higgsfield/Git/外部サービス確認等)で技術的ブロッカーが発生した状態のまま制作タスクへ進むこと(Studio OS v1.3、「調査タスクと制作タスクの分離」)
- AI社員が本番画像・動画生成を実行すること(Version 1.3で撤回済み。Panel04も含め全カットでDirector/GPT Image運用側が実行する)
- MCP・外部サービス・APIが承認待ち/権限不足の場合に、推測のモデルID・Seed・代替値で処理を進めること(Version 1.2、最優先禁止事項)
- Directorの明示的な指示なしにPanel04 Production Packageを再作成すること(5点の再判断待ちで保留中)

## 関連ファイル

- `Projects/WAKE_UP/STATUS.md`(プロジェクト進捗)
- `Projects/WAKE_UP/PRODUCTION_BOARD.md`(Production Board)
- `Projects/WAKE_UP/Reference/CHAR_*_MASTER.md`(Character Master仕様)
- `Projects/WAKE_UP/Prompt/IMAGE_QC_CHECKLIST.md`(Image QC基準)
- `Projects/WAKE_UP/Prompt/DIRECTOR_APPROVAL_SHEET.md`(承認トラッキング)
- `Projects/WAKE_UP/Storyboard/CUT01_Panel03_Take1.md`(Golden Production Image Take1レビュー)
- `IMAGE_GENERATION_POLICY.md`(Production Policy Version 1.3)
