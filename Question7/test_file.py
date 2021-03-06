"""
Imports
"""
from random import randint
from time import time

from bucket_sort import bucket_sort
from insertion_sort import insertion_sort
from merge_sort import merge_sort
from radix_sort import radix_sort

"""
Constants
"""

# Maximum size of integer numbers
N_BITS = 32
N_DIGITS = 10

# Size of each array tested
ARRAYS_SIZES = [1, 10, 20, 100, 1000, 100000]
N_ARRAYS = len(ARRAYS_SIZES)
# Number of different arrays to test the algorithms
N_TESTS_ALG = 10

INSERTION_SORT = 0
MERGE_SORT = 1
RADIX_SORT = 2
BUCKET_SORT = 3
ALGS = [INSERTION_SORT, MERGE_SORT, RADIX_SORT, BUCKET_SORT]
N_ALGS = len(ALGS)


def test_alg(alg, size_array):
    """
    Tests
    """

    t_arrays = []

    # Create the random arrays
    for i in range(N_TESTS_ALG):
        a = [randint(-2 ** N_BITS, 2 ** N_BITS) for i in range(size_array)]
        t_arrays.append(a)

    # Insertion Sort
    if alg == INSERTION_SORT:
        print("INSERTION_SORT", end=",")
        print("N=%d" % (size_array))

        # Test N times to get a more precise average time
        for test in range(N_TESTS_ALG):
            A = list.copy(t_arrays[test])
            t1 = time()
            insertion_sort(A)
            t2 = time()
            print("T%d," % test, t2 - t1)

    elif alg == MERGE_SORT:
        print("MERGE_SORT", end=",")
        print("N=%d" % (size_array))

        # Test N times to get a more precise average time
        for test in range(N_TESTS_ALG):
            A = list.copy(t_arrays[test])
            t1 = time()
            merge_sort(A, 0, len(A) - 1)
            t2 = time()
            print("T%d," % test, t2 - t1)

    elif alg == RADIX_SORT:
        print("RADIX_SORT", end=",")
        print("N=%d" % (size_array))

        # Test N times to get a more precise average time
        for test in range(N_TESTS_ALG):
            A = list.copy(t_arrays[test])
            t1 = time()
            radix_sort(A)
            t2 = time()
            print("T%d," % test, t2 - t1)

    elif alg == BUCKET_SORT:
        print("BUCKET_SORT", end=",")
        print("N=%d" % (size_array))

        # Test N times to get a more precise average time
        for test in range(N_TESTS_ALG):
            A = list.copy(t_arrays[test])
            t1 = time()
            bucket_sort(A, len(A))
            t2 = time()
            print("T%d," % test, t2 - t1)


if __name__ == "__main__":

    # Array creation for each test
    for arr in range(N_ARRAYS):

        # Test sorting in each array
        for alg in range(N_ALGS):
            test_alg(ALGS[alg], ARRAYS_SIZES[arr])

