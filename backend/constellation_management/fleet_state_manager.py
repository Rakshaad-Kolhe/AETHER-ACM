class FleetStateManager:
    """Manage the in-memory state of a satellite fleet."""

    def __init__(self, satellites):
        """Initialize manager with satellites indexed by ID."""
        self._satellites = {sat.id: sat for sat in satellites}

    def get_satellite(self, satellite_id):
        """Return a satellite by ID, or None if missing."""
        return self._satellites.get(str(satellite_id))

    def get_all_satellites(self):
        """Return all satellites currently tracked."""
        return list(self._satellites.values())

    def update_satellite_state(self, satellite_id, new_state):
        """Update a satellite state vector by ID when present."""
        satellite = self.get_satellite(satellite_id)
        if satellite is not None:
            satellite.update_state(new_state)

    def get_nominal_satellites(self):
        """Return satellites with nominal operating status."""
        return [sat for sat in self._satellites.values() if sat.status == "NOMINAL"]

    def get_maneuvering_satellites(self):
        """Return satellites currently marked as maneuvering."""
        return [sat for sat in self._satellites.values() if sat.status == "MANEUVERING"]
