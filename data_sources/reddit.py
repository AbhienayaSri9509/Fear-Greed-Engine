import praw
from config.settings import REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USER_AGENT

# ✅ Use environment variables from settings.py
reddit = praw.Reddit(
    client_id=REDDIT_CLIENT_ID,
    client_secret=REDDIT_CLIENT_SECRET,
    user_agent=REDDIT_USER_AGENT
)

def fetch_reddit_posts(subreddits, limit=1):
    try:
        posts = []
        for subreddit in subreddits:
            for submission in reddit.subreddit(subreddit).hot(limit=limit):
                post_text = submission.title + " " + submission.selftext
                posts.append(post_text.strip())
        return posts
    except Exception as e:
        print("❌ Reddit fetch error:", e)
        return []
