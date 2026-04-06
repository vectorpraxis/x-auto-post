import os
import json
import tweepy
from datetime import datetime

# X API認証
client = tweepy.Client(
    consumer_key=os.environ['X_API_KEY'],
    consumer_secret=os.environ['X_API_SECRET'],
    access_token=os.environ['X_ACCESS_TOKEN'],
    access_token_secret=os.environ['X_ACCESS_SECRET']
)

# 曜日取得
days = ['monday','tuesday','wednesday',
        'thursday','friday','saturday','sunday']
today = days[datetime.now().weekday()]

# 投稿内容読み込み
with open('posts.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 今日の投稿を探して実行
for post in data['posts']:
    if post['day'] == today:
        client.create_tweet(text=post['content'])
        print(f"投稿完了: {today}")
        break
