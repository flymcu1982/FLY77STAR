# LOC_DINER_INT_MASTER — Location Reference（WAKE UP）

Asset ID: `LOC_DINER_INT01`
使用CUT: CUT06(店内)、CUT07(KAI登場、流用)、CUT08(パラレル終了、VFXバリエーション)
目的: 今後すべての画像・動画生成で同一ロケーションの視覚的一貫性を維持するための固定リファレンス。

## 基本情報

「POP DINER」店内(架空店舗)。暖色のネオンとレトロな電飾が店内全体を包む、現実離れした均一な暖かい光。輪郭がわずかに滲むような、夢の中の質感。

## Location Lock Prompt(共通ベース記述)

```
Dreamlike interior of a retro diner, warm neon and vintage bulb
lighting, slightly soft dreamlike focus, retro checkered floor and
neon-lit counter, vintage booth seating, 35mm film grain with soft glow
```

## アングルバリエーション

### 店内全体(Wide interior) — CUT06 Panel2〜5、CUT07全Panel用
```
LOC_DINER_INT01_WIDE — full interior wide view, counter and booth
seating visible, kitchen area implied in background (for KAI's entrance
in CUT07)
```

### 厨房エリア(Kitchen area) — CUT07 Panel1〜2用
```
LOC_DINER_INT01_KITCHEN — kitchen area backlit by warm neon, silhouette
space for a figure to emerge from, connects visually to
LOC_DINER_INT01_WIDE
```

### 崩壊VFXバリエーション(Dissolution) — CUT08全Panel用
```
LOC_DINER_INT01_DISSOLVE — same interior as LOC_DINER_INT01_WIDE but
with irregular flickering warm neon, edges beginning to blur and
dissolve into light particles, progressing toward full white
overexposure
```

## 一貫性アンカー

- CUT06〜07を通じて同一の内装・レイアウト(カウンター、ブース席、厨房の位置関係)を維持する
- CUT08のVFXバリエーションは、あくまでLOC_DINER_INT01_WIDEの「崩壊していくバージョン」として扱い、レイアウト自体は変えない
- パースのわずかな歪み・ソフトフォーカスは強すぎるとブレに見えるため、生成時のパラメータ調整に注意(既知の課題)

## 関連

- 使用Panel: `Storyboard/CUT06_絵コンテ.md`・`CUT07_絵コンテ.md`・`CUT08_絵コンテ.md` 全Panel
- 接続元: `LOC_DINER_EXT_MASTER.md`
- Image Asset List: `Prompt/IMAGE_ASSET_LIST.md`
