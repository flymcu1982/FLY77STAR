# VIDEO ASSET MANIFEST - Excluded from Git Copy

対象:
- Source: `/Users/yamamotohiroshi/Documents/Codex/2026-07-06/p/work/netlify_site/assets`
- Git-managed target: `Web/netlify_site/assets/`

作成日:
- 2026-07-17

## Exclusion Policy

以下の動画は Git 管理コピーから除外する。

- `*_full.mp4`
- `opening_full.mp4`
- 大容量の短尺 mp4
- teaser 以外の本編寄り動画

## Excluded Videos

| File | Size (bytes) | Reason for Exclusion | Temporary Site Handling |
|---|---:|---|---|
| `tomorrow_full.mp4` | 338059374 | Full video too large | Replace with `tomorrow_teaser.mp4`; later swap to YouTube embed or external host |
| `distance_full.mp4` | 64135256 | Full video too large | Replace with `distance_teaser.mp4`; later swap to YouTube embed or external host |
| `step_full.mp4` | 33994391 | Full video too large | Replace with `step_teaser.mp4`; later swap to YouTube embed or external host |
| `opening_full.mp4` | 27497631 | Hero opening video too large | Use static hero state now; later restore with external host or lighter asset |
| `fang_cm_15s.mp4` | 15928108 | Over practical Git threshold; not teaser | Replace with poster only; later external host or YouTube |
| `fang_cm_30s.mp4` | 8878613 | Not teaser; keep Git copy light | Replace with poster only; later external host or YouTube |
| `distance_short_intro.mp4` | 6599830 | Short clip is still large for light Git copy | Replace with poster only; later external host or YouTube Shorts |
| `distance_short_sabi.mp4` | 5416451 | Short clip is still large for light Git copy | Replace with poster only; later external host or YouTube Shorts |

## Handling Decision

現時点では、壊れないように以下で対応する。

1. フル動画は軽量 teaser へ一時置換
2. teaser がない動画はポスター画像へ一時置換
3. YouTube 公開後に埋め込みへ置換するのを推奨

## Recommended Future Replace Targets

- `Distance`, `STEP by STEP`, `TOMORROW`
  - YouTube 公開後に各埋め込みへ差し替え
- `opening_full.mp4`
  - 軽量化版を別生成するか、外部ホスティング URL 参照へ切り替え
- `FANG CM`, `Distance short`
  - 外部ホスティング URL または YouTube Shorts / TikTok 公開後の導線へ切り替え
