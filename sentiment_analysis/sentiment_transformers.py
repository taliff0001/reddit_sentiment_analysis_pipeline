# sentiment_analysis/sentiment_transformers.py

import pandas as pd
from transformers import pipeline
from typing import List

def analyze_sentiment_transformers(text: str) -> dict:
    """
    Analyzes sentiment of the input text using a transformer-based model.

    Args:
        text (str): The text to analyze.

    Returns:
        dict: Dictionary containing sentiment label and score.
    """
    sentiment_pipeline = pipeline('sentiment-analysis')
    result = sentiment_pipeline(text)[0]
    return result

def add_transformers_sentiment(df: pd.DataFrame, text_columns: List[str]) -> pd.DataFrame:
    """
    Adds transformer-based sentiment scores to specified text columns in a DataFrame.

    Args:
        df (pd.DataFrame): DataFrame containing text data.
        text_columns (List[str]): List of column names to analyze.

    Returns:
        pd.DataFrame: DataFrame with added sentiment scores.
    """
    for col in text_columns:
        df[f'{col}_transformer_sentiment'] = df[col].apply(analyze_sentiment_transformers)
    return df