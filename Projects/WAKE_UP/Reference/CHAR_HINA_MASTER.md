# CHAR_HINA_MASTER — Character Master Reference（WAKE UP）

Character Bible参照: HINA（Obsidian Vault `10_Characters/HINA.md`）
Asset ID: `CHAR_HINA_MASTER01`
目的: 今後すべての画像・動画生成で同一人物(HINA)を維持するための固定リファレンス。実際の生成はHiggsfield + GPT Image側の作業(2026-07-11制作方針変更、`IMAGE_GENERATION_POLICY.md`準拠。Nano Banana不使用、Character MasterにSoul 2は使用しない)。本ファイルはその仕様書。

**注記**: HINAとRINは別人物(2026-07-10決定、詳細: Obsidian Vault `03_Company/Decisions/2026-07-10_HINAとRINの分離.md`)。本ファイルはHINA単独のリファレンスであり、RINのビジュアルとは無関係。

## 基本情報

19歳、身長152cm、細身。Don't Stop主演。素直で明るく、実は努力家。黒髪のみ・インナーカラーなし(NANAとの差別化)、肩より5〜8cm短いショートボブ、Kawaii Labsキュート系の顔立ち、大きく丸い下がり目、そばかす最小限(1〜2個)。WAKE UPでは白い服でカメオ出演(Don't Stopの衣装とは別デザイン)。

## Character Lock Prompt(共通ベース記述、GPT Image用、全アングル・表情で必ず含める)

```
East Asian Japanese young woman (HINA), 19 years old, small and
delicate build, black bob hair with no inner color, shoulder-length
minus 5-8cm, soft voluminous bangs lighter than typical, Kawaii Labs
style cute face, large round downturned eyes, small upturned nose,
full pink-toned lips, one or two faint freckles only, pure innocent
expression base, consistent facial structure across all angles and
expressions, exact facial consistency maintained via this fixed
reference description (GPT Image, Soul 2 not used)
```

## アングル

### 真正面(Front)
```
CHAR_HINA_MASTER01_FRONT — HINA, front-facing portrait, direct eye
contact with camera, large round downturned eyes clearly visible,
one or two faint freckles, gentle innocent expression, studio-neutral
background, even lighting, 35mm portrait lens look
```

### 左45°
```
CHAR_HINA_MASTER01_L45 — HINA, head turned 45 degrees to her left,
three-quarter view, short bob silhouette visible, same lighting and
background as front reference
```

### 右45°
```
CHAR_HINA_MASTER01_R45 — HINA, head turned 45 degrees to her right,
three-quarter view, same lighting and background as front reference
```

### 横顔(Profile)
```
CHAR_HINA_MASTER01_PROFILE — HINA, full left profile, short bob and
soft bangs silhouette clearly visible, same lighting and background as
front reference
```

### 全身(Full Body)
```
CHAR_HINA_MASTER01_FULLBODY — HINA, full body standing pose, small
delicate stance, WAKE UP専用の白い服(下記衣装に関する注意を参照),
studio-neutral background, consistent proportions with portrait
references
```

## 表情差分(6種)

1. **通常(ニュートラル)** — `calm gentle neutral expression, soft downturned eyes`
2. **明るい笑顔** — `bright innocent smile, eyes softened, pure and cheerful` (Don't Stop等での基準表情)
3. **控えめな微笑み** — `small quiet smile, calm composure` (WAKE UPカメオでの基準、CUT11で使用)
4. **驚き** — `slightly widened round eyes, soft parted lips, gentle surprise`
5. **無表情/通り過ぎる横顔** — `neutral unremarkable expression, looking straight ahead, not acknowledging surroundings` (CUT11のすれ違いシーン専用、MIU以外には特別視されない演出のため意図的に無表情寄りに)
6. **代表表情(努力家の芯の強さ)** — `quiet determined expression beneath a soft smile, subtle contrast between cute surface and inner resolve`

## 一貫性アンカー(キャラクター崩れ防止の重要ポイント)

- **インナーカラーを入れない**(NANAとの最重要差別化ポイント。誤ってピンク等のインナーカラーを入れないこと)
- そばかすは1〜2個のみ、最小限に抑える(過剰なそばかす描写を避ける)
- 黒髪ショートボブの長さ(NANAより5〜8cm短い)を毎回維持
- WAKE UPのCUT11では、HINAはMIU以外に特別視されない(表情4「無表情/通り過ぎる横顔」を使用し、Don't Stopでの表情2「明るい笑顔」と混同しない)

## 衣装に関する注意

WAKE UP用の「白い服」はDon't Stop用の衣装とは別デザインで、Costume Bible未登録(既知の残課題)。正式デザイン決定までの**技術的な仮置き**として、以下の中立的な描写を使用する: `simple white outfit, no visible logos or brand marks, plain and understated`。彩度をどこまで強調するかはCostume Bible確定待ち(Panel Storyboard既知の課題と一致)。正式デザインが決定次第、Costume Bible登録の上で本ファイルを更新すること。

## 関連

- **CANON(採用済み素材、2026-07-16)**: GitHub `/CANON_FLY77STAR_20260716_final.md` §5「キャラクター & アーティスト」のHINA記述(19歳、白をテーマにしたソロアイドル、SE77NTH.非メンバー)。Character Referenceとして確定。ただしCANONのWAKE UP新構成(4パネル、クラブ出口→ダイナー)にHINAの登場記載はなく、「帰り道の白服カメオ」はLegacy構造(旧12カット)固有の設定である点に留意
- Character Bible: Obsidian Vault `10_Characters/HINA.md`
- Decision Log(HINAとRINの分離): Obsidian Vault `03_Company/Decisions/2026-07-10_HINAとRINの分離.md`
- Image Asset List: `Prompt/IMAGE_ASSET_LIST.md`
