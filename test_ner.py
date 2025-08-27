from utils.ner import extract_financial_entities

sample = "Tesla and Bitcoin are dropping fast. AAPL is looking strong."
entities = extract_financial_entities(sample)

print("Entities found:", entities)
