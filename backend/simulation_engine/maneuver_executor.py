import numpy as np

from backend.domain.satellite import Satellite


def execute_maneuvers(satellites, maneuvers):
    """Apply maneuver delta-v vectors to satellite velocities."""
    satellite_map = {sat.id: sat for sat in satellites}

    for maneuver in maneuvers:
        satellite = satellite_map.get(str(maneuver.satellite_id))
        if satellite is None:
            continue

        current_velocity = np.asarray(satellite.get_velocity(), dtype=float)
        delta_v = np.asarray(maneuver.delta_v_vector, dtype=float)
        new_velocity = current_velocity + delta_v

        satellite.state.v = new_velocity
        satellite.update_state(satellite.state)
        satellite.status = "MANEUVERING"
