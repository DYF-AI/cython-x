import numpy as np
cimport cython
# Version 4: 优化索引
DTYPE = np.intc

cdef int clip(int a, int min_values, int max_values):
    return min(max(a, min_values), max_values)

@cython.boundscheck(False)  # Deactivate bounds checking
@cython.wraparound(False)   # Deactivate negative indexing.
def compute(int[:,:] array_1, int[:,:] array_2, int a, int b, int c):

    cdef Py_ssize_t x_max = array_1.shape[0]
    cdef Py_ssize_t y_max = array_1.shape[1]

    assert tuple(array_1.shape) == tuple(array_2.shape)

    result = np.zeros((x_max, y_max), dtype=DTYPE)
    cdef int[:, :] result_view = result 
    
    cdef int tmp
    cdef Py_ssize_t x, y
    
    for x in range(x_max):
        for y in range(y_max):
            tmp = clip(array_1[x, y], 2, 10)
            tmp = tmp * a + array_2[x, y] * b
            # result[x, y] = tmp + c
            result_view[x, y] = tmp + c
    return result