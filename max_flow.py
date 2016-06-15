class FlowEdge(object):
    def __init__(self, u, v, w):
        self.src = u
        self.dest = v
        self.capacity = w
        self.rev_edge = None

    def __str__(self):
        return "%s->%s:%s" % (self.src, self.dest, self.capacity)


class FlowNetwork(object):
    def __init__(self):
        self.nodes = set()
        self.adj = {}
        self.flow = {}

    def add_node(self, node):
        if not node in self.nodes:
            self.nodes.add(node)
            self.adj[node] = []

    def add_edge(self, src, dest, capacity):
        if src == dest:
            raise ValueError("src == dest")
        if not (src in self.nodes and dest in self.nodes):
            raise ValueError("src or dest not exist")
        edge = FlowEdge(src, dest, capacity)
        rev_edge = FlowEdge(dest, src, 0)
        edge.rev_edge = rev_edge
        rev_edge.rev_edge = edge
        self.adj[src].append(edge)
        self.adj[dest].append(rev_edge)
        self.flow[edge] = 0
        self.flow[rev_edge] = 0

    def find_augmenting_path(self, src, sink, path):
        if src == sink:
            return path
        # BFS to find a shortest augmenting path
        for edge in self.adj[src]:
            residual = edge.capacity - self.flow[edge]
            if residual > 0 and edge not in path:
                result = self.find_augmenting_path(edge.dest, sink, path + [edge])
                if result:
                    return result

    def ford_fulkerson(self, source, sink):
        path = self.find_augmenting_path(source, sink, [])
        while path != None:
            residuals = [edge.capacity - self.flow[edge] for edge in path]
            bottle_flow = min(residuals)
            for edge in path:
                self.flow[edge] += bottle_flow
                self.flow[edge.rev_edge] -= bottle_flow
            for edge in self.flow:
                print edge, self.flow[edge]
            print '---------------------------------------------------------'
            path = self.find_augmenting_path(source, sink, [])
        return sum(self.flow[edge] for edge in self.adj[source])


g = FlowNetwork()
print [g.add_node(v) for v in "sopqrt"]
g.add_edge('s', 'o', 3)
g.add_edge('s', 'p', 3)
g.add_edge('o', 'p', 2)
g.add_edge('o', 'q', 3)
g.add_edge('p', 'r', 2)
g.add_edge('r', 't', 3)
g.add_edge('q', 'r', 4)
g.add_edge('q', 't', 2)
print (g.ford_fulkerson('s', 't'))
