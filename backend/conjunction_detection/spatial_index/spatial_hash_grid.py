import numpy as np


class SpatialHashGrid:
    """Simple 3D spatial hash grid for debris proximity pre-filtering."""

    def __init__(self, cell_size_km):
        """Initialize grid with fixed cubic cell size in kilometers."""
        self.cell_size_km = float(cell_size_km)
        self.grid = {}

    def _cell_key(self, position):
        """Convert a 3D position into integer hash-grid cell coordinates."""
        x, y, z = np.asarray(position, dtype=float)
        cx = int(x / self.cell_size_km)
        cy = int(y / self.cell_size_km)
        cz = int(z / self.cell_size_km)
        return (cx, cy, cz)

    def build(self, debris_objects):
        """Build hash grid from debris objects."""
        self.grid = {}
        for debris in debris_objects:
            key = self._cell_key(debris.get_position())
            if key not in self.grid:
                self.grid[key] = []
            self.grid[key].append(debris)

    def query(self, position, radius):
        """Return debris candidates from nearby cells around the query position."""
        center = self._cell_key(position)
        candidates = []

        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                for dz in (-1, 0, 1):
                    key = (center[0] + dx, center[1] + dy, center[2] + dz)
                    candidates.extend(self.grid.get(key, []))

        return candidates
