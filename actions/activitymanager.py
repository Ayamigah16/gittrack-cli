class GitHubActivityManager:
    def __init__(self, api_client, formatter):
        self.api_client = api_client
        self.formatter = formatter

    def display_user_activity(self, username):
        activity = self.api_client.fetch_user_activity(username)
        if activity:
            print(f"Recent activity for GitHub user: {username}")
            for event in activity:
                print(self.formatter.format_event(event))