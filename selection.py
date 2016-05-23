#Find the k-th smallest number in the list
import random

def median_of_three(a, b, c):
    if a < b:
        if b < c:
            return b
        #If come to this step, means b is largest
        elif a < c:
            return c
        else:
            return a
    else: #a >= b
        if b > c:
            return b
        #If come to step, means a is largest
        else:
            return c


def selection(array, k):
    if k <= 0 or k > len(array):
        return
    pivot = random.choice(array)
    sub_left, sub_mid, sub_right = split(array, pivot)
    if k <= len(sub_left):
        return selection(sub_left, k)
    elif len(sub_left) < k and k <= len(sub_left) + len(sub_mid):
        return pivot
    else:
        return selection(sub_right, k - len(sub_left) - len(sub_mid))


def split(array, v):
    sub_left = []
    sub_mid = []
    sub_right = []
    for item in array:
        if item < v:
            sub_left.append(item)
        elif item == v:
            sub_mid.append(item)
        else:
            sub_right.append(item)
    return sub_left, sub_mid, sub_right

a = [2, 3, 1, 4]

print selection(a, 0)


