# coding=utf-8
# Ex 6.1
def largest_subsequence_sum(seq):
    max_sum_list = [elem for elem in seq]
    max_curr_sum = 0
    max_start = 0
    curr_start = 0
    max_end = 0
    for i in xrange(1, len(seq)):
        if max_sum_list[i - 1] + seq[i] > max_sum_list[i]:
            max_sum_list[i] = max_sum_list[i - 1] + seq[i]
        if max_sum_list[i] > max_curr_sum:
            max_curr_sum = max_sum_list[i]
            max_end = i
            max_start = curr_start
        if max_sum_list[i - 1] + seq[i] < 0:  # 遇到一个令子序列总和<0的数，重新开始算
            curr_start = i + 1
    return max_sum_list, max_start, max_end


# seq = [5, 15, -30, 10, -5, 40, 10]
seq = [-5, 4, -20, 16, -2, -3]
max_sum, max_start, max_end = largest_subsequence_sum(seq)
print max_sum
print max_start
print max_end
