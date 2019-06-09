from datetime import datetime
from math import floor
from random import randint
from time import time


def insertion_sort(A):
    """
    Sort by insertion.
    :param A: Original array
    :return: Permutation of the original array in sorted order
    """

    n = len(A)

    for j in range(1, n):
        key = A[j]

        # Insert A[j] into the sorted sequence A[1, ..., j-1]
        i = j - 1

        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key
    return A

if __name__ == '__main__':
    A = [1, 50, -1, 0, 10, 2]
    B = [4, 3, 2, 1]
    C = [1, -1]
    D = [-1]

    print("Unsorted A: ", A)
    insertion_sort(A)
    print("Sorted A: ", A)
    
    print("Unsorted B: ", B)
    insertion_sort(B)
    print("Sorted B: ", B)
    
    print("Unsorted C: ", C)
    insertion_sort(C)
    print("Sorted C: ", C)
    
    print("Unsorted D: ", D)
    insertion_sort(D)
    print("Sorted D: ", D)

