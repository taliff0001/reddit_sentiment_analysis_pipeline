# data_transformation/normalize_fields.py

import pandas as pd
from datetime import datetime

def normalize_timestamp(df: pd.DataFrame, time_column: str, format: str = '%Y-%m-%d %H:%M:%S') -> pd.DataFrame:
    """
    Normalizes a timestamp column to a standard datetime format.

    Args:
        df (pd.DataFrame): DataFrame containing the timestamp column.
        time_column (str): Name of the timestamp column.
        format (str): Desired datetime format (default is '%Y-%m-%d %H:%M:%S').

    Returns:
        pd.DataFrame: DataFrame with normalized timestamp column.
    """
    df[time_column] = pd.to_datetime(df[time_column], errors='coerce', unit='s')
    df[time_column] = df[time_column].dt.strftime(format)
    return df

def normalize_usernames(df: pd.DataFrame, user_column: str) -> pd.DataFrame:
    """
    Normalizes usernames to lowercase.

    Args:
        df (pd.DataFrame): DataFrame containing the username column.
        user_column (str): Name of the username column.

    Returns:
        pd.DataFrame: DataFrame with normalized username column.
    """
    df[user_column] = df[user_column].str.lower()
    return df

def normalize_thread_ids(df: pd.DataFrame, thread_column: str) -> pd.DataFrame:
    """
    Normalizes thread identifiers to a consistent format.

    Args:
        df (pd.DataFrame): DataFrame containing the thread ID column.
        thread_column (str): Name of the thread ID column.

    Returns:
        pd.DataFrame: DataFrame with normalized thread ID column.
    """
    df[thread_column] = df[thread_column].astype(str).str.lower()
    return df