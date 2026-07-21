# WAKE UP — CANON Scene 1（オープニング）PRODUCTION PACKAGE

**用途**: 生成実行用の最終仕様書（GPT Image 最終プロンプト／Higgsfield 投入用コピペ版／Palmier 接続メモ）
**基準**: `WAKE_UP_CANON_SCENE01_OPENING.md`（Storyboard 本体）＋ Director Decision 2026-07-21
**Decision Log**: `Obsidian_Vault/03_Company/Decisions/2026-07-21_WAKE_UP_CANON_Scene1承認.md`
**生成実行者**: Director / GPT Image 運用側（Production Policy v1.3。AI社員は生成を実行しない）
**生成順序（厳守）**: 各 Panel の起点画像を GPT Image で確定 → Image QC → 採用画像のみ Higgsfield で動画化

---

## Director Decision（2026-07-21、反映済み）

1. **クラブ外観**: 正式店名なし。`LOC_CLUB_EXT01` のまま進行。看板は判読不能ネオン。FLY77STAR 世界の架空クラブ外観として統一
2. **衣装（仮衣装ロック）**: 3人の識別性を必ず確保 — MIU＝白系インナーが見える構成／AYA＝最も落ち着いたダークトーン／NANA＝少し軽さのあるシルエット／全員ノーロゴ
3. **総尺**: 20秒仮ロック（5秒×4セグメント）。イントロ実尺との微調整は編集工程
4. **重視事項**: Panel 3→4 接続の人物精度最優先／3人同時登場は顔の作り込みより**位置関係・シルエット・色差の固定**を優先／MIU の視線バトン維持

## 仮衣装ロック（全プロンプト共通、Costume Bible 正式登録までの技術的仮描写）

| キャラ | 立ち位置 | 衣装記述（英語プロンプト用） | 識別アンカー |
|---|---|---|---|
| AYA | 左 | all-black sleek fitted outfit, matte textures, the darkest silhouette of the three | 最暗・タイト |
| MIU | 中央 | dark open jacket over a clearly visible white inner top, the brightest point of the group | 白インナー・最明部 |
| NANA | 右 | charcoal-gray loose airy outfit, light flowing silhouette, slightly playful | 中間調・軽いシルエット |

シルエット差（タイト／白コア／エアリー）と明度差（暗／白点／中間）の両方で、顔が判別しにくいフレームでも3人を識別できる設計。

---

## A. GPT Image 用最終プロンプト（各 Panel 起点フレーム）

### A-1. Panel 1 起点（空撮）— そのままコピペ可

```
Aerial drone view high above a vast fictional Japanese metropolis
inspired by Shibuya at 4:30AM blue hour, deep indigo pre-dawn sky,
dense cityscape with scattered neon signs still glowing, sparse car
headlights tracing empty streets, no readable text, no real brand
logos, no recognizable real landmarks, cinematic anamorphic look, cool
blue color grade with warm neon accents, 35mm film grain, moody quiet
atmosphere
```

### A-2. Panel 2 起点（ビル間降下）— そのままコピペ可

```
Low aerial shot between buildings descending into a narrow back street
of a fictional Shibuya-like district at 4:30AM, wet asphalt reflecting
pink and cyan neon remnants, shuttered shops, steam from a street
vent, empty street with one distant taxi, all signage abstract and
unreadable, no letters, no real brand logos, deep blue pre-dawn light
mixing with artificial neon, cinematic wide angle, 35mm film grain
```

### A-3. Panel 3 起点（クラブ入口 LOC_CLUB_EXT01）— そのままコピペ可

```
Street-level view facing the entrance of a fictional underground club,
heavy black double door slightly ajar centered in frame, warm amber
light and faint haze spilling out from the gap, abstract glowing neon
sign shapes above the door, completely unreadable, no letters, no
logos, posters rendered as indistinct color patches, cold blue 4:30AM
pre-dawn street contrasting with the warm doorway glow, cinematic,
35mm film grain
```

### A-4. Panel 4 起点（3ショット）— そのままコピペ可【最重要・QC必須】

```
Three East Asian Japanese young women stepping out of a club doorway
together at 4:30AM, warm amber doorway backlight rim-lighting their
hair, cold blue pre-dawn light on their faces, medium three-shot, all
three faces clearly visible and distinguishable:

LEFT (AYA): center-parted straight dark brown hair, nude-toned lips,
silver accessories, cool composed expression with a small tired smile,
all-black sleek fitted outfit, matte textures, the darkest silhouette
of the three;

CENTER (MIU): long light brown loose wavy hair with a white hairband,
warm-toned glossy lips, gold accessories including a red heart
necklace, hoop earrings, warm caring smile mid-laugh, dark open jacket
over a clearly visible white inner top, the brightest point of the
group;

RIGHT (NANA): chin-length inward-curled black bob with heavy blunt
bangs, peach-pink inner hair color, a small mole fixed under her left
eye, rosy cheeks, bright open laugh, charcoal-gray loose airy outfit,
light flowing silhouette;

no visible logos or brand marks on any clothing, natural relaxed
after-party posture, not posing, walking casually out of the door,
exact facial consistency per fixed reference descriptions, cinematic,
35mm film grain
```

### A-5. Negative Prompt（全 Panel 共通）

```
readable text, letters, real brand logos, real landmarks, watermarks,
extra fingers, deformed hands, merged faces, face swap between
characters, duplicated person, fourth person, daylight, sunrise sun
visible, crowd, posing at camera, looking at camera (Panel 4 only),
oversaturated colors
```

---

## B. Higgsfield 投入用コピペ版（動画、image-to-video）

採用済み起点画像を入力し、以下をそのまま投入。各 5〜6 秒。

**Seg1**（Panel 1 画像 →）
```
Slow forward-descending drone move, constant gentle speed, no camera
shake, city lights flickering subtly, clouds drifting very slowly,
5 seconds, cinematic
```

**Seg2**（Panel 2 画像 →）
```
Continuous smooth forward descent into the empty neon back street,
single camera path, no objects crossing frame, wet road reflections
shimmering, 5 seconds, cinematic
```

**Seg3**（Panel 3 画像 →）
```
Extremely stable ground-level forward dolly toward the club door,
warm light and thin haze drifting from the door gap, neon shapes
glowing softly, 5 seconds, cinematic
```

**Seg4**（Panel 4 画像 →）
```
Club double door opens outward, the three women step out together
laughing naturally, subtle handheld feel, camera pulls back slightly
slower than their walking pace, they slow into a loose line, the
center woman (MIU) glances off-screen right at the very end, faces
and outfits stay exactly consistent with the input image, 5-6
seconds, cinematic
```

**Seg4 破綻時の改善案 B**: ドア開放を諦め、起点画像を「既に開いたドアから出てくる途中」に差し替えて動作を単純化（Take 修正上限2回ルール適用、`テイク修正上限ルール.md`）。

---

## C. Palmier 接続メモ（短縮版）

```
[WAKE UP Scene1 / 総尺20秒仮ロック / BPM95.7 / 1×8=5.02s]
Seg1→2: 降下速度マッチ、ビル影が横切る瞬間に4-6Fディゾルブ(速度ランプで隠す)
Seg2→3: 路面が下1/3の構図同士で接続、前進ベクトル一致が最優先
Seg3→4: ドア中央フレームで接続、Seg4「ドア開放」をイントロ強拍に同期 ★人物精度最優先の接続点
Seg4末尾: MIUの視線が向き切るまで見せてからScene 2へ(視線バトン)
音: 3人の笑い声をSeg3のドア越しから先行で薄く入れるとワンカット感が出る
全体: 青グレード+フィルムグレインを統一適用しセグメント間の質感差を均す
微調整: イントロ実尺との合わせ込みは本タイムラインで実施(生成側は5-6秒の余裕あり)
```

---

## D. Panel 3→4 接続 QC（最優先、生成後に実施）

`Prompt/IMAGE_QC_CHECKLIST.md` に加え、本 Scene 固有の確認:

- [ ] Seg3 最終フレームと Panel 4 起点画像で、ドアの形状・ネオン形状・路面の色が一致しているか
- [ ] **位置関係**: 左 AYA／中央 MIU／右 NANA が全フレームで入れ替わっていないか
- [ ] **シルエット**: タイト（AYA）／白コア（MIU）／エアリー（NANA）の差が保たれているか
- [ ] **色差**: MIU の白インナーが画面内で最も明るい点になっているか
- [ ] NANA の泣きぼくろ（左目下）・MIU の白ヘアバンド・AYA のセンターパートの3アンカー確認
- [ ] 衣装にロゴ・文字が出ていないか（全 Panel 共通）
- [ ] Seg4 末尾で MIU の視線移動が明確に読み取れるか
