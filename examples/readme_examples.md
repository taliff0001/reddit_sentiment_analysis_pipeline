**Configuration (config):** Each script defines a configuration dictionary specifying subreddits, keywords, database connection details, storage paths, and sentiment analysis parameters tailored to the topic.

### Main Function (main): Orchestrates the data pipeline by:

1. Initializing the Reddit data collector with specified subreddits and keywords.
2. Collecting raw data from Reddit.
3. Cleaning the collected data to remove noise.
4. Normalizing fields (e.g., timestamps, usernames) for consistency.
5. Performing sentiment analysis using the specified method (VADER or Transformers).
6. Saving the processed data to a database.
7. Visualizing sentiment trends over time.

**Conditional Execution:** The `if '__name__' == '__main__':` block ensures that the `main() `function runs only when the script is executed directly, not when imported as a module.

**Note:** Ensure that the imported modules are correctly implemented and available in your project's directory structure.

__These scripts provide a comprehensive example of how to set up and execute a Reddit data analysis pipeline for specific topics, utilizing modular components for data collection, transformation, sentiment analysis, storage, and visualization.__
