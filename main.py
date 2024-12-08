from data_collection.fetch_reddit_data import authenticate_reddit, fetch_threads
from data_transformation.clean_data import clean_dataframe
from data_transformation.normalize_fields import normalize_timestamp
from sentiment_analysis.sentiment_vader import add_vader_sentiment
from data_storage.database_handler import save_dataframe_to_db
from visualization.visualize_sentiment import plot_sentiment_distribution, plot_sentiment_over_time
import pandas as pd

# Configuration
CONFIG = {
    "subreddits": ["worldnews", "news"],
    "keywords": ["climate", "politics"],
    "db_table": "general_sentiment"
}

def main():
    # Step 1: Authenticate Reddit API
    reddit = authenticate_reddit()

    # Step 2: Collect threads
    threads = []
    for subreddit in CONFIG["subreddits"]:
        threads += fetch_threads(reddit, subreddit, keywords=CONFIG["keywords"], limit=50)

    # Step 3: Convert to DataFrame
    threads_df = pd.DataFrame(threads)

    # Step 4: Clean and normalize data
    cleaned_df = clean_dataframe(threads_df, text_columns=["title", "selftext"])
    normalized_df = normalize_timestamp(cleaned_df, time_column="created_utc")

    # Step 5: Perform sentiment analysis
    sentiment_df = add_vader_sentiment(normalized_df, text_columns=["title", "selftext"])

    # Step 6: Save to database
    save_dataframe_to_db(sentiment_df, table_name=CONFIG["db_table"], engine="your_db_engine_here")

    # Step 7: Visualize results
    plot_sentiment_distribution(sentiment_df)
    plot_sentiment_over_time(sentiment_df, time_column="created_utc")

if __name__ == "__main__":
    main()