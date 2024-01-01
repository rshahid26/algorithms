import pytest
from data_structures import Graph


def test_init_empty():
    g = Graph()
    assert g.vertices == []
    assert g.edges == []
    assert g.adjacency_list == []


def test_init_with_elements():
    vertices = [[0, 0], [1, 1], [2, 2]]
    edges = [[[0, 1], 1], [[1, 2], 4], [[0, 2], 2]]
    g = Graph(vertices, edges)
    assert g.vertices == [0, 1, 2]
    assert g.edges == [[0, 1], [1, 2], [0, 2]]


def test_add_vertex():
    g = Graph()
    g.add_vertex([5, 0])
    assert g.vertices == [5]
    assert g.vertex_weights == [0]


def test_add_edge():
    g = Graph([[5, 0], [6, 1]])
    g.add_edge([[5, 6], 2])
    assert g.edges == [[5, 6]]
    assert g.edge_weights == [2]


def test_bfs():
    vertices = [[0, 0], [1, 1], [2, 2]]
    edges = [[[0, 1], 1], [[1, 2], 4], [[0, 2], 2]]
    g = Graph(vertices, edges)
    assert g.bfs(0) == [0, 2, 1]


def test_dfs():
    vertices = [[0, 0], [1, 1], [2, 2]]
    edges = [[[0, 1], 1], [[1, 2], 4], [[0, 2], 2]]
    g = Graph(vertices, edges)
    assert g.dfs(0) == [0, 2, 1]


def test_get_degree_of():
    vertices = [[0, 0], [1, 1], [2, 2]]
    edges = [[[0, 1], 1], [[1, 2], 4], [[0, 2], 2]]
    g = Graph(vertices, edges)
    assert g.get_degree_of(0) == 2
    assert g.get_degree_of(1) == 2
    assert g.get_degree_of(2) == 2


def test_get_neighbors_of():
    vertices = [[0, 0], [1, 1], [2, 2]]
    edges = [[[0, 1], 1], [[1, 2], 4], [[0, 2], 2]]
    g = Graph(vertices, edges)
    assert g.get_neighbors_of(0) == [1, 2]
    assert g.get_neighbors_of(1) == [0, 2]
    assert g.get_neighbors_of(2) == [0, 1]


def test_get_shortest_path():
    vertices = [[0, 0], [1, 1], [2, 2]]
    edges = [[[0, 1], 1], [[1, 2], 4], [[0, 2], 2]]
    g = Graph(vertices, edges)
    assert g.get_shortest_path(0, 2) == [0, 2]
    assert g.get_shortest_path(1, 0) == [1, 0]
    assert g.get_shortest_path(2, 1) == [2, 1]


def test_get_dfs_path():
    vertices = [[0, 0], [1, 1], [2, 2]]
    edges = [[[0, 1], 1], [[1, 2], 4], [[0, 2], 2]]
    g = Graph(vertices, edges)
    assert g.get_dfs_path(0, 2) == [0, 2]
    assert g.get_dfs_path(1, 0) == [1, 0]
    assert g.get_dfs_path(2, 1) == [2, 0, 1]


def test_get_edge_weight():
    vertices = [[0, 0], [1, 1], [2, 2]]
    edges = [[[0, 1], 1], [[1, 2], 4], [[0, 2], 2]]
    g = Graph(vertices, edges)
    assert g.get_edge_weight([0, 1]) == 1
    assert g.get_edge_weight([1, 2]) == 4
    assert g.get_edge_weight([0, 2]) == 2


def test_is_connected():
    vertices = [[0, 0], [1, 1], [2, 2]]
    edges = [[[0, 1], 1], [[1, 2], 4], [[0, 2], 2]]
    g = Graph(vertices, edges)
    assert g.is_connected() == True


def test_num_components():
    vertices = [[0, 0], [1, 1], [2, 2], [3, 3]]
    edges = [[[0, 1], 1], [[1, 2], 4], [[0, 2], 2]]
    g = Graph(vertices, edges)
    assert g.num_components() == 2


def test_num_distinct_cycles():
    vertices = [[0, 0], [1, 1], [2, 2], [3, 3]]
    edges = [[[0, 1], 1], [[1, 2], 4], [[0, 2], 2], [[2, 3], 3]]
    g = Graph(vertices, edges)
    assert g.num_distinct_cycles() == 1


def test_get_back_edges():
    vertices = [[0, 0], [1, 1], [2, 2], [3, 3]]
    edges = [[[0, 1], 1], [[1, 2], 4], [[0, 2], 2], [[2, 3], 3]]
    g = Graph(vertices, edges)
    assert g.get_back_edges(0) == [[2, 0]]


def test_get_tree_edges():
    vertices = [[0, 0], [1, 1], [2, 2], [3, 3]]
    edges = [[[0, 1], 1], [[1, 2], 4], [[0, 2], 2], [[2, 3], 3]]
    g = Graph(vertices, edges)
    assert g.get_tree_edges(0) == [[0, 1], [1, 2], [2, 3]]


def test_get_cycles():
    vertices = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4]]
    edges = [[[0, 1], 1], [[1, 2], 4], [[2, 3], 3], [[3, 4], 5], [[4, 0], 6]]
    g = Graph(vertices, edges)
    cycles = g.get_cycles()
    assert cycles == {(0, 1, 2, 3, 4, 0), (1, 2, 3, 4, 1)}


def test_minimum_spanning_edges():
    vertices = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4]]
    edges = [[[0, 1], 1], [[1, 2], 4], [[2, 3], 3], [[3, 4], 5], [[4, 0], 6]]
    g = Graph(vertices, edges)
    mse = g.minimum_spanning_edges()
    assert mse == [[[0, 1], 1], [[0, 4], 6], [[4, 3], 5], [[3, 2], 3]]


def test_minimum_spanning_tree():
    vertices = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4]]
    edges = [[[0, 1], 1], [[1, 2], 4], [[2, 3], 3], [[3, 4], 5], [[4, 0], 6]]
    g = Graph(vertices, edges)
    mst = g.minimum_spanning_tree()
    assert mst.edges == [[0, 1], [0, 4], [4, 3], [3, 2]]


def test_get_sorted_edges():
    vertices = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4]]
    edges = [[[0, 1], 1], [[1, 2], 4], [[2, 3], 3], [[3, 4], 5], [[4, 0], 6]]
    g = Graph(vertices, edges)
    sorted_edges = g.get_sorted_edges()
    assert sorted_edges == [[[0, 1], 1], [[2, 3], 3], [[1, 2], 4], [[3, 4], 5], [[4, 0], 6]]


def test_kruskal():
    vertices = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4]]
    edges = [[[0, 1], 1], [[1, 2], 4], [[2, 3], 3], [[3, 4], 5], [[4, 0], 6]]
    g = Graph(vertices, edges)
    kruskal_mst = g.kruskal()
    assert kruskal_mst == [[[0, 1], 1], [[0, 4], 6], [[4, 3], 5], [[3, 2], 3]]
