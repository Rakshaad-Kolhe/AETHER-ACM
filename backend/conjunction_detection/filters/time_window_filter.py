def filter_time_window(events, max_time_seconds):
    """Return conjunction events whose TCA is within the given time window."""
    threshold = float(max_time_seconds)
    return [event for event in events if event.tca <= threshold]
