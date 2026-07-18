# SNS API 統合実装 — 技術仕様書

**Document Version:** 1.0  
**Created:** 2026-07-18  
**Status:** 技術仕様確定・実装開始準備  
**実装言語:** Python 3.10+  
**フレームワーク:** Requests + asyncio（非同期対応）

---

## 全体構成

```
📁 scripts/
├── sns_api_manager.py           — 統合マネージャー（メインファイル）
├── youtube_api_client.py        — YouTube Data API クライアント
├── instagram_api_client.py      — Meta Graph API クライアント
├── twitter_api_client.py        — X API v2 クライアント
├── tiktok_api_client.py         — TikTok Creator API クライアント
├── sns_api_config.py            — 設定管理（API キーなど）
└── sns_api_utils.py             — ユーティリティ関数

📁 tests/
├── test_youtube_api.py
├── test_instagram_api.py
├── test_twitter_api.py
├── test_tiktok_api.py
└── test_sns_integration.py

📁 .env (Git 除外)
├── YOUTUBE_API_KEY=...
├── INSTAGRAM_BUSINESS_TOKEN=...
├── X_BEARER_TOKEN=...
└── TIKTOK_ACCESS_TOKEN=...
```

---

## 実装仕様

### 1. YouTube Data API クライアント

**ファイル:** `scripts/youtube_api_client.py`

```python
class YouTubeAPIClient:
    """YouTube Data API v3 クライアント"""
    
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://www.googleapis.com/youtube/v3"
        self.session = requests.Session()
        
    def get_channel_info(self, channel_id: str = None) -> dict:
        """
        チャンネル情報取得
        
        Args:
            channel_id: チャンネル ID（デフォルト: 認証ユーザーのチャンネル）
            
        Returns:
            {
                "id": "channel_id",
                "title": "FLY77STAR",
                "description": "...",
                "subscribers": 1234,
                "views": 567890,
                "uploads_playlist_id": "PLxxxx"
            }
        """
        params = {
            "part": "snippet,statistics,contentDetails",
            "mine": True,
            "key": self.api_key
        }
        response = self.session.get(f"{self.base_url}/channels", params=params)
        return response.json()
        
    def get_recent_uploads(self, max_results: int = 10) -> list:
        """
        最新動画一覧取得
        
        Returns:
            [
                {
                    "video_id": "xxxxx",
                    "title": "Distance SHORT VER.",
                    "upload_time": "2026-07-18T09:00:00Z",
                    "thumbnail": "https://...",
                    "views": 1234,
                    "likes": 567,
                    "comments": 89
                },
                ...
            ]
        """
        # 実装例
        pass
        
    def get_comments(self, video_id: str) -> list:
        """
        動画のコメント取得・分類
        
        Returns:
            [
                {
                    "author": "user123",
                    "comment": "素晴らしい作品ですね！",
                    "time": "2026-07-18T10:00:00Z",
                    "type": "FAN",  # INQUIRY, COLLAB, FAN, BUSINESS
                    "priority": "LOW"  # URGENT, HIGH, MEDIUM, LOW
                },
                ...
            ]
        """
        pass
        
    def get_statistics(self) -> dict:
        """視聴統計・分析データ取得"""
        pass
```

---

### 2. Instagram (Meta Graph) API クライアント

**ファイル:** `scripts/instagram_api_client.py`

```python
class InstagramAPIClient:
    """Meta Graph API for Instagram クライアント"""
    
    def __init__(self, access_token: str, business_account_id: str):
        self.access_token = access_token
        self.business_account_id = business_account_id
        self.base_url = "https://graph.instagram.com/v18.0"
        self.session = requests.Session()
        
    def get_conversations(self) -> list:
        """
        DM スレッド一覧取得
        
        Returns:
            [
                {
                    "id": "t.1234567890",
                    "participants": ["user1", "user2"],
                    "last_message": "こんにちは",
                    "last_message_time": "2026-07-18T09:00:00Z",
                    "unread_count": 2
                },
                ...
            ]
        """
        pass
        
    def get_messages(self, conversation_id: str) -> list:
        """
        会話のメッセージ取得
        
        Returns:
            [
                {
                    "id": "msg123",
                    "from": "user123",
                    "text": "MV 制作をお願いしたいです",
                    "timestamp": "2026-07-18T09:00:00Z",
                    "type": "INQUIRY",  # INQUIRY, COLLAB, FAN, BUSINESS
                    "priority": "HIGH"
                },
                ...
            ]
        """
        pass
        
    def send_message(self, conversation_id: str, message: str) -> dict:
        """
        DM 送信（YU の【送信】承認後のみ）
        
        Args:
            conversation_id: スレッド ID
            message: メッセージテキスト
            
        Returns:
            {
                "message_id": "msg456",
                "status": "sent",
                "timestamp": "2026-07-18T10:00:00Z"
            }
        """
        pass
        
    def classify_message(self, message: str) -> dict:
        """
        メッセージを自動分類
        
        Returns:
            {
                "type": "INQUIRY",  # INQUIRY, COLLAB, FAN, BUSINESS, SPAM
                "priority": "HIGH",  # URGENT, HIGH, MEDIUM, LOW
                "confidence": 0.95,  # 信頼度
                "suggested_template": 1  # テンプレート番号（1-6）
            }
        """
        pass
```

---

### 3. X API v2 クライアント

**ファイル:** `scripts/twitter_api_client.py`

```python
class XAPIClient:
    """X API v2 クライアント"""
    
    def __init__(self, bearer_token: str):
        self.bearer_token = bearer_token
        self.base_url = "https://api.twitter.com/2"
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {bearer_token}"
        })
        
    def get_dm_conversations(self) -> list:
        """
        DM スレッド一覧取得
        
        Returns:
            [
                {
                    "id": "12345",
                    "participant": "@username",
                    "last_message": "お疲れ様です",
                    "last_message_time": "2026-07-18T09:00:00Z",
                    "unread": True
                },
                ...
            ]
        """
        pass
        
    def get_dm_messages(self, conversation_id: str) -> list:
        """
        会話のメッセージ取得
        
        Returns:
            [
                {
                    "id": "msg_id",
                    "sender": "@user123",
                    "text": "コラボレーションについてお話ししたいのですが",
                    "timestamp": "2026-07-18T09:00:00Z",
                    "type": "COLLAB",
                    "priority": "HIGH"
                },
                ...
            ]
        """
        pass
        
    def send_dm(self, participant_id: str, message: str) -> dict:
        """
        DM 送信（YU の【送信】承認後のみ）
        
        Args:
            participant_id: 相手ユーザーの ID
            message: メッセージテキスト
            
        Returns:
            {
                "message_id": "msg_id",
                "status": "sent",
                "timestamp": "2026-07-18T10:00:00Z"
            }
        """
        pass
        
    def get_mentions(self) -> list:
        """
        メンション一覧取得
        
        Returns:
            [
                {
                    "id": "tweet_id",
                    "author": "@user123",
                    "text": "@FLY77STAR_JP 素晴らしいですね！",
                    "timestamp": "2026-07-18T09:00:00Z",
                    "type": "FAN"
                },
                ...
            ]
        """
        pass
```

---

### 4. TikTok Creator API クライアント

**ファイル:** `scripts/tiktok_api_client.py`

```python
class TikTokAPIClient:
    """TikTok Creator API クライアント"""
    
    def __init__(self, access_token: str):
        self.access_token = access_token
        self.base_url = "https://open.tiktokapis.com/v1"
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {access_token}"
        })
        
    def get_creator_info(self) -> dict:
        """
        クリエイター情報取得
        
        Returns:
            {
                "username": "fly77star",
                "display_name": "FLY77STAR.",
                "followers": 12345,
                "following": 67,
                "video_count": 45,
                "bio": "デジタルクリエイター・音楽・映像・物語"
            }
        """
        pass
        
    def get_video_statistics(self, max_results: int = 10) -> list:
        """
        ビデオ視聴統計取得
        
        Returns:
            [
                {
                    "video_id": "video_id",
                    "title": "Distance SHORT VER.",
                    "views": 123456,
                    "likes": 12345,
                    "shares": 789,
                    "comments": 234,
                    "upload_time": "2026-07-18T09:00:00Z"
                },
                ...
            ]
        """
        pass
        
    def get_followers_info(self) -> dict:
        """
        フォロワー情報取得
        
        Returns:
            {
                "total_followers": 50000,
                "new_followers_today": 123,
                "engagement_rate": 0.045,  # 4.5%
                "top_geographies": ["JP", "US", "KR"]
            }
        """
        pass
        
    def get_analytics(self) -> dict:
        """
        アナリティクス情報取得
        
        Returns:
            {
                "total_views": 1234567,
                "total_likes": 123456,
                "profile_views": 12345,
                "follower_growth": 1234
            }
        """
        pass
```

---

## 統合マネージャー

**ファイル:** `scripts/sns_api_manager.py`

```python
class SNSAPIManager:
    """全 SNS API を統合管理するマネージャー"""
    
    def __init__(self, config: dict):
        self.youtube = YouTubeAPIClient(config["youtube_api_key"])
        self.instagram = InstagramAPIClient(
            config["instagram_token"],
            config["instagram_business_id"]
        )
        self.twitter = XAPIClient(config["x_bearer_token"])
        self.tiktok = TikTokAPIClient(config["tiktok_access_token"])
        
    async def fetch_all_dms(self) -> dict:
        """
        全 SNS の新着 DM を同時に取得（非同期）
        
        Returns:
            {
                "youtube": [...],
                "instagram": [...],
                "x": [...],
                "tiktok": [...]
            }
        """
        # asyncio で並列実行
        pass
        
    async def classify_all_messages(self, messages: dict) -> dict:
        """
        全 SNS のメッセージを自動分類
        
        Returns:
            {
                "youtube": [...],
                "instagram": [...],
                "x": [...],
                "tiktok": [...]
            }
        """
        pass
        
    async def generate_draft_responses(self, messages: dict) -> dict:
        """
        各メッセージに対する返信下書きを自動生成
        
        Returns:
            {
                "SNS-DM-001": {...},
                "SNS-DM-002": {...},
                ...
            }
        """
        pass
        
    async def send_approved_messages(self, approved_ids: list) -> dict:
        """
        YU が【送信】承認したメッセージを実際に送信
        
        Args:
            approved_ids: 【送信】されたメッセージ ID のリスト
            
        Returns:
            送信結果ログ
        """
        pass
```

---

## エラーハンドリング戦略

### リトライロジック

```python
def retry_with_backoff(max_retries: int = 3):
    """指数バックオフによる自動リトライ"""
    
    for attempt in range(max_retries):
        try:
            response = api_call()
            return response
        except requests.exceptions.Timeout:
            wait_time = 2 ** attempt  # 1s, 2s, 4s
            time.sleep(wait_time)
        except requests.exceptions.ConnectionError:
            wait_time = 2 ** attempt
            time.sleep(wait_time)
        except Exception as e:
            # 重大なエラー → 即座に YU に通知
            notify_user(f"API エラー: {e}")
            raise
```

### ロギング

```python
import logging

logger = logging.getLogger("SNS_API")
logger.setLevel(logging.INFO)

# ファイルハンドラ
file_handler = logging.FileHandler("logs/sns_api.log")
file_handler.setLevel(logging.INFO)

# コンソールハンドラ
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.WARNING)

logger.addHandler(file_handler)
logger.addHandler(console_handler)

# 使用例
logger.info("YouTube チャンネル情報取得成功")
logger.warning("Instagram API レート制限に達した")
logger.error("X API 認証失敗")
```

---

## テスト戦略

### ユニットテスト例

```python
# tests/test_youtube_api.py
import unittest
from scripts.youtube_api_client import YouTubeAPIClient

class TestYouTubeAPI(unittest.TestCase):
    
    def setUp(self):
        self.client = YouTubeAPIClient(api_key="test_key")
        
    def test_get_channel_info(self):
        """チャンネル情報取得テスト"""
        result = self.client.get_channel_info()
        self.assertIn("id", result)
        self.assertIn("title", result)
        
    def test_error_handling(self):
        """エラーハンドリングテスト"""
        with self.assertRaises(Exception):
            self.client.get_channel_info(channel_id="invalid_id")
```

### 統合テスト例

```python
# tests/test_sns_integration.py
class TestSNSIntegration(unittest.TestCase):
    
    def test_all_apis_simultaneously(self):
        """全 API の同時実行テスト"""
        manager = SNSAPIManager(config)
        
        # 4 つの API を非同期で実行
        results = asyncio.run(manager.fetch_all_dms())
        
        # 全 API の結果が正しく取得されているか確認
        self.assertIn("youtube", results)
        self.assertIn("instagram", results)
        self.assertIn("x", results)
        self.assertIn("tiktok", results)
```

---

## セキュリティガイドライン

### API キー管理

**❌ してはいけないこと:**
```python
# 絶対にハードコードしない！
API_KEY = "sk-xxx-yyy-zzz"
```

**✅ 正しい方法:**
```python
# .env ファイルから読み込む
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("YOUTUBE_API_KEY")
```

### .gitignore に追加

```
# .gitignore
.env
.env.local
*.key
*.pem
logs/
```

---

## 実装チェックリスト

**Week 1（7月25-26）:**
- [ ] YouTube API クライアント実装完了
- [ ] YouTube ユニットテスト 100% パス
- [ ] YouTube 本番テスト完了

**Week 2（7月27-28）:**
- [ ] Instagram API クライアント実装完了
- [ ] Instagram ユニットテスト 100% パス
- [ ] Instagram 本番テスト完了

**Week 3（7月29-30）:**
- [ ] X API クライアント実装完了
- [ ] X ユニットテスト 100% パス
- [ ] X 本番テスト完了

**Week 4（7月31）:**
- [ ] TikTok API クライアント実装完了
- [ ] TikTok ユニットテスト 100% パス
- [ ] TikTok 本番テスト完了
- [ ] 統合マネージャー実装完了
- [ ] 全ドキュメント完成

---

**技術仕様確定日:** 2026-07-18  
**実装開始日:** 2026-07-25  
**実装完了目標日:** 2026-07-31

