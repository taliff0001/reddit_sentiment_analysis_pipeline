import unittest
from data_collection.fetch_reddit_data import authenticate_reddit, fetch_threads

class TestDataCollection(unittest.TestCase):
    def setUp(self):
        """
        Set up Reddit authentication and test configuration.
        """
        self.reddit = authenticate_reddit()
        self.subreddit = "testsubreddit"  # Replace with an actual test subreddit
        self.keywords = ["testkeyword"]

    def test_authentication(self):
        """
        Test that Reddit authentication returns a valid Reddit instance.
        """
        self.assertIsNotNone(self.reddit, "Reddit authentication failed. Instance is None.")

    def test_fetch_threads_returns_list(self):
        """
        Test that fetch_threads returns a list of threads.
        """
        threads = fetch_threads(self.reddit, self.subreddit, self.keywords, limit=5)
        self.assertIsInstance(threads, list, "fetch_threads should return a list.")

    def test_fetch_threads_with_keywords(self):
        """
        Test that fetch_threads filters threads by keywords.
        """
        threads = fetch_threads(self.reddit, self.subreddit, self.keywords, limit=5)
        for thread in threads:
            self.assertTrue(
                any(keyword in thread["title"].lower() for keyword in self.keywords),
                "Thread does not contain any of the specified keywords."
            )

if __name__ == "__main__":
    unittest.main()