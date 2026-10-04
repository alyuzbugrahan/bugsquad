def parse_price(text):
    """Parse a Turkish-formatted price such as '1.234,50' into a float (1234.5)."""
    return float(text.replace(",", "."))
