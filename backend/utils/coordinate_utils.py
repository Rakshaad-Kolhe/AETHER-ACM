import numpy as np


EARTH_RADIUS = 6371000.0


def eci_to_latlon(position):
    pos = np.asarray(position, dtype=float)
    x, y, z = pos
    r = np.linalg.norm(pos)
    if r == 0.0:
        lat = 0.0
        lon = float(np.degrees(np.arctan2(y, x)))
        alt = -EARTH_RADIUS
        return lat, lon, alt

    lat = float(np.degrees(np.arcsin(z / r)))
    lon = float(np.degrees(np.arctan2(y, x)))
    alt = float(r - EARTH_RADIUS)
    return lat, lon, alt


def eci_to_latlon_batch(positions):
    pos = np.asarray(positions, dtype=float)
    if pos.size == 0:
        return []

    x = pos[:, 0]
    y = pos[:, 1]
    z = pos[:, 2]
    r = np.linalg.norm(pos, axis=1)

    safe_r = np.where(r == 0.0, 1.0, r)
    lat = np.degrees(np.arcsin(z / safe_r))
    lon = np.degrees(np.arctan2(y, x))
    alt = r - EARTH_RADIUS

    zero_mask = r == 0.0
    if np.any(zero_mask):
        lat = lat.copy()
        lat[zero_mask] = 0.0

    return [
        {"lat": float(lat_i), "lon": float(lon_i), "alt": float(alt_i)}
        for lat_i, lon_i, alt_i in zip(lat, lon, alt)
    ]


def normalize_longitude(lon):
    normalized = (float(lon) + 180.0) % 360.0 - 180.0
    return float(normalized)


def latlon_to_cartesian(lat, lon, alt=0):
    lat_rad = np.radians(float(lat))
    lon_rad = np.radians(float(lon))
    radius = EARTH_RADIUS + float(alt)

    cos_lat = np.cos(lat_rad)
    x = radius * cos_lat * np.cos(lon_rad)
    y = radius * cos_lat * np.sin(lon_rad)
    z = radius * np.sin(lat_rad)

    return np.array([x, y, z], dtype=float)


def compute_distance_3d(p1, p2):
    a = np.asarray(p1, dtype=float)
    b = np.asarray(p2, dtype=float)
    return float(np.linalg.norm(a - b))
