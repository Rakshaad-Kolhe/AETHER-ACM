import numpy as np


def _rtn_rotation_matrix(satellite):
    """Build ECI basis matrix with columns [R_hat, T_hat, N_hat]."""
    r = np.asarray(satellite.get_position(), dtype=float)
    v = np.asarray(satellite.get_velocity(), dtype=float)

    r_norm = np.linalg.norm(r)
    if r_norm == 0.0:
        return np.eye(3, dtype=float)
    r_hat = r / r_norm

    n = np.cross(r, v)
    n_norm = np.linalg.norm(n)
    if n_norm == 0.0:
        return np.eye(3, dtype=float)
    n_hat = n / n_norm

    t_hat = np.cross(n_hat, r_hat)
    t_norm = np.linalg.norm(t_hat)
    if t_norm == 0.0:
        return np.eye(3, dtype=float)
    t_hat = t_hat / t_norm

    return np.column_stack((r_hat, t_hat, n_hat))


def eci_to_rtn(satellite, vector_eci):
    """Convert a vector from ECI frame into RTN frame."""
    rotation_matrix = _rtn_rotation_matrix(satellite)
    vec_eci = np.asarray(vector_eci, dtype=float)
    vector_rtn = rotation_matrix.T @ vec_eci
    return np.asarray(vector_rtn, dtype=float)


def rtn_to_eci(satellite, vector_rtn):
    """Convert a vector from RTN frame into ECI frame."""
    rotation_matrix = _rtn_rotation_matrix(satellite)
    vec_rtn = np.asarray(vector_rtn, dtype=float)
    vector_eci = rotation_matrix @ vec_rtn
    return np.asarray(vector_eci, dtype=float)
