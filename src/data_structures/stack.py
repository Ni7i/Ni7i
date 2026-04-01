"""Stack implementation."""


class Stack:
    """A simple stack data structure."""

    def __init__(self):
        self._items = []

    def push(self, item):
        """Push item onto the stack."""
        self._items.append(item)

    def pop(self):
        """Remove and return top item."""
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self._items.pop()

    def peek(self):
        """Return top item without removing it."""
        if self.is_empty():
            raise IndexError("Peek at empty stack")
        return self._items[-1]

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def size(self) -> int:
        return len(self._items)

    def __repr__(self):
        return f"Stack({self._items})"
