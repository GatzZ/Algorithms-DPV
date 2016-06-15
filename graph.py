class Node(object):
    """docstring for Node"""

    def __init__(self, name):
        super(Node, self).__init__()
        self.name = name

    def get_name(self):
        return self.name

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return self.name == other.name

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return self.name.__hash__()


class Edge(object):
    """docstring for Edge"""

    def __init__(self, src, dest):
        super(Edge, self).__init__()
        self.src = src
        self.dest = dest

    def get_source(self):
        return self.src

    def get_destination(self):
        return self.dest

    def __str__(self):
        return '{0}->{1}'.format(self.src, self.dest)


class Digraph(object):
    """docstring for Digraph"""

    def __init__(self):
        super(Digraph, self).__init__()
        self.nodes = set()
        self.raw_edges = set()
        self.edges = {}

    def __getitem__(self, name):
        for node in self.nodes:
            if name == str(node):
                return node

    def add_node(self, node):
        if not (node in self.nodes):
            self.nodes.add(node)
            self.edges[node] = []
            # if node in self.nodes:
            #     raise ValueError('Duplicate Node')
            # else:
            #     self.nodes.add(node)
            #     self.edges[node] = []

    def add_edge(self, edge):
        self.raw_edges.add(edge)
        src = edge.get_source()
        dest = edge.get_destination()
        if not (src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)

    def reverse(self):
        rev_graph = Digraph()
        rev_graph.nodes = self.nodes
        for node in rev_graph.nodes:
            rev_graph.edges[node] = []
        for src in self.edges:
            dest_ls = self.edges[src]
            for dest in dest_ls:
                rev_graph.edges[dest].append(src)
        return rev_graph

    def children_of(self, node):
        return self.edges[node]

    def has_node(self, node):
        return node in self.nodes

    def __str__(self):
        res = ''
        for k in self.edges:
            for d in self.edges[k]:
                res = '{0}{1}->{2}\n'.format(res, k, d)
        return res[:-1]


class WeightedEdge(Edge):
    """docstring for weighted_edge"""

    def __init__(self, src, dest, distance):
        super(WeightedEdge, self).__init__(src, dest)
        self.distance = distance

    def get_distance(self):
        return self.distance

    def __str__(self):
        return '{0}->{1} ({2})'.format(self.src, self.dest, self.distance)


class WeightedDigraph(Digraph):
    """docstring for weighted_digraph"""

    def __init__(self):
        super(WeightedDigraph, self).__init__()

    def add_edge(self, edge):
        self.raw_edges.add(edge)
        src = edge.get_source()
        dest = edge.get_destination()
        if not (src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        self.edges[src].append((dest, edge.get_distance()))

    def childrenOf(self, node):
        return [tmp[0] for tmp in self.edges[node]]

    def __str__(self):
        res = ''
        for k in self.edges:
            for d in self.edges[k]:
                res = '{0}{1}->{2} ({3})\n'.format(res, k.getName(), d[0], float(d[1]))
        return res[:-1]


class WeightedBigraph(WeightedDigraph):
    def __init__(self):
        super(WeightedBigraph, self).__init__()

    def add_edge(self, edge):
        self.raw_edges.add(edge)
        src = edge.get_source()
        dest = edge.get_destination()
        if not (src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        self.edges[src].append((dest, edge.get_distance()))
        self.edges[dest].append((src, edge.get_distance()))


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

    def add_edge(self, src, dest, w=0):
        if src == dest:
            raise ValueError("src == dest")
        if not (src in self.nodes and dest in self.nodes):
            raise ValueError("src or dest not exist")
        edge = FlowEdge(src, dest, w)
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
                path = self.find_augmenting_path(edge.dest, sink, path + [edge])
            return path

    def ford_fulkerson(self, source, sink):
        path = self.find_augmenting_path(source, sink, [])
        while path != None:
            residuals = [edge.capacity - self.flow[edge] for edge in path]
            bottle_flow = min(residuals)
            for edge in path:
                self.flow[edge] += bottle_flow
                self.flow[edge.redge] -= bottle_flow
            path = self.find_augmenting_path(source, sink, [])
        return sum(self.flow[edge] for edge in self.adj[source])



def load_digraph(filename):
    with open(filename) as f:
        digraph = Digraph()
        for line in f:
            words = line.split()
            src = Node(words[0])
            dest = Node(words[1])
            digraph.add_node(src)
            digraph.add_node(dest)
            edge = Edge(src, dest)
            digraph.add_edge(edge)

    return digraph


def load_bigraph(filename):
    with open(filename) as f:
        bigraph = Digraph()
        for line in f:
            words = line.split()
            src = Node(words[0])
            dest = Node(words[1])
            bigraph.add_node(src)
            bigraph.add_node(dest)
            edge = Edge(src, dest)
            bigraph.add_edge(edge)
            edge = Edge(dest, src)
            bigraph.add_edge(edge)

    return bigraph


def load_weighted_digraph(filename):
    with open(filename) as f:
        weighted_digraph = WeightedDigraph()
        for line in f:
            words = line.split()
            src = Node(words[0])
            dest = Node(words[1])
            weighted_digraph.add_node(src)
            weighted_digraph.add_node(dest)
            weighted_edge = WeightedEdge(src, dest, float(words[2]))
            weighted_digraph.add_edge(weighted_edge)

    return weighted_digraph


def load_map(mapFilename):
    """ 
    Parses the map file and constructs a directed graph

    Parameters: 
        mapFilename : name of the map file

    Assumes:
        Each entry in the map file consists of the following four positive 
        integers, separated by a blank space:
            From To TotalDistance DistanceOutdoors
        e.g.
            32 76 54 23
        This entry would become an edge from 32 to 76.

    Returns:
        a directed graph representing the map
    """
    # TODO
    print "Loading map from file..."
    try:
        file = open(mapFilename, 'r')
    except Exception as e:
        print e
    mitMap = WeightedDigraph()

    for line in file:
        words = line.split()
        try:
            na = Node(words[0])
            nb = Node(words[1])
            mitMap.addNode(na)
            mitMap.addNode(nb)
        except Exception as e:
            pass
        try:
            na = Node(words[0])
            nb = Node(words[1])
            edge = WeightedEdge(na, nb, int(words[2]), int(words[3]))
            mitMap.addEdge(edge)
        except Exception as e:
            pass
    file.close()
    return mitMap
