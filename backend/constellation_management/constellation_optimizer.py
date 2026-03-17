from backend.analytics.risk_scoring import compute_risk_score, rank_conjunctions


class ConstellationOptimizer:
    """Apply simple global prioritization for conjunction response planning."""

    def prioritize_maneuvers(self, conjunction_events):
        """Return conjunction events sorted from highest to lowest risk."""
        return rank_conjunctions(conjunction_events)

    def filter_low_priority(self, events, threshold):
        """Remove events whose risk score is below the given threshold."""
        min_risk = float(threshold)
        return [event for event in events if compute_risk_score(event) >= min_risk]

    def limit_maneuvers_per_cycle(self, events, max_count):
        """Return only the top-N events to cap per-cycle maneuver volume."""
        return list(events)[: int(max_count)]
