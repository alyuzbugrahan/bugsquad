def format_try(amount):
    """Format an amount as Turkish lira, e.g. 1234.5 -> '1.234,50 TL'."""
    whole, frac = f"{amount:,.2f}".split(".")
    return whole.replace(",", ".") + "," + frac + " TL"
