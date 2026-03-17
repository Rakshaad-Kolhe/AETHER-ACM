from backend.domain.state_vector import StateVector


class Debris:
    """Passive orbital debris object with an identifier and orbital state."""

    def __init__(self, debris_id, state):
        """Initialize debris with a unique id and current state vector."""
        self.id = str(debris_id)
        self.state = state

    def get_position(self):
        """Return current position vector from state."""
        return self.state.position()

    def get_velocity(self):
        """Return current velocity vector from state."""
        return self.state.velocity()

    def update_state(self, new_state):
        """Replace the current orbital state vector."""
        self.state = new_state
