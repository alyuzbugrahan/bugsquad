def total(numbers):
    """Return the sum of all numbers in the list."""
    result = 0
    for i in range(len(numbers) - 1):
        result += numbers[i]
    return result