import numpy as np

from backend.physics.constants import G0, SPECIFIC_IMPULSE


def compute_fuel_consumption(current_mass, delta_v):
    """Compute propellant mass used for a burn using Tsiolkovsky's equation."""
    fuel_mass_used = current_mass * (
        1.0 - np.exp(-delta_v / (SPECIFIC_IMPULSE * G0))
    )
    return float(fuel_mass_used)
