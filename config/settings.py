from dotenv import load_dotenv
import os

# Load variables from .env file
load_dotenv()

# Twitter API
TWITTER_BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")

# Reddit API
REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
REDDIT_CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")
REDDIT_USER_AGENT = os.getenv("REDDIT_USER_AGENT")

# NewsAPI
NEWSAPI_KEY = os.getenv("NEWSAPI_KEY")
