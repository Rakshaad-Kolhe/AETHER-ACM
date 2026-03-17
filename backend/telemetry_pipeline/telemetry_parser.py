from backend.domain.debris import Debris
from backend.domain.satellite import Satellite
from backend.domain.state_vector import StateVector
from backend.physics.constants import INITIAL_FUEL_MASS, SATELLITE_DRY_MASS


def parse_telemetry(payload):
    """Parse telemetry payload into satellite and debris domain objects."""
    satellites = []
    debris = []

    objects = payload.get("objects", payload)
    if isinstance(objects, dict):
        objects = objects.get("objects", [])

    for obj in objects:
        object_id = obj.get("id")
        object_type = str(obj.get("type", "")).upper()

        r = obj.get("r", {})
        v = obj.get("v", {})
        state = StateVector(
            r.get("x", 0.0),
            r.get("y", 0.0),
            r.get("z", 0.0),
            v.get("vx", 0.0),
            v.get("vy", 0.0),
            v.get("vz", 0.0),
        )

        if object_type == "DEBRIS":
            debris.append(Debris(debris_id=object_id, state=state))
        elif object_type == "SATELLITE":
            satellites.append(
                Satellite(
                    satellite_id=object_id,
                    state=state,
                    fuel_mass=INITIAL_FUEL_MASS,
                    dry_mass=SATELLITE_DRY_MASS,
                )
            )

    return {"satellites": satellites, "debris": debris}
