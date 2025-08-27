import numpy as np

def calculate_correlation(price_changes, sentiment_scores):
    if len(price_changes) != len(sentiment_scores) or len(price_changes) < 2:
        return 0
    return np.corrcoef(price_changes, sentiment_scores)[0,1]
