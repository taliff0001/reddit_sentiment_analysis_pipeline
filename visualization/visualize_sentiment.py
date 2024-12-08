import pandas as pd  # Import pandas for data manipulation
import matplotlib.pyplot as plt  # Import matplotlib for plotting
import seaborn as sns  # Import seaborn for enhanced visualizations

def plot_sentiment_distribution(sentiment_data):
    """
    Plots the distribution of sentiment categories.

    Parameters:
    sentiment_data (pd.DataFrame): DataFrame containing a 'sentiment' column with sentiment labels.

    Returns:
    None
    """
    # Set the aesthetic style of the plots
    sns.set(style="whitegrid")

    # Create a count plot of sentiment categories
    plt.figure(figsize=(10, 6))  # Set the figure size
    sns.countplot(x='sentiment', data=sentiment_data, palette='viridis')  # Create count plot
    plt.title('Sentiment Distribution')  # Set plot title
    plt.xlabel('Sentiment')  # Set x-axis label
    plt.ylabel('Count')  # Set y-axis label
    plt.show()  # Display the plot

def plot_sentiment_over_time(sentiment_data, time_column='timestamp'):
    """
    Plots sentiment trends over time.

    Parameters:
    sentiment_data (pd.DataFrame): DataFrame containing 'sentiment' and time columns.
    time_column (str): Name of the column containing time data.

    Returns:
    None
    """
    # Ensure the time column is in datetime format
    sentiment_data[time_column] = pd.to_datetime(sentiment_data[time_column])

    # Set the time column as the index
    sentiment_data.set_index(time_column, inplace=True)

    # Resample data by day and count sentiment occurrences
    sentiment_counts = sentiment_data.resample('D').sentiment.value_counts().unstack().fillna(0)

    # Plot the sentiment trends over time
    plt.figure(figsize=(12, 8))  # Set the figure size
    sentiment_counts.plot(ax=plt.gca())  # Plot the data on the current axes
    plt.title('Sentiment Over Time')  # Set plot title
    plt.xlabel('Date')  # Set x-axis label
    plt.ylabel('Count')  # Set y-axis label
    plt.legend(title='Sentiment')  # Add legend with title
    plt.show()  # Display the plot