#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    outli = my_list.copy()
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            outli[i] = True
        else:
            outli[i] = False
    return outli
