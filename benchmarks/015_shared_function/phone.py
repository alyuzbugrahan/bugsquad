def normalize_phone(raw):
    """Return a Turkish phone number in E.164 format, e.g. '+905321234567'."""
    digits = "".join(c for c in raw if c.isdigit())
    if digits.startswith("0"):
        digits = "90" + digits[1:]
    return "+" + digits
