from pricing.currency import format_try


def receipt_line(total):
    return f"Your order total is {format_try(total)}."
