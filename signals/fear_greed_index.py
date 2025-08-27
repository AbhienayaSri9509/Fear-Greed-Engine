def calculate_fear_greed_index(correlation, aggregated_sentiment):
    corr_score = (correlation + 1) * 25  
    sentiment_score = (aggregated_sentiment + 1) * 25
    fgi = 0.6 * sentiment_score + 0.4 * corr_score
    return max(0, min(100, fgi))
