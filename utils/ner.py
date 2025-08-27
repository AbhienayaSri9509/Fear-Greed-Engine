# utils/ner.py

import spacy

nlp = spacy.load("en_core_web_sm")

# Add custom financial entities
financial_entities = ["AAPL", "TSLA", "BTC", "Bitcoin", "Ethereum", "NVIDIA", "GOOGL", "Meta"]
ruler = nlp.add_pipe("entity_ruler", before="ner", config={"overwrite_ents": True})
patterns = [{"label": "FIN_ENTITY", "pattern": ent} for ent in financial_entities]
ruler.add_patterns(patterns)

def extract_financial_entities(text):
    doc = nlp(text)
    return [ent.text for ent in doc.ents if ent.label_ == "FIN_ENTITY"]
