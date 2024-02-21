#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newm = []
    for count in range(len(matrix)):
        k = matrix[count].copy()
        for i in range(len(k)):
            j = (k[i] ** 2)
            k[i] = j
        newm.append(k)
    return (newm)
