from sentiment.cleaner import clean_text
from sentiment.analyzer import analyze_sentiment
from sentiment.entity_recognizer import extract_entities

def test_pipeline():
    text = "Huge surge in $AAPL after earnings! #stocks #apple #bullish"
    cleaned = clean_text(text)
    sentiment = analyze_sentiment(cleaned)
    entities = extract_entities(text)

    print("Cleaned:", cleaned)
    print("Sentiment:", sentiment)
    print("Entities:", entities)

if __name__ == "__main__":
    test_pipeline()
