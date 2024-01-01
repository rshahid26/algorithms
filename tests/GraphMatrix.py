from data_structures import GraphMatrix

g = GraphMatrix.Graph([0, 1, 2, 3, 4, 5])
for i in range(len(g.vertices) - 1):
    g.add_edge(g.vertices[i], g.vertices[i + 1])
g.add_edge(0, 3)
g.add_edge(0, 5)

g.print_matrix()
print(g.count_edges())