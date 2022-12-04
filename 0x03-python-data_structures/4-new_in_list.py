#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    my_cpylist = my_list.copy()
    if idx < 0 or idx >= len(my_list):
        return my_cpylist
    my_cpylist[idx] = element
    return my_cpylist
