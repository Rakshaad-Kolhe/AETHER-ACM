# Earth parameters
MU_EARTH = 398600.4418  # Earth's gravitational parameter (km^3/s^2)
EARTH_RADIUS_EQUATORIAL = 6378.137  # Earth equatorial radius (km)
J2_EARTH = 1.08262668e-3  # Earth second zonal harmonic coefficient (dimensionless)

# Physics constants
G0 = 9.80665  # Standard gravity (m/s^2)

# Satellite propulsion constants
SPECIFIC_IMPULSE = 300.0  # Satellite thruster specific impulse (s)
SATELLITE_DRY_MASS = 500.0  # Satellite dry mass (kg)
INITIAL_FUEL_MASS = 50.0  # Initial onboard fuel mass (kg)
MAX_BURN_DELTA_V = 15.0  # Maximum delta-v per maneuver (m/s)
THRUSTER_COOLDOWN = 600.0  # Thruster cooldown time between burns (s)

# Simulation parameters
DEFAULT_INTEGRATION_TIMESTEP = 10.0  # Default numerical integration timestep (s)
CONJUNCTION_CRITICAL_DISTANCE = 0.1  # Critical conjunction distance threshold (km)
WARNING_DISTANCE_NEAR = 1.0  # Near warning distance threshold (km)
WARNING_DISTANCE_FAR = 5.0  # Far warning distance threshold (km)
