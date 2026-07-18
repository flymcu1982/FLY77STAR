const https = require('https');
const xml2js = require('xml2js');
const { google } = require('googleapis');
const nodemailer = require('nodemailer');

// RSS フィード定義
const RSS_FEEDS = {
  ai: 'https://feeds.techcrunch.com/category/artificial-intelligence/',
  kpop: 'https://feeds.sbs.co.kr/kpop/feed/',
  us: 'https://feeds.reuters.com/reuters/businessNews',
  japan: 'https://feeds.nhk.or.jp/news/rss/',
  youtube: 'https://www.youtube.com/feeds/videos.xml?channel_id=UCkQX1tChV7i6SAKL06pNwpQ'
};

// Google Drive & Gmail クライアント初期化
const initGoogleClients = () => {
  const auth = new google.auth.GoogleAuth({
    projectId: process.env.GOOGLE_PROJECT_ID,
    keyFile: process.env.GOOGLE_CREDENTIALS_PATH,
    scopes: [
      'https://www.googleapis.com/auth/drive',
      'https://www.googleapis.com/auth/gmail.send'
    ]
  });

  return {
    drive: google.drive({ version: 'v3', auth }),
    gmail: google.gmail({ version: 'v1', auth })
  };
};

// RSS フィード取得
const fetchFeed = (feedUrl) => {
  return new Promise((resolve, reject) => {
    https.get(feedUrl, (res) => {
      let data = '';
      res.on('data', (chunk) => { data += chunk; });
      res.on('end', async () => {
        try {
          const parser = new xml2js.Parser();
          const result = await parser.parseStringPromise(data);
          const items = result.rss?.channel?.[0]?.item || result.feed?.entry || [];
          resolve(items.slice(0, 5).map(item => ({
            title: item.title?.[0] || item.title,
            link: item.link?.[0]?.$ ? item.link[0].$.href : item.link?.[0],
            pubDate: item.pubDate?.[0] || item.published?.[0],
            description: item.description?.[0] || item.summary?.[0],
            source: feedUrl
          })));
        } catch (err) {
          reject(err);
        }
      });
    }).on('error', reject);
  });
};

// Google Drive に Google Sheet を作成・更新
const saveToGoogleDrive = async (drive, newsData) => {
  try {
    // /AI_NEWS_DIGEST フォルダを検索または作成
    let folderId;
    const folderRes = await drive.files.list({
      q: "name='AI_NEWS_DIGEST' and mimeType='application/vnd.google-apps.folder' and trashed=false",
      spaces: 'drive',
      fields: 'files(id)',
      pageSize: 1
    });

    if (folderRes.data.files.length > 0) {
      folderId = folderRes.data.files[0].id;
    } else {
      const createRes = await drive.files.create({
        resource: {
          name: 'AI_NEWS_DIGEST',
          mimeType: 'application/vnd.google-apps.folder'
        },
        fields: 'id'
      });
      folderId = createRes.data.id;
    }

    // 日付別シート名（例: "News_2026-07-18"）
    const sheetName = `News_${new Date().toISOString().split('T')[0]}`;

    // Google Sheet 作成
    const sheets = google.sheets({ version: 'v4', auth: drive._options.auth });
    const spreadsheetRes = await sheets.spreadsheets.create({
      resource: {
        properties: { title: sheetName },
        sheets: [
          { properties: { title: 'AI' } },
          { properties: { title: 'K-pop' } },
          { properties: { title: 'US' } },
          { properties: { title: 'Japan' } },
          { properties: { title: 'YouTube' } }
        ]
      }
    });

    const spreadsheetId = spreadsheetRes.data.spreadsheetId;

    // ファイルを AI_NEWS_DIGEST フォルダに移動
    await drive.files.update({
      fileId: spreadsheetId,
      addParents: folderId,
      fields: 'id, parents'
    });

    // 各カテゴリーのデータをシートに書き込み
    const updateData = [];
    const categories = ['AI', 'K-pop', 'US', 'Japan', 'YouTube'];
    const tabMap = { ai: 0, kpop: 1, us: 2, japan: 3, youtube: 4 };

    for (const [category, items] of Object.entries(newsData)) {
      const tabIndex = tabMap[category];
      const tabName = categories[tabIndex];

      const rows = items.map(item => [
        item.title,
        item.link,
        item.pubDate,
        item.description?.substring(0, 100) || ''
      ]);

      updateData.push({
        range: `${tabName}!A1:D${rows.length + 1}`,
        values: [['Title', 'Link', 'Date', 'Description'], ...rows]
      });
    }

    await sheets.spreadsheets.values.batchUpdate({
      spreadsheetId,
      resource: { data: updateData, valueInputOption: 'RAW' }
    });

    return spreadsheetId;
  } catch (err) {
    console.error('Google Drive save error:', err);
    throw err;
  }
};

// Gmail でメール送信
const sendEmailNotification = async (gmail, newsData, sheetUrl) => {
  try {
    const categories = ['AI', 'K-pop', 'US', 'Japan', 'YouTube'];
    let emailBody = '<h2>📰 AI News Digest - Latest Updates</h2>';
    emailBody += `<p>Generated: ${new Date().toLocaleString('ja-JP', { timeZone: 'Asia/Tokyo' })}</p>`;
    emailBody += `<p><a href="${sheetUrl}">📊 View Full Report on Google Drive</a></p>`;

    for (const category of categories) {
      const items = newsData[category.toLowerCase()];
      emailBody += `<h3>🔹 ${category}</h3><ul>`;
      items.forEach(item => {
        emailBody += `<li><strong>${item.title}</strong><br><a href="${item.link}">Read more</a></li>`;
      });
      emailBody += '</ul>';
    }

    const message = {
      raw: Buffer.from(
        `From: ${process.env.GMAIL_USER}\r\n` +
        `To: ${process.env.YU_EMAIL}\r\n` +
        `Subject: 📰 AI News Digest\r\n` +
        `Content-Type: text/html; charset=utf-8\r\n\r\n` +
        emailBody
      ).toString('base64')
    };

    await gmail.users.messages.send({
      userId: 'me',
      resource: message
    });

    console.log('Email sent successfully');
  } catch (err) {
    console.error('Gmail send error:', err);
    throw err;
  }
};

// Netlify Function メインハンドラ
exports.handler = async (event, context) => {
  try {
    console.log('🔄 AI News Digest sync started');

    // RSS フィード取得（並列実行）
    const newsData = {};
    const feedPromises = Object.entries(RSS_FEEDS).map(([category, url]) =>
      fetchFeed(url)
        .then(items => { newsData[category] = items; })
        .catch(err => {
          console.error(`Error fetching ${category}:`, err);
          newsData[category] = [];
        })
    );

    await Promise.all(feedPromises);

    // Google Drive に保存
    const { drive, gmail } = initGoogleClients();
    const sheetId = await saveToGoogleDrive(drive, newsData);
    const sheetUrl = `https://docs.google.com/spreadsheets/d/${sheetId}`;

    // Gmail で通知
    await sendEmailNotification(gmail, newsData, sheetUrl);

    return {
      statusCode: 200,
      body: JSON.stringify({
        message: '✅ AI News Digest sync completed',
        timestamp: new Date().toISOString(),
        sheetUrl: sheetUrl,
        newsCount: Object.values(newsData).reduce((sum, items) => sum + items.length, 0)
      })
    };
  } catch (error) {
    console.error('Sync error:', error);
    return {
      statusCode: 500,
      body: JSON.stringify({ error: error.message })
    };
  }
};
