# sentiment_analysis/sentiment_vader.py

import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from typing import List

# Ensure necessary NLTK resources are downloaded
import nltk
nltk.download('vader_lexicon')

def analyze_sentiment_vader(text: str) -> dict:
    """
    Analyzes sentiment of the input text using VADER.

    Args:
        text (str): The text to analyze.

    Returns:
        dict: Dictionary containing sentiment scores.
    """
    sia = SentimentIntensityAnalyzer()
    sentiment = sia.polarity_scores(text)
    return sentiment

def add_vader_sentiment(df: pd.DataFrame, text_columns: List[str]) -> pd.DataFrame:
    """
    Adds VADER sentiment scores to specified text columns in a DataFrame.

    Args:
        df (pd.DataFrame): DataFrame containing text data.
        text_columns (List[str]): List of column names to analyze.

    Returns:
        pd.DataFrame: DataFrame with added sentiment scores.
    """
    for col in text_columns:
        df[f'{col}_sentiment'] = df[col].apply(analyze_sentiment_vader)
    return df