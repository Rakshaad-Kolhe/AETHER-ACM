from fastapi import APIRouter

router = APIRouter()

# Shared in-memory state (must match simulation_endpoint)
from backend.api.simulation_endpoint import satellites, debris_objects
from backend.domain.state_vector import StateVector
from backend.domain.satellite import Satellite
from backend.domain.debris import Debris


@router.post("/api/telemetry")
def ingest_telemetry(payload: dict):
    """Ingest telemetry and update satellite/debris state."""
    objects = payload.get("objects", [])
    processed_count = 0

    for obj in objects:
        obj_id = obj["id"]
        obj_type = obj["type"]

        r = obj["r"]
        v = obj["v"]

        state = StateVector(
            r["x"], r["y"], r["z"],
            v["x"], v["y"], v["z"]
        )

        if obj_type == "SATELLITE":
            satellites.append(
                Satellite(
                    satellite_id=obj_id,
                    state=state,
                    fuel_mass=50.0,
                    dry_mass=500.0,
                )
            )
        else:
            debris_objects.append(
                Debris(
                    debris_id=obj_id,
                    state=state
                )
            )

        processed_count += 1

    return {
        "status": "ACK",
        "processed_count": processed_count,
        "active_cdm_warnings": 0
    }