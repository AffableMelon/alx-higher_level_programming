#!/usr/bin/python3
def print_last_digit(number):
    l_digit = abs(number) % 10

    print("{:d}".format(l_digit), end='')
    return (l_digit)
