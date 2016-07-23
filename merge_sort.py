# -*- coding: utf-8 -*-
__author__ = 'zhichao'

import random

def merge_sort(a_list):
    if a_list.__len__() == 1:
        return a_list
    left_list = merge_sort(a_list[:a_list.__len__()/2])
    right_list = merge_sort(a_list[a_list.__len__() / 2:])
    ret_list = []
    while left_list and right_list:
        if left_list[0] > right_list[0]:
            # right_list.pop(0)并不一定是O(1)，此处不严谨，只是为了方便
            ret_list.append(right_list.pop(0))
        else:
            ret_list.append(left_list.pop(0))
    if left_list:
        ret_list.extend(left_list)
    else:
        ret_list.extend(right_list)
    return ret_list

test_list = [random.randint(0,1000) for item in range(100)]
print test_list
merge_sort(test_list)
print test_list