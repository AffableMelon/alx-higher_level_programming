#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    second_list = my_list.copy()
    if idx < 0 or idx >= len(my_list):
        return second_list
    else:
        second_list[idx] = element
        return second_list
