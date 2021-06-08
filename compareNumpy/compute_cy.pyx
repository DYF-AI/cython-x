
import numpy as np

# Version 1: 速度没什么提升，原因是c代码仍然完全是有python解析器执行
def clip(a, min_values, max_values):
    return min(max(a, min_values), max_values)
    
def compute(array_1, array_2, a, b, c):
    """
        This function must implement the formula
        np.clip(array_1, 2, 10) * a + array_2 * b + c

        array_1 and array_2 are 2D.
    """
    x_max = array_1.shape[0]
    y_max = array_1.shape[1]

    assert array_1.shape == array_2.shape

    result = np.zeros((x_max, y_max), dtype=array_1.dtype)
    
    for x in range(x_max):
        for y in range(y_max):
            tmp = clip(array_1[x, y], 2, 10)
            tmp = tmp * a + array_2[x, y] * b
            result[x, y] = tmp + c
    return result

