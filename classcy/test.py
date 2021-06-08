import time
import example
from example import rectArea_v1, rectArea_v2

from py_code import rectArea


t = time.time()
x0, y0, x1, y1 = 1.0, 2, 3, 4
# area = rectArea(x0, y0, x1, y1)
# area = rectArea_v1(x0, y0, x1, y1)
area = rectArea_v2(x0, y0, x1, y1)
      
print("t: ", time.time()-t)
print(area)
