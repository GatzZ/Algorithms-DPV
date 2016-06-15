from graph import *


def prim(weighted_graph):
    import heapq
    INF = float('inf')
    res_node = []
    cost = {node: INF for node in weighted_graph.nodes}
    prev = {node: None for node in weighted_graph.nodes}
    start = weighted_graph['A']
    cost[start] = 0
    min_heap = [(cost[node], node) for node in weighted_graph.nodes]
    heapq.heapify(min_heap)
    while min_heap:
        src = heapq.heappop(min_heap)[1]
        res_node.append(src)
        for dest, weight in weighted_graph.edges[src]:
            if cost[dest] > weight:
                min_heap.remove((cost[dest], dest))  # remove the obsolete one
                cost[dest] = weight
                heapq.heappush(min_heap, (cost[dest], dest))  # add the new one
                prev[dest] = src
        for node in cost:
            print node, cost[node]
        print '-------------------'
    return cost, prev, res_node


weighted_graph = load_weighted_digraph('data/bigraph_dpv5-9')
# weighted_graph = load_weighted_graph('data/bigraph_dpv_Ex5-1')
cost, prev, res_node = prim(weighted_graph)

for node in res_node:
    print node,
    print
for node in prev:
    print node, prev[node]
