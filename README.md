# Reddit-Powered Trader

## Overview

Reddit-Powered Trader is an automated trading system that leverages sentiment analysis from r/wallstreetbets to make stock trading decisions. It scrapes "due-diligence" tagged posts, evaluates sentiment using an LLM API, and executes trades via the Polygon Stock API. The project also includes a database for tracking trades and a web app for monitoring portfolio performance.

## Features

- **Reddit Scraper**: Collects "due-diligence" posts from r/wallstreetbets.
- **Sentiment Analysis**: Evaluates post sentiment using an LLM API.
- **Trader Script**: Uses sentiment and post engagement to execute trades via Polygon API.
- **Database**: Stores trade history, positions, and tracked Reddit posts.
- **Web App**: Displays portfolio performance and trade history.
- **(Future) Discord Bot**: Allows manual trade execution and Reddit tracking via commands.

## Tech Stack

- **Python**: Primary language.
- **SQLite / Snowflake**: Database for storing trades and post data.
- **yfinance**: Fetches stock price data.
- **Reddit API (PRAW / Pushshift.io)**: Retrieves posts from r/wallstreetbets.
- **Flask**: For the web app interface.
- **Discord.py** (Future): Discord bot for manual trade execution.

## Project Structure

```
reddit-powered-trader/
│── data/                # Stores database files and backups
│── scripts/             # Contains helper scripts
│   ├── reddit_scraper.py      # Fetches Reddit posts
│   ├── sentiment_analysis.py  # Evaluates sentiment using LLM
│   ├── trader.py        # Core script for executing trades
│── tests/               # Contains tests and test data
│   ├── data/            # Sample data for testing use
│   │   ├── test_trades.json   # Sample trade data
│   ├── test_trader.py   # Functional/Unit tests for trader.py
│── web/                 # Web app for tracking portfolio
│── .env.example         # Environment variables (API keys)
│── README.md            # Project documentation
│── requirements.txt     # Dependencies
```

## Getting Started

### Prerequisites

- Python 3.9+
- Reddit API credentials (for scraping, not needed now)
- Polygon API key (for stock data, potentially not used)
- Snowflake credentials (if using Snowflake, not needed now)

### Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/danlee-31/another-reddit-trader.git
   cd another-reddit-trader
   ```

2. Create and activate a virtual environment:

   ```sh
   python -m venv venv
   source venv/bin/activate  # Mac/Linux
   venv\Scripts\activate     # Windows
   ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
   <!--
4. Set up your environment variables:
   - Copy `.env.example` to `.env`
   - Add your Reddit API and Polygon API credentials
     -->

<!--
### Running the Scripts
- **Scrape Reddit posts**
    ```sh
    python scripts/reddit_scraper.py
    ```
- **Analyze sentiment**
    ```sh
    python scripts/sentiment_analysis.py
    ```
- **Run the trader script**
    ```sh
    python scripts/trader.py
    ```
-->
