import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


def extract_compound_scores(sentiment_data):
    """
    Extracts compound scores from sentiment dictionaries.

    Parameters:
    sentiment_data (pd.DataFrame): DataFrame containing sentiment dictionaries

    Returns:
    pd.Series: Series of compound scores
    """
    return sentiment_data['title_sentiment'].apply(lambda x: x['compound'])


def categorize_sentiment(compound_score):
    """
    Converts compound score to categorical sentiment.

    Parameters:
    compound_score (float): The compound sentiment score

    Returns:
    str: Sentiment category
    """
    if compound_score >= 0.05:
        return 'Positive'
    elif compound_score <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'


def plot_sentiment_distribution(sentiment_data):
    """
    Creates multiple visualizations of sentiment distribution.

    Parameters:
    sentiment_data (pd.DataFrame): DataFrame containing sentiment data

    Returns:
    None
    """
    # Extract compound scores
    compound_scores = extract_compound_scores(sentiment_data)

    # Create categorical sentiments
    categorical_sentiments = compound_scores.apply(categorize_sentiment)

    # Create a figure with two subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

    # Plot 1: Histogram/Density plot of compound scores
    sns.histplot(data=compound_scores, bins=30, kde=True, ax=ax1)
    ax1.set_title('Distribution of Sentiment Compound Scores')
    ax1.set_xlabel('Compound Score')
    ax1.set_ylabel('Count')

    # Add vertical lines for sentiment thresholds
    ax1.axvline(x=-0.05, color='r', linestyle='--', alpha=0.5)
    ax1.axvline(x=0.05, color='r', linestyle='--', alpha=0.5)

    # Plot 2: Bar plot of categorical sentiments
    sns.countplot(x=categorical_sentiments, ax=ax2, palette='viridis')
    ax2.set_title('Distribution of Sentiment Categories')
    ax2.set_xlabel('Sentiment Category')
    ax2.set_ylabel('Count')

    # Add count labels on top of bars
    for i in ax2.containers:
        ax2.bar_label(i)

    plt.tight_layout()
    plt.show()


def plot_sentiment_over_time(sentiment_data, time_column='created_utc'):
    """
    Plots sentiment trends over time.

    Parameters:
    sentiment_data (pd.DataFrame): DataFrame containing sentiment and time data
    time_column (str): Name of the column containing time data

    Returns:
    None
    """
    # Convert timestamps and extract compound scores
    sentiment_data = sentiment_data.copy()
    sentiment_data[time_column] = pd.to_datetime(sentiment_data[time_column], unit='s')
    sentiment_data['compound_score'] = extract_compound_scores(sentiment_data)

    # Calculate daily average sentiment
    daily_sentiment = sentiment_data.set_index(time_column).resample('D')['compound_score'].agg(['mean', 'count'])

    # Create figure with two y-axes
    fig, ax1 = plt.subplots(figsize=(12, 6))
    ax2 = ax1.twinx()

    # Plot average sentiment
    line1 = ax1.plot(daily_sentiment.index, daily_sentiment['mean'],
                     color='blue', label='Average Sentiment')
    ax1.set_ylabel('Average Sentiment Score', color='blue')
    ax1.tick_params(axis='y', labelcolor='blue')

    # Plot post count
    line2 = ax2.plot(daily_sentiment.index, daily_sentiment['count'],
                     color='red', label='Post Count')
    ax2.set_ylabel('Number of Posts', color='red')
    ax2.tick_params(axis='y', labelcolor='red')

    # Add combined legend
    lines = line1 + line2
    labels = [l.get_label() for l in lines]
    ax1.legend(lines, labels, loc='upper left')

    plt.title('Sentiment Trends Over Time')
    plt.show()


# Example usage:
if __name__ == "__main__":
    # Load your data
    sentiment_df = pd.read_csv('sentiment_df.csv')

    # Create visualizations
    plot_sentiment_distribution(sentiment_df)
    plot_sentiment_over_time(sentiment_df)