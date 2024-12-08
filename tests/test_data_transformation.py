import unittest
import pandas as pd
from data_transformation.clean_data import clean_text, clean_dataframe
from data_transformation.normalize_fields import normalize_timestamp

class TestDataTransformation(unittest.TestCase):
    def setUp(self):
        """
        Set up test data for transformation.
        """
        self.raw_data = {
            "title": ["Check out https://example.com!", "Test @user"],
            "timestamp": ["2024-12-06 10:00:00", "2024-12-06 15:30:00"]
        }
        self.df = pd.DataFrame(self.raw_data)

    def test_clean_text(self):
        """
        Test the clean_text function.
        """
        cleaned_text = clean_text(self.raw_data["title"][0])
        self.assertNotIn("https://", cleaned_text, "clean_text should remove URLs.")
        self.assertEqual(clean_text("Test #hashtag"), "test", "clean_text should remove hashtags.")

    def test_clean_dataframe(self):
        """
        Test the clean_dataframe function.
        """
        cleaned_df = clean_dataframe(self.df, text_columns=["title"])
        self.assertIsInstance(cleaned_df, pd.DataFrame, "clean_dataframe should return a DataFrame.")

    def test_normalize_timestamp(self):
        """
        Test the normalize_timestamp function.
        """
        normalized_df = normalize_timestamp(self.df, time_column="timestamp")
        self.assertEqual(normalized_df["timestamp"][0], "2024-12-06 10:00:00", "Timestamp normalization failed.")

if __name__ == "__main__":
    unittest.main()