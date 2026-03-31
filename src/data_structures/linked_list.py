"""Linked list implementation."""


class Node:
    """A node in the linked list."""

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """Singly linked list."""

    def __init__(self):
        self.head = None
        self._size = 0

    def append(self, data):
        """Add element to the end."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self._size += 1

    def prepend(self, data):
        """Add element to the beginning."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self._size += 1

    def __len__(self):
        return self._size

    def __repr__(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.data))
            current = current.next
        return " -> ".join(nodes)
