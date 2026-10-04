from convert import c_to_f


def max_fahrenheit(readings):
    """Return the highest of the Celsius readings, converted to Fahrenheit."""
    return c_to_f(min(readings))
