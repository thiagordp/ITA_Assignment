import math
import sys

def merge_sort(A, p, r):
    """
    Merge sort alg implememtation
    :param A: Array
    :param p: Start index (inclusive)
    :param r: Final index (inclusive)
    :return: Array A in ascending sorted order
    """
    if p < r:
        q = math.floor((p + r) / 2)

        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)

        merge(A, p, q, r)


def merge(A, p, q, r):
    """
    Merges two sorted subarrays into one.
    :param A: Original array
    :param p: start index from the first subarray
    :param q: final index from the first subarray / q+1: start index from the second subarray
    :param r: final index from the final subarray
    :return: Subarray with merged subarrays in sorted order
    """

    n1 = q - p + 1
    n2 = r - q

    la = []
    ra = []

    for i in range(0, n1):
        la.append(A[p + i])

    for j in range(0, n2):
        ra.append(A[(q + 1) + j])

    la.append(sys.maxsize)
    ra.append(sys.maxsize)

    i = j = 0
    
    # The second parameter from range() is exclusive. Thus, it's needed to add "+1" to include the index 'r'
    for k in range(p, r + 1):
        if la[i] <= ra[j]:
            A[k] = la[i]
            i = i + 1
        else:
            A[k] = ra[j]
            j = j + 1

if __name__ == '__main__':

    A = [12, 0, 2, 7, 1, -2]
    B = [-1, -2, -3, 4]
    C = [1, -1]
    D = [-1]


    print("Unsorted A: ", A)
    n = len(A) - 1
    merge_sort(A, 0, n)
    print("Sorted A:   ", A)
    
    print("Unsorted B: ", B)
    n = len(B) - 1
    merge_sort(B, 0, n)
    print("Sorted B:   ", B)
    
    print("Unsorted C: ", C)
    n = len(C) - 1
    merge_sort(C, 0, n)
    print("Sorted C:   ", C)
    
    print("Unsorted D: ", D)
    n = len(D) - 1
    merge_sort(D, 0, n)
    print("Sorted D:   ", D)

