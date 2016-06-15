from graph import *
from collections import namedtuple

def longest_increasing_subsequence(seq):
    def get_max_idx(seqnode_list):
        if not seqnode_list:
            return -1
        return max(seqnode_list, key=lambda x: l[x.idx]).idx

    SeqNode = namedtuple('SeqNode', ['idx', 'value'])
    edge_reverse = {SeqNode(idx, node): [] for idx, node in enumerate(seq)}
    print edge_reverse
    length = len(seq)
    l = [1] * length
    prev = {idx: -1 for idx in xrange(length)}
    for i in xrange(length):
        for j in xrange(i + 1, len(seq)):
            if seq[i] < seq[j]:
                edge_reverse[SeqNode(j, seq[j])].append(SeqNode(i, seq[i]))
    print edge_reverse
    for idx in xrange(length):
        prev_idx = get_max_idx(edge_reverse[SeqNode(idx, seq[idx])])
        if prev_idx != -1:
            l[idx] = 1 + l[prev_idx]
            prev[idx] = prev_idx
    return max(enumerate(l), key=lambda x: x[1]), prev


def rebulid_path(prev, dest_node):
    path = [dest_node]
    while prev[dest_node] != -1:
        path.append(prev[dest_node])
        dest_node = prev[dest_node]
    path.reverse()
    return path


seq = [5, 2, 8, 6, 3, 6, 9, 7]
(idx, max_len), prev = longest_increasing_subsequence(seq)
print rebulid_path(prev, idx)
