from phone import normalize_phone


def sms_recipient(raw):
    """Return the recipient address the SMS gateway expects."""
    return normalize_phone(raw)
