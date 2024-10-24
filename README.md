# GitTrack

**GitTrack** is a simple command-line tool that fetches and displays recent GitHub activity for any user. It uses the GitHub API to show public events such as pushes, forks, and issues, all in a clean and readable format right in your terminal.

## Features
- Fetch recent GitHub activity for any user.
- Built-in error handling for missing users or connection issues.
- Lightweight and easy to use, no external libraries required.


## Getting Started

### Prerequisites
- Python 3.x

### Installation

1. Clone the repository:
   ```
   >>> git clone https://github.com/yourusername/gittrack.git
   >>> cd gittrack
   ```
2. Make sure you have python installed
    ```
    python --version
    ```

## Usage
- Run the script:

    ```
    >>> python gittrack.py <github_username>
    ```

## How It Works
* GitTrack uses Python's built-in urllib module to send requests to the GitHub API and fetch the user's public events.
* It then parses the JSON response using the json module and displays the activity in the terminal.


## Contributing
* Feel free to fork this project, submit pull requests, or suggest features by opening issues.

## Future Enhancements
* Add authentication for fetching private or more detailed user activity.
* Support for additional event types and filtering options.
* Enhanced terminal interface with color and formatting.
* Caching the Fetched Data
* Filtering by Event Type


## License
This project is licensed under the MIT License - see the <a href="./LICENSE">LICENSE</a> file for details.