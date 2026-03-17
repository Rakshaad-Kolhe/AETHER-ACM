import numpy as np

from backend.physics.constants import MU_EARTH as MU


def mean_motion(semi_major_axis):
    """Compute mean motion for a Keplerian orbit."""
    a = float(semi_major_axis)
    n = np.sqrt(MU / (a**3))
    return float(n)


def propagate_mean_anomaly(M0, n, dt):
    """Propagate mean anomaly forward by elapsed time."""
    M = float(M0) + float(n) * float(dt)
    return float(M)


def mean_to_eccentric_anomaly(M, e):
    """Approximate eccentric anomaly from mean anomaly for small eccentricity."""
    return float(M)
