import numpy as np

from backend.physics.constants import EARTH_RADIUS_EQUATORIAL


def generate_snapshot(satellites, debris_objects, timestamp):
    """Generate a compact visualization snapshot for satellites and debris."""
    satellite_payload = []
    for sat in satellites:
        r = np.asarray(sat.get_position(), dtype=float)
        r_norm = np.linalg.norm(r)
        if r_norm == 0.0:
            lat = 0.0
            lon = 0.0
        else:
            lat = float(np.degrees(np.arcsin(r[2] / r_norm)))
            lon = float(np.degrees(np.arctan2(r[1], r[0])))

        satellite_payload.append(
            {
                "id": sat.id,
                "lat": lat,
                "lon": lon,
                "fuel_kg": float(sat.fuel_mass),
                "status": sat.status,
            }
        )

    debris_cloud = []
    for obj in debris_objects:
        r = np.asarray(obj.get_position(), dtype=float)
        r_norm = np.linalg.norm(r)
        if r_norm == 0.0:
            lat = 0.0
            lon = 0.0
            altitude = -float(EARTH_RADIUS_EQUATORIAL)
        else:
            lat = np.degrees(np.arcsin(r[2] / r_norm))
            lon = np.degrees(np.arctan2(r[1], r[0]))
            altitude = float(r_norm - EARTH_RADIUS_EQUATORIAL)
        debris_cloud.append([obj.id, lat, lon, altitude])

    return {
        "timestamp": timestamp,
        "satellites": satellite_payload,
        "debris_cloud": debris_cloud,
    }
