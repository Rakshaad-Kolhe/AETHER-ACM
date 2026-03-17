import numpy as np


def compute_relative_motion(obj1, obj2):
    """Compute relative position and velocity from obj1 to obj2."""
    r1 = np.asarray(obj1.get_position(), dtype=float)
    r2 = np.asarray(obj2.get_position(), dtype=float)
    v1 = np.asarray(obj1.get_velocity(), dtype=float)
    v2 = np.asarray(obj2.get_velocity(), dtype=float)

    return {
        "relative_position": r2 - r1,
        "relative_velocity": v2 - v1,
    }
