import numpy as np


def compute_hohmann_transfer_delta_v(satellite, scale_factor):
    """Compute a simplified tangential delta-v for Hohmann-like transfer."""
    velocity = np.asarray(satellite.get_velocity(), dtype=float)
    speed = np.linalg.norm(velocity)

    if speed == 0.0:
        return np.zeros_like(velocity, dtype=float)

    v_hat = velocity / speed
    delta_v = float(scale_factor) * v_hat
    return np.asarray(delta_v, dtype=float)
