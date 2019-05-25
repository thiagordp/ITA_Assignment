import math
from random import randint
from time import time

from merge_sort import merge_sort


def bucket_sort(A, k):
    """
    Bucket sort implementation
    :param A: Array
    :param k: Number of Buckets
    :return: Array A in ascending sorted order
    """
    n = len(A)

    P = []
    N = []

    # Divide the elements in two subarrays:
    # - Positive elements
    # - Negative Elements
    for i in range(n):
        if A[i] >= 0:
            P.append(A[i])
        else:
            N.append((-1) * A[i])

    _A = []

    _P = _bucket_sort(P, k)
    _N = _bucket_sort(N, k)

    n_p = len(_P)
    n_n = len(_N)

    # Append Negative Elements
    for i in range(n_n):
        # Append elements in inverse order
        _A.append(_N[(n_n - 1) - i] * (-1))

    # Append Positive Elements
    for i in range(n_p):
        _A.append(_P[i])

    return _A


def _bucket_sort(A, k):
    # Number of elements in A
    n = len(A)

    if (n <= 1):
        return A

    # Create n buckets
    buckets = [[] for i in range(k)]
    # Maximum element in A
    m = max(A)

    # Insert the array elements in the buckets
    for i in range(n):
        # Decide which bucket will receive the element
        index = math.floor((k - 1) * (A[i] / m))
        # Insert the element
        buckets[index].append(A[i])

    # Sort each bucket
    for i in range(k):
        n_b = len(buckets[i])

        # Sort only if there are one or more elements in the bucket 'i'.
        if n_b > 0:
            merge_sort(buckets[i], 0, n_b - 1)

    _A = []

    # Join the buckets
    for i in range(k):
        n_b = len(buckets[i])

        for j in range(n_b):
            _A.append(buckets[i][j])

    return _A


if __name__ == "__main__":
    print("Generating Random Array...")

    t1 = time()
    A = [randint(-2 ** 32, 2 ** 32) for p in range(0, 100000)]
    t2 = time()

    print(t2 - t1)
    print("Sorting...")
    t1 = time()
    B = bucket_sort(A, 100000)
    t2 = time()

    print(t2 - t1)

#    print("###############################")
#    for i in range(len(A)):
#        print(A[i])
#    print("###############################")
#    for i in range(len(B)):
#        print(B[i])
