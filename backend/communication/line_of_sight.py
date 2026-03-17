import numpy as np


EARTH_RADIUS_KM = 6371.0


def line_of_sight(satellite, ground_station):
    """Return True if satellite is above station horizon plus min elevation."""
    lat_rad = np.deg2rad(float(ground_station.latitude))
    lon_rad = np.deg2rad(float(ground_station.longitude))
    min_elevation = float(ground_station.min_elevation_angle)

    station_position = EARTH_RADIUS_KM * np.array(
        [
            np.cos(lat_rad) * np.cos(lon_rad),
            np.cos(lat_rad) * np.sin(lon_rad),
            np.sin(lat_rad),
        ],
        dtype=float,
    )
    station_normal = station_position / np.linalg.norm(station_position)

    satellite_position = np.asarray(satellite.get_position(), dtype=float)
    station_to_sat = satellite_position - station_position
    norm_station_to_sat = np.linalg.norm(station_to_sat)
    if norm_station_to_sat == 0.0:
        return False

    station_to_sat_hat = station_to_sat / norm_station_to_sat
    cos_angle = np.clip(np.dot(station_normal, station_to_sat_hat), -1.0, 1.0)
    angle_deg = float(np.rad2deg(np.arccos(cos_angle)))
    return angle_deg < (90.0 - min_elevation)
