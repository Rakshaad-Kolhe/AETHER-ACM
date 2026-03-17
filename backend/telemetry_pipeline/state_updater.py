def update_state(existing_satellites, existing_debris, parsed_data):
    """Update in-memory satellites and debris from parsed telemetry objects."""
    satellites = list(existing_satellites)
    debris_objects = list(existing_debris)

    sat_map = {sat.id: sat for sat in satellites}
    deb_map = {deb.id: deb for deb in debris_objects}

    for parsed_satellite in parsed_data.get("satellites", []):
        existing = sat_map.get(parsed_satellite.id)
        if existing is not None:
            existing.update_state(parsed_satellite.state)
        else:
            satellites.append(parsed_satellite)
            sat_map[parsed_satellite.id] = parsed_satellite

    for parsed_debris in parsed_data.get("debris", []):
        existing = deb_map.get(parsed_debris.id)
        if existing is not None:
            existing.update_state(parsed_debris.state)
        else:
            debris_objects.append(parsed_debris)
            deb_map[parsed_debris.id] = parsed_debris

    return satellites, debris_objects
