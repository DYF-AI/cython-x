import numpy as np
cimport cython
# Version 6: 数据类型融合: 有点泛型的意思
# DTYPE = np.intc
ctypedef fused my_type:
    int
    double
    long long

cdef my_type clip(my_type a, my_type min_values, my_type max_values):
    return min(max(a, min_values), max_values)

@cython.boundscheck(False)  # Deactivate bounds checking
@cython.wraparound(False)   # Deactivate negative indexing.
def compute(my_type[:,:] array_1, my_type[:,:] array_2, my_type a, my_type b, my_type c):

    cdef Py_ssize_t x_max = array_1.shape[0]
    cdef Py_ssize_t y_max = array_1.shape[1]

    assert tuple(array_1.shape) == tuple(array_2.shape)

    if my_type is int:
        dtype = np.int
    elif my_type is double:
        dtype = np.double
    elif my_type is cython.longlong:
        dtype = np.longlong

    result = np.zeros((x_max, y_max), dtype=dtype)
    cdef my_type[:, :] result_view = result 
    
    cdef my_type tmp
    cdef Py_ssize_t x, y
    
    for x in range(x_max):
        for y in range(y_max):
            tmp = clip(array_1[x, y], 2, 10)
            tmp = tmp * a + array_2[x, y] * b
            # result[x, y] = tmp + c
            result_view[x, y] = tmp + c
    return result