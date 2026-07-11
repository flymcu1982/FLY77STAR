# WAKE UP — Production Package: CUT01 Panel03（Golden Production Image）

Production Phase 5継続。対象: Scene01 / CUT01 / Panel03。Director Decision(2026-07-11)により、本Panelを**WAKE UP全体のGolden Production Image**(今後のProduction QC・Character QC・Costume QC・Director Approvalの基準画像)として制作する。

Production Source of Truth: Character Master(`Reference/CHAR_MIU_MASTER.md`) / Costume Master(Costume Bible、**未登録**) / Location Master(`Reference/LOC_CROSSING_MASTER.md`) / Story Bible(Obsidian Vault `06_Projects/WAKE_UP/Overview.md`) / Panel Storyboard(`Storyboard/CUT01_絵コンテ.md` Panel3) / Director Notes(`Storyboard/CUT01_Panel03_DirectorNotes.md`)。

既存成果物は変更していない。本ファイルは補助資料(Production Package)として新規追加する。**AI社員は画像生成を実行していない。**

---

## 対象Panelの前提

CUT01 Panel03「MIU、静止（発見）」(0:03.5–0:05、WS、緩やかなアーク)。動く群衆の中でMIUだけが静止する、本CUTの核となるショット。Director Notes試験運用(2026-07-10)の対象パネルでもあり、既に監督の演出意図が言語化されている唯一のPanel01〜03。

**重要な制約**: MIUの私服はCostume Bible未登録(既知の残課題、継続中)。以下のFinal Production Promptでは、`CHAR_MIU_MASTER.md`に定義済みの**技術的な仮描写**(創作決定ではない)を使用する。Golden Production Imageとして採用する場合、衣装が正式デザインでない前提を関係者間で明確にする必要がある(④参照)。

---

## ① Final Production Prompt(GPT Image用、完成版)

Character Master・Costume Master(仮)・Location Master・Story Bible・Panel Storyboard・Director Notesを統合した最終プロンプト。

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
posture with a faint undertone of tension beneath the stillness,
vibrant saturated neon and digital-billboard light filling the crowd
and background, generic fictional store signage only (no real brand
names or logos), MIU lit with a subtly cooler and slightly desaturated
tone relative to the saturated neon around her — as if half a step
removed from reality, cinematic wide shot, 28-35mm lens look, gentle
arc composition leading the eye through the crowd toward MIU, 35mm
film grain, anticipatory atmosphere of a night that feels subtly
different from any other, exact facial consistency maintained via the
MIU Character Master fixed reference description (GPT Image, Soul 2
not used)
```

**出典対応**:
- Character: `CHAR_MIU_MASTER.md` Character Lock Prompt + 表情差分「1. 通常(ニュートラル)」
- Costume: `CHAR_MIU_MASTER.md`「衣装に関する注意」の仮描写(**未承認、Costume Bible未登録**)
- Location: `LOC_CROSSING_MASTER.md` Location Lock Prompt + STREET角度バリエーション
- Story Bible: テーマ「夢と現実。渋谷の夜から始まるSE77NTH.の第一章」、Scene1(まだ現実側、パラレル演出は未使用)
- Panel Storyboard: `CUT01_絵コンテ.md` Panel3(WS、28-35mm、緩やかなアーク、MIU=唯一の静止点)
- Director Notes: 表情・視線・「現実から半歩ずれた」光のトーン差、静止の質感

---

## ② Negative Prompt

```
MIU making direct eye contact with camera, MIU smiling broadly or
showing strong emotion, multiple duplicate MIU figures, inconsistent
or drifting facial features, blurry or distorted face, motion blur
applied to MIU herself (only the surrounding crowd should show motion),
camera-aware or posed/fashion-shoot stance, real brand logos or
readable real store names on signage or clothing, non-East-Asian
racial features, other named characters (AYA, NANA, KAI, HINA)
appearing in frame, daytime or non-night lighting, oversaturated
blown-out highlights losing detail, garbled or illegible signage text,
uniform-like or branded clothing, watermark, text overlay, border,
frame, split-screen, comic panel layout, low-resolution or compression
artifacts
```

---

## ③ Production QC Checklist(本Panel固有、抽出版)

| 項目 | 確認内容 |
|---|---|
| Character | MIUの髪型(緩巻きライトブラウン+白ヘアバンド)・リップ・ゴールドアクセサリーがCharacter Masterと一致。単一人物として明瞭に描写され、他キャラクターとの取り違えがない |
| Costume | `CHAR_MIU_MASTER.md`の仮描写(ダーク系カジュアル、ロゴなし)から逸脱していない。**ただし正式承認ではなく仮描写である前提をQC結果に明記する** |
| Emotion | Director Notes通り「無表情ではないが作り込まれていない」表情。カメラを意識していない、視線が正面やや下で不定 |
| Lighting | 群衆・背景は彩度の高いネオン、MIU本人はわずかに寒色・低彩度寄りのトーン差が視認できる(「現実から半歩ずれた」印象) |
| Composition | WS構図でMIUが動く群衆の中の唯一の静止点として際立っている(ネガティブスペースの活用含む)。画面中央よりやや下の位置 |
| Story | Story Bibleのテーマ(渋谷の夜、まだ現実側)・Universe Rule(「キャラクターは時間を生きる」= MIUの現行era表現)と矛盾しない。実在ブランドを想起させる要素がない |

---

## ④ Director Approval Checklist(社長最終確認、10項目)

1. MIUの顔・髪型・アクセサリーがCharacter Masterと一致しているか(取り違えなし)
2. 表情が「無表情ではないが作り込まれていない」Director Notes通りの質感になっているか
3. 視線がカメラ目線になっていないか、不自然にカメラを意識していないか
4. 衣装がCostume Bible未登録の**仮描写**であることを理解した上での承認か(正式デザイン確定後に再生成が必要になる可能性を許容するか)
5. MIUだけが群衆の中で静止しているという構図の対比が明確に成立しているか
6. MIU周辺の光が周囲とわずかに異なるトーン(「現実から半歩ずれた」質感)になっているか、または過剰になっていないか
7. 群衆・背景・看板に実在ブランドのロゴや読み取れる実在店舗名が紛れ込んでいないか
8. 他キャラクター(AYA/NANA/KAI/HINA)が誤って写り込んでいないか
9. この画像を「WAKE UP全体のGolden Production Image」として今後全Panelの制作基準に採用してよいか
10. 採用した場合、Panel04以降のQC(Character/Location/Lighting等)は本画像を基準に照合してよいか

---

## ⑤ Production Report

### このPanel制作で注意すべきポイント

- **Costume Bible未確定**が最大のリスク。Golden Production Imageという位置づけ上、後日私服デザインが正式確定した際に本画像の再生成・QC再実施が必要になる可能性が高い。採用時点でこのリスクを明示的に許容するかどうかの判断(④項目4)が重要
- MIU単独の一枚絵であるため、Soul ID的な一貫性(顔・髪型の再現性)の精度がそのまま今後全キャラクター・全Panelの品質基準になる。生成時のブレを最小限にするため、複数バリエーションを生成した上で最もCharacter Masterに忠実な1枚を選定することを推奨
- 「現実から半歩ずれた」光のトーン差はDirector Notesの核となる演出意図だが、過剰にすると単なる色補正ミスに見えるリスクがある。QC時は「わずかな差」であることを重視する

### Panel04への引き継ぎ事項

- Panel04(スマホを見る、MS、ドリーイン)はPanel03からの芝居の連続(カット割りせず推移)想定。Panel03で確立した衣装・ライティング基準(仮描写含む)をそのまま引き継ぐこと
- Panel04で初めてスマートフォン(`CUT01_P04_PROP01`)という小道具が登場する。Panel03のGolden Production Imageには含まれないため、小道具の描写基準は別途Panel04制作時に定める必要がある
- Director Notesの「次パネルへの感情のバトン」(周囲との対比→本人内面へのズームイン)を踏まえ、Panel04の表情はPanel03よりもわずかに内向きな質感に調整する

---

## 関連

- Production Prompt元資料: `Storyboard/CUT01.md` / `Storyboard/CUT01_絵コンテ.md`(Panel3仕様)
- Character Master: `Reference/CHAR_MIU_MASTER.md`
- Location Master: `Reference/LOC_CROSSING_MASTER.md`
- Director Notes: `Storyboard/CUT01_Panel03_DirectorNotes.md`
- Director Approval Sheet: `Prompt/DIRECTOR_APPROVAL_SHEET.md`
- Pilot Production(Panel01): `Storyboard/CUT01_Panel01_PILOT_PRODUCTION.md`
- Story Bible: Obsidian Vault `06_Projects/WAKE_UP/Overview.md`
