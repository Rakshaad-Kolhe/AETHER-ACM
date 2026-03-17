import numpy as np


def compute_plane_change_delta_v(satellite, magnitude):
    """Compute an out-of-plane delta-v using the orbital plane normal."""
    r = np.asarray(satellite.get_position(), dtype=float)
    v = np.asarray(satellite.get_velocity(), dtype=float)
    n = np.cross(r, v)
    n_norm = np.linalg.norm(n)

    if n_norm == 0.0:
        return np.zeros_like(r, dtype=float)

    n_hat = n / n_norm
    delta_v = float(magnitude) * n_hat
    return np.asarray(delta_v, dtype=float)
