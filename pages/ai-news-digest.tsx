import React, { useState, useEffect } from 'react';
import { ChevronDown, ExternalLink, RefreshCw } from 'lucide-react';
import styles from '../styles/ai-news-digest.module.css';

interface NewsItem {
  title: string;
  link: string;
  pubDate: string;
  description: string;
}

interface NewsData {
  ai: NewsItem[];
  kpop: NewsItem[];
  us: NewsItem[];
  japan: NewsItem[];
  youtube: NewsItem[];
}

const AINewsDigest: React.FC = () => {
  const [activeTab, setActiveTab] = useState<keyof NewsData>('ai');
  const [newsData, setNewsData] = useState<NewsData>({
    ai: [],
    kpop: [],
    us: [],
    japan: [],
    youtube: []
  });
  const [loading, setLoading] = useState(false);
  const [lastUpdated, setLastUpdated] = useState<string>('');

  const tabs: Array<{ key: keyof NewsData; label: string; emoji: string }> = [
    { key: 'ai', label: 'AI', emoji: '🤖' },
    { key: 'kpop', label: 'K-pop', emoji: '🎵' },
    { key: 'us', label: 'US', emoji: 🇺🇸' },
    { key: 'japan', label: 'Japan', emoji: '🇯🇵' },
    { key: 'youtube', label: 'YouTube', emoji: '📺' }
  ];

  // Google Drive シートからデータ取得
  const fetchNewsData = async () => {
    setLoading(true);
    try {
      const response = await fetch('/.netlify/functions/ai-news-sync', {
        method: 'GET'
      });
      const result = await response.json();

      if (result.sheetUrl) {
        // Google Sheet から最新ニュース取得
        // 実装: Google Sheets API で最新シートを読み込み
        setLastUpdated(new Date().toLocaleString('ja-JP', { timeZone: 'Asia/Tokyo' }));
      }
    } catch (error) {
      console.error('Failed to fetch news:', error);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchNewsData();
    // 3日ごとに自動更新（Cron で実行される）
    const interval = setInterval(fetchNewsData, 3 * 24 * 60 * 60 * 1000);
    return () => clearInterval(interval);
  }, []);

  // ニュースアイテムのレンダリング
  const renderNewsItem = (item: NewsItem, index: number) => (
    <div key={index} className={styles.newsItem}>
      <div className={styles.newsHeader}>
        <h3 className={styles.newsTitle}>{item.title}</h3>
        <a href={item.link} target="_blank" rel="noopener noreferrer" className={styles.externalLink}>
          <ExternalLink size={16} />
        </a>
      </div>
      <p className={styles.newsDate}>{new Date(item.pubDate).toLocaleDateString('ja-JP')}</p>
      <p className={styles.newsDescription}>{item.description?.substring(0, 150)}...</p>
      <a href={item.link} target="_blank" rel="noopener noreferrer" className={styles.readMore}>
        詳細を読む →
      </a>
    </div>
  );

  return (
    <div className={styles.container}>
      <header className={styles.header}>
        <h1>📰 AI News Digest</h1>
        <p className={styles.subtitle}>AI・K-pop・米国・日本・YouTube の最新ニュース</p>
        {lastUpdated && (
          <p className={styles.lastUpdated}>最終更新: {lastUpdated}</p>
        )}
      </header>

      <div className={styles.controlsBar}>
        <button
          onClick={fetchNewsData}
          disabled={loading}
          className={styles.refreshButton}
        >
          <RefreshCw size={18} className={loading ? styles.spinning : ''} />
          {loading ? '更新中...' : '今すぐ更新'}
        </button>
      </div>

      <div className={styles.tabsContainer}>
        {tabs.map(tab => (
          <button
            key={tab.key}
            onClick={() => setActiveTab(tab.key)}
            className={`${styles.tab} ${activeTab === tab.key ? styles.activeTab : ''}`}
          >
            <span className={styles.emoji}>{tab.emoji}</span>
            <span className={styles.tabLabel}>{tab.label}</span>
          </button>
        ))}
      </div>

      <div className={styles.contentArea}>
        {newsData[activeTab] && newsData[activeTab].length > 0 ? (
          <div className={styles.newsList}>
            {newsData[activeTab].map((item, index) => renderNewsItem(item, index))}
          </div>
        ) : (
          <div className={styles.emptyState}>
            <p>ニュースがまだ読み込まれていません</p>
            <p className={styles.emptyStateHint}>「今すぐ更新」ボタンで手動更新できます</p>
          </div>
        )}
      </div>

      <footer className={styles.footer}>
        <p>🔄 自動更新: 3日ごと | 📧 YU に毎回メール通知</p>
        <p>ご質問やご要望は Claude Code までお気軽に</p>
      </footer>
    </div>
  );
};

export default AINewsDigest;
