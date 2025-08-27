import datetime
import yfinance as yf

import random
import os
import pandas as pd
import matplotlib.pyplot as plt

def backtest_signals(dates, sentiment_scores, prices, threshold_buy=0.2, threshold_sell=-0.2):
    correct = 0
    total = 0

    for i in range(len(sentiment_scores) - 1):
        signal = None
        if sentiment_scores[i] >= threshold_buy:
            signal = "BUY"
        elif sentiment_scores[i] <= threshold_sell:
            signal = "SELL"
        else:
            signal = "HOLD"

        price_change = prices[i + 1] - prices[i]
        price_direction = "UP" if price_change > 0 else "DOWN"

        if (signal == "BUY" and price_direction == "UP") or (signal == "SELL" and price_direction == "DOWN"):
            correct += 1
        total += 1

    accuracy = correct / total if total else 0
    return {"accuracy": accuracy, "total_signals": total, "correct_signals": correct}

def download_historical_prices(symbol, period="1mo", interval="1d"):
    ticker = yf.Ticker(symbol)
    hist = ticker.history(period=period, interval=interval)
    return hist

def generate_performance_report(dates, sentiment_scores, prices, output_dir="output", csv_filename="performance_report.csv", plot_filename="performance_plot.png"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    df = pd.DataFrame({
        "date": dates,
        "sentiment_score": sentiment_scores,
        "price": prices,
    })
    csv_path = os.path.join(output_dir, csv_filename)
    df.to_csv(csv_path, index=False)
    print(f"Performance report CSV saved to {csv_path}")

    plt.figure(figsize=(12,6))
    plt.plot(dates, prices, label="Price")
    plt.plot(dates, sentiment_scores, label="Sentiment Score")
    plt.xlabel("Date")
    plt.ylabel("Value")
    plt.title("Price and Sentiment Score Over Time")
    plt.legend()
    plt.grid(True)

    plot_path = os.path.join(output_dir, plot_filename)
    plt.savefig(plot_path)
    plt.show()
    print(f"Performance plot saved to {plot_path}")

if __name__ == "__main__":
    symbol = "AAPL"

    hist = download_historical_prices(symbol, period="1mo", interval="1d")
    dates = hist.index.to_pydatetime().tolist()
    prices = hist['Close'].tolist()

    # Replace this with actual sentiment data
    sentiment_scores = [random.uniform(-1, 1) for _ in range(len(dates))]

    results = backtest_signals(dates, sentiment_scores, prices)
    print(f"Backtest Accuracy: {results['accuracy']*100:.2f}% ({results['correct_signals']} correct out of {results['total_signals']})")

    generate_performance_report(dates, sentiment_scores, prices)
