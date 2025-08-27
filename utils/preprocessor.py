from utils.ner import extract_financial_entities  # adjust import path as needed

def clean_and_filter(text):
    entities = extract_financial_entities(text)
    if not entities:
        return None  # Skip non-financial posts
    # continue cleaning...
    return text  # or cleaned version
