def generate_signal(fgi, buy_threshold=60, sell_threshold=40):
    if fgi >= buy_threshold:
        confidence = (fgi - buy_threshold) / (100 - buy_threshold)
        return "BUY", confidence
    elif fgi <= sell_threshold:
        confidence = (sell_threshold - fgi) / sell_threshold
        return "SELL", confidence
    else:
        return "HOLD", 1.0 - abs(fgi - 50)/50
