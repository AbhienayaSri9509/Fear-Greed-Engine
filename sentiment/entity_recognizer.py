import re

# Simple regex-based recognizer
def extract_entities(text):
    tickers = re.findall(r"\$[A-Z]{1,5}", text)  # e.g., $AAPL, $TSLA
    hashtags = re.findall(r"#\w+", text)         # e.g., #bitcoin
    keywords = [word for word in text.split() if word.upper() in ["BTC", "ETH", "AAPL", "TSLA"]]
    
    return {
        "tickers": list(set(tickers)),
        "hashtags": list(set(hashtags)),
        "keywords": list(set(keywords))
    }
