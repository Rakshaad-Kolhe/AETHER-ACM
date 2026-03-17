import numpy as np


def compute_phasing_delta_v(satellite, magnitude):
    """Compute a tangential phasing maneuver delta-v vector."""
    v = np.asarray(satellite.get_velocity(), dtype=float)
    v_norm = np.linalg.norm(v)
    if v_norm == 0.0:
        return np.zeros_like(v, dtype=float)

    v_hat = v / v_norm
    delta_v = magnitude * v_hat
    return np.asarray(delta_v, dtype=float)
