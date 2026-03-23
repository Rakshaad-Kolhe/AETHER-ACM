import numpy as np

from backend.physics.propagators.orbital_propagator import propagate_state


def generate_ground_track(satellite, duration_seconds, step_seconds):
    """Generate future ground-track latitude/longitude points for a satellite."""
    points = []
    state = satellite.state.copy()
    duration = float(duration_seconds)
    step = float(step_seconds)
    t = 0.0

    while t < duration:
        state = propagate_state(state, step)
        r = np.asarray(state.position(), dtype=float)
        r_norm = np.linalg.norm(r)
        if r_norm == 0.0:
            lat = 0.0
            lon = 0.0
        else:
            z_over_r = np.clip(r[2] / r_norm, -1.0, 1.0)
            lat = float(np.degrees(np.arcsin(z_over_r)))
            lon = float(np.degrees(np.arctan2(r[1], r[0])))

        points.append({"lat": lat, "lon": lon})
        t += step

    return points
