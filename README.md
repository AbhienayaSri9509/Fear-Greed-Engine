**Project Overview**
The Fear & Greed Sentiment Engine is an AI-powered system designed to analyze market sentiment from multiple data sources including Twitter, Reddit, News, and financial market data. By aggregating sentiment scores and correlating them with real-time price movements, the system generates actionable buy/sell signals to assist investors and traders.

**Key Features**:

1.Multi-source data ingestion (social media, news, finance)

2.Sentiment analysis using NLP techniques

3.Weighted sentiment aggregation with time decay

4.Signal generation based on sentiment-price correlation

5.Backtesting to evaluate model accuracy

6.Performance reporting with CSV and visualization

**Setup Instructions**

cd fear-greed-engine
**Create and activate a Python virtual environment**:


python -m venv venv
source venv/bin/activate     # On Windows: venv\Scripts\activate
**Install dependencies**:


pip install -r requirements.txt
**Configure API keys**:

Create a .env file in the root directory and add your API keys for Twitter, Reddit, NewsAPI, etc.

env

TWITTER_BEARER_TOKEN=your_twitter_token_here
REDDIT_CLIENT_ID=your_reddit_client_id
REDDIT_CLIENT_SECRET=your_reddit_client_secret
NEWSAPI_KEY=your_newsapi_key

**Download any required models or NLTK data**:

python -m nltk.downloader all

Usage Guide
**Run the main program to execute the full pipeline**:

python main.py

**Individual Phase Execution**
Phase 1: Data Ingestion

Fetch Twitter data: python data_sources/twitter.py

Fetch Reddit data: python data_sources/reddit.py

Fetch News data: python data_sources/news.py

Fetch Financial data: python data_sources/finance.py

Phase 2: Sentiment Analysis

Run sentiment analyzers on fetched data (sentiment/analyzer.py)

Phase 3: Sentiment Aggregation

Use aggregation/sentiment_aggregator.py to combine scores

Phase 4: Signal Generation

Calculate Fear & Greed index and generate buy/sell signals (signals/signal_generator.py)

Phase 5: Backtesting and Evaluation

Backtest using historical data and generate performance reports (backtesting/evaluator.py)

**Folder Structure**

fear-greed-engine/
│
├── aggregation/                # Sentiment aggregation modules
│   └── sentiment_aggregator.py
│
├── backtesting/                # Backtesting & evaluation modules
│   └── evaluator.py
│
├── data_sources/               # Data ingestion scripts
│   ├── twitter.py
│   ├── reddit.py
│   ├── news.py
│   └── finance.py
│
├── sentiment/                  # Sentiment analysis modules
│   ├── analyzer.py
│   └── cleaner.py
│
├── signals/                   # Signal generation modules
│   └── signal_generator.py
│
├── output/                    # Generated reports, CSVs, and plots
│
├── tests/                     # Unit and integration tests
│
├── main.py                   # Main entry point script
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation

**How to Run Each Phase/Module**
Full pipeline: python main.py

Run unit tests: pytest tests/

Generate performance report: Run the backtesting evaluator module or call generate_performance_report() function from backtesting/evaluator.py

**Architecture Diagram Description**
You can create a diagram with the following flow:

✅Data Sources (Input Layer)

Twitter API (tweets)

Reddit API (posts & comments)

NewsAPI (news articles)

Financial APIs (price, volume, market data)

✅Data Ingestion Layer

Modules that fetch and preprocess raw data from each source

✅Sentiment Analysis Layer

NLP models analyze raw text to produce sentiment scores for each source

✅Sentiment Aggregation Engine

Aggregates sentiment scores from all sources per symbol

Applies source weights and time decay

✅Signal Generation Engine

Correlates aggregated sentiment with price movements

Computes Fear & Greed index

Generates buy/sell/hold signals with confidence scores

✅Backtesting & Evaluation

Downloads historical data

Compares signals vs actual market outcomes

Generates performance reports (CSV, plots)

✅Output Reports & Visualization

Stores reports and plots in output/

Provides insights for trading decisions

# Fear-Greed-Engine-GoQuant-
# Fear-Greed-Engine-GoQuant-
