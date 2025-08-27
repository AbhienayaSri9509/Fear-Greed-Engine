# data_sources/news.py

import requests
from config.settings import NEWSAPI_KEY

def fetch_news(query, page_size=1):
    try:
        url = (
            f"https://newsapi.org/v2/everything?q={query}"
            f"&language=en&pageSize={page_size}&sortBy=publishedAt&apiKey={NEWSAPI_KEY}"
        )
        response = requests.get(url)
        data = response.json()

        articles = []
        for article in data.get("articles", []):
            articles.append({
                "title": article.get("title", ""),
                "description": article.get("description", ""),
                "source": article.get("source", {}).get("name", "")
            })

        return articles
    except Exception as e:
        print("❌ NewsAPI error:", e)
        return []
