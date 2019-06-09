import math
from random import randint
from time import time
from merge_sort import merge_sort

def _bucket_sort(A, k):
    # Number of elements in A
    n = len(A)

    if (n <= 1):
        return A

    # Create k buckets
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

if __name__ == "__main__":

    A = [-6, 5, -4, 3, -2, 1]
    B = [10, 5, 0, 2, 15]
    C = [10, 2]
    D = [-1]
    
    print("Unsorted A: ", A)
    A = bucket_sort(A, 100)
    print("Sorted A:   ", A)
    
    print("Unsorted B: ", B)
    B = bucket_sort(B, 100)
    print("Sorted B:   ", B)
    
    print("Unsorted C: ", C)
    C = bucket_sort(C, 100)
    print("Sorted C:   ", C)
    
    print("Unsorted D: ", D)
    D = bucket_sort(D, 100)
    print("Sorted D:   ", D)
