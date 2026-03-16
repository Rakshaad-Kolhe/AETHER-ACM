import numpy as np

from backend.physics.constants import EARTH_RADIUS_EQUATORIAL, J2_EARTH, MU_EARTH


def compute_j2_acceleration(position):
    """Compute J2 perturbation acceleration for an Earth-centered position vector."""
    x, y, z = position
    r2 = np.dot(position, position)
    if r2 == 0.0:
        return np.zeros(3, dtype=float)

    r = np.sqrt(r2)
    z2_over_r2 = (z * z) / r2
    factor = 1.5 * J2_EARTH * MU_EARTH * (EARTH_RADIUS_EQUATORIAL ** 2) / (r ** 5)

    common_xy = 5.0 * z2_over_r2 - 1.0
    common_z = 5.0 * z2_over_r2 - 3.0

    return factor * np.array(
        [x * common_xy, y * common_xy, z * common_z],
        dtype=float,
    )
