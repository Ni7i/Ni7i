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

def dfs(self, start) -> list:
    """Depth-first search traversal."""
    visited = set()
    result = []
    self._dfs_recursive(start, visited, result)
    return result

def _dfs_recursive(self, vertex, visited, result):
    visited.add(vertex)
    result.append(vertex)
    for neighbor, _ in self.adj.get(vertex, []):
        if neighbor not in visited:
            self._dfs_recursive(neighbor, visited, result)

def has_path(self, start, end) -> bool:
    """Check if path exists between start and end."""
    return end in self.bfs(start)

def shortest_path(self, start, end) -> list:
    """Find shortest path using BFS (unweighted)."""
    visited = {start}
    queue = deque([(start, [start])])
    while queue:
        vertex, path = queue.popleft()
        if vertex == end:
            return path
        for neighbor, _ in self.adj.get(vertex, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    return []
