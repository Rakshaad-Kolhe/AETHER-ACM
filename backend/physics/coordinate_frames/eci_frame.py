import numpy as np


class ECIFrame:
    """Simple container for position and velocity in ECI coordinates."""

    def __init__(self, position, velocity):
        """Initialize ECI frame vectors from position and velocity inputs."""
        self._position = np.asarray(position, dtype=float)
        self._velocity = np.asarray(velocity, dtype=float)

    def get_position(self):
        """Return ECI position vector."""
        return self._position

    def get_velocity(self):
        """Return ECI velocity vector."""
        return self._velocity

    def to_array(self):
        """Return concatenated [position, velocity] vector."""
        return np.concatenate((self._position, self._velocity))
