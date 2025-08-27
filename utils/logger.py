import datetime
import os

def log_results(results, index, signal):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)
    filename = os.path.join(log_dir, f"log_{timestamp}.txt")

    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"Fear & Greed Index: {index}\n")
        f.write(f"Suggested Trade Signal: {signal}\n\n")
        for r in results:
            f.write(f"Text: {r['text'][:100]}...\n")
            f.write(f"Sentiment: {r['sentiment']} (Confidence: {r['confidence']})\n\n")

    print(f"📝 Log saved to {filename}")
