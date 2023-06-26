from LinkedList import LinkedList
from Queue import Queue


class EdgeList(LinkedList):
    @property
    def degree(self):
        return self.get_length()

    def __init__(self):
        super().__init__()


class Graph:
    def __init__(self, vertices: list, edges: list):
        self.vertices = vertices
        self.adjacency_list = []

        for vertex in vertices:
            edge_list = EdgeList()

            for edge in edges:
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

    def bfs(self, root):
        tree = 1
        queue = Queue().enqueue(root)


v = [0, 1, 2, 3, 4, 5, "A"]
e = [
    [0, 1],
    [1, 2],
    [2, 3],
    [3, 4],
    [4, 5],
    [5, 0],
    [0, 3]
]

g = Graph(v, e)
g.print()

print(g.get_degree_of(2))
print(g.get_neighbors_of(0))
g.bfs(g.n)