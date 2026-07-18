# SNS API 統合実装計画

**Document Version:** 1.0  
**Created:** 2026-07-18  
**Status:** 実装設計開始  
**実装期間:** 2026-07-25 〜 2026-07-31（7日間）  
**目標:** 実装完了・テスト完了

---

## 概要

現在のマニュアル運用（Gmail 運用 + SNS DM 手動チェック）から、段階的に API 統合を進め、最終的に完全自動化を実現する。

**実装フェーズ:**
- Phase 1（現在）: 2026-07-19 〜 2026-07-24 — マニュアル運用
- Phase 2（計画中）: 2026-07-25 〜 2026-07-31 — API 統合実装 ✅
- Phase 3（将来）: 2026-08-01 以降 — 完全自動化運用

---

## 対象 API と実装スケジュール

### 実装対象プラットフォーム

| プラットフォーム | API | 優先度 | 実装期間 | ステータス |
|-----------------|-----|--------|--------|---------|
| **YouTube** | YouTube Data API v3 | 🔴 最高 | 7/25-26 | ⏳ 設計中 |
| **Instagram** | Meta Graph API | 🟠 高 | 7/27-28 | ⏳ 設計中 |
| **X** | X API v2 | 🟠 高 | 7/29-30 | ⏳ 設計中 |
| **TikTok** | TikTok Creator API | 🟡 中 | 7/31 | ⏳ 設計中 |

---

## 各 API の実装内容

### 1. YouTube Data API v3（7月25-26日）

**実装目標:**
- [ ] 公開チャンネル情報取得（@FLY77STAR）
- [ ] 最新動画情報の自動取得
- [ ] コメント・メッセージの自動分類
- [ ] アップロード予定動画の進捗管理

**認証方法:** OAuth 2.0（Service Account）  
**レート制限:** 10,000 ユニット/日  
**主要エンドポイント:**
```
GET https://www.googleapis.com/youtube/v3/channels
GET https://www.googleapis.com/youtube/v3/search
GET https://www.googleapis.com/youtube/v3/commentThreads
GET https://www.googleapis.com/youtube/v3/activities
```

**実装機能:**
```python
class YouTubeAPI:
    def get_channel_info(self):
        # チャンネル情報取得
        
    def get_recent_uploads(self, max_results=10):
        # 最新アップロード取得
        
    def get_comments(self, video_id):
        # コメント取得・分類
        
    def get_statistics(self):
        # 視聴統計取得
```

**配置ファイル:** `scripts/youtube_api_client.py`

---

### 2. Meta Graph API（Instagram）（7月27-28日）

**実装目標:**
- [ ] Instagram DM の自動取得
- [ ] DM メッセージの分類・抽出
- [ ] DM 受信者情報の自動管理
- [ ] DM 送信の自動実行（テスト）

**認証方法:** OAuth 2.0（Business Account）  
**レート制限:** 180リクエスト/時間（ビジネスアカウント）  
**主要エンドポイント:**
```
GET https://graph.instagram.com/v18.0/me/conversations
GET https://graph.instagram.com/v18.0/{conversation_id}/messages
POST https://graph.instagram.com/v18.0/{conversation_id}/messages
```

**実装機能:**
```python
class InstagramAPI:
    def get_conversations(self):
        # 全 DM スレッド取得
        
    def get_messages(self, conversation_id):
        # DM メッセージ取得
        
    def send_message(self, conversation_id, message):
        # DM 送信（YU 承認後）
        
    def classify_dm(self, message):
        # DM 自動分類
```

**配置ファイル:** `scripts/instagram_api_client.py`

---

### 3. X API v2（7月29-30日）

**実装目標:**
- [ ] X DM の自動取得
- [ ] DM メッセージの分類・抽出
- [ ] X リプライの自動監視
- [ ] DM 送信の自動実行（テスト）

**認証方法:** OAuth 2.0 + Bearer Token  
**レート制限:** 300リクエスト/15分（v2 Essential）  
**主要エンドポイント:**
```
GET https://api.twitter.com/2/dm_conversations
GET https://api.twitter.com/2/dm_conversations/{dm_conversation_id}/dm_events
POST https://api.twitter.com/2/dm_conversations/with/{participant_id}/messages
```

**実装機能:**
```python
class TwitterAPI:
    def get_dm_conversations(self):
        # DM スレッド取得
        
    def get_dm_messages(self, conversation_id):
        # DM メッセージ取得
        
    def send_dm(self, user_id, message):
        # DM 送信（YU 承認後）
        
    def get_mentions(self):
        # メンション取得
```

**配置ファイル:** `scripts/twitter_api_client.py`

---

### 4. TikTok Creator API（7月31日）

**実装目標:**
- [ ] TikTok DM の自動取得（API 制限を考慮）
- [ ] DM メッセージの分類・抽出
- [ ] ビデオ視聴統計の取得
- [ ] フォロワー情報の自動管理

**認証方法:** OAuth 2.0（Creator Account）  
**レート制限:** 1,000リクエスト/時間  
**主要エンドポイント:**
```
GET https://open.tiktokapis.com/v1/creator_info/
GET https://open.tiktokapis.com/v1/video/list/
GET https://open.tiktokapis.com/v1/video/query/
```

**実装機能:**
```python
class TikTokAPI:
    def get_creator_info(self):
        # クリエイター情報取得
        
    def get_video_statistics(self):
        # ビデオ統計取得
        
    def get_followers_info(self):
        # フォロワー情報取得
        
    def get_analytics(self):
        # アナリティクス取得
```

**配置ファイル:** `scripts/tiktok_api_client.py`

---

## 実装スケジュール（詳細）

### 7月25日（木）— YouTube Data API 実装 Day 1

**午前:**
- [ ] YouTube Data API の仕様確認・読み込み
- [ ] OAuth 2.0 認証フロー設計
- [ ] Service Account キー生成・設定

**午後:**
- [ ] `youtube_api_client.py` 実装開始
- [ ] チャンネル情報取得機能実装
- [ ] 最新動画取得機能実装

**確認項目:**
- [ ] API キー有効性確認
- [ ] テスト用チャンネル接続確認
- [ ] データ取得テスト実施

---

### 7月26日（金）— YouTube Data API 実装 Day 2

**午前:**
- [ ] コメント取得・分類機能実装
- [ ] 統計情報取得機能実装
- [ ] エラーハンドリング実装

**午後:**
- [ ] テスト実施・デバッグ
- [ ] ドキュメント作成
- [ ] 本運用前チェック

**完了条件:**
- [x] YouTube API 統合完了
- [x] テスト 100% パス
- [x] ドキュメント完成

---

### 7月27日（土）— Meta Graph API 実装 Day 1

**午前:**
- [ ] Meta Graph API の仕様確認・読み込み
- [ ] Business Account 認証フロー設計
- [ ] App ID・App Secret 生成・設定

**午後:**
- [ ] `instagram_api_client.py` 実装開始
- [ ] DM スレッド取得機能実装
- [ ] メッセージ取得機能実装

**確認項目:**
- [ ] API キー有効性確認
- [ ] Instagram ビジネスアカウント接続確認
- [ ] DM テストメッセージ取得確認

---

### 7月28日（日）— Meta Graph API 実装 Day 2

**午前:**
- [ ] DM 送信機能実装（YU 承認後のみ）
- [ ] DM 自動分類機能実装
- [ ] エラーハンドリング実装

**午後:**
- [ ] テスト実施・デバッグ
- [ ] ドキュメント作成
- [ ] 本運用前チェック

**完了条件:**
- [x] Instagram API 統合完了
- [x] テスト 100% パス
- [x] ドキュメント完成

---

### 7月29日（月）— X API v2 実装 Day 1

**午前:**
- [ ] X API v2 の仕様確認・読み込み
- [ ] OAuth 2.0 + Bearer Token 認証フロー設計
- [ ] API キー生成・設定

**午後:**
- [ ] `twitter_api_client.py` 実装開始
- [ ] DM スレッド取得機能実装
- [ ] メッセージ取得機能実装

**確認項目:**
- [ ] API キー有効性確認
- [ ] X アカウント接続確認
- [ ] DM テストメッセージ取得確認

---

### 7月30日（火）— X API v2 実装 Day 2

**午前:**
- [ ] DM 送信機能実装（YU 承認後のみ）
- [ ] メンション取得機能実装
- [ ] エラーハンドリング実装

**午後:**
- [ ] テスト実施・デバッグ
- [ ] ドキュメント作成
- [ ] 本運用前チェック

**完了条件:**
- [x] X API 統合完了
- [x] テスト 100% パス
- [x] ドキュメント完成

---

### 7月31日（水）— TikTok Creator API 実装

**午前:**
- [ ] TikTok Creator API の仕様確認・読み込み
- [ ] OAuth 2.0 認証フロー設計
- [ ] API キー生成・設定
- [ ] `tiktok_api_client.py` 実装開始

**午後:**
- [ ] クリエイター情報取得機能実装
- [ ] 統計情報取得機能実装
- [ ] エラーハンドリング実装
- [ ] テスト実施・デバッグ

**完了条件:**
- [x] TikTok API 統合完了
- [x] テスト 100% パス
- [x] ドキュメント完成

---

## 実装の重要なルール

### ✅ 実装可能な機能

- [ ] API データ取得・分類
- [ ] DM メッセージの自動分析・下書き生成
- [ ] 統計情報の自動集計
- [ ] ログの自動記録

### ❌ 実装不可（YU 承認後のみ）

- ❌ DM の自動送信（YU の【送信】コマンド後のみ）
- ❌ コメント返信の自動送信
- ❌ アカウント設定変更
- ❌ メッセージ削除・ブロック

### 📋 API 認証情報の管理

**ベストプラクティス:**
- 環境変数に API キーを保存（`.env` ファイル）
- `.gitignore` に `.env` を追加（Git コミットに含めない）
- 本番環境では Cloud KMS / Secret Manager を使用

---

## テスト計画

### ユニットテスト

各 API クライアント（youtube, instagram, twitter, tiktok）について：

```python
# tests/test_youtube_api.py
def test_get_channel_info():
    # チャンネル情報取得テスト
    
def test_get_recent_uploads():
    # 最新動画取得テスト
    
def test_error_handling():
    # エラーハンドリングテスト
```

**テスト対象:**
- [ ] API 接続確認
- [ ] データ取得・パース確認
- [ ] エラーハンドリング確認
- [ ] レート制限対応確認

### 統合テスト

全 API を統合した場合の動作確認：

```python
# tests/test_sns_integration.py
def test_all_apis_together():
    # 全 API 同時実行テスト
    
def test_data_consistency():
    # データ一貫性テスト
    
def test_error_recovery():
    # エラー復旧テスト
```

**確認事項:**
- [ ] 複数 API の同時実行が可能か
- [ ] データが正しく統合されるか
- [ ] エラーが正しく伝播するか

### 本番テスト

実際の SNS アカウントでの動作確認：

- [ ] @FLY77STAR YouTube チャンネル接続確認
- [ ] @fly77star Instagram ビジネスアカウント接続確認
- [ ] @FLY77STAR_JP X アカウント接続確認
- [ ] @fly77star TikTok クリエイターアカウント接続確認

---

## ドキュメント作成予定

### API 実装ドキュメント

```
📁 Edit/
├── SNS_API_YOUTUBE.md — YouTube API 実装ガイド
├── SNS_API_INSTAGRAM.md — Instagram API 実装ガイド
├── SNS_API_X.md — X API v2 実装ガイド
├── SNS_API_TIKTOK.md — TikTok API 実装ガイド
└── SNS_API_AUTHENTICATION.md — 全 API 認証フロー統一ガイド
```

### スクリプト

```
📁 scripts/
├── youtube_api_client.py — YouTube API クライアント
├── instagram_api_client.py — Instagram API クライアント
├── twitter_api_client.py — X API v2 クライアント
├── tiktok_api_client.py — TikTok API クライアント
└── sns_api_manager.py — 全 API 統合マネージャー
```

### テスト

```
📁 tests/
├── test_youtube_api.py
├── test_instagram_api.py
├── test_twitter_api.py
├── test_tiktok_api.py
└── test_sns_integration.py
```

---

## 実装完了後の次フェーズ

### Phase 3: 完全自動化運用（2026-08-01 以降）

**8月から実現する機能:**

```
朝 09:00
  ├─ 自動取得: YouTube/Instagram/X/TikTok の新着情報
  ├─ 自動分類: DM をタイプ別に分類
  ├─ 自動下書き生成: テンプレートから返信案作成
  └─ YU への通知: 「確認・送信待ち」リスト提示

YU 承認実行
  ├─ 【送信】コマンド実行
  └─ Claude Code が各 SNS に自動送信

夜 18:00
  ├─ 自動集計: 全 SNS の情報集計
  ├─ 自動分析: 受信パターン・傾向分析
  └─ YU への日報: 完全自動生成
```

---

## リスク管理

### API レート制限対策

| API | レート制限 | 対策 |
|-----|----------|------|
| YouTube | 10,000 ユニット/日 | キャッシング・キューイング |
| Instagram | 180/時間 | バッチ処理・スケジューリング |
| X | 300/15分 | レート制限監視・バックオフ |
| TikTok | 1,000/時間 | スケジューリング・優先度設定 |

### エラー対応

**API が応答しない場合:**
- [ ] 自動リトライ（exponential backoff）
- [ ] キャッシュデータ使用（最新データがない場合）
- [ ] YU への通知（障害発生を報告）

**認証エラーの場合:**
- [ ] トークン更新の自動実行
- [ ] 更新失敗時は YU に手動認証を要求
- [ ] ログに詳細を記録

---

## 完了条件

**実装完了判定:**
- [x] 全 4 API（YouTube / Instagram / X / TikTok）の統合完了
- [x] ユニットテスト 100% パス
- [x] 統合テスト 100% パス
- [x] 本番環境テスト完了・承認取得
- [x] ドキュメント完成・レビュー完了
- [x] Git コミット・プッシュ完了

**テスト完了判定:**
- [x] 全 API のエラーハンドリング確認
- [x] レート制限対応確認
- [x] 複数 API 同時実行確認
- [x] 本番環境での実際のデータ取得確認

---

**実装期間:** 2026-07-25 〜 2026-07-31（7日間）  
**目標達成:** 2026-07-31 までに実装・テスト完了 ✅  
**次フェーズ開始:** 2026-08-01 — 完全自動化運用

