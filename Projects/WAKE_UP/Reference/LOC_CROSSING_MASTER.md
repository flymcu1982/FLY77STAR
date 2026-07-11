# LOC_CROSSING_MASTER — Location Reference（WAKE UP）

Asset ID: `LOC_CROSSING01`
使用CUT: CUT01(渋谷)、CUT02(AYA到着、流用)、CUT03(3人集合、流用)
目的: 今後すべての画像・動画生成で同一ロケーションの視覚的一貫性を維持するための固定リファレンス。

## 基本情報

渋谷スクランブル交差点付近、夜。実在の渋谷の地名は使用するが、周辺の店舗・看板は架空表記とする(Production Bible AI Production Policy準拠)。ネオン・電光掲示板の光が入り混じる、彩度の高い夜景。

## Location Lock Prompt(共通ベース記述)

```
Shibuya scramble crossing at night, East Asian metropolitan intersection,
neon signage and digital billboards reflecting on wet pavement, vibrant
saturated night colors, dense pedestrian crowd, generic fictional store
signage only (no real brand names or logos), 35mm film grain
```

## アングルバリエーション

### 俯瞰(Overhead) — CUT01 Panel1〜2用
```
LOC_CROSSING01_OVERHEAD — full overhead/drone view of the crossing,
wide establishing composition, crowd flow patterns visible from above
```

### 路上レベル(Street Level) — CUT01 Panel3〜5、CUT02、CUT03用
```
LOC_CROSSING01_STREET — street-level medium-wide view, crowd at eye
level, neon bokeh in background, enough negative space for a single
still figure to stand out amid moving crowd
```

## 一貫性アンカー

- ネオン・電光掲示板の彩度と色温度(暖色ネオン+彩度の高い夜景)を全パネルで統一
- 実在の渋谷の地理的特徴(交差点の広さ、群衆密度)は維持しつつ、個別店舗名・ロゴは一切表示しない
- CUT01俯瞰(P1-2)→路上レベル(P3-5)への高度変化は、同一ロケーションの角度違いとして扱う(場所が変わったわけではない)

## 関連

- 使用Panel: `Storyboard/CUT01_絵コンテ.md` Panel1-5、`CUT02_絵コンテ.md` 全Panel、`CUT03_絵コンテ.md` 全Panel
- Image Asset List: `Prompt/IMAGE_ASSET_LIST.md`
