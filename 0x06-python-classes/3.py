#!/usr/bin/python3
'''
This file creates a Square class and defines a method square based on
1. private instance size
2. init size (none)
'''


class Square:

    """ represent a square"""
    try:
        def __init__(self, size=0):
            self.__size = size
        
        def square(self):
            pass

    except (size != int):
        return ("TypeError size must be an integer")

    except (size < 0):
        return ("ValueError size must be >=0")
