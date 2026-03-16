import numpy as np
from scipy.spatial import cKDTree


class DebrisSpatialIndex:
    """KD-tree spatial index for fast debris proximity queries."""

    def __init__(self):
        """Initialize an empty spatial index."""
        self.tree = None
        self.debris_list = []

    def build(self, debris_objects):
        """Build the KD-tree from a list of debris objects."""
        self.debris_list = list(debris_objects)
        if not self.debris_list:
            self.tree = None
            return
        positions = np.array([debris.get_position() for debris in self.debris_list], dtype=float)
        self.tree = cKDTree(positions)

    def query(self, position, radius):
        """Return debris objects within radius (km) of the given position."""
        if self.tree is None:
            return []
        indices = self.tree.query_ball_point(np.asarray(position, dtype=float), r=radius)
        return [self.debris_list[i] for i in indices]
