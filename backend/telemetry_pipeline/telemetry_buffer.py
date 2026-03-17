class TelemetryBuffer:
    """Simple in-memory buffer for raw telemetry payloads."""

    def __init__(self):
        """Initialize an empty telemetry buffer."""
        self.buffer = []

    def add(self, payload):
        """Append one telemetry payload to the buffer."""
        self.buffer.append(payload)

    def get_all(self):
        """Return all buffered telemetry payloads."""
        return self.buffer

    def clear(self):
        """Clear all buffered telemetry payloads."""
        self.buffer = []

    def size(self):
        """Return number of telemetry payloads in buffer."""
        return len(self.buffer)
