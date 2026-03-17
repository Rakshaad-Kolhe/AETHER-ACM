from backend.conjunction_detection.conjunction_engine import ConjunctionEngine
from backend.maneuver_planning.maneuver_engine import ManeuverEngine
from backend.physics.propagators.orbital_propagator import propagate_object


class StepExecutor:
    """Execute one simulation step across propagation, detection, and planning."""

    def __init__(self, conjunction_engine, maneuver_engine):
        """Initialize with subsystem engines used during each simulation step."""
        self.conjunction_engine = conjunction_engine
        self.maneuver_engine = maneuver_engine

    def step(self, satellites, debris_objects, spatial_index, dt):
        """Run one timestep and return conjunction events and planned maneuvers."""
        for sat in satellites:
            propagate_object(sat, dt)

        for debris in debris_objects:
            propagate_object(debris, dt)

        spatial_index.build(debris_objects)
        events = self.conjunction_engine.detect_conjunctions(satellites, spatial_index)
        maneuvers = self.maneuver_engine.plan_maneuvers(events, satellites)
        return events, maneuvers
