import data_structures


v = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4]]
e = [
    [[0, 1], 1],
    [[1, 2], 4],
    [[0, 3], 2],
    [[3, 2], 3],
    [[3, 4], 5],
    [[4, 0], 0]
]

g = data_structures.DirectedGraph(v, e)
g.print_adj()
print()
g.print_adj_weights()
print(g.minimum_spanning_edges())
