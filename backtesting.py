# backtesting.py

def backtest_signals(dates, sentiment_scores, prices, threshold_buy=0.2, threshold_sell=-0.2):
    """
    Simple backtest comparing sentiment signals against next-day price movement.
    
    Args:
        dates (list): List of datetime objects.
        sentiment_scores (list): Sentiment scores aligned with dates.
        prices (list): Closing prices aligned with dates.
        threshold_buy (float): Sentiment score above which to BUY.
        threshold_sell (float): Sentiment score below which to SELL.
    
    Returns:
        dict: Metrics including accuracy, total and correct signals.
    """
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
