from datetime import datetime
from math import floor
from random import randint
from time import time


def insertion_sort(A):
    """
    Sort by insertion.
    :param A: Original array
    :return: Subarray with merged subarrays in sorted order
    """

    n = len(A)
    t1 = time()
    for j in range(1, n):


        key = A[j]

        # Insert A[j] into the sorted sequence A[1, ..., j-1]
        i = j - 1

        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i = i - 1

        A[i + 1] = key

        if j % 10000 == 0:
            t2 = time()
            print(floor(j / 10000), " | ", datetime.now(), " | ", t2 - t1)
            t1 = time()
    return A


if __name__ == '__main__':
    print("Generating Random Array...")
    A = [randint(-2 ** 32, 2 ** 32) for p in range(0, 100000)]

    t1 = time()
    print("Sorting...")
    insertion_sort(A)
    t2 = time()
    print("Time: ", (t2 - t1))
    print("Sorted:", A)
