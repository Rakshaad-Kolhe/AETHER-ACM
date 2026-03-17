from fastapi import APIRouter

from backend.conjunction_detection.conjunction_engine import ConjunctionEngine
from backend.conjunction_detection.spatial_index.kd_tree import DebrisSpatialIndex
from backend.maneuver_planning.maneuver_engine import ManeuverEngine
from backend.simulation_engine.step_executor import StepExecutor

router = APIRouter()

# In-memory shared simulation state.
satellites = []
debris_objects = []
spatial_index = DebrisSpatialIndex()
step_executor = StepExecutor(
    conjunction_engine=ConjunctionEngine(search_radius_km=10.0),
    maneuver_engine=ManeuverEngine(),
)


@router.post("/api/simulate/step")
def simulate_step(payload: dict):
    """Advance simulation by one timestep and return summary metrics."""
    step_seconds = float(payload.get("step_seconds", 0.0))
    events, maneuvers = step_executor.step(
        satellites=satellites,
        debris_objects=debris_objects,
        spatial_index=spatial_index,
        dt=step_seconds,
    )
    return {
        "status": "STEP_COMPLETE",
        "collisions_detected": len(events),
        "maneuvers_executed": len(maneuvers),
    }
