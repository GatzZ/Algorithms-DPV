# Ex 5.18
class HuffmanNode(object):
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.name) + ' ' + str(self.left) + ' ' + str(self.right)


def huffuman_tree(freq):
    import Queue
    pq = Queue.PriorityQueue()
    for item in freq:
        pq.put(item)
    # while pq.qsize() > 1:
    for it in range(len(freq) - 1):
        i = pq.get()
        j = pq.get()
        node_ij = HuffmanNode(j, i)
        pq.put((i[0] + j[0], node_ij))

    return pq.get()  # return the root


# Recursively walk the tree down to the leaves,
# assigning a code value to each symbol
def encoding(node, prefix="", code={}):
    if isinstance(node[1].left[1], HuffmanNode):
        encoding(node[1].left, prefix + "0", code)
    else:
        code[node[1].left[1]] = prefix + "0"
    if isinstance(node[1].right[1], HuffmanNode):
        encoding(node[1].right, prefix + "1", code)
    else:
        code[node[1].right[1]] = prefix + "1"
    return code


def avg_bit_cost(code, freq_char):
    res = 0
    for char in freq_char:
        res += char[0] * len(code[char[1]])
    return res


def compute_entropy(freq_char):
    import math
    res = 0
    for freq, char in freq_char:
        res += freq * math.log(1 // freq, 2)
    return res

# freq = [(0.5, 'A'), (0.25, 'B'), (0.125, 'C'), (0.125, 'D')]
freq_char = [(0.173, ' '), (0.102, 'e'), (0.077, 't'), (0.068, 'a'), (0.059, 'o'), (0.058, 'i'), (0.055, 'n'), (0.051, 's'),
             (0.049, 'h'), (0.048, 'r'), (0.035, 'd'), (0.034, 'l'), (0.026, 'c'), (0.024, 'u'), (0.021, 'm'), (0.019, 'w'),
             (0.018, 'f'), (0.017, 'g'), (0.016, 'y'), (0.016, 'p'), (0.013, 'b'), (0.009, 'v'), (0.006, 'k'), (0.002, 'j'),
             (0.002, 'x'), (0.001, 'q'), (0.001, 'z')]

root = huffuman_tree(freq_char)

code = encoding(root)
for i in sorted(freq_char, reverse=True):
    print i[1], '{:6}'.format(i[0]), code[i[1]]

print 'average encoding cost', avg_bit_cost(code, freq_char)
print 'entropy', compute_entropy(freq_char)