from collections import namedtuple


def least_matrix_multipication_times(mat_list):
    length = len(mat_list)
    cost = [[float('inf')] * length for i in xrange(length)]
    for i in xrange(length):
        cost[i][i] = 0

    for scope in xrange(1, length):  # scope in [1...., length-1]
        for i in xrange(length - scope):  # i in [0,...length - scope - 1]
            j = i + scope  # j in [1, ..., length - 1]
            print i, j
            for k in xrange(i, j):
                tmp = cost[i][k] + cost[k + 1][j] + (mat_list[i].m * mat_list[k].n * mat_list[j].n)
                print tmp
                if cost[i][j] > tmp:
                    cost[i][j] = tmp
    for row in cost:
        print row
    return cost[0][-1]


Matrix = namedtuple('Matrix', ['m', 'n'])
mat_a = Matrix(50, 20)
mat_b = Matrix(20, 1)
mat_c = Matrix(1, 10)
mat_d = Matrix(10, 100)
mat_list = [mat_a, mat_b, mat_c, mat_d]
print least_matrix_multipication_times(mat_list)
