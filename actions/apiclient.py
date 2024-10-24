from urllib import request, error
from .config import ConfigManager
import json

class GitHubAPIClient():
    """
    A client for interacting with the GitHub API to fetch user activity.
    Args:
        config (ConfigManager): Configuration manager instance containing API settings.
 
    Methods:
        fetch_user_activity(username):
            Fetches the public activity events of a specified GitHub user.
        handle_http_error(error, username):
            Handles HTTP errors that occur during API requests.
    """

    def __init__(self, config):
        """
        Initializes the API client with the given configuration.
        Args:
            config (dict): A dictionary containing configuration parameters.
        """
        
        self.config = config

    def fetch_user_activity(self, username):
        """
        Fetches the public activity events of a specified GitHub user.
        Args:
            username (str): The GitHub username for which to fetch public activity events.
        Returns:
            list: A list of public activity events if available, otherwise None.
        Raises:
            HTTPError: If an HTTP error occurs during the request.
            URLError: If a URL error occurs during the request.
            JSONDecodeError: If the response cannot be decoded as JSON.
            Exception: For any other unexpected errors.
        """

        url = f'{self.config.github_api_url}/users/{username}/events'
        headers = self.config.get_headers()

        req = request.Request(url, headers=headers)

        try:
            with request.urlopen(req) as response:
                data = response.read().decode()
                events = json.loads(data)

                if events:
                    return events
                else:
                    print(f"No public activity found for user: {username}")
                    return None

        except error.HTTPError as e:
            self.handle_http_error(e, username)
        except error.URLError as e:
            print(f"Error: Failed to reach the server. Reason: {e.reason}")
        except json.JSONDecodeError:
            print("Error: Failed to decode the JSON response from the server.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

        return None

    @staticmethod
    def handle_http_error(error, username):
        """
        Handles HTTP errors returned by the GitHub API.
        Args:
            error (HTTPError): The HTTP error object containing the error code and headers.
            username (str): The GitHub username that was being accessed when the error occurred.
        Returns:
            None
        Raises:
            None
        Prints:
            A user-friendly error message based on the HTTP error code.
        """

        if error.code == 404:
            print(f"Error: GitHub user '{username}' not found.")
        elif error.code == 403:
            if 'X-RateLimit-Remaining' in error.headers and error.headers['X-RateLimit-Remaining'] == '0':
                print("Error: GitHub API rate limit exceeded. Try again later.")
            else:
                print(f"Error: Access forbidden. Please check your API token or permissions.")
        elif error.code == 401:
            print("Error: Unauthorized. Please check your GitHub API token.")
        else:
            print(f"Error: HTTP Error {error.code} occurred.")