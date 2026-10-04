from parsing import parse_price


def format_report(prices):
    """Return a line like 'Total: 12.50 TL' for price strings such as '10,50'."""
    total = sum(parse_price(p) for p in prices)
    return f"Total: {total:.2f} TL"
