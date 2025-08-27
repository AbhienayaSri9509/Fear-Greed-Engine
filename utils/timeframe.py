from datetime import datetime, timedelta

def get_timeframe(minutes=30):
    end = datetime.now()
    start = end - timedelta(minutes=minutes)
    return start, end
