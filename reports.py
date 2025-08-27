# reports.py
import pandas as pd
import matplotlib.pyplot as plt

def generate_performance_report(dates, sentiment_scores, prices, filename="performance_report.csv"):
    """
    Saves sentiment and price data to CSV and plots a graph.
    
    Args:
        dates (list): Dates of data points.
        sentiment_scores (list): Sentiment scores.
        prices (list): Closing prices.
        filename (str): CSV file output name.
    """
    df = pd.DataFrame({
        "date": dates,
        "sentiment_score": sentiment_scores,
        "price": prices,
    })
    df.to_csv(filename, index=False)
    
    plt.figure(figsize=(12,6))
    plt.plot(dates, prices, label="Price")
    plt.plot(dates, sentiment_scores, label="Sentiment Score")
    plt.xlabel("Date")
    plt.ylabel("Value")
    plt.title("Price and Sentiment Score Over Time")
    plt.legend()
    plt.show()
