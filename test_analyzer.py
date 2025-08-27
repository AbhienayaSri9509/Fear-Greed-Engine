from sentiment.analyzer import analyze_sentiment

texts = [
    "The market is looking great today!",
    "Investors are scared about inflation.",
    "I feel positive about tech stocks."
]

results = analyze_sentiment(texts)

for text, res in zip(texts, results):
    print(f"Text: {text}")
    print(f"Sentiment: {res['label']} (Confidence: {res['score']:.2f})\n")
