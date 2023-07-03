from LinkedList import LinkedList
from Queue import Queue
from Stack import Stack


class EdgeList(LinkedList):
    @property
    def degree(self):
        return self.get_length()

    def __init__(self):
        super().__init__()


class Graph:
    def __init__(self, vertices: list, edges: list):
        self.vertices = vertices
        self.edges = edges
        self.adjacency_list = []
        self.parents = []
        self._create_adjacency_list()

    def _create_adjacency_list(self):
        for vertex in self.vertices:
            edge_list = EdgeList()

            for edge in self.edges:
                if vertex == edge[0]:
                    edge_list.prepend(edge[1])
                if vertex == edge[1]:
                    edge_list.prepend(edge[0])

            self.adjacency_list.append(edge_list)

    def print(self):
        for i in range(len(self.adjacency_list)):
            print(self.vertices[i], end=": ")
            self.adjacency_list[i].print()

    def get_degree_of(self, vertex):
        for i in range(len(self.vertices)):
            if self.vertices[i] == vertex:
                return self.adjacency_list[i].get_length()

    def get_neighbors_of(self, vertex):
        for i in range(len(self.vertices)):
            if self.vertices[i] == vertex:

                neighbors = []
                current = self.adjacency_list[i].head

                while current is not None:
                    neighbors.append(current.data)
                    current = current.next
                return neighbors

    def bfs(self, root_vertex: int):
        # Queue for adjacent vertices checked in FIFO order
        queue = Queue()
        queue.enqueue(self.vertices[root_vertex])
        # History of vertices with adjacent lists already searched
        processed = [False for _ in range(len(self.vertices))]
        # Dictionary for storing parents of vertices
        self.parents = [-1 for _ in range(len(self.vertices))]
        # Order in which adjacency lists are exhausted
        history = []

        while queue.size != 0:
            vertex = queue.dequeue()
            current = self.adjacency_list[vertex].head

            if not processed[vertex]:
                while current is not None:
                    if not processed[current.data]:
                        queue.enqueue(current.data)
                        self.parents[current.data] = vertex
                    current = current.next

                processed[vertex] = True
                history.append(vertex)
        return history

    def dfs(self, root_vertex: int):
        # Stack for adjacent vertices checked in LIFO order
        stack = Stack()
        stack.push(root_vertex)
        # History of vertices with adjacent lists already searched
        processed = [False] * len(self.vertices)
        # Dictionary for storing parents of vertices
        self.parents = [-1 for _ in range(len(self.vertices))]
        # Order in which adjacency lists are exhausted
        history = []

        while stack.size != 0:
            vertex = stack.pop()
            current = self.adjacency_list[vertex].head

            if not processed[vertex]:
                while current is not None:
                    if not processed[current.data]:
                        stack.push(current.data)
                        self.parents[current.data] = vertex
                    current = current.next
                history.append(vertex)
                processed[vertex] = True
        return history

    def _recursive_dfs(self, root_vertex: int, marked: list = None, history: list = None):
        # Initialize marked and history matrices non-recursively
        marked = list(False for _ in self.vertices) if marked is None else marked
        history = [root_vertex] if history is None else history

        marked[root_vertex] = True
        current = self.adjacency_list[root_vertex].head

        while current is not None:
            if not marked[current.data]:
                history.append(current.data)
                self._recursive_dfs(current.data, marked, history)
            current = current.next

        return history if len(history) == len(self.vertices) else marked

    def _recursive_get_path(self, source: int, target: int, path: list = None) -> list:
        """Returns an array of vertices that go from source vertex to target vertex"""
        if path is None:
            self.bfs(source)
            path = [target]
        if self.parents[target] == -1:
            return [-1]

        path.append(self.parents[target])
        if self.parents[target] == source:
            return path[::-1]
        else:
            return self._recursive_get_path(source, self.parents[target], path)

    def get_path(self, source: int, target: int):
        self.bfs(source)
        return self._find_path(source, target)

    def get_dfs_path(self, source: int, target: int):
        self.dfs(source)
        return self._find_path(source, target)

    def _find_path(self, source: int, target: int):
        path = [target]
        while self.parents[target] != source:
            if self.parents[target] == -1:
                if target == source:
                    break
                return -1

            path.append(self.parents[target])
            target = self.parents[target]

        path.append(source)
        return path[::-1]

    def is_connected(self):
        component = self.bfs(self.vertices[0])
        return len(component) == len(self.vertices)

    def num_components(self):
        discovered = [False] * len(self.vertices)
        components = 0

        for v in range(len(discovered)):
            if not discovered[v]:
                history = self.bfs(v)
                components += 1
                for found_vertex in history:
                    discovered[found_vertex] = True if \
                        not discovered[found_vertex] else None

        return components

    def num_distinct_cycles(self):
        """Returns number of cycles using first betti number formula"""
        return len(self.edges) - len(self.vertices) + self.num_components()

    def get_back_edges(self, root_vertex: int) -> list:
        stack = Stack()
        stack.push(root_vertex)
        processed = [False] * len(self.vertices)
        self.parents = [-1 for _ in range(len(self.vertices))]
        back_edges = []

        while stack.size != 0:
            vertex = stack.pop()
            current = self.adjacency_list[vertex].head

            if not processed[vertex]:
                while current is not None:
                    if not processed[current.data]:
                        stack.push(current.data)
                        self.parents[current.data] = vertex
                    elif self.parents[vertex] != current.data and self.parents[vertex] != -1:
                        back_edges.append([vertex, current.data])
                    current = current.next

            processed[vertex] = True
        return back_edges

    def get_forward_edges(self, root_vertex: int) -> list:
        forward_edges = self.edges.copy()
        back_edges = self.get_back_edges(root_vertex)
        print("backs:", back_edges)
        for back_edge in back_edges:
            for edge in forward_edges:

                if set(back_edge) == set(edge):
                    forward_edges.remove(edge)

        return forward_edges

    def get_cycles(self, root=None) -> set:
        if root is None:
            back_edges = self.get_back_edges(self.vertices[0])
        else:
            back_edges = self.get_back_edges(root)

        cycles = set()
        for edge in back_edges:
            cycle = self.get_dfs_path(edge[1], edge[0])
            cycle.extend(edge[1:])

            cycles.add(tuple(cycle))
        return cycles

    def get_articulations(self):
        return None


v = [0, 1, 2, 3, 4, 5, 6, 7]
e = [
    [0, 1],
    [1, 2],
    [2, 3],
    [3, 4],
    [4, 5],
    [5, 0],  # back edge
    [0, 3],  # back edge
    [5, 6],
    [6, 7],
    [7, 3]   # back edge
]

g = Graph(v, e)
g.print()
print(g.get_forward_edges(0))
