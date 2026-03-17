import numpy as np


class SlotAssignment:
    """Track nominal orbital slot positions for satellites."""

    def __init__(self, satellites):
        """Initialize nominal slot map from current satellite positions."""
        self._nominal_positions = {
            sat.id: np.asarray(sat.get_position(), dtype=float).copy() for sat in satellites
        }

    def get_nominal_position(self, satellite_id):
        """Return stored nominal position for the given satellite ID."""
        return self._nominal_positions.get(str(satellite_id))

    def is_within_slot(self, satellite, tolerance_km=10):
        """Return True when satellite is within tolerance of nominal slot."""
        nominal = self.get_nominal_position(satellite.id)
        if nominal is None:
            return False

        current = np.asarray(satellite.get_position(), dtype=float)
        distance = np.linalg.norm(current - nominal)
        return bool(distance <= float(tolerance_km))
