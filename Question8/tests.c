/*
 * Skiplists testing
 *
 * @author Ana Caroline, Marcelo and Thiago
 */

#include <time.h>
#include "skiplists.c"

/* Array sizes for testing */
#define N_S256      256
#define N_S512      512
#define N_S4096     4096
#define N_S8192     8192
#define N_S65536    65536

/* Total of tests to run. */
#define N_TESTS     1000

void test(int n_elem, int n_tests) {
    for (int k = 0; k < n_tests; k++) {
        skiplist s;

        clock_t start, stop, start2, stop2;
        double time_diff1, time_diff2;
        int *arr = calloc(n_elem, sizeof(int));

        skiplistInit(&s);

        /* Insertion tests */
        start = clock();
        for (int i = 0; i < n_elem; i++) {
            int key = rand();
            arr[i] = key;

            skiplistInsert(&s, key, rand());
        }
        stop = clock();

        time_diff1 = ((double) (stop - start)) / CLOCKS_PER_SEC;

        /** Removal tests */
        start2 = clock();
        for (int i = 0; i < (int) (n_elem / 5); i++) {
            int index = rand() % n_elem;
            skiplistDelete(&s, arr[index]);

        }
        stop2 = clock();

        time_diff2 = ((double) (stop2 - start2)) / CLOCKS_PER_SEC;

        printf("Teste n=%d:\tIns: %.10lfs\tDel: %.10lfs\n", n_elem, time_diff1, time_diff2);

        free(arr);
    }
}

int main() {

    srand(time(NULL));      // Seed

    test(N_S256, N_TESTS);
    test(N_S512, N_TESTS);
    test(N_S4096, N_TESTS);
    test(N_S8192, N_TESTS);
    test(N_S65536, N_TESTS);

    return 0;
}
