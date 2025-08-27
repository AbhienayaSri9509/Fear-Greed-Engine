
# Fear & Greed Sentiment Engine

An AI-powered market sentiment system that analyzes Twitter, Reddit, News, and financial data to generate actionable buy/sell signals.
Helps investors & traders make data-driven decisions by correlating sentiment with price movements.

**✨ Key Features**

✅ Multi-source data ingestion (Twitter, Reddit, News, Finance APIs)

✅ NLP-powered sentiment analysis

✅ Aggregated sentiment scoring with weighting & time decay

✅ Buy/Sell/Hold signal generation from sentiment-price correlation

✅ Backtesting & performance evaluation

✅ Auto-generated reports (CSV, plots & charts)

⚙️ Setup Instructions
**Clone the repo**
git clone https://github.com/AbhienayaSri9509/fear-greed-engine.git
cd fear-greed-engine

**Create & activate a virtual environment**
python -m venv venv

**On Windows**
venv\Scripts\activate

**Install dependencies**
pip install -r requirements.txt

**API Configuration**

Create a .env file in the project root and add your API keys:

TWITTER_BEARER_TOKEN=AAAAAAAAAAAAAAAAAAAAAEFO3AEAAAAAMZQYgxUfjWlxgIz%2BOe%2Bc79k9S7Y%3DctPEx6p7bDRCQi8oWBThflBKfehdyKV9VEmx1ESgKCAKkv4Vwq

REDDIT_CLIENT_ID=QCBm5Evs5sW4XkBjv6CGoA

REDDIT_CLIENT_SECRET=CC5SrV1H_Ex590sdQU2jdVeMUZYogQ

NEWSAPI_KEY=165fc81156d74945a34431ffd567463a

📦 Download Required Models
python -m nltk.downloader all

🚀 Usage Guide

👉 Run the full pipeline:

python main.py


**👉 Run individual phases**:

Phase 1: Data Ingestion

python data_sources/twitter.py
python data_sources/reddit.py
python data_sources/news.py
python data_sources/finance.py


Phase 2: Sentiment Analysis

python sentiment/analyzer.py


Phase 3: Sentiment Aggregation

python aggregation/sentiment_aggregator.py


Phase 4: Signal Generation

python signals/signal_generator.py


Phase 5: Backtesting & Evaluation

python backtesting/evaluator.py


**👉 Run tests:**

pytest tests/

📂 Folder Structure
fear-greed-engine/
│
├── aggregation/                # Sentiment aggregation modules
│   └── sentiment_aggregator.py
│
├── backtesting/                # Backtesting & evaluation
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
├── signals/                    # Signal generation modules
│   └── signal_generator.py
│
├── output/                     # Reports, CSVs, plots
├── tests/                      # Unit & integration tests
│
├── main.py                     # Main pipeline script
├── requirements.txt            # Dependencies
└── README.md                   # Documentation

**🏗️ Architecture Overview**

flowchart TD
    A[Twitter API] --> B[Data Ingestion]
    A2[Reddit API] --> B
    A3[NewsAPI] --> B
    A4[Financial APIs] --> B

    B --> C[Sentiment Analysis]
    C --> D[Sentiment Aggregator]
    D --> E[Signal Generation Engine]
    E --> F[Backtesting & Evaluation]
    F --> G[Reports & Visualization]

**Outputs**

📈 CSV performance reports

📊 Sentiment & signal visualization plots

✅ Buy/Sell/Hold signal recommendations

**DRIVE LINK**
https://drive.google.com/drive/folders/1wVs9Gp2p_spDyNBR08qoCyK4ywv500cO?usp=drive_link
