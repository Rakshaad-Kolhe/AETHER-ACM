import numpy as np


def compute_debris_density(debris_objects, grid_size_km):
    """Compute debris counts per 3D spatial grid cell."""
    density_map = {}
    cell_size = float(grid_size_km)

    for debris in debris_objects:
        x, y, z = np.asarray(debris.get_position(), dtype=float)
        cell_x = int(x / cell_size)
        cell_y = int(y / cell_size)
        cell_z = int(z / cell_size)
        key = (cell_x, cell_y, cell_z)
        density_map[key] = density_map.get(key, 0) + 1

    return density_map


def get_high_density_cells(density_map, threshold):
    """Return grid cells whose debris count meets or exceeds threshold."""
    return [cell for cell, count in density_map.items() if count >= threshold]
