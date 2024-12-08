# data_transformation/clean_data.py

import re
import pandas as pd
from typing import List
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Ensure necessary NLTK resources are downloaded
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

def clean_text(text: str) -> str:
    """
    Cleans the input text by performing the following operations:
    1. Converts text to lowercase.
    2. Removes URLs.
    3. Removes user mentions and hashtags.
    4. Removes special characters and numbers.
    5. Tokenizes text into words.
    6. Removes stopwords.
    7. Lemmatizes words to their base form.
    8. Joins tokens back into a single string.

    Args:
        text (str): The raw text to be cleaned.

    Returns:
        str: The cleaned text.
    """
    # Convert text to lowercase
    text = text.lower()
    # Remove URLs
    text = re.sub(r'http\S+|www\S+', '', text)
    # Remove user mentions (@username) and hashtags (#hashtag)
    text = re.sub(r'@\w+|#\w+', '', text)
    # Remove special characters and numbers
    text = re.sub(r'[^a-z\s]', '', text)
    # Tokenize text into words
    words = word_tokenize(text)
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words]
    # Lemmatize words to their base form
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word) for word in words]
    # Join tokens back into a single string
    cleaned_text = ' '.join(words)
    return cleaned_text

def clean_dataframe(df: pd.DataFrame, text_columns: List[str]) -> pd.DataFrame:
    """
    Cleans specified text columns in a DataFrame using the clean_text function.

    Args:
        df (pd.DataFrame): The DataFrame containing text data.
        text_columns (List[str]): List of column names to be cleaned.

    Returns:
        pd.DataFrame: DataFrame with cleaned text columns.
    """
    for col in text_columns:
        df[col] = df[col].apply(clean_text)
    return df