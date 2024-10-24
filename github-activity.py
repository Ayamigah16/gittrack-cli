from urllib import request
import json
import os
from dotenv import load_dotenv

load_dotenv()

GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
if not GITHUB_TOKEN:
    raise ValueError("No GITHUB_TOKEN found")
else:
    print("GITHUB_TOKEN found")


GITHUB_API_URL = "https://api.github.com"

headers = {
    'Authorization': f'token {GITHUB_TOKEN}',
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28" ,
}

def get_github_activity(username):
    url = f'{GITHUB_API_URL}/users/{username}/events'

    req = request.Request(url, headers=headers)

    try:
        with request.urlopen(req) as response:
            data = response.read().decode()
            events = json.loads(data)

            if events:
                return events
            # for event in events:
            #     print(event['type'], event['repo']['name'], event['created_at'])
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to translate event types to human-readable format
def format_event(event):
    event_type = event['type']
    repo_name = event['repo']['name']

    if event_type == 'PushEvent':
        commit_count = len(event['payload']['commits'])
        return f"Pushed {commit_count} commits to {repo_name}"

    elif event_type == 'IssuesEvent':
        action = event['payload']['action']
        return f"{action.capitalize()} an issue in {repo_name}"

    elif event_type == 'PullRequestEvent':
        action = event['payload']['action']
        return f"{action.capitalize()} a pull request in {repo_name}"

    elif event_type == 'WatchEvent':
        return f"Starred {repo_name}"

    elif event_type == 'ForkEvent':
        return f"Forked {repo_name}"

    elif event_type == 'CreateEvent':
        ref_type = event['payload']['ref_type']
        return f"Created a {ref_type} in {repo_name}"

    else:
        return f"{event_type} in {repo_name}"

    # with request.urlopen(url) as response:
    #     data = response.read()
    #     data = json.loads(data)
    #     return data
    

if __name__ == '__main__':
    username = 'Ayamigah16'
    activity = get_github_activity(username)
    
    if activity:
        print(f"Recent activity for GitHub user: {username}")
        for event in activity:
            print(format_event(event))