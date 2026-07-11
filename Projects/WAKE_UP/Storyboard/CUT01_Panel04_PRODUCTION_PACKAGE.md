# CUT01 Panel04 — Production Package

**Status**: 720p Pilot Approved(本セッション外) / Director Decision反映済み(2026-07-11) / **4K Production Package準備完了 — Director Reviewを経て720P Pilot Generationへ進行**

---

## Director Decision反映(2026-07-11)

前回提出時、AI社員(Claude Code)は本Packageの原文と既存のWAKE UPプロダクション成果物(Story Bible、Panel Storyboard、Production Bible、Character Master)との間に5件の不整合を確認し、生成実行を保留して社長確認を仰いだ。社長より以下のDirector Decisionが下され、全項目を反映済み。

| # | 論点 | Director Decision | 反映内容 |
|---|---|---|---|
| 1 | 実在ブランド名 | Productionでは実在ブランド名を積極的に使用しない。QFRONT/STARBUCKS等の固有名は避け、「Iconic scramble crossing buildings」「Large illuminated commercial buildings」「Famous intersection café building」等の一般表現へ置き換える。舞台は「渋谷スクランブル交差点をモチーフとした映画的表現」として扱う | §4 Location Master、§7.2 Main Promptを一般表現へ差し替え |
| 2 | Story Bible | 最新版を正とする。現在Directorが運用しているProduction Bibleを基準とし、旧版との差異がある場合はProduction Bibleを優先する | §5を更新。ただしACT2「Night Walk」構成の全文は本リポジトリのObsidian Vault Story Bible(`06_Projects/WAKE_UP/Overview.md`、Scene1〜3・12カット構成)へまだ統合されていないため、この差分は引き続きオープン事項として記録する(下記「留意事項」参照) |
| 3 | Panel Storyboard | Panel04は「静止していた時間が動き始める」を正式採用。旧Storyboードの「スマホを見る」は旧案として扱い、Production Package側を正とする | `Storyboard/CUT01_絵コンテ.md`のPanel4セクションを更新済み(旧案は「旧案(参考・廃止)」として保持)。本Packageの§6は変更なし(元々新内容と一致) |
| 4 | Costume | Panel03と完全同一衣装を正式仕様とする。衣装記述はCharacter Master / Costume Masterに合わせて修正する | §2・§3・§7.2の衣装描写を、Panel03 Production Package(`CUT01_Panel03_PRODUCTION_PACKAGE.md`)および`CHAR_MIU_MASTER.md`と同一の`casual dark top with simple jeans or skirt, no visible logos or brand marks`へ修正 |
| 5 | File Path | 現在のRepository構成に合わせて修正する。存在しないパスは使用しない | §12 Cross-Referencesを実在パスへ修正 |

**留意事項(引き続きオープン)**: 本Packageの原文(下記「提出時点の原文」参照)が言及する「ACT 2『Night Walk』」構成および「後続Panelでの赤いユニフォームのショーウィンドウ」という伏線は、社長判断により優先されるべき最新Story Bibleの一部と理解しているが、その全文はまだこのリポジトリのObsidian Vault Story Bible(`06_Projects/WAKE_UP/Overview.md`)へ統合されていない。矛盾ではなく未統合の状態として記録し、統合作業は別途指示があり次第実施する。

---

## 修正版 Production Package(Director Decision反映済み、生成にはこちらを使用)

### 1. Theme / Director Intent

**Theme**: 「静止していた時間が、わずかに動き始める。」
(The stillness of time begins to move, ever so slightly.)

**Director Intent**:
Panel03で「偶然見つけた少女」を確立した直後の瞬間。少女(MIU)の内側で何かが動き始める予兆を、観客に「気づかせないまま気づかせる」ように描く。演出は徹底的に抑制的で、映画的空気感を保持する。

### 2. Character Master

- **Subject**: MIU(SE77NTH. Center / Lead Vocal)
- **Reference**: MIU Character Master Golden Reference v1.0(`Reference/CHAR_MIU_MASTER.md`)
- **Costume**: 私服 — `casual dark top with simple jeans or skirt, no visible logos or brand marks`(Panel03・`CHAR_MIU_MASTER.md`「衣装に関する注意」の仮描写と完全同一。Costume Bible未登録のため技術的仮置き)
- **Accessories**: 赤いハートネックレス / ブレスレット / フープピアス(Golden Reference v1.0、`CHAR_MIU_MASTER.md`参照)
- **Hair**: シースルーバング / ゆるいワンカール / ソリーネ(赤茶系)

### 3. Costume Master

Panel03と完全同一衣装(`casual dark top with simple jeans or skirt, no visible logos or brand marks`)。Costume Bible登録はまだ未実施(既知の残課題)。正式デザイン確定後、`CHAR_MIU_MASTER.md`とあわせて本Panelの再生成要否を検討する。

### 4. Location Master

- **Location**: 渋谷スクランブル交差点をモチーフとした映画的表現(Shibuya Scramble Crossing、実在ブランド名は使用しない)
- **Time**: Night
- **Environment Details**:
  - Wet pavement with neon reflections
  - Active pedestrian flow around subject
  - Iconic scramble crossing buildings, large illuminated commercial buildings, a famous intersection café building — generic fictional signage only (no real brand names or logos)
  - Ambient neon light, no artificial glow

### 5. Story Bible(該当箇所)

Panel03(偶然の発見)→ **Panel04(内側の予兆)** → 後続Panelへと繋がる導入部という位置づけは維持する。Panel04はあくまで「動き始めの予兆」であり、視線の先の対象はまだ明示しない。観客には「何かが始まる」という予感だけを残す。

社長運用のProduction Bible(最新版)を正とする方針に基づき、本リポジトリのObsidian Vault Story Bible(`06_Projects/WAKE_UP/Overview.md`、Scene1「渋谷の夜、3人集合〜歩き出す」)と矛盾しない範囲でこの位置づけを採用する。ACT構成名(「ACT 2 Night Walk」)そのものの統合は別途対応(上記「留意事項」参照)。

### 6. Panel Storyboard(構図指針)

- **Shot Type**: Medium shot, gradually moving to slight closer framing
- **Camera Position**: Eye-level
- **Camera Motion**: Slow cinematic dolly-in with subtle handheld stabilization
- **Lens**: 50mm equivalent
- **Composition**: MIUを画面中央〜やや右寄り、群衆の頭部が前景と背景に配置される観察的フレーミング
- **Focus**: MIUに合わせつつ、群衆と背景ネオンは自然なボケ

対応するPanel Storyboard本体: `Storyboard/CUT01_絵コンテ.md` Panel4(2026-07-11 Director Decisionにより「静止していた時間が動き始める」へ更新済み)。

### 7. Generation Prompt

#### 7.1 Reference Image

**Upload**: `MIU_Character_Master_Golden_Reference_v1.0.png`
**Method**: Image reference upload(NOT Higgsfield UUID Element-based)
**Note**: 画像リファレンス+フルテキストプロンプト方式のため、UUID Element経由時の「@-mention only」制約は適用されない。フルテキスト記述を積極的に使用可能。

#### 7.2 Main Prompt

```
Reference the uploaded image as the visual source.

Create a cinematic, ultra-realistic live-action shot.

A young East Asian woman (MIU) stands naturally among the crowd at a
busy nighttime Shibuya Scramble Crossing, its iconic crossing buildings
and large illuminated commercial signage in the background (generic
fictional signage only, no real brand names or logos). She is not
posing and is completely unaware of the camera. She appears as if the
viewer has discovered her by chance in the middle of the city.

Camera:
A slow cinematic dolly-in at eye level using a 50mm lens. Very subtle
handheld movement with natural cinematic stabilization. No sudden
camera movement or dramatic zoom.

Character Motion:
MIU remains almost completely still while the city flows around her.
She slowly turns her head just slightly as if sensing something beyond
the crowd. Her gaze naturally shifts upward and slightly to the side,
never looking directly into the camera. She blinks softly once. Loose
strands of hair move gently in the night breeze. She wears a casual
dark top with simple jeans or skirt, no visible logos or brand marks,
matching her Panel03 appearance exactly. Every movement is subtle and
realistic.

Crowd Motion:
Pedestrians continuously walk around MIU in a completely natural way.
Some people pass in front of her while others move behind her. The
crowd never reacts to MIU. The contrast between her calm presence and
the movement around her should feel accidental rather than staged.

Environment:
Wet pavement reflects neon city lights. Soft cinematic bokeh. Realistic
nighttime atmosphere with natural reflections and subtle ambient light.
No excessive glow or artificial visual effects.

Mood:
Quiet. Mysterious. Emotionally restrained. The audience should feel
they have accidentally discovered someone important without knowing
why. The atmosphere must never feel supernatural or overly dramatic.

Ending:
During the final second, MIU's gaze gently settles on something
outside the frame, quietly suggesting that the story is about to
begin.
```

#### 7.3 Negative Prompt

```
No direct eye contact with the camera.
No smiling.
No exaggerated facial expressions.
No posing.
No dancing.
No supernatural effects.
No unrealistic lighting.
No duplicated characters.
No face or hand distortion.
No background flickering.
No floating objects.
No real brand names or logos (e.g. no QFRONT, no STARBUCKS signage).
No watermark.
No text.
No artificial cinematic gimmicks.
```

### 8. Generation Settings

| Parameter | 720p Pilot | 4K Production |
|---|---|---|
| Tool | Higgsfield Cinema Studio | Higgsfield Cinema Studio |
| Resolution | 720p | 4K |
| Plan | (Pro) | Ultra |
| Seed | (Pilot時に記録された値を4K本番でも使用) | Same as pilot |
| Model | Cinema Studio 3.5 / 4K | Cinema Studio 4K |
| Duration | (実測秒数を記録) | Same as pilot |

**重要**: 4K本番生成は、720pテイクと**同一シード・同一プロンプト構成**で実行すること。演出の再現性を最優先。

### 9. Director Review — 720p Pilot

#### 9.1 Review Checklist

| Item | Result | Note |
|---|---|---|
| Character | ✅ Approved | MIU顔・アクセサリー(赤ハートネックレス等)ブレなし、Golden Reference一致 |
| Composition | ✅ Approved | 群衆との対比が自然、渋谷スクランブル交差点をモチーフとした背景配置に違和感なし |
| Lighting | ✅ Approved | ネオン反射・濡れた路面・夜間の空気感リアル |
| Story | ✅ Approved | カメラ目線なし、視線移動が「気づき」の演出意図と一致 |
| Emotion | ✅ Approved | 抑制された表情、超自然的にならない範囲を維持 |

#### 9.2 Director Feedback

- 人混みの動き、慣性の動き、いずれも問題なし
- Panel03承認基準を全項目で維持できている
- **判断**: このまま同一構成で4K本番に進めてよい

#### 9.3 Director Decision

**720p Pilot: APPROVED**
**Next Step: Director Decision(5点)反映後、720P Pilot Generationへ進む**

### 10. 4K Production Generation — Instructions for AI Employee

#### 10.1 Execution Authority

**Production Policy Version 1.1(2026-07-11、`IMAGE_GENERATION_POLICY.md`)**:
WAKE UP Panel04以降、AI社員(Claude Code)が本番生成実行を担当する。ただし以下の運用ルールを厳守すること。

#### 10.2 Operating Rules

1. **1テーク生成 → 停止 → Director Review → GOで次へ**
   1カット(1テーク)生成したら必ず停止。Director(YU)からの明示的な「GO」「次へ」の指示があるまで、次のカット/次のテークに進まないこと。

2. **自己チェック報告(必須)**
   生成後は毎回、以下5項目で簡潔に自己チェック結果を報告:
   - Character(顔・衣装・アクセサリーの一致)
   - Composition(構図・配置)
   - Lighting(光・色調)
   - Story(演出意図の実現度)
   - Emotion(感情表現の抑制度)

3. **承認後の処理**
   Director承認後のみ、以下を実施:
   - STATUS.md更新
   - Daily Studio Report記録
   - Vault側への記録(Character Bible/Costume Bible更新)
   - Git commit & push

4. **バックアップ体制**
   Claude Codeがタイムリミット等で停止した場合、Codex側に本Packageおよび運用ルールをそのまま引き継ぐこと。引き継ぎ後もサイクル(1テーク→停止→確認→GO)は同一。

#### 10.3 First Action

Director Decision(5点)反映を完了し、コミット・push後、720P Pilot Generationへ進む。生成後は上記5項目の自己チェックとともにDirectorへ報告すること。

### 11. Discovery Log(このPanelから得られた学び)

- **画像リファレンス方式 vs Higgsfield UUID Element方式は別物**:
  Higgsfield Element経由の生成では「@-mention UUID + 最小限テキスト」ルールが有効だが、画像リファレンス(画像アップロード)経由の生成では、フルテキストプロンプト(情緒描写・カメラ指示・演技指示すべて含む)がむしろ精度を上げる。
  → 今後、生成手法ごとにプロンプト構成ルールを別建てで管理する。

- **720p Pilot → 4K Productionの2段階運用**:
  Ultraプランでもクレジット効率を意識し、720pで演出確認 → 承認後に4K本番、というサイクルを標準とする。

- **外部セッション由来の資料は既存成果物との照合が必須**:
  本Panelでは実在ブランド名・Story Bible構成・Panel Storyboard・衣装記述・ファイルパスの5点で既存資料との不整合が確認された。社長Director Decisionにより解決済みだが、今後も外部セッション(ChatGPT/GPT Image/Higgsfieldとのやり取り)由来のPackageは、コミット・生成実行前に必ず本リポジトリの既存成果物と照合すること。

### 12. Cross-References

- `Storyboard/CUT01_Panel03_PRODUCTION_PACKAGE.md`(直前Panel、Golden Production Image、演出連続性の基準)
- `Storyboard/CUT01_絵コンテ.md`(Panel Storyboard、Panel4セクション)
- `Reference/CHAR_MIU_MASTER.md`(Character Master、Golden Reference v1.0)
- `Reference/LOC_CROSSING_MASTER.md`(Location Master)
- Obsidian Vault `06_Projects/WAKE_UP/Overview.md`(Story Bible)
- `IMAGE_GENERATION_POLICY.md`(Production Policy Version 1.1)

---

## 提出時点の原文(参考、修正前。社長より共有いただいた内容をそのまま記録)

以下、社長からいただいたPanel04.mdの内容を原文のまま記録する。上記「修正版 Production Package」がDirector Decision反映後の正式版であり、生成実行にはそちらを使用する。

---

**Status**: 720p Pilot Approved / 4K Production Pending
**Date**: 2026-07-12
**Project**: WAKE UP
**CUT**: CUT01
**Panel**: Panel04
**Continuity**: Direct continuation from Panel03(Golden Production Image, Take1 approved)

---

### 1. Theme / Director Intent

**Theme**: 「静止していた時間が、わずかに動き始める。」
(The stillness of time begins to move, ever so slightly.)

**Director Intent**:
Panel03で「偶然見つけた少女」を確立した直後の瞬間。少女(MIU)の内側で何かが動き始める予兆を、観客に「気づかせないまま気づかせる」ように描く。演出は徹底的に抑制的で、映画的空気感を保持する。

### 2. Character Master

- **Subject**: MIU(SE77NTH. Center / Lead Vocal)
- **Reference**: MIU Character Master Golden Reference v1.0
- **Costume**: 私服 — ライトグレーのオーバーサイズシャツジャケット / 白タンクトップ / デニム
- **Accessories**: 赤いハートネックレス / 赤いハートブレスレット / シルバーフープピアス
- **Hair**: シースルーバング / ゆるいワンカール / ソリーネ(赤茶系)

### 3. Costume Master

Panel03と完全同一。Costume Bible登録はCharacter Master v1.0の「私服スタイル」欄を参照。

### 4. Location Master

- **Location**: 渋谷スクランブル交差点(Shibuya Scramble Crossing)
- **Time**: Night
- **Environment Details**:
  - Wet pavement with neon reflections
  - Active pedestrian flow around subject
  - Realistic Shibuya landmarks visible(QFRONT, STARBUCKS building, etc.)
  - Ambient neon light, no artificial glow

### 5. Story Bible(Applicable Section)

**ACT 2「Night Walk」内の位置づけ**:
Panel03(偶然の発見)→ **Panel04(内側の予兆)** → 後続Panelで具体的な視線対象(赤いユニフォームのショーウィンドウ)へと繋がっていく導入部。

Panel04はあくまで「動き始めの予兆」であり、視線の先の対象はまだ明示しない。観客には「何かが始まる」という予感だけを残す。

### 6. Panel Storyboard(構図指針)

- **Shot Type**: Medium shot, gradually moving to slight closer framing
- **Camera Position**: Eye-level
- **Camera Motion**: Slow cinematic dolly-in with subtle handheld stabilization
- **Lens**: 50mm equivalent
- **Composition**: MIUを画面中央〜やや右寄り、群衆の頭部が前景と背景に配置される観察的フレーミング
- **Focus**: MIUに合わせつつ、群衆と背景ネオンは自然なボケ

### 7. Generation Prompt

#### 7.1 Reference Image

**Upload**: `MIU_Character_Master_Golden_Reference_v1.0.png`
**Method**: Image reference upload(NOT Higgsfield UUID Element-based)
**Note**: 画像リファレンス+フルテキストプロンプト方式のため、UUID Element経由時の「@-mention only」制約は適用されない。フルテキスト記述を積極的に使用可能。

#### 7.2 Main Prompt

```
Reference the uploaded image as the visual source.

Create a cinematic, ultra-realistic live-action shot.

A young East Asian woman (MIU) stands naturally among the crowd at a busy nighttime Shibuya Scramble Crossing. She is not posing and is completely unaware of the camera. She appears as if the viewer has discovered her by chance in the middle of the city.

Camera:
A slow cinematic dolly-in at eye level using a 50mm lens. Very subtle handheld movement with natural cinematic stabilization. No sudden camera movement or dramatic zoom.

Character Motion:
MIU remains almost completely still while the city flows around her. She slowly turns her head just slightly as if sensing something beyond the crowd. Her gaze naturally shifts upward and slightly to the side, never looking directly into the camera. She blinks softly once. Loose strands of hair and her oversized light-gray jacket move gently in the night breeze. Every movement is subtle and realistic.

Crowd Motion:
Pedestrians continuously walk around MIU in a completely natural way. Some people pass in front of her while others move behind her. The crowd never reacts to MIU. The contrast between her calm presence and the movement around her should feel accidental rather than staged.

Environment:
Wet pavement reflects neon city lights. Soft cinematic bokeh. Realistic nighttime atmosphere with natural reflections and subtle ambient light. No excessive glow or artificial visual effects.

Mood:
Quiet. Mysterious. Emotionally restrained. The audience should feel they have accidentally discovered someone important without knowing why. The atmosphere must never feel supernatural or overly dramatic.

Ending:
During the final second, MIU's gaze gently settles on something outside the frame, quietly suggesting that the story is about to begin.
```

#### 7.3 Negative Prompt

```
No direct eye contact with the camera.
No smiling.
No exaggerated facial expressions.
No posing.
No dancing.
No supernatural effects.
No unrealistic lighting.
No duplicated characters.
No face or hand distortion.
No background flickering.
No floating objects.
No brand logos.
No watermark.
No text.
No artificial cinematic gimmicks.
```

### 8. Generation Settings

| Parameter | 720p Pilot | 4K Production |
|---|---|---|
| Tool | Higgsfield Cinema Studio | Higgsfield Cinema Studio |
| Resolution | 720p | 4K |
| Plan | (Pro) | Ultra |
| Seed | (Pilot時に記録された値を4K本番でも使用) | Same as pilot |
| Model | Cinema Studio 3.5 / 4K | Cinema Studio 4K |
| Duration | (実測秒数を記録) | Same as pilot |

**重要**: 4K本番生成は、720pテイクと**同一シード・同一プロンプト構成**で実行すること。演出の再現性を最優先。

### 9. Director Review — 720p Pilot

#### 9.1 Review Checklist

| Item | Result | Note |
|---|---|---|
| Character | ✅ Approved | MIU顔・アクセサリー(赤ハートネックレス等)ブレなし、Golden Reference一致 |
| Composition | ✅ Approved | 群衆との対比が自然、渋谷ランドマーク配置に違和感なし |
| Lighting | ✅ Approved | ネオン反射・濡れた路面・夜間の空気感リアル |
| Story | ✅ Approved | カメラ目線なし、視線移動が「気づき」の演出意図と一致 |
| Emotion | ✅ Approved | 抑制された表情、超自然的にならない範囲を維持 |

#### 9.2 Director Feedback

- 人混みの動き、慣性の動き、いずれも問題なし
- Panel03承認基準を全項目で維持できている
- **判断**: このまま同一構成で4K本番に進めてよい

#### 9.3 Director Decision

**720p Pilot: APPROVED**
**Next Step: Proceed to 4K Production Generation**

### 10. 4K Production Generation — Instructions for AI Employee

#### 10.1 Execution Authority

**Policy Update(2026-07-12)**:
本セッションよりProduction Policy Version 1.0を更新。Panel04以降、AI社員(Claude Code)が本番生成実行を担当する。ただし以下の運用ルールを厳守すること。

#### 10.2 Operating Rules

1. **1テーク生成 → 停止 → Director Review → GOで次へ**
   1カット(1テーク)生成したら必ず停止。Director(YU)からの明示的な「GO」「次へ」の指示があるまで、次のカット/次のテークに進まないこと。

2. **自己チェック報告(必須)**
   生成後は毎回、以下5項目で簡潔に自己チェック結果を報告:
   - Character(顔・衣装・アクセサリーの一致)
   - Composition(構図・配置)
   - Lighting(光・色調)
   - Story(演出意図の実現度)
   - Emotion(感情表現の抑制度)

3. **承認後の処理**
   Director承認後のみ、以下を実施:
   - STATUS.md更新
   - Daily Studio Report記録
   - Vault側への記録(Panel04.md最終版, Character Bible/Costume Bible更新)
   - Git commit & push

4. **バックアップ体制**
   Claude Codeがタイムリミット等で停止した場合、Codex側に本Panel04.mdおよび運用ルールをそのまま引き継ぐこと。引き継ぎ後もサイクル(1テーク→停止→確認→GO)は同一。

#### 10.3 First Action

まずPanel04の4K本番生成を実行し、生成後に上記5項目の自己チェックとともにDirectorへ報告すること。

### 11. Discovery Log(このPanelから得られた学び)

- **画像リファレンス方式 vs Higgsfield UUID Element方式は別物**:
  Higgsfield Element経由の生成では「@-mention UUID + 最小限テキスト」ルールが有効だが、画像リファレンス(画像アップロード)経由の生成では、フルテキストプロンプト(情緒描写・カメラ指示・演技指示すべて含む)がむしろ精度を上げる。
  → 今後、生成手法ごとにプロンプト構成ルールを別建てで管理する。

- **720p Pilot → 4K Productionの2段階運用**:
  Ultraプランでもクレジット効率を意識し、720pで演出確認 → 承認後に4K本番、というサイクルを標準とする。

### 12. Cross-References

- `CUT01_Panel03.md`(直前Panel、演出連続性の基準)
- `Character_Bible/MIU.md`(Character Master v1.0)
- `Costume_Bible/MIU_私服.md`(私服設定、Panel03と共通)
- `Location_Bible/Shibuya_Scramble_Night.md`(ロケーション設定)
- `Story_Bible/WAKE_UP_v2.0.md`(ACT 2「Night Walk」該当節)

---

*Document generated: 2026-07-12*
*Director: YU(FLY77STAR.)*
*Creative Direction Support: チャッピー(ChatGPT chat instance)*
*Execution: クロちゃん(Claude Code, AI Employee)*
