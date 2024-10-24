import os
from dotenv import load_dotenv

load_dotenv()

class ConfigManager:
    """
    Manages configuration settings for GitHub API interactions.
    Attributes:
        github_token (str): The GitHub API token retrieved from environment variables.
        github_api_url (str): The GitHub API URL, defaults to 'https://api.github.com'.
    Methods:
        get_headers():
            Generates the headers required for GitHub API requests.
    """
    
    def __init__(self):
        self.github_token = os.getenv('GITHUB_API_TOKEN')
        self.github_api_url = os.getenv('GITHUB_API_URL', 'https://api.github.com')

    def get_headers(self):
        return {
            'User-Agent': 'Mozilla/5.0',
            'Accept': 'application/vnd.github.v3+json',
            'Authorization': f'token {self.github_token}'
        }