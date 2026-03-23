from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Union


ManeuverId = Union[str, int]
SatelliteId = Union[str, int]


@dataclass
class Maneuver:
    id: ManeuverId
    satellite_id: SatelliteId
    maneuver_type: str
    delta_v: float
    status: str
    timestamp: Union[float, int]
    metadata: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "satellite_id": self.satellite_id,
            "maneuver_type": self.maneuver_type,
            "delta_v": self.delta_v,
            "status": self.status,
            "timestamp": self.timestamp,
            "metadata": self.metadata,
        }


class ManeuverRegistry:
    def __init__(self) -> None:
        self._maneuvers: Dict[ManeuverId, Maneuver] = {}

    def add_maneuver(self, maneuver: Maneuver) -> None:
        self._maneuvers[maneuver.id] = maneuver

    def get_maneuver(self, maneuver_id: ManeuverId) -> Optional[Maneuver]:
        return self._maneuvers.get(maneuver_id)

    def get_all_maneuvers(self) -> List[Maneuver]:
        return list(self._maneuvers.values())

    def get_maneuvers_by_satellite(self, satellite_id: SatelliteId) -> List[Maneuver]:
        return [
            maneuver
            for maneuver in self._maneuvers.values()
            if maneuver.satellite_id == satellite_id
        ]

    def get_recent_maneuvers(self, limit: int = 50) -> List[Maneuver]:
        return list(self._maneuvers.values())[-limit:]

    def update_metadata(self, maneuver_id: ManeuverId, metadata: Dict[str, Any]) -> None:
        maneuver = self._maneuvers.get(maneuver_id)
        if maneuver is not None:
            maneuver.metadata.update(metadata)

    def get_maneuvers_by_status(self, status: str) -> List[Maneuver]:
        return [
            maneuver
            for maneuver in self._maneuvers.values()
            if maneuver.status == status
        ]

    def update_status(self, maneuver_id: ManeuverId, status: str) -> None:
        maneuver = self._maneuvers.get(maneuver_id)
        if maneuver is not None:
            maneuver.status = status

    def remove_maneuver(self, maneuver_id: ManeuverId) -> None:
        self._maneuvers.pop(maneuver_id, None)

    def clear(self) -> None:
        self._maneuvers.clear()

    def count(self) -> int:
        return len(self._maneuvers)
