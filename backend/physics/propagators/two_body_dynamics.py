import numpy as np

from backend.physics.constants import MU_EARTH


def compute_gravity_acceleration(position):
    """Compute Earth two-body gravitational acceleration for a position vector."""
    r_norm = np.linalg.norm(position)
    if r_norm == 0.0:
        return np.zeros(3, dtype=float)
    return -MU_EARTH * position / (r_norm ** 3)
