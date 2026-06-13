from transformers import pipeline

# Sentiment Analysis pipeline
classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
result = classifier("I love learning about Large Language Models!")
print(f"Sentiment: {result}")

# Tokenization example
from transformers import AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
tokens = tokenizer.tokenize("Subword tokenization is awesome.")
print(f"Tokens: {tokens}")
