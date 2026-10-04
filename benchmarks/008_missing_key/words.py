def word_count(text):
    """Count how many times each word appears in the text (case-insensitive)."""
    counts = {}
    for word in text.lower().split():
        counts[word] += 1
    return counts
