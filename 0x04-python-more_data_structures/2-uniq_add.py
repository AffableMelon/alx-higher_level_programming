#!/usr/bin/python3
def uniq_add(my_list=[]):
    newl = []
    sum = 0
    for i in my_list:
        if i in newl:
            pass
        else:
            newl.append(i)
    for i in newl:
        sum += i
    return sum
