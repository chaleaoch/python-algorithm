# -*- coding: utf-8 -*-
__author__ = 'zhichao'

import random

def bubble_sort(a_list):
    while True:
        is_sorted = True
        for location in range(1,len(a_list)):
            if a_list[location] < a_list[location-1]:
                is_sorted = False
                a_list[location],a_list[location-1] = a_list[location-1],a_list[location]
        if is_sorted:
            break

test_list = [random.randint(0,1000) for item in range(100)]
print test_list
bubble_sort(test_list)
print test_list