from math import floor
from random import randint
from time import time

from counting_sort import counting_sort


def radix_sort(A):
    """
    Radix Sort Implementation
    :param A: Array A
    :return:
    """

    max_elem = max(A)

    i = 0
    while floor(max_elem / (10 ** i)) > 0:
        counting_sort(A, i)
        i += 1


if __name__ == "__main__":
    print("Generating Random Array...")

    t1 = time()
    A = [randint(0, 2 ** 8) for p in range(0, 4 ** 10)]
    t2 = time()

    print(t2 - t1)
    print(A)
    t1 = time()
    radix_sort(A)
    t2 = time()

    print(A)
    print(t2 - t1)
