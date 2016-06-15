# time complexity: O(mn)
def LCS(str_a, str_b):
    n_row, n_col = len(str_a) + 1, len(str_b) + 1
    L = [[0] * n_col for i in xrange(n_row)]
    for i in xrange(1, n_row):
        for j in xrange(1, n_col):
            if str_a[i - 1] == str_b[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
    # print matrix
    for row in L:
        print row
    return get_max_idx(L)


def get_max_idx(mat):
    curr_max = -10000000000000
    max_i = -1
    max_j = -1
    for i in xrange(len(mat)):
        for j in xrange(len(mat[i])):
            if mat[i][j] > curr_max:
                curr_max = mat[i][j]
                max_i = i
                max_j = j
    return max_i, max_j


str_a = "UNNSAAAABC"
str_b = "KKAAAABCSNA"

r, c = LCS(str_a, str_b)
print r, c
print str_a[:r]
print str_b[:c]
