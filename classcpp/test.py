import rect
print("Cython")
x0, y0, x1, y1 = 1, 2, 3, 4
rect_obj = rect.PyRectangle(x0, y0, x1, y1)
print("Size: ", rect_obj.get_size())
print("Area: ", rect_obj.get_area())

print("x0: ", rect_obj.x0)
