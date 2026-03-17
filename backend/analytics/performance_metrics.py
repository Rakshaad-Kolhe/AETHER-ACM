class PerformanceMetrics:
    """Track lightweight in-memory constellation performance counters."""

    def __init__(self):
        """Initialize all performance counters to zero."""
        self.total_maneuvers_executed = 0
        self.total_fuel_consumed = 0.0
        self.total_conjunctions_detected = 0
        self.total_collisions_avoided = 0
        self.total_uptime_seconds = 0.0

    def record_conjunction(self, count):
        """Add detected conjunction count."""
        self.total_conjunctions_detected += int(count)

    def record_maneuver(self, fuel_used):
        """Record one executed maneuver and its fuel usage."""
        self.total_maneuvers_executed += 1
        self.total_fuel_consumed += float(fuel_used)

    def record_uptime(self, seconds):
        """Add elapsed uptime in seconds."""
        self.total_uptime_seconds += float(seconds)

    def record_collision_avoided(self):
        """Increment avoided-collision counter."""
        self.total_collisions_avoided += 1

    def get_summary(self):
        """Return a summary snapshot of current metrics."""
        return {
            "maneuvers": self.total_maneuvers_executed,
            "fuel_consumed": self.total_fuel_consumed,
            "conjunctions": self.total_conjunctions_detected,
            "collisions_avoided": self.total_collisions_avoided,
            "uptime": self.total_uptime_seconds,
        }
