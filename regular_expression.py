from graph import *
from dfs import dfs


class NFA(object):
    def __init__(self, re):
        self.ops = []
        self.G = Digraph()  # only epsilon transition !!!!!!!!
        self.M = len(re)
        self.re = re  # match transition

        for i in xrange(self.M):
            self.G.add_node(Node(i, re[i]))
        self.G.add_node(Node(self.M, "Accepted"))

        for i in xrange(self.M):
            lp = i
            if re[i] == "(" or re[i] == "|":
                self.ops.append(i)
            elif re[i] == ")":
                op_or = self.ops.pop()  # "|" or "("
                if re[op_or] == "|":
                    lp = self.ops.pop()
                    self.G.add_edge(Edge(self.G[lp], self.G[op_or + 1]))
                    self.G.add_edge(Edge(self.G[op_or], self.G[i]))
                else:
                    lp = op_or
            else:
                pass

            if i < self.M - 1 and re[i + 1] == "*":
                self.G.add_edge(Edge(self.G[lp], self.G[i + 1]))
                self.G.add_edge(Edge(self.G[i + 1], self.G[lp]))

            if re[i] == "(" or re[i] == "*" or re[i] == ")":
                self.G.add_edge(Edge(self.G[i], self.G[i + 1]))

    def recognizes(self, text):
        pc = set()
        pre, _, _ = dfs(self.G, [self.G[0]])
        for v in pre:
            pc.add(v)

        for c in text:
            match = set()
            for v in pc:
                if v.name < self.M:
                    if self.re[v.name] == c or self.re[v.name] == ".":  # matched
                        match.add(self.G[v.name + 1])
            pc.clear()
            pre, _, _ = dfs(self.G, match)
            for v in pre:
                pc.add(v)

        for v in pc:
            if v.name == self.M:
                return True
        return False


regexp = "(.*" + "(A*B|AC)D" + ".*)"
# regexp = "(" + "(A*B|AC)D" +")"
nfa = NFA(regexp)
tmp = nfa.G.edges
for src in tmp:
    for dest in tmp[src]:
        print str(src), str(dest)
with open("data/re_tiny") as f:
    for line in f:
        if nfa.recognizes(line):
            print "True"
            print line
