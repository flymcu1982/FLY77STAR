# HANDOFF.md

現在の作業状態の引き継ぎ記録。Claude Code / Codex どちらが作業する場合も、着手前に本ファイルを確認すること。作業終了時は必ず本ファイルを更新してから次の担当に渡す。

最終更新: 2026-07-18(FLY77STAR U., Codex)

## 公式情報・SNS登録(2026-07-18)

FLY77STAR. 公式SNS・Webサイト一覧は [`OFFICIAL_INFO.md`](OFFICIAL_INFO.md) にまとめている。

**登録完了アカウント**（2026-07-18 FLY77STAR U.による）:
- TikTok: @fly77star
- Instagram: @fly77star
- X公式: @FLY77STAR_JP
- X LAB: @FLY77STAR_LAB
- 公式サイト: https://flystar77-studio.netlify.app/

**公開作品・準備状況**:
- 『Distance』(RUI) — ショート2本公開中、YouTube 2026年8月配信予定
- 『WAKE UP』(SE77NTH.) — 公開準備中

**コンテンツ製作スケジュール**:
- **Note公式アカウント** — 2026年7月末製作予定、『Distance』YouTube配信時（8月）に同時公開

**YouTube解像度方針**:
- 4K と 1K の2系統で運用する

**情報発信チャネル**: SNS全体でMV・Shorts・noteの公開情報を発信。

## YouTube 運用方針(2026-07-17)

詳細: [`YOUTUBE_OPERATIONS.md`](YOUTUBE_OPERATIONS.md) 参照

**決定事項**（FLY77STAR U.最終承認済み）:
- 配信解像度: 4K と 1K
- 公式チャンネル: 既存 `@yuyama6664` をブランド移行（新規開設しない）
- 既存動画: 削除禁止、分類管理（公開継続/限定公開/非公開/再編集活用）
- 公式Gmail: 新規作成 OK（アドレス未確定、YU指定）
- 本番操作（ハンドル確定・バナー変更・公開設定変更・新作公開）: YU最終承認待ち

**現在**: 運用方針の記録を完了。チャンネル移行の本番作業は YU最終承認待ち。

## 公式Gmail AI社員運用体制（2026-07-17）

詳細: 以下5つのドキュメントを参照
- [`OFFICIAL_GMAIL_OPERATIONS.md`](OFFICIAL_GMAIL_OPERATIONS.md) — 全体運用マニュアル
- [`AI_MAIL_REVIEW_RULES.md`](AI_MAIL_REVIEW_RULES.md) — メール分析・判定ルール
- [`GMAIL_LABEL_POLICY.md`](GMAIL_LABEL_POLICY.md) — ラベル運用ポリシー
- [`MAIL_RESPONSE_APPROVAL_FLOW.md`](MAIL_RESPONSE_APPROVAL_FLOW.md) — メール返信承認フロー
- [`CODEX_GMAIL_AUTOMATION.md`](CODEX_GMAIL_AUTOMATION.md) — Codex 自動化実行指示

**実装状況**（FLY77STAR U.実装完了）:
- Gmail アカウント: `fly77star.official@gmail.com` 作成・ログイン・リカバリー設定完了
- AI社員役割: Mail Reception Department（読み取り・分類・報告）
- 日報: 毎日 18:00 に YU へ報告（重要度別・カテゴリ別分類）
- 返信フロー: AI が下書き作成 → YU が承認・修正 → YU が送信

**運用フェーズ**:
- **Phase 1（現在）**: 毎日のメール確認・分類・報告（手動）
- **Phase 2（2026-07-24～）**: 週間レポート・月間監査の自動化（Codex）
- **Phase 3（2026-08-07～）**: 返信下書き自動準備（Codex）
- **Phase 4（TBD）**: Gmail API / OAuth 統合

**重要ルール**:
- ✅ AI社員: メール読み取り、分類、下書き作成、日報報告
- ❌ AI社員: パスワード管理、メール送信、ラベル自動付与、削除
- 👤 YU のみ: Gmail ログイン、OAuth認証、メール送信、削除、ラベル管理

**現在**: Phase 1 運用開始準備完了。AI社員が毎朝 09:00 からメール確認を開始予定。

## 進行中の企画・プロジェクト

### 制作中
- WAKE UP(`Projects/WAKE_UP/`) — Production Phase 5、CUT01パイロット制作中

### 企画・検討中（2026-07-18 新規追記）
**CM タイアップMV 制作予定**: [`CM_PROJECTS.md`](CM_PROJECTS.md) 参照

**HINA（アイドル）関連**:
- 「Don't Stop」— ポッキー CM タイアップ版、MV同時アップ予定
- 「SPOT LiGHT」（2番）— KAI、バスケットボール男子ワールドカップ CM イメージ版
- 「水かい」— CM タイアップ版（バスケットボール関連）

**グループ / 他アーティスト**:
- 「WAKE UP」(SE77NTH.) — アパレルブランド CM タイアップ版
- 「スウェイカップセブンス」（3人）— アパレル CM タイアップ版

## 現在のプロジェクト

WAKE UP(`Projects/WAKE_UP/`)

## Web / Netlify 引き継ぎ(2026-07-17)

FLY77STAR 公式Webサイトまわりで、以下を確認・反映済み。

1. **公開URL切替確認**
   - 新URL: `https://fly77star-studio.netlify.app/`
   - 旧URL: `https://flystar77-studio.netlify.app/`
   - 2026-07-17時点で、新URLは `HTTP 200`、旧URLは `HTTP 404` を確認済み

2. **正式管理対象**
   - Git上の管理先: `Web/netlify_site/`
   - ただし作業中に `Web/netlify_site 2/` と `Web/netlify_site 2.zip` が生成されている
   - 追跡・commit対象は `Web/netlify_site/` を優先すること
   - `Web/netlify_site 2/` は未追跡の作業残骸として残っているため、削除や整理はYU確認後に行う

3. **動画公開ポリシー更新**
   - 残す動画:
     - `Distance` ショート2本のみ
     - `assets/distance_short_intro.mp4`
     - `assets/distance_short_sabi.mp4`
   - 停止済み:
     - `Distance` フル動画
     - `Distance` teaser
     - `TOMORROW` 動画
     - `STEP by STEP / ENERGY-D CM` 動画
     - `FANG CM 15s / 30s` 動画
   - 上記停止動画は、サイト上ではポスター画像 + 公開停止中メッセージへ置換済み
   - YouTube解像度方針は `4K と 1K`

4. **URL表示テキスト**
   - サイト内のWEB表示は `FLY77STAR-studio.netlify.app` に変更済み
   - これは表示テキストのみであり、実URL変更はNetlify側で行う

5. **写真・ポスター復旧**
   - `assets/` 欠落により写真・ポスターが404になっていたため復旧済み
   - `rui_snap_*` / `ruka_snap_*` / `talent_*` / 各poster画像 / teaser動画は表示確認済み

6. **関連コミット**
   - `841bb1d` `web: refine hero title treatment`
   - `52939da` `web: remove Distance, TOMORROW, and CM videos`

7. **次回AI社員向け注意**
   - `netlify.app` の実URL変更はHTML修正ではなくNetlify設定作業
   - Web更新後は、公開URLの `HTTP 200/404` を新旧両方で確認すること
   - 動画を戻す場合でも、YU最終承認なしで `Distance` フル / `TOMORROW` / CM動画を再公開しないこと

## CANON受領(2026-07-16、最重要)

社長より**FLY77STAR CANON 完全制作基盤**(`CANON_FLY77STAR_20260716_final.md`、FLY77STAR U.承認・確定版)と**AI社員向け最終統合発注書**(`FLY77STAR_AI社員向け_最終統合発注書_20260716.md`)を受領し、リポジトリルートへ登録した。CANONは全制作活動の中核・最上位資料であり、全AI社員は実装前に必ず参照すること。

**CANONと既存リポジトリ資料の主な差分(Director確認待ち、勝手に上書きしない)**:

1. **WAKE UPの物語構成が大きく変更されている**: CANONでは「青い時刻4:30AM、クラブ出口の3人、MIU『始発まであそこで待とう！』、AYAがダイナーのドアを開ける」という4パネル構成+ラストコーラス(満員ライブ、KAIステージ・LIEN DJ)+エンディング(NANA「楽しかったね」)。既存リポジトリの12カット構成Story Bible(渋谷スクランブル交差点開始、KAI=謎のコック、HINA白服カメオ)とは別物。既存CUT01〜12のStoryboard資産の扱い(旧案化するか)はDirector判断待ち
2. **「Panel04」の指し先が2つ存在**: CANONの新4パネル構成のPanel4=「AYAがダイナーのドアを開ける」。従来リポジトリのCUT01 Panel04=「交差点でMIUの時間が動き始める」。近日のDirector指示の「Panel04」「未解決5点」の混乱はこの名前衝突が原因である可能性が高い。**2026-07-16、この衝突を含むリポジトリ内の全「Panel04」ファイル(4件: CUT01/CUT03/CUT08/CUT12)を`PROJECT_CUT##_PANEL##_内容名`形式へリネーム済み(対応表: `Obsidian_Vault/08_Studio_OS/Rules/Panel04_命名規則_旧新ID対応表.md`)。ただしファイル名の衝突が解消されただけで、CANONとの物語構成そのものの統合(上記1点目)はまだDirector判断待ち**
3. **新キャラクター**: LIEN(DJ/フロアコマンダー、確定)はVault未登録。RIN/RINの父(AKIHIKO)/RUI/RUKAはハブノート既存。LIENのCharacter Bible登録が必要
4. **カラーコード不一致**: CANON本体(§1: Navy #0F0F1A/Silver #C0C0C7/Star Blue #1E5BA8)と発注書(Navy #0A0F1A/Silver #C0C3C7/Star Blue #1E9BFF)で3色とも値が異なる。Web/バナー実装前に要確認
5. **CANON §6の書式崩れ**: RUKA『TOMORROW』セクションの直後にWAKE UPのステータス行が見出しなしで続いており、WAKE UP見出しが欠落している模様(原文のまま保存済み)
6. MIUの記述差: CANONは「ライトブラウンのウェーブ」のみで、既存Character Masterの識別性の核「白ヘアバンド」に言及なし。外部セッション由来の「シースルーバング/ソリーネ(赤茶系)」とも整合未確認

**発注書タスクの実行可能性(この環境からの制約)**: YouTube/TikTok/Instagram/note/Google Formのアカウント作成・投稿・設定はこの実行環境からは操作不可(社長側またはブラウザ作業が必要)。Netlify(Webサイトリニューアル)はMCPツール経由で対応可能な見込み。サムネイル等の画像生成はProduction Policy v1.3によりAI社員は実行しない(設計のみ)。ショート動画編集はPalmier側の工程。

## 現在の工程

Production Phase 5。CUT01のPanel単位パイロット制作中。Production Policy Version 1.3準拠(`IMAGE_GENERATION_POLICY.md`)。

**技術検証タスクの結論(2026-07-11)**: `generate_video`(get_cost:trueの無課金見積りプリフライトを含む)も含め、Higgsfield MCP経由の生成系ツールはこの環境(managed remote execution environment)では承認待ちにより実行不可能と確定。Director判断により、**v1.1で導入した「AI社員による生成実行」の例外はv1.3で撤回**。生成実行はDirector/GPT Image運用側へ戻った。AI社員はProduction Package作成・QC・記録・Git管理を担当する原則に復帰。

**現在の状態(2026-07-11、CUT01 Panel04)**: Directorより「CUT01 Panel04のProduction Package再作成は、絵コンテ側の未解決5点(実在ブランド名/Story Bible版/Panel Storyboard整合/衣装記述矛盾/ファイルパス不一致)についてDirectorが判断した後に指示する」との指示があり、待機中。**⚠️留意(未解決のまま)**: この5点は、本セッション内で同日(2026-07-11)に一度「Director Decision」として解決済み・コミット済み(commit `b72ea77`、`Storyboard/WAKE_UP_CUT01_PANEL04_静止時間動き出し_PRODUCTION_PACKAGE.md`修正版・`CUT01_絵コンテ.md`更新・Decision Log記録)。最新のDirector指示はこれを「未解決のまま」としており、両者に矛盾があるためClaude Codeより確認依頼中(次に対応するAIは、Directorへこの矛盾を確認してから作業すること)。**2026-07-12追記**: 別件として「CUT05→CUT06(POP DINERへの接近シーン)」についてDirector Decisionがあり反映済み(下記参照)だが、これは**CUT01 Panel04の5点とは無関係の決定**であり、Panel04の矛盾は本追記時点でも未解決のまま。

**2026-07-12、CUT05→CUT06(POP DINERへの接近シーン)Director Decision反映**: POP DINERへ向かう追加の歩行テイクは削除、入口を通り過ぎてから戻る動線は不採用(歩行シーンの過剰化を避ける)。次の正式な展開はCUT06 Panel1(AYAがPOP DINERのドアを開けるシーン、旧「誰の視点かは限定しない」から変更)から開始。前後の接続は編集(Palmier)で補完。`CUT05_絵コンテ.md`/`CUT06_絵コンテ.md`/`CUT06_Panel01_DirectorNotes.md`へ反映済み、Decision Log・Discovery Log記録済み。テイク修正上限ルール(`Obsidian_Vault/08_Studio_OS/Rules/テイク修正上限ルール.md`)を適用。**この決定はCUT01 Panel04の未解決5点を解決するものではない。**

## Production Baseline(Director Decision、2026-07-11)

| Panel | 役割 | 状態 |
|---|---|---|
| CUT01 Panel01 | Location Validation | Go(社長承認済み、未生成) |
| CUT01 Panel02 | Camera Validation | Go(未生成) |
| CUT01 Panel03 | **Golden Production Image**(基準画像) | Take1 Production Package社長承認済み(未生成) |
| CUT01 Panel04 | 本番制作(720pテイクを本セッション外で承認済み) | **生成実行はDirector側へ復帰(v1.3)。Production Package再作成はDirectorの5点再判断待ちで保留中(下記「現在の工程」の留意事項参照)** |

## 完了済み

- Character Master 5点(MIU/AYA/NANA/KAI/HINA)、Location Master 5点(いずれも設計のみ、生成画像なし)
- Image Asset List / Asset ID / 撮影優先順位 / Image QC Checklist / Director Approval Sheet
- CUT01 Panel01 Pilot Production(Location Validation)、Panel03 Production Package + Take1レビュー(Golden Production Image)
- MIU Diner Ver.・AYA Diner Ver.・NANA Diner Ver.・KAI Cook Ver.(衛生仕様修正版) — 衣装、Costume Bible未登録
- Panel04: 720pテイクが本セッション外(社長⇄ChatGPT/GPT Image/Higgsfield)で承認済み(Character/Composition/Lighting/Story/Emotionすべて問題なしと判断)
- Panel04.md原文と既存プロダクション成果物の不整合5点(実在ブランド名/Story Bible/Panel Storyboard/Costume/File Path)を検出し生成保留、Director Decision(2026-07-11)で全点解決。`Storyboard/WAKE_UP_CUT01_PANEL04_静止時間動き出し_PRODUCTION_PACKAGE.md`を修正版として更新、`CUT01_絵コンテ.md` Panel4も更新済み(その後、Directorより「未解決のまま」との指示があり矛盾を確認依頼中、上記「現在の工程」参照)
- CUT05→CUT06(POP DINERへの接近シーン)Director Decision(2026-07-12)反映: 歩行テイク過剰の是正、CUT06 Panel1をAYAのドア開けシーンへ視点固定
- **2026-07-16、Panel04命名規則リネーム**: CUT01/CUT03/CUT08/CUT12の「Panel04」4ファイルを`PROJECT_CUT##_PANEL##_内容名`形式へリネーム(git mv、既存ファイルは削除せず、旧ファイル名はLegacy IDとして各ファイル冒頭に保持)。本文内参照(パス・wikilink)も更新。対応表: `Obsidian_Vault/08_Studio_OS/Rules/Panel04_命名規則_旧新ID対応表.md`。**Panel01〜03を含む全17件の一括リネームは、CANONとStoryboardの整合性が安定してから別フェーズで検討(Director判断、2026-07-16)**
- **2026-07-16、既存12カット資産のLegacy化**: Story Bible(Vault `06_Projects/WAKE_UP/Overview.md`)、STATUS.md、PRODUCTION_BOARD.md、`Storyboard/`フォルダにLegacy noticeを追記(新規: `Storyboard/00_LEGACY_STRUCTURE_NOTICE.md`)。ファイルは削除・移動せず、そのまま保持。採用済み素材(Character Master5点、POP DINER関連Location Master2点)にCANON参照リンクを追記。渋谷交差点・帰り道関連のLocation Master3点(CROSSING/STREET/SIDEWALK)は「Legacy構造固有の可能性が高い」と注記(CANONの新構成に該当描写がないため)、KAI/HINAのCharacter MasterにはLegacy構造固有の設定(KAI=謎のコック、HINA=帰り道カメオ)である旨を注記
- **2026-07-16、LIEN Character Bible登録**: `Obsidian_Vault/10_Characters/LIEN.md`をCANON §5・§7を基に新規作成。`10_Characters/_Index.md`・`00_Start_Here/索引.md`へ登録

## 重要決定

- HINAはソロアーティスト(SE77NTH.のメンバーではない)。**Character Bibleへの正式反映・Decision Log記録はまだ未実施(下記「次の作業」参照)**
- 通常の画像制作はGPT Imageを標準とする。Nano BananaはProductionフローから除外
- Soul 2(Higgsfield Soul 2.0)は雰囲気重視の限定用途のみ。Character Masterには使用しない
- **2026-07-11、Production Policy Version 1.1: WAKE UP Panel04以降、AI社員(Claude Code)がHiggsfield/GPT Imageでの本番生成を実行する運用へ変更。** ただし厳格運用サイクル必須(1テーク生成→自己チェック→改善提案→Director Review→明示的GOで次へ、承認後のみ記録・コミット)。Panel01〜03はこの変更の対象外(引き続き社長/GPT Image側が生成)
- **2026-07-11、Production Policy Version 1.3: 上記v1.1の例外を撤回。** 技術検証タスクで`generate_video`含むHiggsfield MCP生成系ツールがこの環境で実行不可能と確定したため、生成実行はDirector/GPT Image運用側へ戻った。AI社員はProduction Package作成・QC・記録・Git管理を担当する原則に復帰
- **2026-07-11、Studio OS v1.3: 「調査タスクと制作タスクの分離」を運用原則として正式採用(`AI_WORKFLOW_V1.md`)。** 調査タスク(MCP/API/Higgsfield/Git/外部サービス/モデル確認/権限確認)で技術的ブロッカーが発生した場合、制作タスク(Production Package/画像生成/動画生成/QC/Documentation)へ進まず、技術課題解決→Director報告→解決後に制作再開、の順を守る。Production EnvironmentをProductionより優先
- **2026-07-11、Production Policy Version 1.2: 「分からないまま進まない」を最優先原則として明文化。** MCP・外部サービス・APIで承認待ち・権限不足に遭遇した場合、推測・代替値では絶対に進めず、①何を実行しようとしたか②何がブロックされたか③何が分かっていて何が分からないか④Directorに何を確認してほしいか、の4点整理で必ず報告・停止する。同一Seedを取得できない場合はDirector Approved Pilotをbaselineとして4K生成する運用も新設。Panel04の720P Pilot Generation試行中に発生したHiggsfield MCP承認待ちブロッカーへの対応がこのルール制定の契機
- 実際の画像は原則として社長とChatGPT側で制作・採用する(Panel04以降のみ例外)
- AI社員は設計、文書化、QC、登録、レビューを担当する
- KAIコック衣装では指輪、時計、ブレスレットを外し、7ネックレスは制服内へ収納。両耳ダイヤスタッドを採用(Cook Ver.限定の承認済み仕様、通常Character Masterは上書きしない)
- MIU Golden Reference v1.0(Panel04開発より): 赤いハートネックレス/ブレスレット/フープピアス。CHAR_MIU_MASTER.mdへの反映要確認(下記「次の作業」)
- **2026-07-12、CUT05→CUT06 Director Decision**: POP DINERへの追加歩行テイクは削除、入口を通り過ぎて戻る動線は不採用。正式な次の展開はCUT06 Panel1(AYAがドアを開ける)から開始、前後は編集で補完。CUT01 Panel04の5点とは別件

## 次の作業

- **最優先**: CANONと既存リポジトリ資料の差分6点(上記「CANON受領」参照)についてDirectorの判断を仰ぐ。Panel04ファイル名の衝突は解消済み、既存12カット資産はLegacy notice(削除・移動なし)を追記済みだが、(1)Legacy構造とCANONのどちらを最終的に正式採用とするか(または統合するか)自体はまだ未確定
- Directorへ「Panel04絵コンテ5点は本セッション内で一度解決済み・コミット済み(commit `b72ea77`)」という矛盾を確認する(CANON受領により、この混乱は新旧Panel04の名前衝突が原因の可能性が高いと判明)
- HINAをソロアーティストとしてCharacter Bibleへ正式反映する
- Decision Logへ決定を記録する
- Discovery Logの「HINA: SE77NTH. VOCAL」矛盾を解決済みに更新する
- 完成したCharacter MasterとCostume Masterを登録し、Image QCとDirector Approval Sheetを更新する
- Story Bible: ACT2「Night Walk」構成のObsidian Vault Story Bible(`06_Projects/WAKE_UP/Overview.md`)への統合(社長より全文共有があれば対応)

## 禁止事項

- 完成画像の再生成(Director承認済みのものを無断で作り直さない)
- 承認済み設定の変更
- HINAをSE77NTH.メンバーとして登録すること
- Studio OSの無断改修(`AI_WORKFLOW_V1.md`のバージョン番号、現行v1.3)
- 調査タスク(MCP/API/Higgsfield/Git/外部サービス確認等)で技術的ブロッカーが発生した状態のまま制作タスクへ進むこと(Studio OS v1.3、「調査タスクと制作タスクの分離」)
- AI社員が本番画像・動画生成を実行すること(Version 1.3で撤回済み。Panel04も含め全カットでDirector/GPT Image運用側が実行する)
- MCP・外部サービス・APIが承認待ち/権限不足の場合に、推測のモデルID・Seed・代替値で処理を進めること(Version 1.2、最優先禁止事項)
- Directorの明示的な指示なしにPanel04 Production Packageを再作成すること(5点の再判断待ちで保留中)

## 関連ファイル

- `Projects/WAKE_UP/STATUS.md`(プロジェクト進捗)
- `Projects/WAKE_UP/PRODUCTION_BOARD.md`(Production Board)
- `Projects/WAKE_UP/Reference/CHAR_*_MASTER.md`(Character Master仕様)
- `Projects/WAKE_UP/Prompt/IMAGE_QC_CHECKLIST.md`(Image QC基準)
- `Projects/WAKE_UP/Prompt/DIRECTOR_APPROVAL_SHEET.md`(承認トラッキング)
- `Projects/WAKE_UP/Storyboard/CUT01_Panel03_Take1.md`(Golden Production Image Take1レビュー)
- `IMAGE_GENERATION_POLICY.md`(Production Policy Version 1.3)
