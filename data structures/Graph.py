class Graph:
    def __init__(self, V):
        self.V = V
        self.adj = [[] for i in range(V)]

    # add edge to graph
    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    # Returns count of edge in undirected graph
    def count_edges(self):
        Sum = 0

        # traverse all vertex
        for i in range(self.V):

            # add all edge that are linked
            # to the current vertex
            Sum += len(self.adj[i])

        return Sum // 2


if __name__ == '__main__':

    V = 9
    g = Graph(V)

    g.add_edge(0, 1)
    g.add_edge(0, 7)
    g.add_edge(1, 2)
    g.add_edge(1, 7)
    g.add_edge(2, 3)
    g.add_edge(2, 8)
    g.add_edge(2, 5)
    g.add_edge(3, 4)
    g.add_edge(3, 5)
    g.add_edge(4, 5)
    g.add_edge(5, 6)
    g.add_edge(6, 7)
    g.add_edge(6, 8)
    g.add_edge(7, 8)

    print(g.count_edges())
