from backend.physics.propagators.rk4_integrator import rk4_step


def propagate_state(state_vector, dt):
    """Propagate a StateVector forward by dt seconds using RK4."""
    return rk4_step(state_vector, dt)


def propagate_object(obj, dt):
    """Propagate a Satellite or Debris object state and update it in place."""
    new_state = propagate_state(obj.state, dt)
    obj.update_state(new_state)
    return obj
