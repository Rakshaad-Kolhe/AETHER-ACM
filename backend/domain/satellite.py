from domain.state_vector import StateVector


class Satellite:
    """Active spacecraft model used by simulation and planning modules."""

    def __init__(
        self,
        satellite_id,
        state,
        fuel_mass,
        dry_mass,
        status="NOMINAL",
        last_burn_time=None,
    ):
        """Initialize a satellite with state, mass properties, and status."""
        self.id = str(satellite_id)
        self.state = state
        self.fuel_mass = float(fuel_mass)
        self.initial_fuel_mass = float(fuel_mass)
        self.dry_mass = float(dry_mass)
        self.total_mass = self.dry_mass + self.fuel_mass
        self.status = status
        self.last_burn_time = last_burn_time

    def get_position(self):
        """Return current position vector from state."""
        return self.state.position()

    def get_velocity(self):
        """Return current velocity vector from state."""
        return self.state.velocity()

    def update_state(self, new_state):
        """Replace the current orbital state vector."""
        self.state = new_state

    def consume_fuel(self, delta_m):
        """Consume propellant mass and update total spacecraft mass."""
        self.fuel_mass = max(0.0, self.fuel_mass - float(delta_m))
        self.total_mass = self.dry_mass + self.fuel_mass

    def is_fuel_critical(self):
        """Return True when remaining fuel is below 5% of initial fuel."""
        return self.fuel_mass < 0.05 * self.initial_fuel_mass
