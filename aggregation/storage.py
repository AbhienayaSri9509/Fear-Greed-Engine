import json

def save_to_file(data, filename="sentiment_data.json"):
    with open(filename, "w") as f:
        json.dump(data, f)

def load_from_file(filename="sentiment_data.json"):
    with open(filename) as f:
        return json.load(f)
