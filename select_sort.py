# -*- coding: utf-8 -*-
__author__ = 'zhichao'
import random

def select_sort(a_list):
    location = a_list.__len__() - 1
    while True:
        max_value = a_list[0]
        max_location = 0
        for index in range(1,location+1):
            if a_list[index] > max_value:
                max_location = index
                max_value = a_list[index]
        a_list[max_location],a_list[location] = a_list[location], a_list[max_location]
        location -= 1
        if location == 0:
            break

test_list = [random.randint(0, 1000) for item in range(100)]
print test_list
select_sort(test_list)

print test_list