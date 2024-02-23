#!/usr/bin/python3
def weight_average(my_list=[]):
    sum = 0
    tot = 0
    for (x, y) in my_list:
        sum += (x*y)
        tot += y
    return (float(sum/tot))
