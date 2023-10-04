import collections

from .Graph import Graph


class DirectedGraph(Graph):

    def __init__(self, vertices: list = None, edges: list = None):
        super().__init__(vertices, edges)
        self._reset_edge_class()
        self._timer = 0
        self._time = [{
            "entry": -1,
            "exit": -1
        } for _ in range(len(self.vertices))]

    def _reset_edge_class(self):
        self.edge_class = {
            "tree": [],
            "back": [],
            "forward": [],
            "cross": [],
        }

    def add_edge(self, edge_):
        edge, weight = self._parse_edge(edge_)
        self.edges.append(edge)
        self.edge_weights.append(weight)

        # Add edges in the v1 -> v2 direction only
        self.adjacency_list[edge[0]].prepend(edge[1], weight)

    def dfs(self, root_vertex, marked: list = None):
        marked = list(False for _ in self.vertices) if marked is None else marked
        history = []  # postorder traversal history
        self.parents = [-1] * len(self.vertices)
        self._reset_edge_class()
        self._timer = 0

        self._recursive_dfs(root_vertex, marked, history)
        return history

    def _recursive_dfs(self, vertex: int, marked: list = None, history: list = None):
        marked[vertex] = "visited"
        self._timer += 1
        self._time[vertex]["entry"] = self._timer

        current = self.adjacency_list[vertex].head
        while current is not None:
            if not marked[current.data]:
                self.parents[current.data] = vertex
                self._recursive_dfs(current.data, marked, history)

            self._classify_edge(vertex, current.data, marked)
            current = current.next

        marked[vertex] = "processed"
        history.append(vertex)
        self._timer += 1
        self._time[vertex]["exit"] = self._timer
        return marked

    def _classify_edge(self, source, target, marked):
        # Direct ancestor in the dfs tree
        if self.parents[target] == source:
            self.edge_class["tree"].append([source, target])

        # Ancestor in the dfs tree
        elif marked[target] == "visited":
            self.edge_class["back"].append([source, target])

        elif marked[target] == "processed" and (self._time[target]["entry"] > self._time[source]["entry"]):
            self.edge_class["forward"].append([source, target])

        elif marked[target] == "processed" and (self._time[target]["entry"] < self._time[source]["entry"]):
            self.edge_class["cross"].append([source, target])

    def _get_time(self, vertex):
        return [self._time[vertex]["entry"], self._time[vertex]["exit"]]

    def get_back_edges(self, root_vertex: int) -> list:
        """Override undirected back edges method"""
        return self.edge_class["back"]

    def get_tree_edges(self, root_vertex: int) -> list:
        """Override undirected tree edges method"""
        return self.edge_class["tree"]

    def num_distinct_cycles(self):
        return len(self.edge_class["back"])

    def top_sort(self) -> list:
        marked = list(False for _ in self.vertices)
        history = []

        for vertex in range(len(marked)):
            if not marked[vertex]:
                history += self.dfs(vertex, marked)
                if self.num_distinct_cycles() > 0:
                    return None

        # Vertices processed first (leaves) should go last and so on
        history.reverse()
        return history

    def kahns(self):
        """Returns a topological sort of the graph by pruning roots"""
        in_degree = [0] * len(self.vertices)
        for vertex in self.vertices:
            for neighbor in self.adjacency_list[vertex]:
                in_degree[neighbor] += 1

        queue = collections.deque()
        for vertex in self.vertices:
            if in_degree[vertex] == 0:
                queue.append(vertex)

        history = []
        while queue:
            vertex = queue.popleft()
            for neighbor in self.adjacency_list[vertex]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
            history.append(vertex)
        return history if len(history) == len(self.vertices) else None

    def get_root_vertex(self) -> int:
        """Returns the first vertex found with no parents"""
        is_child = [False] * len(self.vertices)
        for vertex in self.adjacency_list:
            current = vertex.head

            while current is not None:
                is_child[current.data] = True
                current = current.next

        for i in range(len(is_child)):
            if not is_child[i]:
                return i
        raise AssertionError("Every vertex in this graph has a parent.")

    def get_edge_transpose(self):
        edge_transpose = self.edges.copy()
        for i in range(len(self.edges)):
            # Flip the direction of every edge
            edge_transpose[i] = [self.edges[i][1], self.edges[i][0]]

        return edge_transpose

    def get_transpose(self):
        return DirectedGraph(self.vertices, self.get_edge_transpose())

    def is_weakly_connected(self) -> bool:
        undirected_graph = Graph(self.vertices, self.edges)

        component = undirected_graph.bfs(self.vertices[0])
        return len(component) == len(self.vertices)

    def is_connected(self) -> bool:
        """Override connectedness test for undirected graphs"""
        return self.is_weakly_connected()

    def is_strongly_connected(self) -> bool:
        """Strongly connected requirement using Kosaraju's algorithm"""
        if not self.vertices:
            return True

        marked = [False] * len(self.vertices)
        marked_from = [False] * len(self.vertices)

        self.dfs(self.vertices[0], marked)
        self.get_transpose().dfs(self.vertices[0], marked_from)

        for vertex in range(len(self.vertices)):
            if not marked[vertex] or not marked_from[vertex]:
                return False
        return True

    def strongly_connected_components(self) -> set:
        """Stateful Kosaraju's algorithm for getting SCCs"""
        marked = list(False for _ in self.vertices)
        history = []
        for vertex in range(len(self.vertices)):
            if not marked[vertex]:
                history += self.dfs(vertex, marked)

        transpose = self.get_transpose()
        marked = list(False for _ in self.vertices)

        scc = set()
        while history:
            vertex = history.pop()
            if not marked[vertex]:
                curr_scc = transpose.bfs(vertex, marked)
                if len(curr_scc) > 1:  # Ignore leaves
                    scc.add(curr_scc)
        return scc

    def minimum_spanning_tree(self, vertex: int = None):
        return DirectedGraph(self._vertex_set(), self.minimum_spanning_edges(vertex))

    def kruskal(self):
        raise Exception("For directed graphs, use minimum_spanning_tree(vertex) instead.")