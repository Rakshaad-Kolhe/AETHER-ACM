class Event:
    def __init__(self, timestamp, event_type, data):
        self.timestamp = timestamp
        self.event_type = event_type
        self.data = data

    def to_dict(self):
        return {
            "timestamp": self.timestamp,
            "event_type": self.event_type,
            "data": self.data
        }


class EventLog:
    def __init__(self):
        self._events = []

    def log_event(self, event):
        self._events.append(event)

    def create_event(self, timestamp, event_type, data):
        event = Event(timestamp=timestamp, event_type=event_type, data=data)
        self._events.append(event)
        return event

    def get_all_events(self):
        return list(self._events)

    def get_events_by_type(self, event_type):
        return [event for event in self._events if event.event_type == event_type]

    def get_events_in_time_range(self, start, end):
        return [event for event in self._events if start <= event.timestamp <= end]

    def get_recent_events(self, limit=50):
        return self._events[-limit:]

    def clear(self):
        self._events.clear()

    def count(self):
        return len(self._events)