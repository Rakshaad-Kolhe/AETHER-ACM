import numpy as np


def compute_time_of_closest_approach(r_rel, v_rel):
    """Compute time of closest approach from relative position and velocity."""
    v_rel_sq = np.dot(v_rel, v_rel)
    if v_rel_sq == 0.0:
        return 0.0
    return float(-np.dot(r_rel, v_rel) / v_rel_sq)
