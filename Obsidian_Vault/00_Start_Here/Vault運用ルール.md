# Vault運用ルール

このVaultを10年後も「誰でも5分でわかる」状態に保つための、書き方のルールです。

## 0. すべてこのルールより優先されること

[[FLY77STAR_Philosophy]] が、以下すべてのルールより優先されます。ここに書かれたルールとPhilosophyがぶつかったら、Philosophyを優先し、ルールの方を見直してください。作品制作を止めてまで、以下のルールを守る必要はありません。

## 1. 専門用語には必ず一行説明を付ける

初めて出てきた専門用語には、名前の下(または横)に一行で平易な説明を添えます。

例:

Discovery Log
（今日の気づきノート）

Founder's Journal
（創業者の想い・考えを残すノート）

Knowledge
（正式採用された会社ルール）

Production Bible
（映像制作マニュアル）

- 新しい用語を作ったら、この説明とあわせて [[用語集]] にも追記する。
- 「知っている前提」で書かない。半年後の自分、新しく入った人、AI社員が読んでもわかることを基準にする。

## 2. Founder's JournalとDiscovery Logは書き換えない

- どちらも日付ファイルへの追記のみ。過去のエントリーは削除・修正しない。
- 訂正したいときは、新しい日付のエントリーとして書き、元のエントリーにリンクを貼る。
- 目的は「その時どう考えたか・何に気づいたか」という記録そのものを残すこと。後から見て内容が変わっていても書き換えない。
- 例外: Discovery Logの昇格状態タグ(`#昇格候補` → `#昇格済み`)と、昇格先ノートへの1行リンク追記だけは認める。発見の内容そのものは変えない。詳細は [[05_Knowledge/_Index|Knowledge]] を参照。

## 3. 生の記憶と精製された知識を分ける(二層構造)

- Founder's Journal / Discovery Log = 原液。分類や正しさを気にせず、思いついた瞬間・発見した瞬間にそのまま書く。
- Knowledge / Company/Decisions = 精製後。「収穫の儀式」で見直し、繰り返し使えると分かったものだけを昇格させる。
- Discovery LogからKnowledgeへの具体的な昇格基準(目安: 異なる日に3回以上使われたら候補)は [[05_Knowledge/_Index|Knowledge]] にまとめてある。

## 4. 収穫の儀式(見直しのタイミング)

- **Knowledge Review**: カレンダーではなく件数トリガー。未レビューのDiscovery Logが**10件たまったら**実施する(詳細: [[05_Knowledge/_Index|Knowledge]])。
- 半年〜年次: Founder's Journalを読み返し、`01_Founders_Journal/_節目の振り返り.md` にまとめる。方針として固まったものは `03_Company/Vision_Mission.md` や `Decisions/` に反映。
- 年次: Knowledgeの全ノートの「最終確認日」を棚卸しする。古くなったものは `08_Archive` へ移す(詳細: [[05_Knowledge/_Index|Knowledge]])。

## 5. GitHubとの役割分担

- 制作ルールの正本(せいほん)は常にGitHubリポジトリ直下のファイル(`OPERATING_MANUAL.md` 等)。
- このVaultはそれを上書きしない。正式ルールへのリンクは貼ってよいが、コピーして重複させない(重複すると必ずズレて古くなるため)。
- Vaultが担うのは、ルールブックには書かれない「なぜ」「気づき」「文脈」。

## 6. 階層は深くしすぎない

- フォルダは3階層までを目安にする。
- 横断的に探したいときはフォルダではなくタグ(例: `#CUT17` `#Palmier` `#色ルール`)を使う。

## 7. Daily Studio Reportは30秒で読める量を超えない

- [[09_Daily_Studio_Report/_Index|Daily Studio Report]] は1項目1行、1日分で20行を超えない。
- 詳しい経緯は書かず、該当する場所([[02_Discovery_Log/_Index|Discovery Log]] や [[06_Projects/_Index|Projects]] など)にリンクするだけにする。
- 報告することがないAI社員は書かない。「特になし」で埋めない。

## 8. 書く前に一度検索する(重複を防ぐ)

- 新しくDiscovery LogやKnowledgeを書く前に、[[00_Start_Here/用語集|用語集]] と [[05_Knowledge/_Index|Knowledge]] を検索する。
- すでに同じ気づきがあれば、新規に書かず既存ノートにリンクする。これがVaultを「検索しやすく、迷わない」状態に保つ最初の一歩。

## 9. エンティティは必ずハブノートを持つ(検索性を保つ)

- プロジェクト・キャラクター・ツール・概念など「名前を持つもの」は、1つだけ正式なハブノートを持つ。同じ名前の説明を複数箇所に書き散らさない。
- ハブノートは [[99_Templates/Hub_Note|テンプレート]] を使い、frontmatterに `aliases`(別名・表記ゆれ)を設定する。検索・クイックスイッチャーがどの呼び方でも一発で到達できるようにするため。
- ハブノート末尾には固定フォーマットの「関連」セクション(Knowledge/Projects/People/Characters/AI Employees/Prompt/GitHub正本)を置く。
- 実在の人間・スタッフは [[04_Team/People/README|People]]、AI社員は [[04_Team/AI_Employees/_Index|AI Employees]]、作品内キャラクターは [[10_Characters/_Index|Characters]] と、この3つを混ぜない。検索した時に人物・AI社員・キャラクターが迷子にならないようにするため。
- 新しいハブノートを作ったら、[[00_Start_Here/索引|索引]] に1行追加する。忘れても実害は小さいので気負わなくてよい。
- 詳細な設計意図は [[03_Company/検索システム設計書|検索システム設計書]] を参照。
