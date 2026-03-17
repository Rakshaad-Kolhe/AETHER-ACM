from backend.maneuver_planning.fuel.rocket_equation import compute_fuel_consumption


def apply_fuel_consumption(satellite, delta_v):
    """Compute and apply fuel usage for a planned burn."""
    fuel_used = compute_fuel_consumption(satellite.total_mass, delta_v)
    satellite.consume_fuel(fuel_used)
    return fuel_used
