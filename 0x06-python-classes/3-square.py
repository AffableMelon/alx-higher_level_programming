#!/usr/bin/python3
'''
This file creates a Square class and defines a method square based on
1. private instance size
2. init size (none)
'''


class Square:

    """ represent a square"""
    def __init__(self, size=0):
        if type(size) != int:
            raise (TypeError("size must be an integer"))
        elif size < 0:
            raise (ValueError("size must be >= 0"))
        else:
            self.__size = size

    def area(self):
        """gives the current square(geometric side) area"""
        print("Area: {:d}".format(self.__size * self.__size))
