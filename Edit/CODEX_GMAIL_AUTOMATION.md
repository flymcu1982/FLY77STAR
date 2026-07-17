# Codex Gmail Automation Instructions（自動化システム用実行指示）

**Document Version:** 1.0  
**Created:** 2026-07-17  
**Status:** 自動化タスク定義完了・スケジューリング準備中

---

## Overview

Codex（自動化・スケジューリングシステム）が実行する Gmail 関連のタスク定義。  
Claude Code / AI社員の日常業務を自動化。

**対象システム:**
- スケジューラー（Cron等）
- ワークフロー管理ツール
- Codex / その他の自動化エンジン

---

## Task 1: Daily Mail Review（毎日のメール確認）

### タスク定義

| 項目 | 詳細 |
|------|------|
| **タスク名** | Daily Mail Review |
| **実行頻度** | 毎日 09:00 |
| **実行者** | AI社員（Claude Code） |
| **実行時間** | 約30分 |
| **成果物** | 日報フォーマット |

---

### 実行手順

#### Step 1: Gmail にアクセス

**実行内容:**
- Gmail UI を開く（ブラウザまたはモバイルアプリ）
- fly77star.official@gmail.com のアカウントで YU がログイン（完了済み）
- AI社員は "受信トレイ" を確認開始

**チェック:**
- [ ] 未読メール数を確認
- [ ] スター付きメール（★）を確認
- [ ] 前日からの繰越未読をチェック

**出力例:**
```
【本日のメール確認開始】
- 未読メール: 5件
- スター付き: 2件
- 前日繰越未読: 1件
```

---

#### Step 2: 優先度の高いメールをスキャン

**対象:**
- 🔴 URGENT の可能性があるメール
- 🟠 HIGH の可能性があるメール
- 返信期限が迫っているメール

**実行内容:**
1. 件名を読む
2. 送信者を確認
3. 本文の冒頭をスキャン
4. 重要度を判定

**出力例:**
```
【重要度の高いメール】

1. 件名: 「エラー: YouTube チャンネル制限」
   送信者: noreply@youtube.com
   重要度判定: 🔴 URGENT
   → 即 YU に報告（電話推奨）

2. 件名: 「CM制作依頼のご相談」
   送信者: inquiry@agency.jp
   重要度判定: 🟠 HIGH
   → 本日中に YU に報告
```

---

#### Step 3: メール分類・ラベル提案

**実行内容:**
- 各メールをカテゴリに分類
- ラベル付与の提案を作成
- 返信が必要かを判定

**出力例:**
```
【本日のメール分類】

📋 WORK: 2件
  - CM制作依頼
  - ウェビナー企画相談

🤝 COLLAB: 1件
  - ゲーム企業のコラボ提案

📱 PLATFORM: 3件
  - YouTube 通知
  - TikTok フォロワー通知
  - Instagram インサイト通知

⚙️ SYSTEM: 2件
  - Netlify デプロイ完了
  - GitHub セキュリティアラート

👥 FAN: 4件
  - ファン質問 x2
  - 感想メール x2

⚫ SPAM: 3件
  - 営業メール
  - 詐欺メール疑い x2

【提案されたラベル付与】
- 🔴 URGENT: 1件
- 🟠 HIGH: 3件
- 🟡 MEDIUM: 6件
- 🟢 LOW: 5件
```

---

#### Step 4: 返信が必要なメール抽出

**判定基準:**
返信が必須 / 推奨 のメールのみ抽出

**出力例:**
```
【返信が必要なメール】

優先度1: 緊急対応
- YouTube チャンネル制限通知（確認・状況把握が必須）

優先度2: 本日中対応
- CM制作依頼への詳細確認返信
- コラボ提案への検討中の旨返信

優先度3: 今週中対応
- ファン質問 x2 への回答返信

【推奨アクション】
1. AI社員が返信下書きを作成
2. YU が承認後に送信
```

---

#### Step 5: 日報作成・YU に報告

**出力フォーマット:**
上記の「OFFICIAL_GMAIL_OPERATIONS.md」の「日報テンプレート」を使用

**報告方法:**
- メール / チャットで YU に送信
- または Slack / その他の連絡ツールで転送

---

### Codex タスク定義（YAML形式）

```yaml
Task:
  name: Daily Mail Review
  schedule: "0 9 * * *"  # 毎日 09:00
  
  steps:
    - step: 1
      name: "Gmail 受信トレイを開く"
      action: "manual-access"
      note: "YU が既にログイン済みの状態を想定"
      
    - step: 2
      name: "未読メール数・重要メールをスキャン"
      action: "scan-and-categorize"
      time_limit: "15分"
      
    - step: 3
      name: "メール分類・ラベル提案"
      action: "classify-emails"
      output: "分類リスト"
      
    - step: 4
      name: "返信が必要なメール抽出"
      action: "extract-responses"
      output: "返信対象リスト"
      
    - step: 5
      name: "日報作成・報告"
      action: "generate-report"
      output: "日報ドキュメント"
      
  owner: "Claude Code (AI社員)"
  approval_required: false
  data_security: "機密情報を含まない"
```

---

## Task 2: Urgent Mail Alert（緊急メール通知）

### タスク定義

| 項目 | 詳細 |
|------|------|
| **タスク名** | Urgent Mail Alert |
| **実行頻度** | リアルタイム（新メール受信時） |
| **実行者** | Codex / 自動通知システム |
| **実行時間** | 1分以内 |
| **成果物** | YU への緊急通知 |

---

### 実行手順

#### Step 1: 緊急メール検出

**トリガー条件:**
```
IF 
  (件名に「緊急」「エラー」「停止」「削除」「制限」) 
  OR
  (送信者が YouTube / TikTok で「ポリシー違反」「制限」)
  OR
  (Netlify / GitHub で「エラー」「アラート」)
THEN
  → 即 Alert 発火
```

**検出例:**
- ✅ 「YouTube チャンネルが24時間停止されました」
- ✅ 「Netlify デプロイエラー」
- ✅ 「SSL証明書の有効期限切れ警告」
- ✅ 「不正アクセスが検出されました」

---

#### Step 2: 緊急通知を YU に送信

**通知方法:**
1. **電話（推奨）** - 最も緊急性が高い
2. **SMS / チャット** - 次点
3. **メール** - 最後の手段

**通知内容:**
```
【緊急通知】公式Gmail より

件目: [元のメール件名]
送信者: [送信元]
概要: [メール内容の要点]

詳細は Gmail をご確認ください。
```

**例:**
```
【緊急通知】公式Gmail より

件目: YouTube チャンネル - ポリシー違反警告
送信者: noreply@youtube.com
概要: チャンネルが24時間停止状態です。
      詳細確認と異議申し立ての検討が必要です。

詳細は Gmail をご確認ください。
```

---

### Codex タスク定義

```yaml
Task:
  name: Urgent Mail Alert
  trigger: "incoming-email"
  
  detection_rules:
    - pattern: "緊急|エラー|停止|削除|制限|アラート"
      fields: ["subject", "body"]
      sensitivity: "high"
      
    - pattern: "ポリシー違反|不正アクセス|有効期限切れ"
      fields: ["subject", "body"]
      sensitivity: "critical"
      
  notification_flow:
    - priority: 1
      method: "phone_call"
      recipient: "YU"
      
    - priority: 2
      method: "sms"
      recipient: "YU"
      
    - priority: 3
      method: "email"
      recipient: "YU"
      
  owner: "Codex Automation"
  approval_required: false
  security: "YU のみに通知"
```

---

## Task 3: Weekly Mail Summary（週間メール集計）

### タスク定義

| 項目 | 詳細 |
|------|------|
| **タスク名** | Weekly Mail Summary |
| **実行頻度** | 毎週月曜 09:00 |
| **実行者** | AI社員（Claude Code） |
| **実行時間** | 約20分 |
| **成果物** | 週間レポート |

---

### 実行手順

#### Step 1: 先週のメール統計を集計

**集計項目:**
- 受信総数
- 重要度別集計（URGENT / HIGH / MEDIUM / LOW）
- カテゴリ別集計（WORK / COLLAB / PLATFORM など）
- 返信数・対応数

**出力例:**
```
【先週のメール統計】（2026-07-11～07-17）

【受信総数】
- 総受信: 52件
- 重要度別:
  🔴 URGENT: 2件
  🟠 HIGH: 8件
  🟡 MEDIUM: 18件
  🟢 LOW: 20件
  ⚫ SPAM: 4件

【カテゴリ別】
- 📋 WORK: 6件
- 🤝 COLLAB: 2件
- 📱 PLATFORM: 15件
- ⚙️ SYSTEM: 8件
- 👥 FAN: 12件
- 📧 ADMIN: 5件
- ⚫ SPAM: 4件

【対応状況】
- ✅ 返信送信: 8件
- ⏳ 返信待機中: 3件
- 🗂️ アーカイブ済み: 25件
```

---

#### Step 2: 重要なメール・トレンドを分析

**分析項目:**
- 最も多く来たメール種別
- 返信に時間がかかったメール
- 対応漏れがあるメール
- 改善提案

**出力例:**
```
【先週のハイライト】

1. 仕事依頼が増加傾向
   → CM制作 / イベント企画の問い合わせが 6件
   → 来週は返信対応が集中か

2. YouTube からの通知が多い
   → チャンネル成長通知 5件
   → ポリシー関連警告 1件（対応済み）

3. 対応改善点
   → コラボ提案の返信が 2日遅延
   → テンプレート返信をあらかじめ用意することで改善可能
```

---

#### Step 3: 週間レポートを作成・報告

**レポートフォーマット:**
```
【公式Gmail 週間レポート】2026-07-11～07-17

【受信サマリー】
[上記の統計データ]

【重要なメール・トレンド】
[分析結果]

【来週の推奨アクション】
1. [改善提案1]
2. [改善提案2]
3. [改善提案3]

【添付】
- 詳細な分類リスト（CSV）
- ラベル別メール一覧
```

---

### Codex タスク定義

```yaml
Task:
  name: Weekly Mail Summary
  schedule: "0 9 * * MON"  # 毎週月曜 09:00
  
  steps:
    - step: 1
      name: "先週のメール統計を集計"
      action: "aggregate-weekly-stats"
      query: "past 7 days"
      
    - step: 2
      name: "重要なメール・トレンドを分析"
      action: "analyze-trends"
      
    - step: 3
      name: "週間レポート作成"
      action: "generate-weekly-report"
      output: "レポートドキュメント"
      
  owner: "Claude Code (AI社員)"
  approval_required: false
```

---

## Task 4: Monthly Label Audit（月間ラベル監査）

### タスク定義

| 項目 | 詳細 |
|------|------|
| **タスク名** | Monthly Label Audit |
| **実行頻度** | 毎月第1日曜 10:00 |
| **実行者** | AI社員（Claude Code） |
| **実行時間** | 約30分 |
| **成果物** | 監査レポート・改善提案 |

---

### 実行手順

#### Step 1: ラベル体系の確認

**確認項目:**
- [ ] Layer 1（優先度）: URGENT / HIGH / MEDIUM / LOW / SPAM が機能しているか
- [ ] Layer 2（カテゴリ）: WORK / COLLAB / PLATFORM / SYSTEM / FAN / ADMIN が機能しているか
- [ ] Layer 3（進捗）: INBOX / REVIEW / PENDING / DRAFT / DONE / ARCHIVE が正しく使い分けられているか

---

#### Step 2: ラベル利用統計を集計

**集計項目:**
- 各ラベルの使用頻度
- 使われていないラベル
- 曖昧な分類（複数ラベルで迷ったメール）

**出力例:**
```
【ラベル利用統計】（先月）

【優先度別】
- 🔴 URGENT: 5件 (8%)
- 🟠 HIGH: 12件 (20%)
- 🟡 MEDIUM: 25件 (42%)
- 🟢 LOW: 15件 (25%)
- ⚫ SPAM: 3件 (5%)

【カテゴリ別】
- 📋 WORK: 15件 (高頻度)
- 🤝 COLLAB: 3件 (低頻度)
- 📱 PLATFORM: 18件 (高頻度)
- ⚙️ SYSTEM: 12件 (中程度)
- 👥 FAN: 10件 (中程度)
- 📧 ADMIN: 4件 (低頻度)

【問題分類】
- 分類が曖昧だったメール: 2件
- ラベルなしで残されたメール: 1件
```

---

#### Step 3: 改善提案を作成

**提案内容:**
- 新しいラベルが必要か
- 不要なラベルがあるか
- カテゴリ分けの改善案

**出力例:**
```
【改善提案】

1. 新ラベル提案: 「📰 NEWS」
   理由: ニュースレター / PR情報が増加
        現在は LOW に分類されているが、
        フォローアップが不要な情報なので分離したい
   
2. カテゴリ改善: COLLAB の定義を拡大
   理由: パートナーシップ / 協業の提案が増加
        現在の COLLAB だけでは不足

3. 削除提案: 「📧 ADMIN」を統合
   理由: 使用頻度が低い（月4件）
        SYSTEM ラベルに統合可能
```

---

### Codex タスク定義

```yaml
Task:
  name: Monthly Label Audit
  schedule: "0 10 ? * SUN#1"  # 毎月第1日曜 10:00
  
  steps:
    - step: 1
      name: "ラベル体系の確認"
      action: "verify-label-system"
      
    - step: 2
      name: "ラベル利用統計を集計"
      action: "aggregate-label-stats"
      period: "past 30 days"
      
    - step: 3
      name: "改善提案を作成"
      action: "generate-improvement-suggestions"
      
  owner: "Claude Code (AI社員)"
  approval_required: true
  approval_by: "YU"
```

---

## Task 5: Daily Response Draft Preparation（毎日の返信下書き準備）

### タスク定義

| 項目 | 詳細 |
|------|------|
| **タスク名** | Daily Response Draft Preparation |
| **実行頻度** | 毎日 15:00 |
| **実行者** | AI社員（Claude Code） |
| **実行時間** | 約20分 |
| **成果物** | 返信下書きドキュメント |

---

### 実行手順

#### Step 1: 返信が必要なメールを抽出

**対象メール:**
- ラベル: 🟠 HIGH / 🟡 MEDIUM で「返信が必要」と判定されたメール
- ステータス: PENDING / DRAFT のメール

---

#### Step 2: 返信下書きを作成

**作成内容:**
- 件名（Re: [元の件名]）
- 敬語・ビジネストーンの本文
- 署名（FLY77STAR. STUDIO + Webサイト）

**使用テンプレート:**
上記の「MAIL_RESPONSE_APPROVAL_FLOW.md」のテンプレートを参照

---

#### Step 3: 下書きドキュメント作成

**出力フォーマット:**

```
【メール返信下書き】2026-07-17

【返信 #1】
件目: Re: CM制作依頼について
送信者: agency@example.jp
[下書き本文]

【返信 #2】
件目: Re: コラボ提案について
送信者: collab@creator.com
[下書き本文]

【返信 #3】
件目: Re: SE77NTH. についての質問
送信者: fan@example.com
[下書き本文]

【AI社員からのコメント】
- 計3件の返信下書きを準備しました
- すべて敬語・ビジネストーンで作成しています
- YU の修正・承認後、送信してください
```

---

### Codex タスク定義

```yaml
Task:
  name: Daily Response Draft Preparation
  schedule: "0 15 * * *"  # 毎日 15:00
  
  steps:
    - step: 1
      name: "返信が必要なメールを抽出"
      action: "extract-emails-needing-response"
      filter: "labels: HIGH or MEDIUM, status: needs-response"
      
    - step: 2
      name: "返信下書きを作成"
      action: "generate-response-drafts"
      templates: "MAIL_RESPONSE_TEMPLATES"
      
    - step: 3
      name: "下書きドキュメント作成"
      action: "create-draft-document"
      output: "返信下書きリスト"
      
  owner: "Claude Code (AI社員)"
  approval_required: false
```

---

## セキュリティ・コンプライアンス

### 全タスク共通の注意点

#### ✅ 実行してよい操作

- メール読み取り（読み取り専用）
- メール分類・ラベル提案
- 統計集計・レポート作成
- 下書き作成

#### ❌ 実行してはいけない操作

- メール削除（YU 承認後のみ）
- メール送信（YU が実行）
- ラベル自動付与（YU が承認後に手動実行）
- パスワード変更
- 転送設定の変更

---

## 実装タイムライン

| Phase | 時期 | 実装内容 | 担当 |
|-------|------|---------|------|
| Phase 1 | 2026-07-17 | Task 1: 毎日のメール確認（手動） | AI社員 |
| Phase 1 | 2026-07-17 | Task 2: 緊急メール通知（手動） | AI社員 |
| Phase 2 | 2026-07-24 | Task 3: 週間レポート自動化 | Codex |
| Phase 2 | 2026-08-01 | Task 4: 月間監査自動化 | Codex |
| Phase 3 | 2026-08-07 | Task 5: 返信下書き自動化 | Codex |
| Phase 4 | TBD | Gmail API / OAuth 統合 | Claude Code + Codex |

---

## 関連ドキュメント

- `OFFICIAL_GMAIL_OPERATIONS.md` - 全体運用マニュアル
- `AI_MAIL_REVIEW_RULES.md` - 分類・判定ルール
- `GMAIL_LABEL_POLICY.md` - ラベル運用ポリシー
- `MAIL_RESPONSE_APPROVAL_FLOW.md` - 返信承認フロー

---

**Document Status:** 自動化タスク定義完了・スケジューリング準備中  
**Maintained by:** Claude Code (CTO)  
**Version:** 1.0  
**Last Updated:** 2026-07-17
