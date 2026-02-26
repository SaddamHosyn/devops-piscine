import re
from collections import Counter

def tokenizer_counter(text: str) -> dict:
    # Convert to lowercase
    text = text.lower()
    # Replace non-alphanumeric characters with spaces
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    # Split into words
    words = text.split()
    # Count occurrences
    counts = Counter(words)
    # Sort dictionary alphabetically by key
    return dict(sorted(counts.items()))
