import numpy as np


class Debris:
    def __init__(self, debris_id, state, radius=1.0, risk=0.0, last_updated=None):
        self.id = debris_id
        self.state = np.asarray(state, dtype=float)
        self.radius = float(radius)
        self.risk = float(risk)
        self.last_updated = last_updated


class DebrisRegistry:
    def __init__(self):
        self._debris = {}

    def add_debris(self, debris):
        self._debris[debris.id] = debris

    def remove_debris(self, debris_id):
        self._debris.pop(debris_id, None)

    def get_debris(self, debris_id):
        return self._debris.get(debris_id)

    def get_all_debris(self):
        return list(self._debris.values())

    def update_state(self, debris_id, new_state, timestamp=None):
        debris = self._debris.get(debris_id)
        if debris is None:
            return
        debris.state = np.asarray(new_state, dtype=float)
        if timestamp is not None:
            debris.last_updated = timestamp

    def bulk_load(self, debris_list):
        self._debris.update({debris.id: debris for debris in debris_list})

    def clear(self):
        self._debris.clear()

    def count(self):
        return len(self._debris)

    def get_positions_array(self):
        if not self._debris:
            return np.empty((0, 3), dtype=float)
        return np.asarray([debris.state[:3] for debris in self._debris.values()], dtype=float)
