# Reddit Sentiment Analysis Pipeline

## Overview

This project is a modular, scalable pipeline designed to analyze sentiment in Reddit threads and comments. The pipeline integrates data collection, transformation, sentiment analysis, storage, and visualization.

Key features include:

- Real-time or batch data collection from Reddit using PRAW.
- Configurable cleaning and normalization of Reddit posts and comments.
- Sentiment analysis using VADER or Transformer-based models.
- Data storage in PostgreSQL and JSON files.
- Visualization of sentiment trends over time.

---

## Project Structure
```
reddit_streaming_pipeline/
├── data_collection/
│   ├── fetch_reddit_data.py
│   ├── stream_comments.py
│   ├── stream_threads.py
├── data_transformation/
│   ├── clean_data.py
│   ├── normalize_fields.py
├── sentiment_analysis/
│   ├── sentiment_vader.py
│   ├── sentiment_transformers.py
├── data_storage/
│   ├── database_handler.py
│   ├── save_to_json.py
│   ├── config.yaml
├── visualization/
│   ├── visualize_sentiment.py
├── config/
│   ├── reddit_credentials.json
│   ├── pipeline_config.json
├── examples/
│   ├── analyze_american_politics.py
│   ├── analyze_climate_change.py
├── tests/
│   ├── test_data_collection.py
│   ├── test_data_transformation.py
│   ├── test_sentiment_analysis.py
├── README.md
├── requirements.txt
└── main.py
```

## Setup

### Prerequisites
1. Python 3.8 or higher.
2. PostgreSQL installed and running (optional for database storage).
3. Necessary libraries installed (see `requirements.txt`).

---

### Installation
1. Clone this repository:
    ```bash
    git clone https://github.com/your-username/reddit-sentiment-pipeline.git
    cd reddit-sentiment-pipeline
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Configure Reddit API credentials:
    - Add your credentials to `config/reddit_credentials.json`.

4. Configure the pipeline settings:
    - Update `config/pipeline_config.json` to customize subreddits, keywords, storage paths, and sentiment analysis options.

---

## Usage

### Run the Example Scripts
- Analyze American politics sentiment:
    ```bash
    python examples/analyze_american_politics.py
    ```
- Analyze climate change sentiment:
    ```bash
    python examples/analyze_climate_change.py
    ```

### Run Tests
- Validate functionality with unit tests:
    ```bash
    python -m unittest discover tests/
    ```

---

## Main Pipeline
Run the main pipeline for general use:
```bash
python main.py
```

---

## Features

### Data Collection

* **Scripts**: `fetch_reddit_data.py`, `stream_threads.py`, `stream_comments.py`.
* Collects Reddit posts and comments based on subreddits and keywords.

### Data Transformation

* **Scripts**: `clean_data.py`, `normalize_fields.py`.
* Cleans text, normalizes timestamps, usernames, and thread identifiers.

### Sentiment Analysis

* **Scripts**: `sentiment_vader.py`, `sentiment_transformers.py`.
* Supports VADER for lightweight sentiment analysis.
* Uses Transformers for advanced, context-aware sentiment detection.

### Data Storage

* **Scripts**: `database_handler.py`, `save_to_json.py`.
* Stores results in PostgreSQL or local JSON files.

### Visualization

* **Scripts**: `visualize_sentiment.py`.
* Visualizes sentiment distribution and trends over time.

---

## Contributors

* **Tommy Aliff** - Lead Developer, Guru

---

## License

This project is licensed under the MIT License. See `LICENSE` for details.

---
![]()