# LOC_STREET_MASTER — Location Reference（WAKE UP）

Asset ID: `LOC_STREET01`
使用CUT: CUT04(歩き出す)
目的: 今後すべての画像・動画生成で同一ロケーションの視覚的一貫性を維持するための固定リファレンス。

## 基本情報

渋谷、スクランブル交差点から路地へ向かう通り、夜。大通りのネオンから、路地に入るにつれ光量が落ち着いたトーンへ変化する。CUT01〜03のLOC_CROSSING01と地続きのエリアという設定。

## Location Lock Prompt(共通ベース記述)

```
Shibuya side street at night, transitioning from a busy neon-lit avenue
into a narrower quieter alley, gradual shift from vibrant neon to
warmer dimmer tones, generic fictional signage only (no real brand
names or logos), 35mm film grain
```

## アングルバリエーション

### 大通り側(Avenue side) — CUT04 Panel1〜3用
```
LOC_STREET01_AVENUE — wide street view, neon backdrop still visible,
open pedestrian space for three walking figures
```

### 路地入口(Alley entrance) — CUT04 Panel4用
```
LOC_STREET01_ALLEY_ENTRANCE — narrower alley entrance, light quality
shifting from cool neon to warmer dimmer tones, framing composition
that leads the eye toward the alley depth (connects to LOC_STREET01→
LOC_DINER_EXT01 continuity)
```

## 一貫性アンカー

- 大通り→路地の光量変化は連続的に(唐突な切り替えを避ける、CUT05 Panel1のBG(LOC_STREET01の延長)へ自然に繋がるようにする)
- LOC_CROSSING01と同じ「渋谷の夜」の色温度・彩度基準を踏襲する

## 関連

- **CANON関連メモ(2026-07-16)**: GitHub `/CANON_FLY77STAR_20260716_final.md` §6のWAKE UP新構成は「クラブ出口」から始まる。本ファイルはLegacy構造(旧12カット、`Storyboard/00_LEGACY_STRUCTURE_NOTICE.md`参照)固有のロケーションである可能性が高く、無条件の「採用済み素材」とは扱わない。Director判断待ち
- 使用Panel: `Storyboard/CUT04_絵コンテ.md` 全Panel
- 接続先: `LOC_DINER_EXT_MASTER.md`(CUT05へ繋がる)
- Image Asset List: `Prompt/IMAGE_ASSET_LIST.md`
