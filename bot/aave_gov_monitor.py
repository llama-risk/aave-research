import os
import json
import re
import requests
import telebot
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')
bot = telebot.TeleBot(TELEGRAM_TOKEN, parse_mode='HTML')

iso_8601 = '%Y-%m-%dT%H:%M:%S.%fZ'

def load_last_processed_timestamp():
    if os.path.exists('last_processed_timestamp'):
        with open('last_processed_timestamp', 'r') as f:
            return datetime.strptime(f.read().strip(), iso_8601)
    else:
        return datetime.min

def save_last_processed_timestamp(last_processed_timestamp):
    with open('last_processed_timestamp', 'w') as f:
        # export to ISO 8601 (microsecond to millisecond truncation)
        f.write(last_processed_timestamp.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z")

def check_new_topics(url, last_processed_timestamp):

    data = requests.get(url).json()
    for topic in data['latest_posts']:

        topic_timestamp = datetime.strptime(topic['created_at'], iso_8601)

        if topic_timestamp <= last_processed_timestamp:
            break # break since list is ordered by decreasing timestamp

        topic_id = topic['topic_id']
        print("checking topic ID " + str(topic_id) + " at " + topic['created_at'])

        last_processed_timestamp = topic_timestamp
        if re.search(r'\[?ARFC\]?|\[?TEMP CHECK\]?', topic['topic_title'], re.IGNORECASE):
            print("MATCH for topic ID " + str(topic_id))
            title = topic['topic_title']
            link = f"https://governance.aave.com/t/{topic_id}"
            send_alert(title, link)

    save_last_processed_timestamp(last_processed_timestamp)

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
    last_processed_timestamp = load_last_processed_timestamp()
    url = "https://governance.aave.com/posts.json"
    check_new_topics(url, last_processed_timestamp)

if __name__ == '__main__':
    main()
