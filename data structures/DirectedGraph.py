from Graph import Graph
from Graph import EdgeList


class DirectedGraph(Graph):

    def __init__(self, vertices: list, edges: list):
        super().__init__(vertices, edges)
        self.edge_class = {
            "tree": [],
            "back": [],
            "forward": [],
            "cross": [],
        }
        self._timer = 0
        self._time = [{
            "entry": -1,
            "exit": -1
        } for _ in range(len(self.vertices))]

    def dfs(self, root_vertex):
        return self._recursive_dfs(root_vertex)

    def _recursive_dfs(self, root_vertex: int, marked: list = None, history: list = None):
        # Initialize marked and history matrices non-recursively
        if history is None:
            marked = list(False for _ in self.vertices)
            history = [root_vertex]
            self.parents = [-1] * len(self.vertices)
            self._timer = 0

        marked[root_vertex] = "discovered"
        self._timer += 1
        self._time[root_vertex]["entry"] = self._timer

        current = self.adjacency_list[root_vertex].head
        while current is not None:
            if not marked[current.data]:
                history.append(current.data)
                self.parents[current.data] = root_vertex
                self._recursive_dfs(current.data, marked, history)

            self._classify_edge(root_vertex, current.data, marked)
            current = current.next

        marked[root_vertex] = "processed"
        self._timer += 1
        self._time[root_vertex]["exit"] = self._timer
        return history if len(history) == len(self.vertices) else marked

    def _classify_edge(self, source, target, marked):
        if source == 4:
            print(target, marked[target])
        if self.parents[target] == source:
            self.edge_class["tree"].append([source, target])

        elif marked[target] == "discovered" and not marked[target] == "processed":
            self.edge_class["back"].append([source, target])

        elif marked[target] == "processed" and (self._time[target]["entry"] > self._time[source]["entry"]):
            self.edge_class["forward"].append([source, target])

        elif marked[target] == "processed" and (self._time[target]["entry"] < self._time[source]["entry"]):
            self.edge_class["cross"].append([source, target])

    def _get_time(self, vertex):
        return [self._time[vertex]["entry"], self._time[vertex]["exit"]]

    def _set_adjacency_list(self):
        for vertex in self.vertices:
            edge_list = EdgeList()

            for edge in self.edges:
                if vertex == edge[0]:
                    edge_list.prepend(edge[1])

            self.adjacency_list.append(edge_list)

    def top_sort(self):
        return None

    def prim(self):
        return None


v = [0, 1, 2, 3, 4]
e = [
    [0, 3],
    [0, 1],
    [1, 2],
    [3, 2],
    [3, 4],
]

g = DirectedGraph(v, e)
g.print()
print(g.dfs(0))