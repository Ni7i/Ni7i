"""Design pattern implementations - Observer."""
from abc import ABC, abstractmethod


class EventEmitter:
    """Simple event emitter / observer pattern."""

    def __init__(self):
        self._listeners = {}

    def on(self, event: str, callback):
        """Register a listener for an event."""
        if event not in self._listeners:
            self._listeners[event] = []
        self._listeners[event].append(callback)

    def off(self, event: str, callback):
        """Remove a listener."""
        if event in self._listeners:
            self._listeners[event] = [
                cb for cb in self._listeners[event] if cb != callback
            ]

    def emit(self, event: str, *args, **kwargs):
        """Emit an event, calling all registered listeners."""
        for callback in self._listeners.get(event, []):
            callback(*args, **kwargs)

    @property
    def events(self) -> list[str]:
        """List all registered event names."""
        return list(self._listeners.keys())
