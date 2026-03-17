import numpy as np

from backend.physics.constants import MU_EARTH as MU


def compute_orbital_elements(state_vector):
    """Compute basic orbital elements from a position-velocity state vector."""
    r = np.asarray(state_vector.position(), dtype=float)
    v = np.asarray(state_vector.velocity(), dtype=float)

    r_norm = np.linalg.norm(r)
    v_norm = np.linalg.norm(v)

    if r_norm == 0.0:
        return {"semi_major_axis": float("inf"), "eccentricity": 0.0}

    h = np.cross(r, v)
    e_vec = (np.cross(v, h) / MU) - (r / r_norm)
    e = float(np.linalg.norm(e_vec))

    denom = (2.0 / r_norm) - ((v_norm * v_norm) / MU)
    if denom == 0.0:
        a = float("inf")
    else:
        a = float(1.0 / denom)

    return {
        "semi_major_axis": a,
        "eccentricity": e,
    }
