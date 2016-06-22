# coding=utf-8
import array


###########################################################################################
# 例1 0-1交换
# 把一个0-1串（只包含0和1的串）进行排序，你可以交换任意两个位置，问最少交换的次数？
###########################################################################################

# 利用类似于快排的“partition”动作
def sort_string(in_string):
    string = array.array('c', in_string)
    i = 0
    j = len(string) - 1

    while 1:
        while string[i] == '0':
            i += 1
        while string[j] == '1':
            j -= 1
        if i > j:
            break
        string[i], string[j] = string[j], string[i]
    return string.tostring()


# string_array = '010100100101010100001001111111'
# string2 = '011001'
#
# print 'source string', string_array
# print 'result', sort_string(string_array)
# print 'source string', string2
# print 'result', sort_string(string2)


##################################################################################################
# 例2 字符替换和复制
# 删除一个字符串所有的a,并且复制所有的b。注：字符数组足够大
##################################################################################################
# 方法：对于有重叠部分的，倒着来复制（C语言的malloc也是这样干的）
def dela_copyb(string_array):
    if not isinstance(string_array, array.array):
        raise ValueError('Not a array')
    i = 0
    j = 0
    num_b = 0
    while string_array[i] != '\0':
        if string_array[i] != 'a':
            string_array[j] = string_array[i]
            j += 1  # count the number of all chars except 'a'
        if string_array[i] == 'b':
            num_b += 1  # count the number of 'b'
        i += 1
    new_last = j + num_b
    string_array[new_last] = '\0'
    while new_last > 0:  # 倒着来复制，j 永远也追不上 new_last
        new_last -= 1
        j -= 1
        string_array[new_last] = string_array[j]
        if string_array[j] == 'b':
            new_last -= 1
            string_array[new_last] = 'b'
    return string_array[:string_array.index('\0') + 1]


# string_array1 = array.array('c', 'accccaacacbbacdacbabcabccaabacab\0                          ')
# print string_array1
# print dela_copyb(string_array1)

##################################################################################################
# 例3 一个字符串只包含*和数字，请把它的*号都放开头。
##################################################################################################
# 方法1：快排partition，但数字的顺序会发生改变
def put_star_begin1(in_string):
    string = array.array('c', in_string)
    i = 0
    j = len(string) - 1
    while 1:
        while string[i] == '*':
            i += 1
        while string[j] != '*':
            j -= 1
        if i > j:
            break
        string[i], string[j] = string[j], string[i]
    return string.tostring()


# 方法2：倒着
def put_star_begin2(in_string):
    string = array.array('c', in_string)
    length = len(string)
    idx = length - 1
    for j in range(length - 1, -1, -1):
        if string[j] != '*':
            string[idx] = string[j]
            idx -= 1
    string[:idx + 1] = array.array('c', ['*'] * (idx + 1))
    return string.tostring()


# string = '**232*4343*43'
# print put_star_begin1(string)
# print put_star_begin2(string)


##################################################################################################
# 例4 子串变位词
# 给定两个串a和b，问b是否是a的子串的变位词。
# 例如输入a = hello, b = lel, lle, ello都是true,但是b = elo是false。 （国外某公司最新面试题）
##################################################################################################
def substring_anagram(base_string, substring):
    len_base = len(base_string)
    len_sub = len(substring)
    if len_sub > len_base:
        return
    count = [0] * 26
    non_zero_char = 0
    for i in range(len_sub):
        curr_char_num = ord(substring[i]) - ord('a')
        count[curr_char_num] += 1
        if count[curr_char_num] == 1: #new char
            non_zero_char += 1

    #第一个窗口
    for i in range(len_sub):
        curr_char_num = ord(base_string[i]) - ord('a')
        count[curr_char_num] -= 1
        if count[curr_char_num] == 0:
            non_zero_char -= 1
        if count[curr_char_num] == -1:  #minus too many(base substring has more occurrence of the curr char)
            non_zero_char += 1
    if non_zero_char == 0:
        return True

    #其他窗口
    for i in range(len_sub, len_base):
        last_first_char_num = ord(base_string[i - len_sub]) - ord('a')
        count[last_first_char_num] += 1
        if count[last_first_char_num] == 0: #说明之前为-1，丢弃后才匹配
            non_zero_char -= 1
        if count[last_first_char_num] == 1: #说明之前为0，丢弃后反而不匹配了
            non_zero_char += 1

        curr_char_num = ord(base_string[i]) - ord('a')
        count[curr_char_num] -= 1
        if count[curr_char_num] == 0:
            non_zero_char -= 1
        if count[curr_char_num] == -1:
            non_zero_char += 1
        if non_zero_char == 0:
            return True
    return False

base_string = 'hello'
substring = 'lool'
print substring_anagram(base_string, substring)




