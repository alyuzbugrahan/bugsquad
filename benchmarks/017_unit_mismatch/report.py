from stats import average_seconds
from timing import elapsed_ms


def format_report(runs):
    """runs is a list of (start_ms, end_ms) timestamps. Return e.g. 'Average: 1.5 s'."""
    durations = [elapsed_ms(start, end) for start, end in runs]
    return f"Average: {average_seconds(durations):.1f} s"
