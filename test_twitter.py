import os
from dotenv import load_dotenv
import tweepy

load_dotenv()
bearer_token = os.getenv("TWITTER_BEARER_TOKEN")
print(f"Token loaded? {bearer_token is not None}")

client = tweepy.Client(bearer_token=bearer_token)

response = client.search_recent_tweets(query="#stockmarket", max_results=5)
for tweet in response.data:
    print(tweet.text)
