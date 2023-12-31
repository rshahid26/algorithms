import collections

from .Stack import Stack
from .WeightedEdgeList import WeightedEdgeList
from .MinHeap import MinHeap
from .UnionFind import UnionFind


class Graph:
    def __init__(self, vertices: list = None, edges: list = None):
        self.vertices = []
        self.vertex_weights = []

        self.edges = []
        self.edge_weights = []
        self.adjacency_list = []
        self.parents = []
        try:
            for vertex in vertices:
                self.add_vertex(vertex)
            for edge in edges:
                self.add_edge(edge)
        except TypeError:
            pass  # Initialized with no elements.

    def add_vertex(self, vertex_):
        # Vertices can be entered as either an integer or [vertex, weight]
        vertex = vertex_ if type(vertex_) == int else vertex_[0]
        weight = 0 if type(vertex_) == int else vertex_[1]

        self.vertices.append(vertex)
        self.vertex_weights.append(weight)
        self.adjacency_list.append(WeightedEdgeList())

    def add_edge(self, edge_):
        edge, weight = self._parse_edge(edge_)
        self.edges.append(edge)
        self.edge_weights.append(weight)

        # Add edges in the v1 -> v2 and v2 -> v1 directions
        self.adjacency_list[edge[0]].prepend(edge[1], weight)
        self.adjacency_list[edge[1]].prepend(edge[0], weight)

    @staticmethod
    def _parse_edge(edge_) -> tuple:
        # Edges can be entered as either [source_v, target_v] or [[source_v, target_v], weight]
        edge = edge_ if type(edge_[0]) == int else edge_[0]
        weight = 0 if type(edge_[0]) == int else edge_[1]
        return edge, weight

    def print_adj(self):
        for i in range(len(self.adjacency_list)):
            print(self.vertices[i], end=": ")
            self.adjacency_list[i].print()

    def print_adj_weights(self):
        for i in range(len(self.adjacency_list)):
            print(self.vertices[i], end=": ")
            self.adjacency_list[i].print_weights()

    def get_degree_of(self, vertex):
        for i in range(len(self.vertices)):
            if self.vertices[i] == vertex:
                return self.adjacency_list[i].degree

    def get_neighbors_of(self, vertex):
        for i in range(len(self.vertices)):
            if self.vertices[i] == vertex:

                neighbors = []
                current = self.adjacency_list[i].head

                while current is not None:
                    neighbors.append(current.val)
                    current = current.next
                return neighbors

    def bfs(self, root_vertex: int, visited: list = None):
        visited = [False for _ in range(len(self.vertices))] if visited is None else visited
        self.parents = [-1 for _ in range(len(self.vertices))]

        history = []
        queue = collections.deque([root_vertex])

        while queue:
            vertex = queue.popleft()
            visited[vertex] = True

            current = self.adjacency_list[vertex].head
            while current is not None:
                if not visited[current.val]:
                    queue.append(current.val)
                    self.parents[current.val] = vertex
                    visited[current.val] = True
                current = current.next

            history.append(vertex)
        return history

    def dfs(self, root_vertex: int, visited: list = None):
        visited = [False] * len(self.vertices) if visited is None else visited
        self.parents = [-1 for _ in range(len(self.vertices))]

        history = [] # preorder traversal history
        stack = Stack()
        stack.push(root_vertex)

        while stack.size != 0:
            vertex = stack.pop()
            visited[vertex] = True

            current = self.adjacency_list[vertex].head
            while current is not None:
                if not visited[current.val]:
                    stack.push(current.val)
                    self.parents[current.val] = vertex
                    visited[current.val] = True
                current = current.next

            history.append(vertex)
        return history

    def _recursive_dfs(self, root_vertex: int, marked: list = None, history: list = None):
        marked = list(False for _ in self.vertices) if marked is None else marked
        history = []

        self.__undirected_recursive_dfs(root_vertex, marked, history)
        return history

    def __undirected_recursive_dfs(self, root_vertex: int, marked: list, history: list):
        marked[root_vertex] = True
        current = self.adjacency_list[root_vertex].head

        while current is not None:
            if not marked[current.val]:
                history.append(current.val)
                self.__undirected_recursive_dfs(current.val, marked, history)
            current = current.next

        return marked

    def get_shortest_path(self, source: int, target: int):
        self.bfs(source)
        return self._find_path(source, target)

    def get_dfs_path(self, source: int, target: int):
        self.dfs(source)
        return self._find_path(source, target)

    def _find_path(self, source: int, target: int) -> list:
        path = [target]
        while self.parents[target] != source:
            if self.parents[target] == -1:
                if target == source:
                    break
                return []

            path.append(self.parents[target])
            target = self.parents[target]

        path.append(source)
        return path[::-1]
    
    def get_path_weight(self, path: list) -> int:
        weight = 0
        for i in range(len(path) - 1):
            current = self.adjacency_list[path[i]].head
            while current is not None:
                if current.val == path[i + 1]:
                    weight += current.weight
                    break
                current = current.next
            if current is None:
                raise ReferenceError("Path does not exist")
        return weight

    def get_lightest_path(self, source: int, target: int) -> list:
        self.parents = [-1] * len(self.vertices)
        processed = [False] * len(self.vertices)
        distances = [float('inf')] * len(self.vertices)
        distances[source] = 0

        queue = MinHeap()
        queue.append(source, 0)
        while queue.size != 0:
            vertex, distance = queue.pop_object().values()
            if not processed[vertex]:
                processed[vertex] = True

                current = self.adjacency_list[vertex].head
                while current is not None:
                    if not processed[current.val]:
                        if distances[current.val] > distance + current.weight:
                            self.parents[current.val] = vertex
                            distances[current.val] = distance + current.weight
                            queue.append(current.val, distances[current.val])
                    current = current.next
        return self._find_path(source, target)

    def is_connected(self) -> bool:
        component = self.bfs(self.vertices[0])
        return len(component) == len(self.vertices)

    def num_components(self) -> int:
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
                    if not processed[current.val]:
                        stack.push(current.val)
                        self.parents[current.val] = vertex
                    # back edges lead to already processed vertices
                    elif self.parents[vertex] != current.val:
                        back_edges.append([vertex, current.val])
                    current = current.next

            processed[vertex] = True
        return back_edges

    def get_tree_edges(self, root_vertex: int) -> list:
        tree_edges = self.edges.copy()
        back_edges = self.get_back_edges(root_vertex)
        for back_edge in back_edges:
            for edge in tree_edges:

                if set(back_edge) == set(edge):
                    tree_edges.remove(edge)

        return tree_edges

    def get_cycles(self, root_vertex: int) -> list:
        stack = Stack()
        stack.push(root_vertex)
        processed = [False] * len(self.vertices)
        self.parents = [-1 for _ in range(len(self.vertices))]
        cycles = []

        while stack.size != 0:
            vertex = stack.pop()
            current = self.adjacency_list[vertex].head

            if not processed[vertex]:
                while current is not None:
                    if not processed[current.val]:
                        stack.push(current.val)
                        self.parents[current.val] = vertex
                    elif self.parents[vertex] != current.val:
                        cycles.append([vertex] +
                                      self.get_dfs_path(self.parents[vertex], current.val) +
                                      [vertex])
                    current = current.next
                processed[vertex] = True
        return cycles

    def minimum_spanning_edges(self, vertex: int = None) -> list:
        def add_edges_to_heap(v):
            current = self.adjacency_list[v].head
            while current is not None:
                if not processed[current.val]:
                    heap.append([v, current.val], current.weight)
                current = current.next

        def get_minimum_edge():
            while processed[heap.peek()["item"][1]]:
                heap.pop_object()
            return heap.pop_object()

        vertex = vertex if vertex is not None else self.vertices[0]
        processed = [False] * len(self.vertices)
        heap, mse = MinHeap(), []

        add_edges_to_heap(vertex)
        processed[vertex] = True
        while processed.count(True) < len(self.vertices):
            min_edge = get_minimum_edge()
            found_vertex = min_edge["item"][1]

            mse.append([min_edge["item"], min_edge["priority"]])
            add_edges_to_heap(found_vertex)
            processed[found_vertex] = True
        return mse

    def minimum_spanning_tree(self, vertex: int = None):
        """Returns the minimum spanning edges as an object of the Graph class"""
        return Graph(self._vertex_set(), self.minimum_spanning_edges(vertex))

    def _vertex_set(self):
        """Reconstructs vertex argument passed into constructor"""
        return list(zip(self.vertices, self.vertex_weights))

    def _edge_set(self):
        """Reconstructs edge argument passed into constructor"""
        return list(zip(self.edges, self.edge_weights))

    def get_sorted_edges(self):
        return MinHeap(self._edge_set()).get_sort()

    def kruskal(self):    
        sorted_edges = self.get_sorted_edges()
        uf = UnionFind(self.vertices)
        mse = []

        for edge in sorted_edges:
            if not uf.is_connected(edge[0], edge[1]):
                uf.union(edge[0], edge[1])
                mse.append(edge)
                
        return mse
