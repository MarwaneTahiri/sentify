from transformers import pipeline

analyzer = pipeline("sentiment-analysis")

print(analyzer("I love this!"))