from timing import elapsed_ms


def is_timed_out(start_ms, now_ms, limit_ms):
    """Return True if more than limit_ms milliseconds have passed."""
    return elapsed_ms(start_ms, now_ms) > limit_ms
