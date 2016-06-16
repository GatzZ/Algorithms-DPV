from graph import *


def hungarian_method(bipartie):
    matched_dict = {}
    matched_nodes = set()
    used = set()
    count = 0

    def find(node):
        for neighbor in bipartie.edges[node]:
            if neighbor in used:  # if used then no need to search again
                continue
            used.add(neighbor)
            if neighbor not in matched_nodes:
                matched_nodes.add(neighbor)
                matched_nodes.add(node)
                matched_dict[node] = neighbor
                matched_dict[neighbor] = node
                return True
            else:
                if find(neighbor):
                    matched_nodes.add(neighbor)
                    matched_nodes.add(node)
                    matched_dict[node] = neighbor
                    matched_dict[neighbor] = node
                    return True
        return False

    for node in bipartie.nodes:
        used.clear()
        if find(node):
            count += 1
    print 'Number of match', count
    return matched_dict


bipartie = load_digraph("data/bipartie_dpv-EX7-24")
matched_dict = hungarian_method(bipartie)

for key in matched_dict:
    print key, matched_dict[key]
