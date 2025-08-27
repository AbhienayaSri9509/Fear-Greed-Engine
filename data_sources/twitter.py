# data_sources/twitter.py

import tweepy
from config.settings import TWITTER_BEARER_TOKEN

client = tweepy.Client(bearer_token=TWITTER_BEARER_TOKEN)

def fetch_recent_tweets(query="crypto", max_results=10):
    try:
        if max_results < 10:
            max_results = 10  # Twitter API requires 10-100

        tweets = client.search_recent_tweets(
            query=query,
            max_results=max_results,
            tweet_fields=["created_at", "author_id", "lang"]
        )

        if tweets.data:
            return tweets.data
        else:
            return []

    except Exception as e:
        print("❌ Twitter fetch error:", e)
        return []
