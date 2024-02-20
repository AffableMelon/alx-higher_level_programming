#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    k = list(a_dictionary.keys())
    k.sort()
    for i in k:
        print(i + ":".format(i), end=' ')
        print(a_dictionary[i])
