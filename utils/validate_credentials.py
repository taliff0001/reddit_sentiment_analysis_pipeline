# validate_credentials.py

import json
import os
import praw

def validate_credentials(credentials_path='../config/reddit_credentials.json'):
    """
    Validates the Reddit API credentials.

    Args:
        credentials_path (str): Path to the credentials JSON file.

    Returns:
        bool: True if credentials are valid, False otherwise.
    """
    required_keys = ['client_id', 'client_secret', 'user_agent', 'username', 'password']

    if not os.path.exists(credentials_path):
        print(f"Credentials file not found: {credentials_path}")
        return False

    with open(credentials_path, 'r') as f:
        credentials = json.load(f)

    for key in required_keys:
        if key not in credentials or not credentials[key]:
            print(f"Missing or empty credential: {key}")
            return False

    try:
        reddit = praw.Reddit(
            client_id=credentials['client_id'],
            client_secret=credentials['client_secret'],
            user_agent=credentials['user_agent'],
            username=credentials['username'],
            password=credentials['password']
        )
        # Test the authentication by making a simple API call
        reddit.user.me()
    except Exception as e:
        print(f"Failed to authenticate with Reddit API: {e}")
        return False

    print("All credentials are valid and authentication was successful.")
    return True

if __name__ == "__main__":
    validate_credentials()