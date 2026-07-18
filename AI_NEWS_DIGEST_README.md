# 📰 AI News Digest - Complete Implementation Guide

## 概要

FLY77STAR.「AI News Digest」は、**AI・K-pop・米国・日本・YouTube** の最新ニュースを自動収集・集約し、Google Drive に保存して YU にメール通知する完全自動化システムです。

**実行スケジュール**: 3日ごと（毎日 09:00 UTC）  
**配信先**: fly77star.official@gmail.com  
**収集元**: 5つの RSS フィード + Google Drive + Gmail  

---

## ファイル構成

```
FLY77STAR/
├── netlify/
│   └── functions/
│       └── ai-news-sync.js          # RSS パーサー + Google Drive + Gmail
├── pages/
│   └── ai-news-digest.tsx           # React フロントエンド（5タブ UI）
├── styles/
│   └── ai-news-digest.module.css    # CSS モジュール（レスポンシブ対応）
├── netlify.toml                      # Netlify 設定（Cron 設定含む）
├── next.config.js                    # Next.js 設定
├── package.json                      # 依存関係
├── .env.example                      # 環境変数テンプレート
└── AI_NEWS_DIGEST_README.md          # このファイル
```

---

## 🚀 セットアップ手順

### ステップ 1: 環境変数の設定

**.env.example をコピーして .env を作成:**

```bash
cp .env.example .env
```

**以下の環境変数を Netlify Dashboard で設定:**

```
GOOGLE_PROJECT_ID           (Google Cloud)
GOOGLE_PRIVATE_KEY_ID       (Google Cloud)
GOOGLE_PRIVATE_KEY          (Google Cloud - JSON キー)
GOOGLE_CLIENT_EMAIL         (Google Cloud)
GOOGLE_CLIENT_ID            (Google Cloud)
GMAIL_USER                  (fly77star.official@gmail.com)
GMAIL_APP_PASSWORD          (16 文字スペース含む)
YU_EMAIL                    (fly77star.official@gmail.com)
```

### ステップ 2: Google API キーの取得

1. **Google Cloud Console にアクセス**: https://console.cloud.google.com/
2. **新規プロジェクト作成**: 「AI_NEWS_DIGEST」
3. **API を有効化**:
   - Google Drive API
   - Gmail API
4. **サービスアカウント作成**:
   - IAM → Service Accounts → Create Service Account
   - 名前: `ai-news-sync-bot`
   - ロール: Editor
5. **JSON キーを生成**:
   - Keys タブ → Add Key → Create new key
   - Type: JSON
   - ダウンロードしたファイルから以下をコピー:
     - `project_id` → GOOGLE_PROJECT_ID
     - `private_key_id` → GOOGLE_PRIVATE_KEY_ID
     - `private_key` → GOOGLE_PRIVATE_KEY
     - `client_email` → GOOGLE_CLIENT_EMAIL
     - `client_id` → GOOGLE_CLIENT_ID

### ステップ 3: Gmail App Password の取得

1. **Google Account Security**: https://myaccount.google.com/security
2. **2-Step Verification が有効か確認**（必須）
3. **App passwords に移動**:
   - App: Mail
   - Device: Linux
   - 生成されたパスワードをコピー（例: `xxxx xxxx xxxx xxxx`）
4. **.env に設定**:
   ```bash
   GMAIL_APP_PASSWORD="xxxx xxxx xxxx xxxx"
   ```

### ステップ 4: パッケージをインストール

```bash
npm install
```

**インストール対象:**
- `googleapis` (Google Drive/Gmail API)
- `xml2js` (RSS パーサー)
- `nodemailer` (メール送信 - 既存)
- `react`, `react-dom` (フロントエンド)
- `next` (React フレームワーク)
- `lucide-react` (アイコン UI)

### ステップ 5: ローカルで動作確認

```bash
npm run dev
```

開く: http://localhost:3000/ai-news-digest

### ステップ 6: Netlify へデプロイ

```bash
npm run build
git add .
git commit -m "feat: FLY77STAR AI News Digest システム実装"
git push origin claude/fly77star-obsidian-structure-a010jj
```

**Netlify Dashboard で:**
1. 新サイト作成: ai-news-digest
2. GitHub リポジトリに接続
3. 環境変数を設定（Step 1 参照）
4. デプロイ実行

---

## 📊 機能詳細

### Netlify Function: `ai-news-sync.js`

**実行タイミング**: 3日ごと 09:00 UTC（`netlify.toml` で設定）

**処理内容:**
1. **RSS フィード取得** (並列実行):
   - 🤖 AI: TechCrunch AI News
   - 🎵 K-pop: SBS K-pop News
   - 🇺🇸 US: Reuters Business News
   - 🇯🇵 Japan: NHK News
   - 📺 YouTube: Channel Feed

2. **Google Drive 保存**:
   - `/AI_NEWS_DIGEST` フォルダを自動作成（初回のみ）
   - 日付別 Google Sheet 作成（例: `News_2026-07-18`）
   - 5 タブに各カテゴリーのニュースを書き込み

3. **Gmail 通知**:
   - YU にメール送信（HTML 形式）
   - 各カテゴリーの最新 5 件を表示
   - Google Sheet へのリンク付き

**環境変数**:
- `GOOGLE_PROJECT_ID` など Google API 認証
- `GMAIL_USER`, `GMAIL_APP_PASSWORD`
- `YU_EMAIL`

### React フロントエンド: `ai-news-digest.tsx`

**UI 構成:**

| 要素 | 説明 |
|------|------|
| **ヘッダー** | タイトル + 最終更新日時 |
| **更新ボタン** | 「今すぐ更新」ボタン（手動トリガー） |
| **タブバー** | 5 つのカテゴリータブ |
| **ニュースリスト** | 選択したカテゴリーのニュース表示 |
| **各アイテム** | タイトル・日付・説明・外部リンク |
| **フッター** | 自動更新スケジュール情報 |

**機能:**
- 5 つのタブ（AI/K-pop/US/Japan/YouTube）
- 手動更新ボタン
- レスポンシブデザイン（モバイル対応）
- 外部リンククリック時に新規タブで開く

**スタイル**: `ai-news-digest.module.css`（CSS Modules）

---

## 🔄 自動実行フロー

```
毎 3 日 09:00 UTC
    ↓
[Netlify Scheduled Function]
    ↓
[RSS フィード 5 本から並列取得]
    ↓
[Google Drive に Google Sheet 作成]
    ↓
[Gmail で YU に通知メール送信]
    ↓
[完了ログ記録]
```

---

## 📋 動作確認チェックリスト

### デプロイ後の確認

- [ ] Netlify デプロイ成功（https://ai-news-digest.netlify.app）
- [ ] フロントエンド表示（5 タブが表示される）
- [ ] Google Drive に `/AI_NEWS_DIGEST` フォルダが作成されている
- [ ] 最初の自動実行から 3 日後、Google Sheet が新規作成される
- [ ] YU のメールボックスに通知メールが到着
- [ ] HTML メール形式で正しく表示される
- [ ] 「詳細を読む」リンクが機能する

### トラブルシューティング

| 問題 | 原因 | 解決方法 |
|------|------|---------|
| Netlify デプロイエラー | package.json の依存関係不足 | `npm install` → `npm run build` 確認 |
| Google Drive エラー | API キーが無効 | Google Cloud Console でキー再生成 |
| Gmail 送信失敗 | App Password 不正 | 新規生成して .env に設定 |
| Cron が動作しない | 環境変数未設定 | Netlify Dashboard で環境変数確認 |
| フロントエンド真っ白 | Next.js ビルド失敗 | `npm run build` ログ確認 |

---

## 🔐 セキュリティ注意事項

- **.env ファイルは絶対に Git にコミットしない**（`.gitignore` に追加済み）
- **Google Private Key は最小権限で設定**（Editor → Viewer に変更推奨）
- **Gmail App Password は定期的に更新**（90 日ごと）
- **本番環境では HTTPS のみ使用**（Netlify で自動対応）

---

## 📞 サポート・お問い合わせ

ご質問・バグ報告・機能リクエストは Claude Code までお気軽に。

---

## 📅 更新履歴

| 日付 | バージョン | 内容 |
|------|-----------|------|
| 2026-07-18 | v1.0.0 | 初版実装・完成 |

---

**AI News Digest - FLY77STAR Studio による完全自動化ニュース配信システム** ✅
