# WAKE UP — Director Approval Sheet

Production Policy Version 1.0に基づく、社長(YU)承認支援シート。AI社員(Claude Code)は画像生成を行わず、生成後の画像についてImage QC(`Prompt/IMAGE_QC_CHECKLIST.md`)を実施し、その結果をここに整理して承認判断を支援する。**承認そのもの(Director Approval)は社長が行う。**

## 使い方

1. GPT Imageでの本番生成完了後、対象Asset IDの画像をこのシートに紐づける
2. AI社員が`IMAGE_QC_CHECKLIST.md`の6項目でQCを実施し、結果を記入する
3. 社長が「Director Approval」欄を承認/差し戻しで判断する
4. 承認済みのみ⑤(Higgsfieldでの動画生成)へ進む

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

Character Master / Location Master承認後、`Prompt/IMAGE_ASSET_LIST.md`の撮影優先順位に従い、まず重要Panel12件を優先してQC・承認を行う。

| CUT | Panel | Asset ID(IMG) | 生成画像 | QC総合判定 | Director Approval |
|---|---|---|---|---|---|
| CUT01 | P03 | `CUT01_P03_IMG01` | 未生成 | 未実施 | ⬜ 未承認 |
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
