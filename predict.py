# from transformers import BertTokenizer, BertForSequenceClassification
# import torch

# tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
# model = BertForSequenceClassification.from_pretrained("bert-base-uncased", num_labels=2)

# def predict_sentiment(text):
#     inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
#     with torch.no_grad():
#         outputs = model(**inputs)
#     return torch.argmax(outputs.logits).item()


from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Use a smaller model already fine-tuned for sentiment
tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")
model = AutoModelForSequenceClassification.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")

def predict_sentiment(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
    return torch.argmax(outputs.logits).item()  # 0 = Negative, 1 = Positive
