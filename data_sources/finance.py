# data_sources/finance.py

import yfinance as yf

def fetch_financial_data(symbol="BTC-USD"):
    ticker = yf.Ticker(symbol)
    hist = ticker.history(period="1d")
    return hist[["Open", "Close", "Volume"]]

def download_historical_prices(symbol="BTC-USD", period="3mo", interval="1d"):
    """
    Downloads historical price data for a symbol.
    
    Args:
        symbol (str): Ticker symbol like "BTC-USD", "AAPL", etc.
        period (str): e.g., "1y", "3mo", "6mo"
        interval (str): e.g., "1d", "1h"
    
    Returns:
        DataFrame with price history
    """
    ticker = yf.Ticker(symbol)
    hist = ticker.history(period=period, interval=interval)
    return hist
 