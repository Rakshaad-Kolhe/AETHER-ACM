import numpy as np

from backend.analytics.risk_scoring import compute_risk_score, rank_conjunctions
from backend.domain.maneuver import Maneuver
from backend.maneuver_planning.avoidance.phasing_maneuver import (
    compute_phasing_delta_v,
)
from backend.maneuver_planning.fuel.propellant_tracker import apply_fuel_consumption


class ManeuverEngine:
    """Plan simple evasion maneuvers from conjunction events."""

    def plan_maneuvers(self, conjunction_events, satellites):
        """Generate one evasion maneuver per satellite for this cycle."""
        satellite_map = {sat.id: sat for sat in satellites}
        maneuvers = []
        planned_satellites = set()
        # Processing high-risk events first improves safety and fuel efficiency.
        sorted_events = rank_conjunctions(conjunction_events)

        for event in sorted_events:
            if compute_risk_score(event) < 0.2:
                continue

            satellite_id = str(event.satellite_id)
            if satellite_id in planned_satellites:
                continue

            satellite = satellite_map.get(satellite_id)
            if satellite is None:
                continue

            if event.miss_distance < 0.1:
                magnitude = 5.0
            elif event.miss_distance < 1.0:
                magnitude = 2.0
            else:
                magnitude = 0.5

            delta_v_vector = compute_phasing_delta_v(satellite, magnitude)
            delta_v_mag = float(np.linalg.norm(delta_v_vector))
            apply_fuel_consumption(satellite, delta_v_mag)

            maneuvers.append(
                Maneuver(
                    satellite_id=satellite_id,
                    delta_v_vector=delta_v_vector,
                    burn_type="EVASION",
                )
            )
            planned_satellites.add(satellite_id)

        return maneuvers
