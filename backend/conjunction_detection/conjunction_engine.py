import numpy as np

from backend.conjunction_detection.spatial_index.kd_tree import DebrisSpatialIndex
from backend.conjunction_detection.tca.closest_approach import (
    compute_time_of_closest_approach,
)
from backend.conjunction_detection.tca.miss_distance import compute_miss_distance
from backend.domain.conjunction_event import ConjunctionEvent


class ConjunctionEngine:
    """Detect potential conjunctions between satellites and nearby debris."""

    def __init__(self, search_radius_km):
        """Initialize with conjunction search radius in kilometers."""
        self.search_radius_km = float(search_radius_km)

    def detect_conjunctions(self, satellites, spatial_index):
        """Return conjunction events for satellites against indexed debris."""
        events = []
        for satellite in satellites:
            sat_pos = satellite.get_position()
            sat_vel = satellite.get_velocity()
            candidates = spatial_index.query(sat_pos, self.search_radius_km)

            for debris in candidates:
                r_rel = np.asarray(debris.get_position(), dtype=float) - np.asarray(
                    sat_pos, dtype=float
                )
                v_rel = np.asarray(debris.get_velocity(), dtype=float) - np.asarray(
                    sat_vel, dtype=float
                )

                tca = compute_time_of_closest_approach(r_rel, v_rel)
                if tca < 0.0:
                    continue

                miss_distance = compute_miss_distance(r_rel, v_rel, tca)
                if miss_distance < self.search_radius_km:
                    events.append(
                        ConjunctionEvent(
                            satellite_id=satellite.id,
                            debris_id=debris.id,
                            tca=tca,
                            miss_distance=miss_distance,
                        )
                    )

        return events
