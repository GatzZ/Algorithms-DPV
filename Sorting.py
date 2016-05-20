def merge(item1, item2):
    return item1 if item1 < item2 else item2


def enqueue(array, item):
    array.append(item)


def dequeue(array):
    if array:
        return array.pop(0)


def iterative_mergesort(array):
    while len(array) > 1:
        enqueue(array, merge(dequeue(array), dequeue(array)))
    return dequeue(array)


array = [3, 1, 4, 2, -1, 5, 8, 3, 9]
result = []
for i in range(len(array)):
    print array
    tmp = iterative_mergesort(array[:])
    array.remove(tmp)
    result.append(tmp)

print result
