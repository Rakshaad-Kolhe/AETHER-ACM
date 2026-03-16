import numpy as np


def vector_norm(v):
    """Return the magnitude of a 3D vector."""
    return float(np.linalg.norm(v))


def unit_vector(v):
    """Return the normalized unit vector of a 3D vector."""
    n = np.linalg.norm(v)
    if n == 0.0:
        return np.zeros(3, dtype=float)
    return v / n


def dot_product(a, b):
    """Return the dot product of two 3D vectors."""
    return float(np.dot(a, b))


def cross_product(a, b):
    """Return the cross product of two 3D vectors."""
    return np.cross(a, b)


def angle_between(a, b):
    """Return the angle in radians between two 3D vectors."""
    na = np.linalg.norm(a)
    nb = np.linalg.norm(b)
    if na == 0.0 or nb == 0.0:
        return 0.0
    cos_theta = np.dot(a, b) / (na * nb)
    cos_theta = np.clip(cos_theta, -1.0, 1.0)
    return float(np.arccos(cos_theta))
