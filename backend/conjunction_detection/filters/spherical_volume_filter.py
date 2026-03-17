import numpy as np


def filter_within_radius(satellite_position, debris_objects, radius_km):
    """Return debris objects within a spherical radius of the satellite position."""
    sat_pos = np.asarray(satellite_position, dtype=float)
    radius = float(radius_km)
    filtered = []

    for debris in debris_objects:
        debris_pos = np.asarray(debris.get_position(), dtype=float)
        distance = np.linalg.norm(sat_pos - debris_pos)
        if distance <= radius:
            filtered.append(debris)

    return filtered
