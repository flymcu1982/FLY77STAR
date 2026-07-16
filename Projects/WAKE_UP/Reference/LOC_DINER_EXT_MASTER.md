# LOC_DINER_EXT_MASTER — Location Reference（WAKE UP）

Asset ID: `LOC_DINER_EXT01`
使用CUT: CUT05(ダイナー発見)
目的: 今後すべての画像・動画生成で同一ロケーションの視覚的一貫性を維持するための固定リファレンス。

## 基本情報

渋谷の路地裏、周囲から浮いた佇まいのレトロダイナー「POP DINER」外観(架空店舗、実在ブランドとの関連は一切ない)。周囲の路地は暗く落ち着いたトーン、ダイナーの窓からだけ暖色のネオンとレトロな電飾が漏れる、対比の強い光。

## Location Lock Prompt(共通ベース記述)

```
A retro diner exterior glowing warmly at the end of a dark Shibuya
alley, warm neon and vintage bulb signage reading a short fictional
name ("POP DINER", entirely fictional, no resemblance to any real
brand), out of place against the surrounding modern night street, warm
color contrast against cool alley tones, 35mm film grain
```

## アングルバリエーション

### 発見時の遠景(Discovery, wide) — CUT05 Panel1〜2用
```
LOC_DINER_EXT01_WIDE — distant wide view from the dark alley entrance,
only the warm glow visible, no architectural detail legible yet
```

### 外観クローズ(Close, signage visible) — CUT05 Panel4用
```
LOC_DINER_EXT01_CLOSE — closer dolly-in view, retro neon signage and
vintage bulb decoration legible, warm inviting entrance, door visible
```

## 一貫性アンカー

- 「POP DINER」の看板テキストは簡潔な表記に留める(生成時の文字崩れを避ける、既知の課題)
- 架空店舗であることを常に意識し、実在の飲食チェーンのロゴ・意匠を想起させる要素は避ける(Production Bible AI Production Policy準拠)
- CUT06のLOC_DINER_INT01(店内)へ光の質感(暖色ネオン)を引き継ぐ

## 関連

- **CANON(採用済み素材、2026-07-16)**: GitHub `/CANON_FLY77STAR_20260716_final.md` §6のWAKE UP新構成でも「ダイナーで繋がる別の世界」としてPOP DINERが登場するため、本ファイルは物語構成(Legacy/CANON)の判断によらず有効。Location Referenceとして確定
- 使用Panel: `Storyboard/CUT05_絵コンテ.md` 全Panel
- 接続先: `LOC_DINER_INT_MASTER.md`(CUT06〜08へ繋がる)
- Image Asset List: `Prompt/IMAGE_ASSET_LIST.md`
