class EventFormatter:
    """
    A class used to format GitHub event data into human-readable strings.
    Methods
    -------
    format_event(event)
        Formats a given GitHub event into a human-readable string based on the event type.
    """

    @staticmethod
    def format_event(event):
        """
        Formats a given GitHub event into a human-readable string.
        Parameters
        ----------
        event : dict
            A dictionary containing the event data. The dictionary must have the following structure:
            {
                'type': str,  # The type of the event (e.g., 'PushEvent', 'IssuesEvent', etc.)
                'repo': {
                    'name': str  # The name of the repository where the event occurred
                },
                'payload': dict  # Additional data specific to the event type
            }
        Returns
        -------
        str
            A formatted string describing the event.
        """
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