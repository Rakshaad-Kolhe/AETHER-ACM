class Maneuver:
    """Represents a maneuver command applied to a satellite."""

    def __init__(self, satellite_id, delta_v_vector, burn_type="EVASION"):
        """
        Initialize a maneuver.

        Args:
            satellite_id (str): Target satellite ID
            delta_v_vector (array-like): Δv vector (km/s)
            burn_type (str): Type of maneuver (EVASION, RECOVERY, etc.)
        """
        self.satellite_id = str(satellite_id)
        self.delta_v_vector = delta_v_vector
        self.burn_type = burn_type

    def to_dict(self):
        """Convert maneuver to dictionary (useful for logging/API)."""
        return {
            "satellite_id": self.satellite_id,
            "delta_v_vector": list(self.delta_v_vector),
            "burn_type": self.burn_type,
        }