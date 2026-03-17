import numpy as np


def plan_graveyard_orbit(satellite):
    """Return an outward radial delta-v for end-of-life graveyard transfer."""
    if not satellite.is_fuel_critical():
        return None

    position = np.asarray(satellite.get_position(), dtype=float)
    norm = np.linalg.norm(position)
    if norm == 0.0:
        return np.zeros_like(position, dtype=float)

    direction = position / norm
    magnitude = 1.0
    delta_v = magnitude * direction
    return np.asarray(delta_v, dtype=float)
