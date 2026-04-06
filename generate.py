import os
import anthropic
import json
from datetime import datetime
import re

client = anthropic.Anthropic(
    api_key=os.environ["CLAUDE_API_KEY"]
)

prompt = """
あなたはAI×スマホ収益化の専門家です。
以下の条件で今週のX投稿7本を生成してください。

条件：
- テーマ：AIとスマホだけで収益化する方法
- トーン：実践的・数字あり・短文
- 各投稿140文字以内
- 末尾に必ず行動を促すCTA
- JSON形式で出力

出力形式：
{"posts": [
  {"day": "monday", "content": "投稿内容"},
  {"day": "tuesday", "content": "投稿内容"},
  {"day": "wednesday", "content": "投稿内容"},
  {"day": "thursday", "content": "投稿内容"},
  {"day": "friday", "content": "投稿内容"},
  {"day": "saturday", "content": "投稿内容"},
  {"day": "sunday", "content": "投稿内容"}
]}
"""

message = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=2000,
    messages=[{"role": "user", "content": prompt}]
)

result = message.content[0].text
json_match = re.search(r'\{.*\}', result, re.DOTALL)

if json_match:
    with open("posts.json", "w", encoding="utf-8") as f:
        f.write(json_match.group())
    print("posts.json更新完了")
else:
    print("JSON抽出失敗")
