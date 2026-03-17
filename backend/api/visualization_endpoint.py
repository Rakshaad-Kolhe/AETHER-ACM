from fastapi import APIRouter
from datetime import datetime
import numpy as np

from backend.api.simulation_endpoint import satellites, debris_objects
from backend.physics.constants import EARTH_RADIUS_EQUATORIAL

router = APIRouter()


def eci_to_lat_lon(position):
    """Convert ECI position to approximate lat/lon."""
    x, y, z = position
    r = np.linalg.norm(position)

    if r == 0:
        return 0.0, 0.0, 0.0

    lat = np.degrees(np.arcsin(z / r))
    lon = np.degrees(np.arctan2(y, x))
    alt = r - EARTH_RADIUS_EQUATORIAL

    return lat, lon, alt


@router.get("/api/visualization/snapshot")
def get_snapshot():
    """Return lightweight visualization snapshot."""

    sat_data = []
    for sat in satellites:
        lat, lon, alt = eci_to_lat_lon(sat.get_position())

        sat_data.append({
            "id": sat.id,
            "lat": lat,
            "lon": lon,
            "fuel_kg": sat.fuel_mass,
            "status": sat.status,
        })

    debris_data = []
    for d in debris_objects[:1000]:  # LIMIT for performance
        lat, lon, alt = eci_to_lat_lon(d.get_position())
        debris_data.append([d.id, lat, lon, alt])

    return {
        "timestamp": datetime.utcnow().isoformat(),
        "satellites": sat_data,
        "debris_cloud": debris_data,
    }