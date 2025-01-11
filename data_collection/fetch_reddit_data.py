"""
fetch_reddit_data.py

This module handles authentication with the Reddit API and provides functions
to fetch threads and comments based on specified criteria.
"""

from praw.models import Submission, Comment
from typing import List, Optional
import praw
import json


def authenticate_reddit():
    """
    Authenticates and returns a Reddit instance using PRAW.

    Returns:
        praw.Reddit: Authenticated Reddit instance.
    """
    with open("config/reddit_credentials.json", "r") as f:
        credentials = json.load(f)

    return praw.Reddit(
        client_id=credentials["client_id"],
        client_secret=credentials["client_secret"],
        user_agent=credentials["user_agent"],
        username=credentials["username"],
        password=credentials["password"]
    )


def fetch_threads(reddit, subreddit, keywords=None, limit=100):
    sub = reddit.subreddit(subreddit)
    threads = []

    for submission in sub.new(limit=limit):
        if keywords and not any(keyword.lower() in submission.title.lower() for keyword in keywords):
            continue

        threads.append({
            "id": submission.id,
            "title": submission.title or "No Title",
            "selftext": submission.selftext or "No Content",
            "author": str(submission.author),
            "subreddit": submission.subreddit.display_name,
            "score": submission.score,
            "created_utc": submission.created_utc
        })

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
