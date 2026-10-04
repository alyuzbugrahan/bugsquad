from phone import normalize_phone


def display_phone(raw):
    """Return a human-friendly phone number like '0532 123 45 67'."""
    number = normalize_phone(raw)
    return f"{number[:4]} {number[4:7]} {number[7:9]} {number[9:]}"
