#!/usr/bin/python3

def uniq_add(my_list=[]):

    add = 0

    for idx in set(my_list):

        add += idx

    return add
