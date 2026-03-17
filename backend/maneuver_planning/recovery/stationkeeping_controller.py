import numpy as np


def compute_stationkeeping_delta_v(satellite, nominal_position):
    """Compute a small delta-v to steer satellite back toward its nominal slot."""
    current_position = np.asarray(satellite.get_position(), dtype=float)
    target_position = np.asarray(nominal_position, dtype=float)
    delta_r = target_position - current_position
    delta_r_norm = np.linalg.norm(delta_r)

    if delta_r_norm == 0.0:
        return np.zeros_like(current_position, dtype=float)

    direction = delta_r / delta_r_norm
    magnitude = 0.5
    delta_v = magnitude * direction
    return np.asarray(delta_v, dtype=float)
