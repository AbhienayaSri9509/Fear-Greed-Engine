def calculate_index(sentiment_results):
    score = 0
    for result in sentiment_results:
        if result['sentiment'] == 'POSITIVE':
            score += 1
        elif result['sentiment'] == 'NEGATIVE':
            score -= 1
    return score
