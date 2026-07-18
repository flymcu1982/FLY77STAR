# FLY77STAR. Unified Inbox — アーキテクチャ設計書

**バージョン:** 1.0  
**作成日:** 2026-07-18  
**責任者:** Claude Code (CTO)

---

## 📐 システムアーキテクチャ

```
┌─────────────────────────────────────────────────────────────┐
│                   FLY77STAR Unified Inbox                    │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  ┌──────────────────────────────────────────────────────┐   │
│  │         Frontend Layer (React / Vue.js)              │   │
│  │  ┌─────────────┬──────────────┬──────────────┐       │   │
│  │  │ Unified     │ Message      │ Analytics    │       │   │
│  │  │ Inbox View  │ Detail View  │ Dashboard    │       │   │
│  │  └─────────────┴──────────────┴──────────────┘       │   │
│  └──────────────────────────────────────────────────────┘   │
│                          ↓ REST API / WebSocket             │
│  ┌──────────────────────────────────────────────────────┐   │
│  │         API Gateway Layer (Flask / FastAPI)          │   │
│  │  ┌──────────┬──────────┬──────────┬────────────┐     │   │
│  │  │ Auth     │ Messages │ Actions  │ Analytics  │     │   │
│  │  │ API      │ API      │ API      │ API        │     │   │
│  │  └──────────┴──────────┴──────────┴────────────┘     │   │
│  └──────────────────────────────────────────────────────┘   │
│                          ↓                                    │
│  ┌──────────────────────────────────────────────────────┐   │
│  │       Business Logic Layer (Python)                  │   │
│  │  ┌───────────┬────────────┬───────────┬────────────┐ │   │
│  │  │ Message   │ Priority   │ Template  │ Analytics  │ │   │
│  │  │ Processor │ Classifier │ Engine    │ Engine     │ │   │
│  │  └───────────┴────────────┴───────────┴────────────┘ │   │
│  └──────────────────────────────────────────────────────┘   │
│                          ↓                                    │
│  ┌──────────────────────────────────────────────────────┐   │
│  │        Data Access Layer (ORM)                       │   │
│  │  ┌──────────────────────────────────────────────┐   │   │
│  │  │  SQLite / PostgreSQL Database                │   │   │
│  │  │  ├─ messages (メール・DM 統一テーブル)      │   │   │
│  │  │  ├─ users (送信者情報)                       │   │   │
│  │  │  ├─ accounts (Gmail・SNS アカウント)        │   │   │
│  │  │  ├─ templates (返信テンプレート)            │   │   │
│  │  │  ├─ actions (ユーザー操作ログ)              │   │   │
│  │  │  └─ analytics (統計・ログ)                  │   │   │
│  │  └──────────────────────────────────────────────┘   │   │
│  └──────────────────────────────────────────────────────┘   │
│                          ↓                                    │
│  ┌──────────────────────────────────────────────────────┐   │
│  │      External APIs (非同期・並列実行)                │   │
│  │  ┌────────┬────────┬────────┬────────┐              │   │
│  │  │ Gmail  │ TikTok │Instagram│ X/API │              │   │
│  │  │ API    │ API    │ API     │ v2    │              │   │
│  │  └────────┴────────┴────────┴────────┘              │   │
│  └──────────────────────────────────────────────────────┘   │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

---

## 🗄️ データベーススキーマ

### messages テーブル（統一メール・DM テーブル）

```sql
CREATE TABLE messages (
  id INTEGER PRIMARY KEY,
  message_id VARCHAR(255) UNIQUE NOT NULL,
  platform VARCHAR(50),           -- 'gmail', 'tiktok', 'instagram', 'x'
  sender_id VARCHAR(255),         -- 送信者 ID / Email
  sender_name VARCHAR(255),       -- 送信者名
  subject VARCHAR(500),           -- メール件名 / DM トピック
  body TEXT,                      -- 本文
  attachment_urls JSON,           -- 添付ファイル URL
  received_at DATETIME,           -- 受信日時
  read BOOLEAN DEFAULT FALSE,     -- 既読フラグ
  priority VARCHAR(10),           -- URGENT, HIGH, MEDIUM, LOW
  classification VARCHAR(50),     -- WORK, COLLAB, FAN, PLATFORM, SYSTEM, SPAM
  status VARCHAR(20),             -- INBOX, REVIEW, PENDING, DRAFT, DONE, ARCHIVE
  draft_response TEXT,            -- 返信下書き
  draft_template_id VARCHAR(50),  -- 使用テンプレート ID
  sent_response TEXT,             -- 実際の返信内容
  sent_at DATETIME,               -- 送信日時
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (sender_id) REFERENCES users(user_id)
);

-- インデックス
CREATE INDEX idx_platform ON messages(platform);
CREATE INDEX idx_priority ON messages(priority);
CREATE INDEX idx_status ON messages(status);
CREATE INDEX idx_received_at ON messages(received_at DESC);
CREATE INDEX idx_read ON messages(read);
```

### users テーブル（送信者情報）

```sql
CREATE TABLE users (
  user_id VARCHAR(255) PRIMARY KEY,
  platform VARCHAR(50),
  username VARCHAR(255),
  display_name VARCHAR(255),
  avatar_url VARCHAR(500),
  email VARCHAR(255),
  interaction_count INTEGER DEFAULT 0,
  last_interaction_at DATETIME,
  is_important BOOLEAN DEFAULT FALSE,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

### templates テーブル（返信テンプレート）

```sql
CREATE TABLE templates (
  template_id VARCHAR(50) PRIMARY KEY,
  name VARCHAR(100),              -- テンプレート名
  category VARCHAR(50),           -- 制作依頼, コラボ, ファン, ビジネス, URGENT, 対応不可
  default_body TEXT,              -- デフォルト本文
  variables JSON,                 -- テンプレート変数（{{name}} など）
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

### actions テーブル（ユーザー操作ログ）

```sql
CREATE TABLE actions (
  action_id INTEGER PRIMARY KEY,
  message_id VARCHAR(255),
  action_type VARCHAR(50),        -- 'send', 'modify', 'confirm', 'delete'
  action_detail TEXT,
  acted_by VARCHAR(50),           -- YU
  acted_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (message_id) REFERENCES messages(message_id)
);
```

### analytics テーブル（日報・統計）

```sql
CREATE TABLE analytics (
  report_id INTEGER PRIMARY KEY,
  report_date DATE,
  platform VARCHAR(50),
  total_received INTEGER,
  urgent_count INTEGER,
  high_count INTEGER,
  medium_count INTEGER,
  low_count INTEGER,
  sent_count INTEGER,
  avg_response_time FLOAT,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

---

## 🔄 データフロー

### 1. メール・DM 受信フロー

```
External API（Gmail/SNS）
    ↓ (非同期 API 呼び出し)
Message Ingestion Service
    ↓ (メッセージ正規化)
Unified Message Processor
    ↓ (優先度判定・分類)
Priority Classifier + Categorizer
    ↓ (DB 保存)
SQLite / PostgreSQL
    ↓ (リアルタイム通知)
Frontend (WebSocket)
    ↓
YU の画面に即座に表示
```

### 2. 返信フロー

```
YU が下書きを確認
    ↓
【送信】コマンド実行
    ↓
Template Engine が最終下書きを準備
    ↓
API Client が該当プラットフォームに送信
    ↓
Action Log に記録
    ↓
messages テーブル status = DONE
    ↓
YU に完了通知
```

### 3. 分析・日報生成フロー

```
毎日 18:00 トリガー
    ↓
Analytics Engine
    ├─ 本日の統計集計
    ├─ 重要度別カウント
    ├─ プラットフォーム別カウント
    └─ レスポンス時間計算
    ↓
Report Generator
    ↓
日報（Markdown）生成
    ↓
YU に提示
```

---

## 🔌 API 統合アーキテクチャ

### API Manager（統一インターフェース）

```python
class UnifiedInboxAPIManager:
    def __init__(self, config):
        self.gmail_client = GmailAPIClient(config["gmail_key"])
        self.tiktok_client = TikTokAPIClient(config["tiktok_token"])
        self.instagram_client = InstagramAPIClient(config["instagram_token"])
        self.x_client = XAPIClient(config["x_bearer_token"])
    
    async def fetch_all_messages(self):
        """全プラットフォームからメッセージを並列取得"""
        results = await asyncio.gather(
            self.gmail_client.get_messages(),
            self.tiktok_client.get_dm_messages(),
            self.instagram_client.get_conversations(),
            self.x_client.get_dm_conversations()
        )
        return self._normalize_messages(results)
    
    def _normalize_messages(self, platform_messages):
        """プラットフォーム間の差異を正規化"""
        # gmail → { id, sender, subject, body, received_at }
        # tiktok → { video_id, from, text, timestamp }
        # instagram → { id, from, text, timestamp }
        # x → { id, sender, text, timestamp }
        # ↓
        # 統一フォーマット: Message(id, platform, sender_id, body, ...)
        pass
```

---

## 🎨 UI/UX アーキテクチャ

### 画面構成

```
┌─────────────────────────────────────────────────────────┐
│  FLY77STAR Unified Inbox                       [Menu]   │
├─────────────────────────────────────────────────────────┤
│                                                           │
│  Filter & Search                                         │
│  ├─ Platform: [Gmail] [TikTok] [Instagram] [X]          │
│  ├─ Priority: [URGENT] [HIGH] [MEDIUM] [LOW]           │
│  ├─ Status: [INBOX] [REVIEW] [DRAFT] [DONE]            │
│  ├─ Search: [____________________]                      │
│                                                           │
├─────────────────────────────────────────────────────────┤
│                                                           │
│  Message List                                            │
│  ┌─────────────────────────────────────────────────┐    │
│  │ 🔴 2026-07-18 09:15 | 山田太郎 (Gmail)         │    │
│  │ Re: Distance 制作依頼について                    │    │
│  │ プレビュー: 「Distance の MV 制作を...」        │    │
│  │ [View Details] [Edit Draft] [Send] [Skip]     │    │
│  ├─────────────────────────────────────────────────┤    │
│  │ 🟠 2026-07-18 08:45 | @creator_account (TikTok) │    │
│  │ コラボについて相談                               │    │
│  │ プレビュー: 「コラボ企画はいかがですか...」    │    │
│  │ [View Details] [Edit Draft] [Send] [Skip]     │    │
│  ├─────────────────────────────────────────────────┤    │
│  │ 🟡 2026-07-18 07:30 | fan@example.com (Gmail)   │    │
│  │ Distance 素晴らしい！                            │    │
│  │ プレビュー: 「このビデオ本当に感動しました...」│    │
│  │ [View Details] [Template] [Send] [Skip]       │    │
│  └─────────────────────────────────────────────────┘    │
│                                                           │
│  [Load More]                                             │
│                                                           │
└─────────────────────────────────────────────────────────┘
```

### メッセージ詳細画面

```
┌──────────────────────────────────────────────────┐
│ Message Details                          [Back]  │
├──────────────────────────────────────────────────┤
│                                                   │
│ From: 山田太郎 (yamada@example.com)             │
│ Platform: Gmail                                  │
│ Received: 2026-07-18 09:15                      │
│ Priority: 🔴 URGENT                             │
│ Category: WORK (制作依頼)                        │
│                                                   │
│ Subject: Distance 制作依頼について                │
│ ────────────────────────────────────────────    │
│ 本文：                                           │
│ お疲れ様です。                                   │
│ 「Distance」の MV 制作をお願いしたいのですが... │
│                                                   │
│ ────────────────────────────────────────────    │
│ 返信下書き:                                      │
│ [Template: 制作依頼 - 詳細確認]                 │
│ ┌──────────────────────────────────────────┐   │
│ │ お疲れ様です。                             │   │
│ │ ご相談ありがとうございます。                │   │
│ │ 以下の内容でご確認させていただきたいです:  │   │
│ │ ・スケジュール                             │   │
│ │ ・ご予算帯                                 │   │
│ │ ・その他仕様                               │   │
│ │ よろしくお願いいたします。                │   │
│ └──────────────────────────────────────────┘   │
│                                                   │
│ [Edit] [Template List] [Clear]                  │
│                                                   │
│ [【修正】修正内容] [【送信】発送] [【確認中】保留] │
│                                                   │
└──────────────────────────────────────────────────┘
```

---

## 🔐 セキュリティアーキテクチャ

### 認証フロー

```
YU がログイン
    ↓
OAuth 2.0 (Gmail)
    ↓
Session Token 発行
    ↓
API リクエスト (Authorization: Bearer <token>)
    ↓
Token Validation
    ↓
API Response
```

### API キー管理

```
.env ファイル（Git 除外）
├─ GMAIL_API_KEY=...
├─ TIKTOK_ACCESS_TOKEN=...
├─ INSTAGRAM_BUSINESS_TOKEN=...
└─ X_BEARER_TOKEN=...

環境変数読み込み
    ↓
config.py で管理
    ↓
API Client に渡す
```

---

## 📈 スケーラビリティ対策

### 受信メッセージ数の増加対策

| 件数 | 対策 |
|------|------|
| 0-50 件/日 | SQLite + メモリキャッシュ |
| 50-500 件/日 | PostgreSQL + Redis キャッシュ |
| 500+ 件/日 | 分散DB + 非同期ワーカー |

### パフォーマンス最適化

- **DB インデックス**: platform, priority, status, received_at
- **ページング**: リスト表示時は 20 件/page
- **キャッシング**: Redis で最新 100 件を保持
- **非同期処理**: API 取得は asyncio で並列実行

---

## 🚀 デプロイメントアーキテクチャ

### 開発環境

```
Local Development
├─ Python 3.10+
├─ SQLite
├─ React Dev Server
└─ Flask/FastAPI Dev Server
```

### 本番環境

```
Netlify / Vercel
├─ Frontend (React/Vue.js)
├─ Static Assets
└─ CDN

自社サーバー / AWS / Heroku
├─ Backend API (Flask/FastAPI)
├─ PostgreSQL Database
└─ Redis Cache
```

### CI/CD パイプライン

```
GitHub Push
    ↓
GitHub Actions
    ├─ Lint / Format チェック
    ├─ ユニットテスト実行
    ├─ 統合テスト実行
    └─ Build
    ↓
本番環境へ自動デプロイ（Tag 時）
```

---

## 📅 フェーズ別実装項目

| フェーズ | 期間 | 重点 |
|---------|------|------|
| Phase 1（設計） | 7/25-31 | アーキテクチャ確定・技術検証 |
| Phase 2（実装） | 8/1-20 | 全機能実装・統合テスト |
| Phase 3（デプロイ） | 8/21- | 本番環境・運用開始 |

---

**ステータス:** 🔴 待機中（設計詳細確定待ち）
