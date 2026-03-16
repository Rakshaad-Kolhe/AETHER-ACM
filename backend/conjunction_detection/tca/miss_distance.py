import numpy as np


def compute_miss_distance(r_rel, v_rel, tca):
    """Compute miss distance at time of closest approach."""
    separation = r_rel + v_rel * tca
    return float(np.linalg.norm(separation))
