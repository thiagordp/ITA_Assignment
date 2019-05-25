from math import floor

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


if __name__ == "__main__":
    print("Counting Sort")

    A = [1, 22, 43, 12, 50, 2, 4, 3]
    counting_sort(A, 0)

    print(A)

    counting_sort(A, 1)
    print(A)
