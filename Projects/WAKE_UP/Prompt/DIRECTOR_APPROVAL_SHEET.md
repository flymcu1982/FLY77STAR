# WAKE UP — Director Approval Sheet

Production Policy Version 1.0に基づく、社長(YU)承認支援シート。AI社員(Claude Code)は画像生成を行わず、生成後の画像についてImage QC(`Prompt/IMAGE_QC_CHECKLIST.md`)を実施し、その結果をここに整理して承認判断を支援する。**承認そのもの(Director Approval)は社長が行う。**

## 使い方

1. GPT Imageでの本番生成完了後、対象Asset IDの画像をこのシートに紐づける
2. AI社員が`IMAGE_QC_CHECKLIST.md`の6項目でQCを実施し、結果を記入する
3. 社長が「Director Approval」欄を承認/差し戻しで判断する
4. 承認済みのみ⑤(Higgsfieldでの動画生成)へ進む

---

## Pilot Production Baseline(Director Decision、2026-07-11)

社長承認済み。Production Baselineを以下の通り確定:

| Panel | 役割 | 状態 |
|---|---|---|
| CUT01 Panel01 | Location Validation | Go(社長承認済み、生成待ち) |
| CUT01 Panel02 | Camera Validation | Go(Panel01に続き実施) |
| CUT01 Panel03 | **Golden Production Image**(基準画像) | 今後のProduction QC・Character QC・Costume QC・Director Approvalの基準として扱う |

### CUT01 Panel01 — Location Validation

詳細: `Storyboard/CUT01_Panel01_PILOT_PRODUCTION.md`。

| 項目 | 状態 |
|---|---|
| 対象 | CUT01 Panel01(渋谷、俯瞰、被写体なし) |
| Asset ID | `CUT01_P01_IMG01` |
| Production Prompt | 最終確認済み(`CUT01_Panel01_PILOT_PRODUCTION.md`参照) |
| 生成画像 | 未生成(社長承認後、GPT Imageで生成予定) |
| QC総合判定 | 未実施 |
| Go/Hold | Go(社長承認済み) |
| Director Approval | ⬜ 未承認(画像生成・QC後に判断) |
| 備考 | Location Validation。人物不在のためCharacter/Costume整合は対象外。Location/Lighting/Composition/Emotionのみが判定対象 |

### CUT01 Panel02 — Camera Validation

| 項目 | 状態 |
|---|---|
| 対象 | CUT01 Panel02(降下クレーン、被写体なし) |
| Asset ID | `CUT01_P02_IMG01` |
| Production Prompt | 未作成(Panel01に続き必要時に整備) |
| 生成画像 | 未生成 |
| QC総合判定 | 未実施 |
| Go/Hold | Go(Director Decision) |
| Director Approval | ⬜ 未承認 |
| 備考 | Camera Validation。カメラワーク(俯瞰→降下)の検証が主目的。人物不在のためCharacter/Costume整合は対象外 |

### CUT01 Panel03 — Golden Production Image(基準画像)

Production Package完成: `Storyboard/CUT01_Panel03_PRODUCTION_PACKAGE.md`(Final Production Prompt・Negative Prompt・Production QC Checklist・Director Approval Checklist・Production Reportを収録)。

| 項目 | 状態 |
|---|---|
| 対象 | CUT01 Panel03(MIU初登場、静止・発見) |
| Asset ID | `CUT01_P03_IMG01` |
| Production Prompt | **最終確認済み**(`Storyboard/CUT01_Panel03_PRODUCTION_PACKAGE.md`①参照。Character/Costume(仮)/Location/Story Bible/Panel Storyboard/Director Notesを統合) |
| Negative Prompt | 整備済み(同資料②) |
| 生成画像 | 未生成(社長承認後、GPT Imageで生成予定) |
| QC総合判定 | 未実施(基準は同資料③) |
| Director Approval Checklist | 整備済み(同資料④、10項目) |
| Director Approval | ⬜ 未承認 |
| 備考 | **今後のProduction QC・Character QC・Costume QC・Director Approvalの基準画像**。Costume(私服)はCostume Bible未登録のため技術的な仮描写を使用——正式デザイン確定後に再生成が必要になる可能性を承認時に許容するか要確認(Director Approval Checklist項目4) |

#### Take 1

生成直前レビュー: `Storyboard/CUT01_Panel03_Take1.md`(Final Production Prompt/Negative Prompt/Director Shooting Notes/Take 1 Director Goal/Take 1採用基準)。

| 項目 | 状態 |
|---|---|
| Take | 1(Take2・Take3は社長承認があるまで作成しない) |
| Production Package | **社長承認済み(2026-07-11)** |
| 生成画像 | 未生成。GPT Imageでの本番生成は社長/GPT Image運用側が実施(AI社員は画像生成を行わない、Production Policy Version 1.0準拠) |
| Take 1採用基準 | 整備済み(7項目、`CUT01_Panel03_Take1.md`⑤参照) |
| Director Review | 未実施(生成画像提供後に実施) |
| 判定 | 未定(Director Approved / Take 2要 のいずれかを社長が判断) |

### CUT01 Panel04 — 本番制作(720pテイク承認済み)

Production Package: `Storyboard/CUT01_Panel04_PRODUCTION_PACKAGE.md`。Production Policy Version 1.1により、Panel04以降はAI社員(Claude Code)が厳格運用サイクルのもとで生成実行を担当する。

| 項目 | 状態 |
|---|---|
| Theme | 「静止していた時間が、わずかに動き始める。」 |
| 720p Pilot | Director承認済み(本セッション外、5項目すべて✅) |
| Director Decision(5点) | **反映済み(2026-07-11)**: 実在ブランド名を一般表現へ差し替え / Story Bible最新版優先(統合は別途) / Panel Storyboard「静止していた時間が動き始める」を正式採用 / 衣装をPanel03と完全同一へ修正 / Cross-Referencesを実在パスへ修正 |
| Production Package | Director Decision反映済み、コミット・push待ち |
| 4K Production Generation | 未実施(Director Decision反映・コミット後、720P Pilot Generationへ進行予定) |
| Director Approval | ⬜ 未承認(4K本番生成前に最終確認) |

---

## Character Master

### MIU — `CHAR_MIU_MASTER01`

| 項目 | 状態 |
|---|---|
| 生成画像 | 未生成(社長承認後、GPT Imageで生成予定) |
| QC実施日 | — |
| Character Masterとの一致 | — |
| 表情 | — |
| 衣装 | — |
| 背景 | — |
| Story Bibleとの整合 | — |
| Panel Storyboardとの一致 | (Character Masterのため対象外。生成後の各Panel画像QC時に別途確認) |
| QC総合判定 | 未実施 |
| Director Approval | ⬜ 未承認 |
| 備考 | Costume Bible未登録のため、衣装項目は正式デザイン確定まで「保留」判定になる可能性あり |

### AYA — `CHAR_AYA_MASTER01`

| 項目 | 状態 |
|---|---|
| 生成画像 | 未生成 |
| QC総合判定 | 未実施 |
| Director Approval | ⬜ 未承認 |

### NANA — `CHAR_NANA_MASTER01`

| 項目 | 状態 |
|---|---|
| 生成画像 | 未生成 |
| QC総合判定 | 未実施 |
| Director Approval | ⬜ 未承認 |

### KAI — `CHAR_KAI_MASTER01`

| 項目 | 状態 |
|---|---|
| 生成画像 | 未生成 |
| QC総合判定 | 未実施 |
| Director Approval | ⬜ 未承認 |
| 備考 | "East Asian Japanese"明記・MA-1期意匠・銀の「7」ペンダント視認性を重点確認 |

### HINA — `CHAR_HINA_MASTER01`

| 項目 | 状態 |
|---|---|
| 生成画像 | 未生成 |
| QC総合判定 | 未実施 |
| Director Approval | ⬜ 未承認 |
| 備考 | インナーカラーなし・そばかす1〜2個・NANAとの混同なしを重点確認 |

---

## Location Master

| ロケーション | Asset ID | 生成画像 | QC総合判定 | Director Approval |
|---|---|---|---|---|
| 渋谷交差点 | `LOC_CROSSING01` | 未生成 | 未実施 | ⬜ 未承認 |
| 大通り〜路地 | `LOC_STREET01` | 未生成 | 未実施 | ⬜ 未承認 |
| POP DINER外観 | `LOC_DINER_EXT01` | 未生成 | 未実施 | ⬜ 未承認 |
| POP DINER内装 | `LOC_DINER_INT01` | 未生成 | 未実施 | ⬜ 未承認 |
| 帰り道 | `LOC_SIDEWALK01` | 未生成 | 未実施 | ⬜ 未承認 |

---

## Production Images(重要Panel、優先QC対象)

Character Master / Location Master承認後、`Prompt/IMAGE_ASSET_LIST.md`の撮影優先順位に従い、まず重要Panel12件を優先してQC・承認を行う。CUT01 P03は上記「Pilot Production Baseline」でGolden Production Image(基準画像)に指定済み(詳細はそちらを参照)。

| CUT | Panel | Asset ID(IMG) | 生成画像 | QC総合判定 | Director Approval |
|---|---|---|---|---|---|
| CUT01 | P03 | `CUT01_P03_IMG01` | 未生成 | 未実施 | ⬜ 未承認(Golden Production Image、上記参照) |
| CUT02 | P01 | `CUT02_P01_IMG01` | 未生成 | 未実施 | ⬜ 未承認 |
| CUT03 | P01 | `CUT03_P01_IMG01` | 未生成 | 未実施 | ⬜ 未承認 |
| CUT03 | P04 | `CUT03_P04_IMG01` | 未生成 | 未実施 | ⬜ 未承認 |
| CUT04 | P01 | `CUT04_P01_IMG01` | 未生成 | 未実施 | ⬜ 未承認 |
| CUT05 | P01 | `CUT05_P01_IMG01` | 未生成 | 未実施 | ⬜ 未承認 |
| CUT06 | P01 | `CUT06_P01_IMG01` | 未生成 | 未実施 | ⬜ 未承認 |
| CUT07 | P02 | `CUT07_P02_IMG01` | 未生成 | 未実施 | ⬜ 未承認 |
| CUT08 | P04 | `CUT08_P04_IMG01` | 未生成 | 未実施 | ⬜ 未承認 |
| CUT09 | P01 | `CUT09_P01_IMG01` | 未生成 | 未実施 | ⬜ 未承認 |
| CUT10 | P02 | `CUT10_P02_IMG01` | 未生成 | 未実施 | ⬜ 未承認 |
| CUT11 | P01 | `CUT11_P01_IMG01` | 未生成 | 未実施 | ⬜ 未承認 |
| CUT12 | P04 | `CUT12_P04_IMG01` | 未生成 | 未実施 | ⬜ 未承認 |

残り38Panelは、上記重要Panel承認後に同様の表で追記する(`Prompt/IMAGE_ASSET_LIST.md`のAsset ID一覧を参照)。

---

## 採用率サマリー(Credit Monitor連動)

| 区分 | 生成数 | 採用数 | 採用率 |
|---|---:|---:|---:|
| Character Master | 0 | 0 | — |
| Location Master | 0 | 0 | — |
| Production Images(重要Panel) | 0 | 0 | — |
| Production Images(全体) | 0 | 0 | — |

Higgsfieldクレジットは採用決定素材のみに使用する方針(Production Policy Version 1.0)のため、この表の「採用数」がそのままHiggsfield投入対象数になる。

## 関連

- Image QC Checklist: `Prompt/IMAGE_QC_CHECKLIST.md`
- Production Board: `PRODUCTION_BOARD.md`
- Production Report(Phase3): `PRODUCTION_REPORT_PHASE3.md`
- Production Policy: GitHub `IMAGE_GENERATION_POLICY.md`
