def heap_insert(h, x):
    bubble_up(h, x, len(h) + 1)


# def heap_decreasekey(h, x):
#     bubble_up(h, x, pos[x])


def delete_min(h):
    if len(h) <= 1:
        raise ValueError('Empty heap')
    x = h[1]
    last = h.pop()
    if len(h) > 1:
        sift_down(h, last, 1)
    return x


def bubble_up(h, x, i):
    p = (i + 1) / 2
    while i != 1 and h[p] > x:
        h[i] = h[p]
        i = p
        p = (i + 1) / 2
    h[i] = x


def sift_down(h, x, i):
    c = min_child(h, i)  # c==0, if no children
    while c != 0 and h[c] < x:
        h[i] = h[c]
        i = c
        c = min_child(h, i)
    # print i
    h[i] = x


def min_child(h, i):
    if 2 * i > len(h) - 1:
        return 0  # no children
    elif len(h) - 1 < 2 * i + 1 or h[2 * i] < h[2 * i + 1]:
        return 2 * i
    else:
        return 2 * i + 1


def make_heap(h):
    h.insert(0, 'heap_head')
    for i in xrange(len(h) - 1, 0, -1):
        sift_down(h, h[i], i)


def heap_sort(h):
    res = []
    make_heap(h)
    while len(h) > 1:
        print 'heap before', h
        res.append(delete_min(h))
        print 'res:', res
        print 'heap after', h
    return res


h = [2, 1, 3, 5, 4, -1, -2, 10, 9, 1888, 33]
res = heap_sort(h)
print res
