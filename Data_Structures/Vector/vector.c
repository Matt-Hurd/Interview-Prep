#include <vector.h>

t_vector *vect_new(size_t count, size_t size)
{
    t_vector *ret;
    size_t x;

    ret = malloc(sizeof(t_vector));
    x = 16;
    while (x < count)
    {
        if (x * 2 < x) //We're at size_t max
            return NULL;
        x *= 2;
    }
    ret->capacity = x;
    ret->data = calloc(x, size);
    ret->size = 0;
    ret->item_size = size;
    return (ret);
}

//number of items
size_t  vect_size(t_vector *vect)
{
    return (vect->size);
}

//number of items it can hold
size_t  vect_capacity(t_vector *vect)
{
    return (vect->capacity);
}

int     vect_is_empty(t_vector *vect)
{
    return (vect->size == 0);
}

//Private
void    increase_size(t_vector *vect)
{
    vect->data = realloc(vect->data, vect->capacity * 2);
    vect->capacity *= 2;
}

//Private
void    decrease_size(t_vector *vect)
{
    vect->data = realloc(vect->data, vect->capacity / 2);
    vect->capacity /= 2;
}

//returns item at given index, blows up if index out of bounds
void    *vect_at(t_vector *vect, size_t index)
{
    if (index > vect->size)
        return NULL; //Returning NULL is a bit more obvious than outside of the memory
    return (vect->data + (index * vect->item_size));
}

void    vect_insert(t_vector *vect, size_t index, void *item)
{
    size_t offset;

    if (index > vect->size)
        ; //Some sort of error, not sure what to do in C
    if (vect->size == vect->capacity)
        increase_size(vect);
    offset = vect->item_size * index;
    memmove(vect->data + (offset + vect->item_size),
        vect->data + offset,
        (vect->size * vect->item_size) - offset);
    memcpy(vect->data + offset, item, vect->item_size);
    vect->size += 1;
}

void    vect_delete(t_vector *vect, size_t index)
{
    size_t offset;

    offset = vect->item_size * index;
    memmove(vect->data + offset,
        vect->data + (offset + vect->item_size),
        (vect->size * vect->item_size) - offset);
    if (vect->size - 1 <= vect->capacity / 4)
        decrease_size(vect);
    vect->size -= 1;
}

void    *pop(t_vector *vect, size_t index)
{
    size_t offset;
    void   *ret;

    if (index > vect->size)
        ; //Some sort of error, not sure what to do in C
    offset = vect->item_size * index;
    ret = malloc(vect->item_size);
    memcpy(ret, vect->data + offset, vect->item_size);
    vect_delete(vect, index);
    return (ret);
}

void    vect_push_front(t_vector *vect, void *item)
{
    vect_insert(vect, 0, item);
}

void    vect_push_back(t_vector *vect, void *item)
{
    vect_insert(vect, vect->size, item);
}

void    *vect_pop_front(t_vector *vect, void *item)
{
    return (pop(vect, 0));
}

void    *vect_pop_back(t_vector *vect, void *item)
{
    return (pop(vect, vect->size - 1));
}
