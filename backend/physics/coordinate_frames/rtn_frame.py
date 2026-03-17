import numpy as np


class RTNFrame:
    """Simple container for vectors represented in RTN coordinates."""

    def __init__(self, vector):
        """Initialize RTN vector from array-like input."""
        self._vector = np.asarray(vector, dtype=float)

    def get_vector(self):
        """Return RTN vector."""
        return self._vector

    def to_array(self):
        """Return raw RTN NumPy vector."""
        return self._vector
