# WAKE UP — CUT01 Panel03（Golden Production Image）Take 1

Production Phase 5継続。本番生成直前の最終レビュー。対象: Scene01 / CUT01 / Panel03、**Take 1のみ**(Take2・Take3は本ファイルでは扱わない)。

本ファイルは`Storyboard/CUT01_Panel03_PRODUCTION_PACKAGE.md`(Final Production Prompt/Negative Prompt/Production QC Checklist/Director Approval Checklist/Production Report)を基に、Take 1の生成直前チェック用に再整理した実行版。既存成果物・Production Packageは変更していない。**AI社員は画像生成を実行していない。**

**2026-07-11追記(Director方針)**: 「群衆は自然に交差点を動き、MIUは完全に静止している——それは微妙だが確実な対比であり、超自然的には見えない。MIUはカメラのためにポーズを取らず、観客が偶然彼女を見つけたかのように、シーンの中に自然に存在している」という演出方針を追加でいただいた。これを①③④⑤へ反映済み。

---

## ① Final Production Prompt（GPT Image用、コピーしてそのまま使用可）

```
Night street-level wide shot of the Shibuya scramble crossing, dense
pedestrian crowd streaming in multiple directions with natural motion,
East Asian Japanese young woman (MIU) standing perfectly still amid the
moving crowd as the single static figure, positioned slightly below
center-frame with generous negative space around her, long light brown
loose wavy hair with a white hairband, warm-toned glossy lips, gold
accessories, calm neutral expression with soft warm eyes and a relaxed
unguarded mouth — not smiling, not blank, an unposed off-guard look,
gaze directed slightly downward and unfocused, not looking at the
camera, vaguely tracking the crowd's movement, casual dark top with
simple jeans or skirt, no visible logos or brand marks, quiet composed
posture with a faint undertone of tension beneath the stillness, the
crowd moves naturally through the intersection while MIU remains
perfectly still, creating a subtle but unmistakable contrast that never
reads as supernatural or staged — she does not pose for the camera, she
exists naturally within the scene as if the viewer has discovered her
by chance, vibrant saturated neon and digital-billboard light filling
the crowd and background, generic fictional store signage only (no
real brand names or logos), MIU lit with a subtly cooler and slightly
desaturated tone relative to the saturated neon around her — as if half
a step removed from reality, cinematic wide shot, 28-35mm lens look,
gentle arc composition leading the eye through the crowd toward MIU,
35mm film grain, anticipatory atmosphere of a night that feels subtly
different from any other, exact facial consistency maintained via the
MIU Character Master fixed reference description (GPT Image, Soul 2
not used)
```

---

## ② Negative Prompt

### 避けるべき描写

```
MIU making direct eye contact with camera, MIU smiling broadly or
showing strong emotion, MIU posing for the camera or striking a
model-like stance, supernatural or eerie appearance, glowing or
ethereal effect around MIU, MIU looking unnaturally cut out or
composited from the crowd, other named characters (AYA, NANA, KAI,
HINA) appearing in frame, daytime or non-night lighting, real brand
logos or readable real store names on signage or clothing, uniform-like
or branded clothing
```

### AI破綻を防ぐ要素

```
multiple duplicate MIU figures, distorted or inconsistent facial
features, extra or malformed limbs and fingers, blurry or warped face,
motion blur applied to MIU herself (only the surrounding crowd should
show motion blur), garbled or illegible signage text, watermark, text
overlay, border, frame, split-screen, comic panel layout,
low-resolution or compression artifacts
```

### Character Masterとの不一致要素

```
hair color other than light brown, straight or short hair instead of
long loose waves, missing or non-white hairband, nude or matte lips
instead of warm-toned glossy lips, silver or colorful accessories
instead of gold, non-East-Asian facial features, incorrect age
appearance or body proportions
```

---

## ③ Director Shooting Notes(最重要演出意図、3項目以内)

1. **MIUは「動く群衆の中の唯一の静止点」であること** — 群衆は自然に交差点を動き、MIUは完全に静止している。これは微妙だが確実な対比であり、**超自然的には見えない**。MIUはカメラのためにポーズを取らず、観客が偶然彼女を見つけたかのように、シーンの中に自然に存在している(2026-07-11 Director方針)
2. **表情は「無表情ではないが作り込まれていない」** — 素の状態、カメラを意識していない、口角の力が抜けている
3. **MIU周辺の光だけがわずかに周囲と異なるトーン**(現実から半歩ずれた質感)——過剰な色被りにしない、あくまで「わずか」に留める

---

## ④ Take 1 Director Goal(今回の生成で必ず達成したいポイント、5項目)

1. MIUがCharacter Masterと完全に一致した顔・髪型(緩巻きライトブラウン+白ヘアバンド)・アクセサリー(ゴールド系)で生成される
2. 群衆の動き(モーション感)とMIUの静止(シャープでブレのない)の対比が一目で分かる形で成立し、かつ**超自然的・合成的には見えない**(微妙だが確実な対比、2026-07-11追加)
3. カメラ目線ではない、不自然にポーズを取っていない——観客が偶然発見したかのような自然な存在感が実現する(2026-07-11追加)
4. 実在ブランド・ロゴ・他キャラクターの混入が一切ない
5. MIU周辺の光のトーン差(現実から半歩ずれた質感)が破綻せず、自然な範囲で表現される

---

## ⑤ Take 1 採用基準(Director Approvedとする条件)

以下をすべて満たす場合のみ「Director Approved」とし、Take 2への再生成は不要と判断する。1項目でも満たさない場合はDirector Reviewを経てTake 2の要否を判断する。

- [ ] Character Masterとの一致(顔・髪型・アクセサリー)に問題がない
- [ ] 表情・視線がDirector Shooting Notes通り(カメラ目線でない、無表情ではない、作り込まれていない)
- [ ] MIUの静止と群衆の動きの対比が視覚的に明確
- [ ] その対比が**超自然的・合成的に見えない**——MIUがポーズを取っておらず、偶然発見されたような自然さがある(2026-07-11追加)
- [ ] Negative Prompt該当要素(AI破綻・ブランド混入・他キャラ混入)が一切見られない
- [ ] 光のトーン差が「わずか」の範囲内(過剰な色被り・不自然な処理に見えない)
- [ ] 衣装が仮描写(ダーク系カジュアル、ロゴなし)の範囲内に収まっている(正式デザインでないことの承認は別途Director Approval Checklistで扱う)

**判定フロー**: 社長がGPT ImageでTake 1を生成 → 上記基準で社長がDirector Review → 全項目クリアで「Director Approved」、Golden Production Image確定 → 未達成項目があればTake 2の要否をご判断いただく(Take 2の資料は本ファイルでは作成していない)。

---

## 関連

- Production Package(詳細版): `Storyboard/CUT01_Panel03_PRODUCTION_PACKAGE.md`
- Character Master: `Reference/CHAR_MIU_MASTER.md`
- Location Master: `Reference/LOC_CROSSING_MASTER.md`
- Director Notes: `Storyboard/CUT01_Panel03_DirectorNotes.md`
- Director Approval Sheet: `Prompt/DIRECTOR_APPROVAL_SHEET.md`
