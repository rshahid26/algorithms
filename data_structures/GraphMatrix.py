class Graph:
    def __init__(self, vertices: list):
        self.vertices = vertices
        self.matrix = [
            [0 for _ in range(len(vertices))] for _ in range(len(vertices))
        ]

    def add_edge(self, v1, v2):
        self.matrix[v1][v2] += 1
        self.matrix[v2][v1] += 1

    def remove_edge(self, v1, v2):
        if self.matrix[v1][v2] == 0:
            return
        else:
            self.matrix[v1][v2] -= 1
            self.matrix[v2][v1] -= 1

    def count_edges(self):
        count = 0

        for i in range(len(self.matrix)):
            for j in range(0, i + 1, 1):

                if self.matrix[i][j] is not 0:
                    count += 1

        return count

    def print_matrix(self):
        for v in self.matrix:
            print(v)


g = Graph([0, 1, 2, 3, 4, 5])
for i in range(len(g.vertices) - 1):
    g.add_edge(g.vertices[i], g.vertices[i + 1])
g.add_edge(0, 3)
g.add_edge(0, 5)

g.print_matrix()
print(g.count_edges())
