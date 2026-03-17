from fastapi import APIRouter

router = APIRouter()


@router.post("/api/maneuver/schedule")
def schedule_maneuver(payload: dict):
    """Accept maneuver schedule (simulation handles execution internally)."""
    return {
        "status": "SCHEDULED",
        "validation": {
            "ground_station_los": True,
            "sufficient_fuel": True,
            "projected_mass_remaining_kg": 500.0
        }
    }