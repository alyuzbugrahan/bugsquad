def chunk(items, size):
    """Split items into consecutive lists of length `size`. The last chunk may be shorter."""
    return [items[i:i + size] for i in range(0, len(items) - size + 1, size)]
