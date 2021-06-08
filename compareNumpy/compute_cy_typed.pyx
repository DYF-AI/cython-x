import numpy as np
# Version 2
DTYPE = np.intc

cdef int clip(int a, int min_values, int max_values):
    return min(max(a, min_values), max_values)
    
def compute(array_1, array_2, int a, int b, int c):

    cdef Py_ssize_t x_max = array_1.shape[0]
    cdef Py_ssize_t y_max = array_1.shape[1]

    assert array_1.shape == array_2.shape
    assert array_1.dtype == DTYPE
    assert array_2.dtype == DTYPE


    result = np.zeros((x_max, y_max), dtype=array_1.dtype)
    
    cdef int tmp
    cdef Py_ssize_t x, y
    
    for x in range(x_max):
        for y in range(y_max):
            tmp = clip(array_1[x, y], 2, 10)
            tmp = tmp * a + array_2[x, y] * b
            result[x, y] = tmp + c
    return result