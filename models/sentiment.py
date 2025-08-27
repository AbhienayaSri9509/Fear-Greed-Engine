# models/sentiment.py

from textblob import TextBlob
import re

def clean_text(text):
    """
    Normalize text by removing URLs, mentions, hashtags, and special characters.
    """
    text = re.sub(r"http\S+|www\S+|https\S+", '', text, flags=re.MULTILINE)
    text = re.sub(r"[@#\$]\w+", '', text)  # Remove @mentions, #hashtags, $tickers
    text = re.sub(r"[^A-Za-z\s]", '', text)  # Remove punctuation
    return text.lower().strip()

def extract_entities(text):
    """
    Extract financial entities (tickers) prefixed by $ symbol.
    """
    tickers = re.findall(r"\$[A-Z]{2,5}", text.upper())
    return list(set(tickers))

def analyze_sentiment(text):
    """
    Perform simple sentiment analysis using TextBlob.
    Returns: 'positive', 'neutral', or 'negative'
    """
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0.2:
        return "positive"
    elif polarity < -0.2:
        return "negative"
    else:
        return "neutral"

def run_sentiment_pipeline(raw_text):
    """
    Run full sentiment pipeline: clean → analyze → extract entities.
    Returns: dict with cleaned text, sentiment, entities
    """
    cleaned = clean_text(raw_text)
    sentiment = analyze_sentiment(cleaned)
    entities = extract_entities(raw_text)

    return {
        "cleaned": cleaned,
        "sentiment": sentiment,
        "entities": entities
    }
