from data_collection.fetch_reddit_data import authenticate_reddit, fetch_threads
from data_transformation.clean_data import clean_dataframe
from data_transformation.normalize_fields import normalize_timestamp
from sentiment_analysis.sentiment_vader import add_vader_sentiment
from data_storage.database_handler import save_dataframe_to_db
from visualization.visualize_sentiment import plot_sentiment_distribution, plot_sentiment_over_time
import pandas as pd

# Configuration
CONFIG = {
    "subreddits": ["worldnews", "politics"],
    "keywords": ["climate"],
    # "db_table": "general_sentiment"
}

def main():
    # Step 1: Authenticate Reddit API
    reddit = authenticate_reddit()
    # threads = fetch_threads(reddit, "worldnews", limit=5)
    # print(threads)

    # Convert threads to a DataFrame
    # threads_df = pd.DataFrame(threads)

    # Print the DataFrame
    # print("Threads DataFrame:")
    # print(threads_df.head())

    # Step 2: Collect threads
    threads = []
    for subreddit in CONFIG["subreddits"]:
        threads += fetch_threads(reddit, subreddit, keywords=None, limit=5)

    if not threads:
        print("No threads were fetched. Check subreddit names, keywords, or API limits.")
        return
    print(threads)
    # Step 3: Convert to DataFrame
    threads_df = pd.DataFrame(threads)
    print("Threads DataFrame:")
    print(threads_df.head())

    # Step 4: Clean and normalize data
    cleaned_df = clean_dataframe(threads_df, text_columns=["title", "selftext"])
    normalized_df = normalize_timestamp(cleaned_df, time_column="created_utc")
    normalized_df.to_csv("normalized_df.csv")
    print("Normalized DataFrame:", normalized_df.head())

    #  #### WORKS TO HERE ####


    # # Step 5: Perform sentiment analysis
    # sentiment_df = add_vader_sentiment(normalized_df, text_columns=["title", "selftext"])
    #
    # # Step 6: Visualize results
    # plot_sentiment_distribution(sentiment_df)
    # plot_sentiment_over_time(sentiment_df, time_column="created_utc")

if __name__ == "__main__":
    main()