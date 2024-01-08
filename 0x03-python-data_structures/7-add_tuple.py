#!/usr/bin/python3
def add_tuple(tuple_a, tuple_b):
    na_tuple = tuple_a + (0, 0)
    nb_tuple = tuple_b + (0, 0)
    sumt = (na_tuple[0] + nb_tuple[0], na_tuple[1] + nb_tuple[1])
    return sumt
