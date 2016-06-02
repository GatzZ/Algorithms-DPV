from networkx.algorithms.bipartite.projection import weighted_projected_graph

from graph import *


def kruskal(weighted_graph):
    # Makeset
    pi = {node: node for node in weighted_graph.nodes}
    rank = {node: 0 for node in weighted_graph.nodes}
    res = set()

    def find(x):
        if pi[x] != x:
            pi[x] = find(pi[x])
        return pi[x]

    def union(x, y):
        root_x = find(x)
        root_y = find(y)
        if root_x == root_y:
            return
        if rank[root_x] > rank[root_y]:
            pi[root_y] = pi[root_x]
        else:
            pi[root_x] = pi[root_y]
            if rank[root_x] == rank[root_y]:
                rank[root_y] += 1


    # Sort edges by weight
    sorted_edges = sorted(weighted_graph.raw_edges, key=lambda x: x.get_distance())
    for edge in sorted_edges:
        print edge
        u = edge.get_source()
        v = edge.get_destination()
        if find(u) != find(v):
            res.add(edge)
            union(u, v)
    return res


# weighted_graph = load_weighted_graph('data/bigraph_dpv5-3')
weighted_graph = load_weighted_graph('data/bigraph_dpv_Ex5-1')
result = kruskal(weighted_graph)
print '--------------------------result-------------------------------- '
for edge in result:
    print edge