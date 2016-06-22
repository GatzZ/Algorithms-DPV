from graph import *


def find(node):
    for neighbor in bipartie.edges[node]:
        if neighbor not in used:  # if used then no need to search again
            used.add(neighbor)
            ####!!!not matched or the the owner of neighbor can find another partner?
            if (neighbor not in matched_dict) or (find(matched_dict[neighbor])):
                print node, neighbor, '----------5555555-----------'
                matched_dict[neighbor] = node
                return True
    return False


def hungarian_method(bipartie, count):
    tmp_nodes = []
    for node in bipartie.nodes:
        if str(node) in "ABCD":
            tmp_nodes.append(node)
    tmp_nodes.sort()
    for node in tmp_nodes:
        used.clear()
        if find(node):
            count += 1
        for key in matched_dict:
            print key, matched_dict[key]
        print '-----------------------------------'
    print 'Number of match', count
    return matched_dict


matched_dict = {}
used = set()
count = 0
bipartie = load_bigraph("data/bipartie_dpv-EX7-24")
# bipartie = load_bigraph("data/bipartie_1")
matched_dict = hungarian_method(bipartie, count)

for key in matched_dict:
    print key, matched_dict[key]
