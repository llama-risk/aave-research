import os
import json
import re
import requests
import telebot
import time
from dotenv import load_dotenv
from datetime import datetime, timedelta

load_dotenv()
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN_AAVE')
CHAT_ID = os.getenv('CHAT_ID_AAVE')
bot = telebot.TeleBot(TELEGRAM_TOKEN, parse_mode='HTML')

AAVE_GOVERNANCE_URL = 'https://governance.aave.com/posts.json'

GITHUB_TOKEN = os.getenv('GITHUB_TOKEN_AAVE')
GITHUB_GRAPHQL_URL = 'https://api.github.com/graphql'

GITHUB_REPOSITORY = "R_kgDOMl-plw" # 'aave-private' repository
GITHUB_PROJECT = "PVT_kwDOCSIUVc4Ao7mq" # 'aave' project

GITHUB_HEADER = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Content-Type": "application/json"
}

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

def get_new_arfc(url, last_processed_timestamp):

    latest_posts = requests.get(url).json()['latest_posts']
    new_arfc = []

    for topic in latest_posts:
    
        topic_timestamp = datetime.strptime(topic['created_at'], iso_8601)

        if topic_timestamp <= last_processed_timestamp:
            break # break since list is ordered by decreasing timestamp

        topic_id = topic['topic_id']
        print("checking topic ID " + str(topic_id) + " at " + topic['created_at'])

        if topic['post_number'] != 1:
            continue # ignore if post is a reply

        if not re.search(r'\[?ARFC\]?|\[?TEMP CHECK\]?', topic['topic_title'], re.IGNORECASE):
            continue # ignore if post is not ARFC or TEMP_CHECK

        print("MATCH for topic ID " + str(topic_id))
        title = topic['topic_title']
        link = f"https://governance.aave.com/t/{topic_id}"
        new_arfc.append({'title': title, 'link': link})

    return new_arfc, datetime.strptime(latest_posts[0]['created_at'], iso_8601)

def publish_to_telegram_channel(chat_id, message):

    try:
        bot.send_message(CHAT_ID, message, disable_web_page_preview=True)
    except telebot.apihelper.ApiTelegramException as e:
        if e.error_code == 429:
            print("too many requests, wait 1s and continue")
            time.sleep(1)
        else:
            print(f"error sending message: {str(e)}")

GITHUB_ADD_ISSUE_TO_REPO_QUERY = """
    mutation($repositoryId: ID!, $title: String!, $body: String!) {
      createIssue(input: {
        repositoryId: $repositoryId, 
        title: $title, 
        body: $body
      }) {
        issue {
          id
          url
        }
      }
    }"""

def create_github_issue(repo_id, issue_title, issue_body):
    
    response = requests.post(GITHUB_GRAPHQL_URL, headers=GITHUB_HEADER, data=json.dumps({
        "query": GITHUB_ADD_ISSUE_TO_REPO_QUERY,
        "variables": {
            "repositoryId": repo_id,
            "title": issue_title,
            "body": issue_body
        }
    }))

    if response.status_code == 200:
        print("github issue with title " + issue_title + " created in repo " + str(repo_id))
        return response.json()['data']['createIssue']['issue']['id']
    else:
        print("failed to create github issue in repo " + str(repo_id) + " with title " + str(issue_title) + ": " + str(response.status_code))
        print(response.json())
        return 0

GITHUB_ADD_PROJECT_ITEM_QUERY = """
    mutation($projectId: ID!, $issueId: ID!) {
      addProjectV2ItemById(input: {projectId: $projectId, contentId: $issueId}) {
        item {
          id
        }
      }
    }"""

def add_project_item(project_id, issue_id):

    response = requests.post(GITHUB_GRAPHQL_URL, headers=GITHUB_HEADER, data=json.dumps({
        "query": GITHUB_ADD_PROJECT_ITEM_QUERY,
        "variables": {
            "projectId": project_id,
            "issueId": issue_id
        }
    }))

    if response.status_code == 200:
        print("github issue " + str(issue_id) + " added to project " + str(project_id))
        return response.json()['data']['addProjectV2ItemById']['item']['id']
    else:
        print("failed to add github issue " + str(issue_id) + " to project " + str(project_id) + ": " + str(response.status_code))
        print(response.json())
        return 0

GITHUB_UPDATE_PROJECT_ITEM_QUERY = """
    mutation(
        $projectId: ID!, 
        $projectItemId: ID!, 
        $classFieldId: ID!, 
        $classOptionId: String!
    ) {
        # Update Status
        updateStatus: updateProjectV2ItemFieldValue(input: {
            projectId: $projectId, 
            itemId: $projectItemId, 
            fieldId: $classFieldId, 
            value: {singleSelectOptionId: $classOptionId}
            }) {
            projectV2Item {
              id
            }
        }
    }"""

def update_project_item(project_id, project_item_id, prefix):

    if prefix == "[ARFC]":
        classOptionId = "596877b0"
    elif prefix == "[TEMP_CHECK]":
        classOptionId = "23b48dd6"
    else: # default to 'Research'
        classOptionId = "4cf134c2"

    today = datetime.today()
    in_5_days = today + timedelta(days=5)

    response = requests.post(GITHUB_GRAPHQL_URL, headers=GITHUB_HEADER, data=json.dumps({
        "query": GITHUB_UPDATE_PROJECT_ITEM_QUERY,
        "variables": {
            "projectId": project_id,
            "projectItemId": project_item_id,
            "classFieldId": "PVTSSF_lADOCSIUVc4Ao7mqzggbSCc",  # 'Class' field ID
            "classOptionId": classOptionId
        }
    }))

    if response.status_code == 200:
        print("project item " + str(project_item_id) + " updated")
    else:
        print("failed to update project item " + str(project_item_id) + ": " + str(response.status_code))
        print(response.json())

def main():
    last_processed_timestamp = load_last_processed_timestamp()
    new_arfc, last_processed_timestamp = get_new_arfc(AAVE_GOVERNANCE_URL, last_processed_timestamp)

    for post in new_arfc:
        publish_to_telegram_channel(CHAT_ID, f"New topic alert:\n\nTitle: {post['title']}\nLink: {post['link']}")

        issue_id = create_github_issue(GITHUB_REPOSITORY, post['title'], post['link'])
        if issue_id == 0:
            continue

        project_item_id = add_project_item(GITHUB_PROJECT, issue_id)
        if project_item_id == 0:
            continue

        update_project_item(GITHUB_PROJECT, project_item_id, post['title'].split(" ")[0])
        
    save_last_processed_timestamp(last_processed_timestamp)

if __name__ == '__main__':
    main()
