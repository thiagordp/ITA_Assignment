from math import floor
from random import randint
from time import time

from counting_sort import counting_sort

def radix_sort(A):
    n = len(A)

    p_n = []
    n_n = []

    # Create Positive and Negative Arrays
    for i in range(n):
        if A[i] < 0:
            n_n.append((-1) * A[i])
        else:
            p_n.append(A[i])

    # Sort each Array
    _radix_sort(n_n)
    _radix_sort(p_n)

    Nn = len(n_n)
    Np = len(p_n)

    # Merge the results

    # Include Negatives in inverse order
    for i in range(Nn):
        ind = (Nn - 1) - i
        A[i] = (-1) * n_n[ind]

    # Include Positives in order starting after the last negative.
    for i in range(Np):
        ind = (Nn + i)
        A[ind] = p_n[i]


def _radix_sort(A):
    if len(A) > 0:
        max_elem = max(A)

        i = 0
        while floor(max_elem / (10 ** i)) > 0:
            counting_sort(A, i)
            i += 1


if __name__ == "__main__":
    print("Generating Random Array...")

    t1 = time()
    A = [randint(-2 ** 32, 2 ** 32) for p in range(0, 4 ** 4)]
    t2 = time()

    print(t2 - t1)
    print(A)
    t1 = time()
    radix_sort(A)
    t2 = time()

    print(A)
    print(t2 - t1)
