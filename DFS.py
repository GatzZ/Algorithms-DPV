# coding=utf-8
def dfs(g, src_list):
    def previsit(node):
        # import pdb; pdb.set_trace()
        ccnum[node] = component
        global _clock
        pre[node] = _clock
        # 引用在赋值之前，Python3有个关键字nonlocal可以解决这个问题，但在Python2中还是不要尝试修改闭包中的变量 （_clock）。
        _clock += 1  # 如果有重新赋值，python就认为__clock是个内部变量,而不是外部变量。所以我们用全局变量来定义_clock

    def postvisit(node):
        global _clock
        post[node] = _clock
        _clock += 1

    def explore(node):
        visited[node] = True
        previsit(node)
        for u in g.edges[node]:
            if not visited[u]:
                explore(u)
        postvisit(node)

    visited = {}
    ccnum = {}  # record the components. it is easily achieved in Undirected graph
    pre = {}
    post = {}
    global _clock
    _clock = 1
    component = 0

    for node in g.nodes:
        visited[node] = False

    for node in src_list:
        if not visited[node]:
            component += 1  # Just ecord the components in outer loop of DFS
            explore(node)
    return pre, post, ccnum
