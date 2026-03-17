from backend.physics.propagators.orbital_propagator import propagate_object


class PhysicsScheduler:
    """Coordinate physics propagation for satellites and debris objects."""

    def __init__(self, satellites, debris_objects):
        """Initialize scheduler with in-memory simulation object lists."""
        self.satellites = list(satellites)
        self.debris_objects = list(debris_objects)

    def step(self, dt):
        """Propagate all tracked objects by one simulation timestep."""
        for satellite in self.satellites:
            propagate_object(satellite, dt)

        for debris in self.debris_objects:
            propagate_object(debris, dt)

        return self.satellites, self.debris_objects
