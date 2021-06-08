import time
import numpy as np
from compute_np import compute_np as cnp
from compute_py import compute as cpy
import compute_cy as ccy
import compute_cy_typed as ccy_typed
import compute_cy_typed_memview as ccy_typed_memview
import compute_cy_typed_memview_index as ccy_typed_memview_index

array_1 = np.random.uniform(0, 1000, size=(300, 200)).astype(np.intc)
array_2 = np.random.uniform(0, 1000, size=(300, 200)).astype(np.intc)

a, b, c = 4, 3, 9

print("test compute_np")
t_np = time.time()
ret = cnp(array_1, array_2, a, b, c)
print("t_np: ", time.time() - t_np)
# print("ret[0][0]: ", ret[0][0])


print("test compute_py")
t_np = time.time()
ret = cpy(array_1, array_2, a, b, c)
print("t_py: ", time.time() - t_np)
# print("ret[0][0]: ", ret[0][0])


print("test compute_cy")
t_cy = time.time()
ret = ccy.compute(array_1, array_2, a, b, c)
print("t_cp: ", time.time() - t_cy)
# print("ret[0][0]: ", ret[0][0])

print("test compute_cy_typed")
t_cy_typed = time.time()
ret = ccy_typed.compute(array_1, array_2, a, b, c)
print("t_cy_typed: ", time.time() - t_cy_typed)
# print("ret[0][0]: ", ret[0][0])

print("test compute_cy_typed_memview")
t_cy_typed_memview = time.time()
ret = ccy_typed_memview.compute(array_1, array_2, a, b, c)
print("t_cy_typed_memview: ", time.time() - t_cy_typed_memview)
# print("ret[0][0]: ", ret[0][0])

print("test compute_cy_typed_memview_index")
t_cy_typed_memview_index = time.time()
ret = ccy_typed_memview_index.compute(array_1, array_2, a, b, c)
print("t_cy_typed_memview_index: ", time.time() - t_cy_typed_memview_index)
# print("ret[0][0]: ", ret[0][0])
