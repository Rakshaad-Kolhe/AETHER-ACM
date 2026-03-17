from backend.communication.line_of_sight import line_of_sight


def get_visible_stations(satellite, ground_stations):
    """Return ground stations that currently have line of sight to the satellite."""
    return [station for station in ground_stations if line_of_sight(satellite, station)]


def is_in_blackout_zone(satellite, ground_stations):
    """Return True when no ground station can see the satellite."""
    return len(get_visible_stations(satellite, ground_stations)) == 0
