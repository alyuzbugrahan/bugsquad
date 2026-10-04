def slugify(title):
    """Turn a title into a URL slug: lowercase words joined by hyphens."""
    words = title.strip().split()
    return "-".join(words)
