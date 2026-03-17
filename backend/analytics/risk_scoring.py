def compute_risk_score(conjunction_event):
    """Compute a simple conjunction risk score from miss distance and TCA."""
    miss_distance = float(conjunction_event.miss_distance)
    tca = float(conjunction_event.tca)

    if miss_distance < 0.1:
        base = 1.0
    elif miss_distance < 1.0:
        base = 0.7
    elif miss_distance < 5.0:
        base = 0.4
    else:
        base = 0.1

    if tca < 600:
        multiplier = 1.5
    elif tca < 3600:
        multiplier = 1.2
    else:
        multiplier = 1.0

    risk = base * multiplier
    return float(risk)


def rank_conjunctions(events):
    """Return conjunction events sorted by descending risk score."""
    return sorted(events, key=compute_risk_score, reverse=True)
