def find_first_negative(numbers):
    """Return the first negative number in the list, or None if there is none."""
    for n in numbers:
        if n < 0:
            return n
        else:
            return None
    return None
