import os
import json
import re
import requests
import telebot
from dotenv import load_dotenv

# Bot setup
load_dotenv()
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')
bot = telebot.TeleBot(TELEGRAM_TOKEN, parse_mode='HTML')

def load_processed_ids():
    if os.path.exists('processed_ids.json'):
        with open('processed_ids.json', 'r') as f:
            return json.load(f)
    else:
        return []

def save_processed_ids(processed_ids):
    with open('processed_ids.json', 'w') as f:
        json.dump(processed_ids, f)

def check_new_topics(url, processed_ids):
    response = requests.get(url)
    data = response.json()

    for topic in data['latest_posts']:
        print("checking", topic)
        topic_id = topic['topic_id']
        if topic_id not in processed_ids and re.search(r'\[?ARFC\]?|\[?TEMP CHECK\]?', topic['topic_title'], re.IGNORECASE):
            print("MATCH")
            title = topic['topic_title']
            link = f"https://governance.aave.com/t/{topic_id}"
            send_alert(title, link)
            processed_ids.append(topic_id)

    save_processed_ids(processed_ids)

def send_alert(title, link):
    message = f"New topic alert:\n\nTitle: {title}\nLink: {link}"
    try:
        bot.send_message(CHAT_ID, message)
    except telebot.apihelper.ApiTelegramException as e:
        if e.error_code == 429:
            print("Too Many Requests. Skipping and continuing...")
        else:
            print(f"Error sending message: {str(e)}")

def main():
    processed_ids = load_processed_ids()
    url = "https://governance.aave.com/posts.json"
    check_new_topics(url, processed_ids)

if __name__ == '__main__':
    main()