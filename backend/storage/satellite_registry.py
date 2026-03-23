from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Union

import numpy as np


SatelliteId = Union[str, int]


@dataclass
class Satellite:
    id: SatelliteId
    state: np.ndarray
    fuel: float
    health: str
    last_updated: Optional[Union[float, int]] = None
    metadata: Dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        self.state = np.asarray(self.state, dtype=float)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "state": self.state.tolist(),
            "fuel": self.fuel,
            "health": self.health,
            "last_updated": self.last_updated,
            "metadata": self.metadata,
        }


class SatelliteRegistry:
    def __init__(self) -> None:
        self._satellites: Dict[SatelliteId, Satellite] = {}

    def add_satellite(self, satellite: Satellite) -> None:
        self._satellites[satellite.id] = satellite

    def get_satellite(self, satellite_id: SatelliteId) -> Optional[Satellite]:
        return self._satellites.get(satellite_id)

    def get_all_satellites(self) -> List[Satellite]:
        return list(self._satellites.values())

    def get_active_satellites(self) -> List[Satellite]:
        return [
            satellite
            for satellite in self._satellites.values()
            if satellite.health != "critical"
        ]

    def update_state(
        self,
        satellite_id: SatelliteId,
        new_state: Any,
        timestamp: Optional[Union[float, int]] = None,
    ) -> None:
        satellite = self._satellites.get(satellite_id)
        if satellite is not None:
            satellite.state = np.asarray(new_state, dtype=float)
            if timestamp is not None:
                satellite.last_updated = timestamp

    def update_fuel(self, satellite_id: SatelliteId, fuel: float) -> None:
        satellite = self._satellites.get(satellite_id)
        if satellite is not None:
            satellite.fuel = fuel

    def update_health(self, satellite_id: SatelliteId, health: str) -> None:
        satellite = self._satellites.get(satellite_id)
        if satellite is not None:
            satellite.health = health

    def update_metadata(self, satellite_id: SatelliteId, metadata: Dict[str, Any]) -> None:
        satellite = self._satellites.get(satellite_id)
        if satellite is not None:
            satellite.metadata.update(metadata)

    def remove_satellite(self, satellite_id: SatelliteId) -> None:
        self._satellites.pop(satellite_id, None)

    def clear(self) -> None:
        self._satellites.clear()

    def count(self) -> int:
        return len(self._satellites)

    def to_dict_list(self) -> List[Dict[str, Any]]:
        return [satellite.to_dict() for satellite in self._satellites.values()]

    def get_positions_array(self) -> np.ndarray:
        if not self._satellites:
            return np.empty((0, 3), dtype=float)
        return np.array([satellite.state[:3] for satellite in self._satellites.values()])

    def get_recent_satellites(self, limit: int = 50) -> List[Satellite]:
        return list(self._satellites.values())[-limit:]
