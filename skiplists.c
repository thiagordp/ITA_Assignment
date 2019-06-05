#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include <time.h>
#include <math.h>

#define MAX_LEVEL 10
#define P 0.5

// Node
typedef struct node_ {
    int key;
    int value;
    struct node_ **forward;
} node;


// Skiplist
typedef struct skiplist_ {
    int level;
    int size;
    node *header;
} skiplist;


// Rand
int random_level() {
    int level = 1;

    while ((rand() < (int) floor(P * RAND_MAX)) && (level < MAX_LEVEL)) {
        level += 1;
    }

    return level;
}


static node *nil = NULL;

// Inicializa
void skiplistInit(skiplist *s) {

    int i;
    node *header = (node *) malloc(sizeof(node));
    nil = (node *) malloc(sizeof(node));

    s->level = 1;
    s->size = 0;

    s->header = header;
    s->header->key = INT_MIN;
    s->header->value = 0;
    s->header->forward = (node **) calloc(MAX_LEVEL, sizeof(node *));

    node *x = nil;

    nil->key = INT_MAX;

    for (i = 0; i < MAX_LEVEL; i++) {
        s->header->forward[i] = nil;
    }

    srand(time(NULL));
}


// Procura
node *skiplistSearch(skiplist *s, int key) {

    node *x = s->header;

    for (int i = s->level - 1; i >= 0; i--) {
        while (x->forward[i]->key < key) {
            x = x->forward[i];
        }
    }

    x = x->forward[0];

    if (x->key == key)
        return x;

    return NULL;
}


/**
 * Insert a key-value pair into the skiplist.
 * @param s
 * @param key
 * @param value
 * @return
 */
int skiplistInsert(skiplist *s, int key, int value) {

    node *update[MAX_LEVEL];
    node *x = s->header;

    int i, new_level;

    for (i = (s->level - 1); i >= 0; i--) {

        while (x->forward[i]->key < key) {
            x = x->forward[i];
        }

        update[i] = x;
    }

    x = x->forward[0];

    // If the key already exists in the skiplist
    if (x->key == key) {
        x->value = value;
    } else {  // If it's a new key
        s->size += 1;

        new_level = random_level();

        if (new_level > s->level) {

            for (i = s->level; i < new_level; i++) {
                update[i] = s->header;
            }

            s->level = new_level;
        }

        x = (node *) malloc(sizeof(node));

        x->key = key;
        x->value = value;
        x->forward = (node **) calloc(new_level, sizeof(node *));

        for (i = 0; i < new_level; i++) {
            x->forward[i] = update[i]->forward[i];
            update[i]->forward[i] = x;
        }
    }


    return 0;
}

// Free node
void freeNode(node *x) {

    if (x != NULL) {
        free(x->forward);
        free(x);
    }
}

/**
 * Delete a specific key in the skiplist
 * @param s Skiplist
 * @param key Key to delete
 * @return 1 if the key was found and deleted, 0 otherwise.
 */
int skiplistDelete(skiplist *s, int key) {

    node *update[MAX_LEVEL];
    node *x = s->header;

    for (int i = (s->level - 1); i >= 0; i--) {
        while (x->forward[i]->key < key) {
            x = x->forward[i];
        }

        update[i] = x;
    }

    x = x->forward[0];

    if (x->key == key) {
        for (int i = 0; i < s->level; i++) {
            if (update[i]->forward[i] != x) {
                break;
            }

            update[i]->forward[i] = x->forward[i];
        }
        freeNode(x);

        while (s->level > 1 && s->header->forward[s->level - 1] == nil) {
            s->level -= 1;
        }

        s->size -= 1;

        return 1;
    }

    return 0;
}

/**
 * Print All Levels of the Skiplist
 * @param s Skiplist
 */
void skiplistPrint(skiplist *s) {
    node *x;

    for (int i = s->level - 1; i >= 0; i--) {
        x = s->header;

        printf("Head, ");

        while (x != NULL && x->forward[i] != nil) {
            printf("(%d, %d), ", x->forward[i]->key, x->forward[i]->value);
            x = x->forward[i];
        }

        if (x == NULL) printf("NULL");
        else if (x->forward[i] == nil) printf("nil");

        printf("\n");
    }
}

int main() {
    int arr[10], i;
    skiplist list;

    skiplistInit(&list);

    srand(time(NULL));                                              // Seed

    /**
     * Generate array with size 100 w/ random elements.
     */
    printf("Test array:");
    for (i = 0; i < sizeof(arr) / sizeof(arr[0]); i++) {
        arr[i] = 10+rand()%5;
        printf("\t%d", arr[i]);
    }

    /**
     * Insert Elements
     */
    printf("\nInsert:--------------------\n");
    for (i = 0; i < sizeof(arr) / sizeof(arr[0]); i++) {
        skiplistInsert(&list, arr[i], rand() % 10000);
    }


    skiplistPrint(&list);

    /**
     * Search Elements
     */
    printf("\nSearch:--------------------\n");
    for (i = 0; i < 10; i++) {

        int index = rand() % (sizeof(arr) / sizeof(arr[0]));
        node *x = skiplistSearch(&list, arr[index]);

        if (x) {
            printf("key = %d, value = %d\n", arr[index], x->value);
        } else {
            printf("key = %d, not found\n", arr[index]);
        }
    }

    /**
     * Delete Elements
     */
    printf("\nDelete:--------------------\n");
    int index = rand() % (sizeof(arr) / sizeof(arr[0]));
    skiplistDelete(&list, arr[index]);
    index = rand() % (sizeof(arr) / sizeof(arr[0]));
    skiplistDelete(&list, arr[index]);

    skiplistPrint(&list);

    return 0;
}
