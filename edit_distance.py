def edit_distance(str_a, str_b):
    nrow, ncol = len(str_a) + 1, len(str_b) + 1
    dist = [[0] * ncol for i in xrange(nrow)]
    for i in xrange(nrow):
        dist[i][0] = i
    for j in xrange(ncol):
        dist[0][j] = j
    for i in xrange(1, nrow):
        for j in xrange(1, ncol):
            diff = 0 if str_a[i - 1] == str_b[j - 1] else 1
            dist[i][j] = min(1 + dist[i - 1][j], 1 + dist[i][j - 1], diff + dist[i - 1][j - 1])
    print_matrix(dist)
    return dist[-1][-1]


def print_matrix(x):
    for row in x:
        print row


# str_a = 'EXPONENTIAL'
# str_b = 'POLYNOMIAL'
str_a = 'SNOWY'
str_b = 'SUNNY'
result = edit_distance(str_a, str_b)
print 'result', result
