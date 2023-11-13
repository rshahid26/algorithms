from .Graph import Graph
from .Queue import Queue


class BipartiteGraph(Graph):
    def __init__(self, vertices, edges):
        super().__init__(vertices, edges)
        graph = Graph(vertices, edges)
        self.vertices = graph.vertices
        self.edges = graph.edges

    def get_two_color(self) -> list:
        queue = Queue()
        queue.append(self.vertices[0])
        colors = ["Uncolored"] * len(self.vertices)
        processed = [False] * len(self.vertices)

        while queue.length != 0:
            vertex = queue.popleft()
            colors[vertex] = "White" if colors[vertex] == "Uncolored" else colors[vertex]

            current = self.adjacency_list[vertex].head
            while current is not None:
                if not processed[current.val]:
                    queue.append(current.val)
                    colors[current.val] = "Black" if colors[vertex] == "White" else "White"
                current = current.next
            processed[vertex] = True
        return colors
