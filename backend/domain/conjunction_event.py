class ConjunctionEvent:
    """Represents a predicted close approach between a satellite and debris."""

    def __init__(self, satellite_id, debris_id, tca, miss_distance):
        """
        Initialize a conjunction event.

        Args:
            satellite_id (str): ID of the satellite
            debris_id (str): ID of the debris object
            tca (float): Time of closest approach (seconds)
            miss_distance (float): Distance at closest approach (km)
        """
        self.satellite_id = str(satellite_id)
        self.debris_id = str(debris_id)
        self.tca = float(tca)
        self.miss_distance = float(miss_distance)

    def to_dict(self):
        """Convert event to dictionary (useful for logging or API)."""
        return {
            "satellite_id": self.satellite_id,
            "debris_id": self.debris_id,
            "tca": self.tca,
            "miss_distance": self.miss_distance,
        }