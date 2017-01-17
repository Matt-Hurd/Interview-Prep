#include <stdio.h>
#include <vector.h>

int     main(void)
{
    t_vector *test_vect;
    int ints[11] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

    test_vect = vect_new(1, sizeof(int));
    printf("Raw Structure values:\n");
    printf("Pointer Location: %p\n", test_vect->data);
    printf("Capacity: %zu\n", test_vect->capacity);
    printf("Size: %zu\n", test_vect->size);
    printf("Item Size: %zu\n", test_vect->item_size);

    printf("Inserting 1 at pos 0\n");
    vect_insert(test_vect, 0, &ints[1]);
    printf("Inserting 2 at pos 1\n");
    vect_insert(test_vect, 1, &ints[2]);
    printf("Inserting 3 at pos 2\n");
    vect_insert(test_vect, 2, &ints[3]);
    printf("Inserting 4 at pos 3\n");
    vect_insert(test_vect, 3, &ints[4]);
    printf("Inserting 5 at pos 4\n");
    vect_insert(test_vect, 4, &ints[5]);
    printf("Inserting 6 at pos 5\n");
    vect_insert(test_vect, 5, &ints[6]);
    printf("Inserting 7 at pos 6\n");
    vect_insert(test_vect, 6, &ints[7]);
    printf("Item at pos 0: %d\n", *(int *)vect_at(test_vect, 0));
    printf("Item at pos 1: %d\n", *(int *)vect_at(test_vect, 1));
    printf("Item at pos 2: %d\n", *(int *)vect_at(test_vect, 2));
    printf("Item at pos 3: %d\n", *(int *)vect_at(test_vect, 3));
    printf("Item at pos 4: %d\n", *(int *)vect_at(test_vect, 4));
    printf("Item at pos 5: %d\n", *(int *)vect_at(test_vect, 5));
    printf("Item at pos 6: %d\n", *(int *)vect_at(test_vect, 6));



    printf("Inserting 2 at pos 4\n");
    vect_insert(test_vect, 4, &ints[2]);
    printf("Pushing 10 to front\n");
    vect_push_front(test_vect, &ints[10]);
    printf("Pushing 7 to back\n");
    vect_push_back(test_vect, &ints[7]);
    printf("Item at pos 0: %d\n", *(int *)vect_at(test_vect, 0));
    printf("Item at pos 1: %d\n", *(int *)vect_at(test_vect, 1));
    printf("Item at pos 2: %d\n", *(int *)vect_at(test_vect, 2));
    printf("Item at pos 3: %d\n", *(int *)vect_at(test_vect, 3));
    printf("Item at pos 4: %d\n", *(int *)vect_at(test_vect, 4));
    printf("Item at pos 5: %d\n", *(int *)vect_at(test_vect, 5));
    printf("Item at pos 6: %d\n", *(int *)vect_at(test_vect, 6));
    printf("Item at pos 7: %d\n", *(int *)vect_at(test_vect, 7));
    printf("Item at pos 8: %d\n", *(int *)vect_at(test_vect, 8));
    printf("Item at pos 9: %d\n", *(int *)vect_at(test_vect, 9));
    printf("Size: %zu\n", test_vect->size);
}
