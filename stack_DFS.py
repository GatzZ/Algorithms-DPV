from  graph import *
#Ex3.10
def stack_DFS(g):
    def previsit(node):
        ccnum[node] = component
        global _clock
        pre[node] = _clock
        print 'previsit', node, _clock
        _clock += 1

    def postvisit(node):
        global _clock
        post[node] = _clock
        print 'postvisit', node, _clock
        _clock += 1

    stack = []
    ccnum = {}
    pre = {}
    post = {}
    global _clock
    _clock = 1
    component = 0
    import copy
    not_visited_nodes = copy.copy(g.nodes)
    while not_visited_nodes:
        component += 1
        node = not_visited_nodes.pop()
        stack.append(node)
        previsit(node)
        while stack:
            curr_node = stack[-1]
            child_list = g.edges[curr_node]
            has_child_to_processed = False
            for child in child_list:
                if child in not_visited_nodes:
                    has_child_to_processed = True
                    stack.append(child)
                    not_visited_nodes.remove(child)
                    previsit(child)
                    break
            if not has_child_to_processed:
                last_node = stack.pop()
                postvisit(last_node)
                continue
    return pre, post, ccnum

bigraph = load_bigraph('data/bigraph_dpv_Ex3-1')
pre, post, ccnum = stack_DFS(bigraph)
for node in pre:
    print node, pre[node]

print '-------------------------------'

for node in post:
    print node, post[node]

print '-------------------------------'

for node in ccnum:
    print node, ccnum[node]