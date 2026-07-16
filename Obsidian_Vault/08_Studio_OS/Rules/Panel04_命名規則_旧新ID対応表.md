---
title: Panel04 命名規則リネーム — 旧新ID対応表
category: Studio OS
status: Active
version: 1.0
applies_to:
  - WAKE UP
---

# Panel04 命名規則リネーム — 旧新ID対応表

## 背景

2026-07-16、FLY77STAR CANON(`CANON_FLY77STAR_20260716_final.md`)受領により、「Panel04」という呼称が2つの異なる内容を指していたことが判明した。

- **旧12カット構成のCUT01 Panel04**: 渋谷スクランブル交差点、MIU単独、「静止していた時間が動き始める」
- **CANON新4パネル構成のPanel4**: クラブ出口〜ダイナーの4パネル構成のうち、AYAがPOP DINERのドアを開けるシーン

この名前衝突が、Director指示における「Panel04」「未解決5点」を巡る混乱の一因だった(詳細は`HANDOFF.md`参照)。この対応表は、リポジトリ内に実在する「Panel04」という名前を含むファイル(全4件: CUT01/CUT03/CUT08/CUT12)を対象に、一意な新IDへリネームした記録。

## 方針(Director確定、2026-07-16)

- 既存ファイルは削除しない(git mvによるリネームのみ、内容は保持)
- 旧IDは各ファイル冒頭に「Legacy ID」として明記し、追跡可能にする
- 新IDの形式: `PROJECT_CUT##_PANEL##_内容名`
- 本文内の参照(ファイルパス・wikilink)も、この4件に関する範囲で更新済み
- **今回はPanel04の4件のみが対象。** Panel01〜03を含む全17件のPanel関連ファイルの一括リネームは、CANONとStoryboardの整合性が安定してから別フェーズで検討する(2026-07-16、Director判断)

## 対応表

| Legacy ID(旧ファイル名) | New Canon ID(新ファイル名) | 内容 |
|---|---|---|
| `CUT01_Panel04_PRODUCTION_PACKAGE` | `WAKE_UP_CUT01_PANEL04_静止時間動き出し_PRODUCTION_PACKAGE` | 旧12カット構成、渋谷交差点、MIU単独、「静止していた時間が動き始める」。CANONの新Panel4(AYAがドアを開ける)とは別内容 |
| `CUT03_Panel04_DirectorNotes` | `WAKE_UP_CUT03_PANEL04_3人集結_DirectorNotes` | 象徴カット。SE77NTH.3人が初めて画面内に横並びで揃う構図(「3ショットへ引く」) |
| `CUT08_Panel04_DirectorNotes` | `WAKE_UP_CUT08_PANEL04_ホワイトアウト_DirectorNotes` | 象徴カット。Scene2「現実からパラレルワールドへの入口」の到達点(「ホワイトアウト」) |
| `CUT12_Panel04_DirectorNotes` | `WAKE_UP_CUT12_PANEL04_次回への余韻_DirectorNotes` | ラストカット。全12カットの最終パネル、次回への余韻(「クレーンアップ」) |

## 更新した参照元ファイル(本文内パス・wikilink)

- `CUT01_Panel04_PRODUCTION_PACKAGE` → `Projects/WAKE_UP/Prompt/DIRECTOR_APPROVAL_SHEET.md` / `Projects/WAKE_UP/STATUS.md` / `Projects/WAKE_UP/Storyboard/CUT01_絵コンテ.md` / `Projects/WAKE_UP/PRODUCTION_BOARD.md` / `Obsidian_Vault/03_Company/Decisions/2026-07-11_WAKE_UP.md` / `HANDOFF.md`
- `CUT03_Panel04_DirectorNotes` → `Projects/WAKE_UP/Storyboard/CUT04_Panel01_DirectorNotes.md` / `Obsidian_Vault/06_Projects/WAKE_UP/Overview.md`
- `CUT08_Panel04_DirectorNotes` → `Projects/WAKE_UP/Storyboard/Scene2_Review.md` / `Projects/WAKE_UP/Storyboard/CUT09_Panel01_DirectorNotes.md`
- `CUT12_Panel04_DirectorNotes` → `Projects/WAKE_UP/Storyboard/Scene3_Review.md` / `Projects/WAKE_UP/Edit/EDIT_PLAN.md`

STATUS.mdのDirector Notes進捗一覧など、ファイルパスを伴わない地の文中の「Panel04」表記(例:「CUT03 Panel01・Panel04」)は、リンク切れを起こさないため未更新のまま残している。

## 関連

- `HANDOFF.md`(CANON差分・Panel04名前衝突の経緯)
- `Obsidian_Vault/08_Studio_OS/Rules/テイク修正上限ルール.md`(同フォルダの先行ルール)
- `CANON_FLY77STAR_20260716_final.md`
