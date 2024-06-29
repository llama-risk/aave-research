import os
import json
import re
import time
import requests
import telebot
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv

load_dotenv()
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN_AAVE')
CHAT_ID = os.getenv('CHAT_ID_AAVE')
bot = telebot.TeleBot(TELEGRAM_TOKEN, parse_mode='HTML')

def load_proposal_data():
    if os.path.exists('proposal_data.json'):
        with open('proposal_data.json', 'r') as f:
            return json.load(f)
    else:
        return {}

def save_proposal_data(proposal_data):
    with open('proposal_data.json', 'w') as f:
        json.dump(proposal_data, f)

def fetch_and_parse(url):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    driver.implicitly_wait(20)

    driver.get(url)

    WebDriverWait(driver, 10).until(
        EC.invisibility_of_element_located((By.XPATH, "//div[contains(@class, 'skeleton')]"))
    )

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()
    return soup

def extract_proposals(soup):
    proposals = []
    items = soup.find_all('div', class_='ProposalListItem')
    if not items:
        return proposals

    for item in items:
        link = item.find('a')
        if link is None:
            continue
        link = link['href']
        proposal_id = re.search(r'proposalId=(\d+)', link).group(1)
        title = item.find('h2', class_='ProposalListItem__title').text.strip()
        status = None

        if 'Created' in item.text:
            status = 'AIP Created'
        elif 'Voting' in item.text:
            status = 'Voting Started'
        elif 'Passed' in item.text:
            status = 'AIP Vote Passed'
        elif 'Failed' in item.text:
            status = 'AIP Vote Failed'

        if status:
            print(status, title)
            proposals.append({'proposal_id': proposal_id, 'title': title, 'status': status})
    return proposals

def send_alert(title, status, link):
    message = f"*AIP status has changed*\n\n*Title:* {title}\n*Status:* {status}\n*Link:* {link}"
    try:
        bot.send_message(CHAT_ID, message, parse_mode="markdown")
    except telebot.apihelper.ApiTelegramException as e:
        if e.error_code == 429:
            print("Too Many Requests. Skipping and continuing...")
        else:
            print(f"Error sending message: {str(e)}")

def check_proposals(url, proposal_data):
    soup = fetch_and_parse(url)
    proposals = extract_proposals(soup)

    for proposal in proposals:
        proposal_id = proposal['proposal_id']
        title = proposal['title']
        status = proposal['status']
        link = f"https://vote.onaave.com/proposal/?proposalId={proposal_id}"

        if proposal_id not in proposal_data:
            send_alert(title, status, link)
            proposal_data[proposal_id] = status
        elif proposal_data[proposal_id] != status:
            send_alert(title, status, link)
            proposal_data[proposal_id] = status

    save_proposal_data(proposal_data)

def main():
    proposal_data = load_proposal_data()
    url = "https://vote.onaave.com/"
    check_proposals(url, proposal_data)

if __name__ == '__main__':
    main()
