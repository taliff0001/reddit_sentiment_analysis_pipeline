"""
fetch_reddit_data.py

This module handles authentication with the Reddit API and provides functions
to fetch threads and comments based on specified criteria.
"""

import os
import praw
from praw.models import Submission, Comment
from typing import List, Optional

def authenticate_reddit() -> praw.Reddit:
    """
    Authenticates and returns a Reddit instance using PRAW.

    Returns:
        praw.Reddit: Authenticated Reddit instance.
    """
    # Retrieve Reddit API credentials from environment variables
    client_id = os.getenv('REDDIT_CLIENT_ID')
    client_secret = os.getenv('REDDIT_CLIENT_SECRET')
    user_agent = os.getenv('REDDIT_USER_AGENT')

    # Ensure all necessary credentials are available
    if not all([client_id, client_secret, user_agent]):
        raise ValueError("Missing Reddit API credentials.")

    # Create and return the Reddit instance
    return praw.Reddit(
        client_id=client_id,
        client_secret=client_secret,
        user_agent=user_agent
    )

def fetch_threads(
    reddit: praw.Reddit,
    subreddit: str,
    keywords: Optional[List[str]] = None,
    limit: int = 100
) -> List[Submission]:
    """
    Fetches threads from a specified subreddit, optionally filtered by keywords.

    Args:
        reddit (praw.Reddit): Authenticated Reddit instance.
        subreddit (str): Name of the subreddit to fetch threads from.
        keywords (Optional[List[str]]): List of keywords to filter threads.
        limit (int): Maximum number of threads to fetch.

    Returns:
        List[Submission]: List of fetched Reddit submissions.
    """
    # Access the specified subreddit
    sub = reddit.subreddit(subreddit)

    # Initialize an empty list to store fetched threads
    threads = []

    # Iterate over the subreddit's new submissions up to the specified limit
    for submission in sub.new(limit=limit):
        # If keywords are specified, filter threads that contain any of the keywords
        if keywords:
            if any(keyword.lower() in submission.title.lower() for keyword in keywords):
                threads.append(submission)
        else:
            threads.append(submission)

    return threads

def fetch_comments(
    reddit: praw.Reddit,
    submission_id: str,
    limit: int = 100
) -> List[Comment]:
    """
    Fetches comments from a specified Reddit submission.

    Args:
        reddit (praw.Reddit): Authenticated Reddit instance.
        submission_id (str): ID of the Reddit submission to fetch comments from.
        limit (int): Maximum number of comments to fetch.

    Returns:
        List[Comment]: List of fetched Reddit comments.
    """
    # Fetch the submission using its ID
    submission = reddit.submission(id=submission_id)

    # Replace "MoreComments" instances to fetch all comments
    submission.comments.replace_more(limit=None)

    # Retrieve the specified number of top-level comments
    comments = submission.comments.list()[:limit]

    return comments