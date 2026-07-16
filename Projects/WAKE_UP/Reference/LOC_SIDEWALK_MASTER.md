# LOC_SIDEWALK_MASTER — Location Reference（WAKE UP）

Asset ID: `LOC_SIDEWALK01`
使用CUT: CUT09(現実、空き区画バリエーション)、CUT10(KAIとすれ違う)、CUT11(HINA登場)、CUT12(エンディング)
目的: 今後すべての画像・動画生成で同一ロケーションの視覚的一貫性を維持するための固定リファレンス。

## 基本情報

渋谷、帰り道の歩道・雑踏(夜)。ダイナー消失後の現実の路地(空き区画)から、帰り道の雑踏、そして最終カットの夜景全体まで、Scene3を通じて使用する現実側の一連のロケーション。

## Location Lock Prompt(共通ベース記述)

```
Ordinary Shibuya night street on the way home, dim ordinary streetlight,
normal urban bustle, no trace of the earlier warm diner neon, 35mm film
grain
```

## アングルバリエーション

### 空き区画(Empty lot) — CUT09 Panel1〜2用
```
LOC_SIDEWALK01_EMPTYLOT — the alley where the diner used to stand, now
just a closed shutter and empty lot, dim ordinary streetlight, no trace
of the warm neon from before
```

### 雑踏の歩道(Crowded sidewalk) — CUT10・CUT11用
```
LOC_SIDEWALK01_CROWD — bustling sidewalk with moderate crowd density,
enough depth for a background silhouette to be glimpsed (CUT10) and for
a passerby to cross paths with the group (CUT11)
```

### 帰り道の通り(Homeward street) — CUT12 Panel1〜3用
```
LOC_SIDEWALK01_HOMEWARD — quieter residential-leaning street, fewer
pedestrians, calm ending atmosphere
```

### 渋谷夜景全体(Full cityscape) — CUT12 Panel4用
```
LOC_SIDEWALK01_CITYSCAPE — wide elevated view of the full Shibuya night
skyline, neon and streetlights extending into the distance, space
reserved for end-card text overlay
```

## 一貫性アンカー

- ダイナーの暖色ネオンは完全に消え、現実の落ち着いた常夜灯色で統一する(Reality Scale=1の視覚的裏付け)
- CUT09〜12を通じて同一の「帰り道」という地理的連続性を保つ(唐突に無関係な場所へ切り替わらない)
- CUT12 Panel4のテロップ挿入スペースを画面上部または下部に確保する(既知の課題)

## 関連

- **CANON関連メモ(2026-07-16)**: GitHub `/CANON_FLY77STAR_20260716_final.md` §6のWAKE UP新構成には「帰り道」に相当する描写がなく(エンディングは「現実の渋谷へ帰還」とのみ記載)、本ファイルはLegacy構造(旧12カット、`Storyboard/00_LEGACY_STRUCTURE_NOTICE.md`参照)固有のロケーションである可能性が高い。無条件の「採用済み素材」とは扱わない。Director判断待ち
- 使用Panel: `Storyboard/CUT09_絵コンテ.md`〜`CUT12_絵コンテ.md` 全Panel
- Image Asset List: `Prompt/IMAGE_ASSET_LIST.md`
