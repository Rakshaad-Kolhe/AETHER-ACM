import csv


_GROUND_STATIONS = []


class GroundStation:
    """Simple ground station model used for communication visibility checks."""

    def __init__(
        self,
        station_id,
        name,
        latitude,
        longitude,
        elevation,
        min_elevation_angle,
    ):
        """Initialize ground station metadata and geometric constraints."""
        self.id = str(station_id)
        self.name = str(name)
        self.latitude = float(latitude)
        self.longitude = float(longitude)
        self.elevation = float(elevation)
        self.min_elevation_angle = float(min_elevation_angle)


def load_ground_stations(file_path):
    """Load ground stations from CSV and cache them in memory."""
    global _GROUND_STATIONS

    stations = []
    with open(file_path, "r", newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            stations.append(
                GroundStation(
                    station_id=row["Station_ID"],
                    name=row["Station_Name"],
                    latitude=row["Latitude"],
                    longitude=row["Longitude"],
                    elevation=row["Elevation_m"],
                    min_elevation_angle=row["Min_Elevation_Angle_deg"],
                )
            )

    _GROUND_STATIONS = stations
    return stations


def get_all_stations():
    """Return cached ground stations loaded from CSV."""
    return _GROUND_STATIONS
