"""Design pattern implementations - Singleton."""


class SingletonMeta(type):
    """Thread-safe Singleton metaclass."""
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class DatabaseConnection(metaclass=SingletonMeta):
    """Example singleton: database connection pool."""

    def __init__(self, host="localhost", port=5432):
        self.host = host
        self.port = port
        self._connected = False

    def connect(self):
        if not self._connected:
            self._connected = True
            return f"Connected to {self.host}:{self.port}"
        return "Already connected"

    def disconnect(self):
        self._connected = False

    @property
    def is_connected(self):
        return self._connected
