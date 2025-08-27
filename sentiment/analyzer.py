from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import torch.nn.functional as F

# Load FinBERT
model_name = "yiyanghkust/finbert-tone"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

labels = ["Positive", "Negative", "Neutral"]

def analyze_sentiment(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True)
    with torch.no_grad():
        outputs = model(**inputs)
        probs = F.softmax(outputs.logits, dim=-1)
        confidence, prediction = torch.max(probs, dim=1)
        return {
            "label": labels[prediction.item()],
            "confidence": round(confidence.item(), 3),
            "probabilities": {labels[i]: round(p.item(), 3) for i, p in enumerate(probs[0])}
        }
