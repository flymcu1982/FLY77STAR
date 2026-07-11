# HANDOFF.md

現在の作業状態の引き継ぎ記録。Claude Code / Codex どちらが作業する場合も、着手前に本ファイルを確認すること。作業終了時は必ず本ファイルを更新してから次の担当に渡す。

最終更新: 2026-07-11(Claude Code)

## 現在のプロジェクト

WAKE UP(`Projects/WAKE_UP/`)

## 現在の工程

Production Phase 5。CUT01のPanel単位パイロット制作中。Production Policy Version 1.1準拠(`IMAGE_GENERATION_POLICY.md`)。

## Production Baseline(Director Decision、2026-07-11)

| Panel | 役割 | 状態 |
|---|---|---|
| CUT01 Panel01 | Location Validation | Go(社長承認済み、未生成) |
| CUT01 Panel02 | Camera Validation | Go(未生成) |
| CUT01 Panel03 | **Golden Production Image**(基準画像) | Take1 Production Package社長承認済み(未生成) |
| CUT01 Panel04 | 本番制作(720pテイクを本セッション外で承認済み) | **Director Decision(5点: 実在ブランド名/Story Bible/Panel Storyboard/Costume/File Path)反映済み。コミット・push後、720P Pilot Generationへ進行予定** |

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
- **2026-07-11、Production Policy Version 1.1: WAKE UP Panel04以降、AI社員(Claude Code)がHiggsfield/GPT Imageでの本番生成を実行する運用へ変更。** ただし厳格運用サイクル必須(1テーク生成→停止→Director Review→明示的GOで次へ、5項目自己チェック、承認後のみ記録・コミット)。Panel01〜03はこの変更の対象外(引き続き社長/GPT Image側が生成)
- 実際の画像は原則として社長とChatGPT側で制作・採用する(Panel04以降のみ例外)
- AI社員は設計、文書化、QC、登録、レビューを担当する
- KAIコック衣装では指輪、時計、ブレスレットを外し、7ネックレスは制服内へ収納。両耳ダイヤスタッドを採用(Cook Ver.限定の承認済み仕様、通常Character Masterは上書きしない)
- MIU Golden Reference v1.0(Panel04開発より): 赤いハートネックレス/ブレスレット/フープピアス。CHAR_MIU_MASTER.mdへの反映要確認(下記「次の作業」)

## 次の作業

- Panel04 Production Package(Director Decision反映済み)を基に、720P Pilot Generationを実行 → 厳格運用サイクルに従い1テーク生成ごとにDirector Reviewを待つ
- 720P Pilot承認後、同一シード/プロンプト構成のまま4K・Cinema Studio(Ultra)で本番生成
- HINAをソロアーティストとしてCharacter Bibleへ正式反映する
- Decision Logへ決定を記録する
- Discovery Logの「HINA: SE77NTH. VOCAL」矛盾を解決済みに更新する
- 完成したCharacter MasterとCostume Masterを登録し、Image QCとDirector Approval Sheetを更新する
- Story Bible: ACT2「Night Walk」構成のObsidian Vault Story Bible(`06_Projects/WAKE_UP/Overview.md`)への統合(社長より全文共有があれば対応)

## 禁止事項

- 完成画像の再生成(Director承認済みのものを無断で作り直さない)
- 承認済み設定の変更
- HINAをSE77NTH.メンバーとして登録すること
- Studio OSの無断改修(`AI_WORKFLOW_V1.md`のバージョン番号、現行v1.2)
- Panel04以降の生成実行において、厳格運用サイクル(1テーク→停止→Review→GO)を破ること
- Panel01〜03(Panel04の許可範囲外)で無断生成すること

## 関連ファイル

- `Projects/WAKE_UP/STATUS.md`(プロジェクト進捗)
- `Projects/WAKE_UP/PRODUCTION_BOARD.md`(Production Board)
- `Projects/WAKE_UP/Reference/CHAR_*_MASTER.md`(Character Master仕様)
- `Projects/WAKE_UP/Prompt/IMAGE_QC_CHECKLIST.md`(Image QC基準)
- `Projects/WAKE_UP/Prompt/DIRECTOR_APPROVAL_SHEET.md`(承認トラッキング)
- `Projects/WAKE_UP/Storyboard/CUT01_Panel03_Take1.md`(Golden Production Image Take1レビュー)
- `IMAGE_GENERATION_POLICY.md`(Production Policy Version 1.1)
