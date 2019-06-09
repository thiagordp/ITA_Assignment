from math import floor
from random import randint
from time import time

_RANGE = 9
_N_MAX_DIGITS = 10

def _get_k_element(n, k):
    """
    Get the k'th element in integer n.
    :param n: Integer n
    :param k: k'th element
    :return:
    """
    x = floor(n / (10 ** k))
    y = x % (_RANGE + 1)

    return y

def counting_sort(A, k):
    """
    Counting sort algorithm
    :param A: Original array
    :param k: Position to sort
    :return: Permutation of A in sorted order
    """
    
    # Create the array of (n-m)+1 positions
    count_array = [0 for i in range(_RANGE + 1)]

    # Calculate the counting
    for i in range(len(A)):
        x = _get_k_element(A[i], k)
        count_array[x] = count_array[x] + 1

    # Modify the counting array so that each index is the sum of previous countings
    # Starting from the second position in the array
    for i in range(1, len(count_array)):
        count_array[i] = count_array[i - 1] + count_array[i]

    b = [0 for i in range(len(A))]

    # Insert the elements into order
    for i in range(len(A) - 1, -1, -1):
        elem = _get_k_element(A[i], k)
        count_array[elem] = count_array[elem] - 1
        pos = count_array[elem]
        b[pos] = A[i]

    # Copy to the output
    for i in range(len(A)):
        A[i] = b[i]

def _radix_sort(A):
    if len(A) > 0:
        max_elem = max(A)

        i = 0
        while floor(max_elem / (10 ** i)) > 0:
            counting_sort(A, i)
            i += 1

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

if __name__ == "__main__":

    A = [-2, 14, 1, 2, 1, 8]
    B = [6, 23, 12, 13]
    C = [10, -1]
    D = [-1]
    
    print("Unsorted A: ", A)
    radix_sort(A)
    print("Sorted A:   ", A)
    
    print("Unsorted B: ", B)
    radix_sort(B)
    print("Sorted B:   ", B)
    
    print("Unsorted C: ", C)
    radix_sort(C)
    print("Sorted C:   ", C)
    
    print("Unsorted D: ", D)
    radix_sort(D)
    print("Sorted D:   ", D)
