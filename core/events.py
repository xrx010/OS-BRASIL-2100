from datetime import datetime


class EventLog:
    """Registro em memória dos eventos recentes da plataforma."""

    def __init__(self):
        self._events = []

    def record(self, name, details=""):
        event = {
            "name": name,
            "details": details,
            "timestamp": datetime.now(),
        }
        self._events.insert(0, event)
        return event

    def recent(self, limit=10):
        return self._events[:limit]
