import numpy as np


class StateVector:
    """Lightweight 3D position/velocity state vector for orbital simulation."""

    def __init__(self, x, y, z, vx, vy, vz):
        """Initialize from scalar position (km) and velocity (km/s) components."""
        self.r = np.array([x, y, z], dtype=float)
        self.v = np.array([vx, vy, vz], dtype=float)

    def position(self):
        """Return the position vector [x, y, z] in km."""
        return self.r

    def velocity(self):
        """Return the velocity vector [vx, vy, vz] in km/s."""
        return self.v

    def to_array(self):
        """Return the full 6D state [x, y, z, vx, vy, vz]."""
        return np.concatenate((self.r, self.v))

    def copy(self):
        """Return a deep copy of this state vector."""
        return StateVector(self.r[0], self.r[1], self.r[2], self.v[0], self.v[1], self.v[2])
