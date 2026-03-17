import numpy as np


def compute_radial_delta_v(satellite, magnitude):
    """Compute a radial delta-v along the satellite position direction."""
    r = np.asarray(satellite.get_position(), dtype=float)
    r_norm = np.linalg.norm(r)

    if r_norm == 0.0:
        return np.zeros_like(r, dtype=float)

    r_hat = r / r_norm
    delta_v = float(magnitude) * r_hat
    return np.asarray(delta_v, dtype=float)
