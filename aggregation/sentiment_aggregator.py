from collections import defaultdict
import time

class SentimentAggregator:
    def __init__(self, decay_half_life=300):  # 5 minutes by default
        self.data = defaultdict(list)  # symbol -> list of (timestamp, score, source)
        self.decay_half_life = decay_half_life

    def add_sentiment(self, symbol, score, source):
        timestamp = time.time()
        self.data[symbol].append((timestamp, score, source))

    def get_aggregated_score(self, symbol):
        now = time.time()
        weighted_sum = 0.0
        weight_total = 0.0

        source_weights = {
            "twitter": 0.4,
            "reddit": 0.3,
            "news": 0.2,
            "finance": 0.1,
        }

        for timestamp, score, source in self.data[symbol]:
            age = now - timestamp
            decay = 0.5 ** (age / self.decay_half_life)
            weight = source_weights.get(source, 0.1) * decay
            weighted_sum += score * weight
            weight_total += weight

        if weight_total == 0:
            return 0
        return weighted_sum / weight_total
