#ifndef VECTOR_H
# define VECTOR_H
# include <stdlib.h>
# include <string.h>

typedef struct  s_vector
{
        void    *data;
        size_t  capacity;
        size_t  size;
        size_t  item_size;
}               t_vector;

t_vector    *vect_new(size_t count, size_t size);
size_t      vect_size(t_vector *vect);
size_t      vect_capacity(t_vector *vect);
int         vect_is_empty(t_vector *vect);
void        *vect_at(t_vector *vect, size_t index);
void        vect_insert(t_vector *vect, size_t index, void *item);
void        vect_push_front(t_vector *vect, void *item);
void        vect_push_back(t_vector *vect, void *item);
void        *vect_pop_front(t_vector *vect, void *item);
void        *vect_pop_back(t_vector *vect, void *item);
#endif
