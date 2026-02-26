import re

def tokenize(sentence):
    # Convert to lowercase
    sentence = sentence.lower()
    # Replace all non-alphanumeric characters with spaces
    sentence = re.sub(r"[^a-z0-9]", " ", sentence)
    # Split into words and remove empty strings
    tokens = [word for word in sentence.split() if word]
    return tokens
