"""Graph data structure and algorithms."""
from collections import deque


class Graph:
    """Adjacency list graph implementation."""

    def __init__(self, directed=False):
        self.adj = {}
        self.directed = directed

    def add_vertex(self, vertex):
        if vertex not in self.adj:
            self.adj[vertex] = []

    def add_edge(self, u, v, weight=1):
        """Add edge between u and v."""
        self.add_vertex(u)
        self.add_vertex(v)
        self.adj[u].append((v, weight))
        if not self.directed:
            self.adj[v].append((u, weight))

    def bfs(self, start) -> list:
        """Breadth-first search traversal."""
        visited = set()
        queue = deque([start])
        visited.add(start)
        result = []
        while queue:
            vertex = queue.popleft()
            result.append(vertex)
            for neighbor, _ in self.adj.get(vertex, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return result
