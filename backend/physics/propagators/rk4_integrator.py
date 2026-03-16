import numpy as np

from backend.domain.state_vector import StateVector
from backend.physics.propagators.j2_perturbation import compute_j2_acceleration
from backend.physics.propagators.two_body_dynamics import compute_gravity_acceleration


def rk4_step(state_vector, dt):
    """Advance a StateVector by one timestep using RK4 with gravity and J2."""
    r0 = np.array(state_vector.position(), dtype=float)
    v0 = np.array(state_vector.velocity(), dtype=float)

    def total_acceleration(r):
        return compute_gravity_acceleration(r) + compute_j2_acceleration(r)

    k1_r = v0
    k1_v = total_acceleration(r0)

    k2_r = v0 + 0.5 * dt * k1_v
    k2_v = total_acceleration(r0 + 0.5 * dt * k1_r)

    k3_r = v0 + 0.5 * dt * k2_v
    k3_v = total_acceleration(r0 + 0.5 * dt * k2_r)

    k4_r = v0 + dt * k3_v
    k4_v = total_acceleration(r0 + dt * k3_r)

    r_new = r0 + (dt / 6.0) * (k1_r + 2.0 * k2_r + 2.0 * k3_r + k4_r)
    v_new = v0 + (dt / 6.0) * (k1_v + 2.0 * k2_v + 2.0 * k3_v + k4_v)

    return StateVector(r_new[0], r_new[1], r_new[2], v_new[0], v_new[1], v_new[2])
