# FLY77STAR. Web / Netlify Site

このフォルダは、現行 Netlify 公開サイト `flystar77-studio.netlify.app` （表示URL: `FLY77STAR-studio.netlify.app`）の Git 管理受け皿です。

## 公式リンク

**公式サイト**: https://flystar77-studio.netlify.app/  
**SNS・公式情報**: [`../../OFFICIAL_INFO.md`](../../OFFICIAL_INFO.md) 参照

## Current Status

- Source origin:
  - `/Users/yamamotohiroshi/Documents/Codex/2026-07-06/p/work/netlify_site`
- Public host:
  - `fly77star-studio.netlify.app`
- Netlify production operations:
  - Not performed from this repository

## Migration Policy

- Web 公開資産は `Assets/` 直下へ混ぜず、この `Web/netlify_site/` 配下で独立管理する。
- `index.html` と `assets/` は、現行公開サイトの構成を保ったまま段階的に移管する。
- 大容量動画が多いため、移管前に `ASSET_MANIFEST.md` で容量と参照関係を確認する。
- フル動画と大容量短尺動画は Git に含めず、`VIDEO_ASSET_MANIFEST.md` で別管理する。
- Netlify 本番操作、ドメイン変更、管理画面操作はここでは行わない。

## Current Assessment

- `assets/` file count: `44`
- Total asset size: `511,561,604 bytes`
- `index.html` referenced assets: `44 / 44`
- Unreferenced assets: `0`

## Current Managed Copy Policy

現時点の Git 管理コピーは中間案です。

- 含める:
  - `index.html`
  - `assets/FLY77STAR_Logo.png`
  - `.jpg` / `.png` などの画像資産
  - 軽量 teaser 動画のみ
- 含めない:
  - `*_full.mp4`
  - `opening_full.mp4`
  - FANG CM 本編動画
  - 大容量の短尺 mp4

## Current Web Policy

- `Distance` は 2026年8月のYouTube配信開始まで、ショート2本のみ掲載する
- `Distance` フル / teaser、`TOMORROW`、ENERGY-D CM、FANG CM動画は掲載停止
- 停止対象は `video` ではなく、ポスター画像と案内文で表示する
- URL表示テキストは `FLY77STAR-studio.netlify.app` に統一する

除外対象の詳細は `VIDEO_ASSET_MANIFEST.md` を参照してください。

## Recommendation

現時点では `assets/` 一式を無条件にコピーせず、まず `ASSET_MANIFEST.md` を基準に以下を判断するのが安全です。

1. フル動画を Git 管理へ含めるか
2. ポスター・静止画・ロゴ・teaser だけを先行移管するか
3. 大容量動画を別保管にするか

特に以下の動画は容量が大きく、コピー前に再確認が必要です。

- `tomorrow_full.mp4` - `338,059,374 bytes`
- `distance_full.mp4` - `64,135,256 bytes`
- `step_full.mp4` - `33,994,391 bytes`
- `opening_full.mp4` - `27,497,631 bytes`

## Next Step

YU 承認後に、次のどちらかで進める想定です。

1. `index.html` + 軽量資産を `Web/netlify_site/` へ正式管理する
2. 大容量動画は別保管または YouTube / 外部ホスティング運用に切り分ける
