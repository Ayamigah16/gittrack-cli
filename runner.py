from actions.config import ConfigManager
from actions.apiclient import GitHubAPIClient
from actions.eventformatter import EventFormatter
from actions.activitymanager import GitHubActivityManager

import sys

if __name__ == "__main__":
    config_manager = ConfigManager()
    github_client = GitHubAPIClient(config_manager)

    event_formatter = EventFormatter()

    # Create the activity manager to handle the main logic
    activity_manager = GitHubActivityManager(github_client, event_formatter)

    # Input username and display their activity
    username = input("Enter GitHub username: ")
    activity_manager.display_user_activity(username)