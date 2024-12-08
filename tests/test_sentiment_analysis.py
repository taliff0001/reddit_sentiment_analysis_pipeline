import unittest
from sentiment_analysis.sentiment_vader import analyze_sentiment_vader
from sentiment_analysis.sentiment_transformers import analyze_sentiment_transformers

class TestSentimentAnalysis(unittest.TestCase):
    def setUp(self):
        """
        Set up sample text data for sentiment analysis.
        """
        self.positive_text = "I love this!"
        self.negative_text = "I hate this."
        self.neutral_text = "This is okay."

    def test_vader_positive(self):
        """
        Test VADER sentiment analysis on positive text.
        """
        sentiment = analyze_sentiment_vader(self.positive_text)
        self.assertGreater(sentiment["pos"], 0.5, "VADER should detect positive sentiment.")

    def test_vader_negative(self):
        """
        Test VADER sentiment analysis on negative text.
        """
        sentiment = analyze_sentiment_vader(self.negative_text)
        self.assertGreater(sentiment["neg"], 0.5, "VADER should detect negative sentiment.")

    def test_transformers_positive(self):
        """
        Test Transformers sentiment analysis on positive text.
        """
        sentiment = analyze_sentiment_transformers(self.positive_text)
        self.assertEqual(sentiment["label"], "POSITIVE", "Transformers should detect positive sentiment.")

    def test_transformers_negative(self):
        """
        Test Transformers sentiment analysis on negative text.
        """
        sentiment = analyze_sentiment_transformers(self.negative_text)
        self.assertEqual(sentiment["label"], "NEGATIVE", "Transformers should detect negative sentiment.")

if __name__ == "__main__":
    unittest.main()