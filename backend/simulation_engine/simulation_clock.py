class SimulationClock:
    """Track and update simulation time in seconds."""

    def __init__(self, initial_time=0.0):
        """Initialize simulation clock in seconds."""
        self._time = float(initial_time)

    def get_time(self):
        """Return current simulation time in seconds."""
        return self._time

    def advance(self, dt):
        """Advance simulation time by dt seconds."""
        self._time += float(dt)
        return self._time

    def set_time(self, new_time):
        """Set simulation time."""
        self._time = float(new_time)