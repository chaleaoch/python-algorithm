# -*- coding: utf-8 -*-
__author__ = 'zhichao'

import sys

sys.setrecursionlimit(10000)


def binary_search(a_list, item, low, high):
    middle = (low + high) / 2
    if item == a_list[middle]:
        return middle
    elif item > a_list[middle]:
        return binary_search(a_list, item, middle + 1, high)
    else:
        return binary_search(a_list, item, low, middle - 1)


test_list = range(100, 1000)
print binary_search(test_list, 666, 0, len(test_list) - 1)
