#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    ln = len(my_list) - 1
    while ln >= 0:
        print("{:d}".format(my_list[ln]))
        ln -= 1
