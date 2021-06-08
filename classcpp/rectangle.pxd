
# pxd可以看做cython的头文件
cdef extern from "rectangle.cpp":
    pass

# 声明一个C++类接口
cdef extern from "rectangle.h" namespace "shapes":
    cdef cppclass Rectangle:
        Rectangle() except+
        Rectangle(int, int, int, int) except+
        int x0, y0, x1, y1
        int getArea()
        void getSize(int* width, int* height)
        void move(int, int)
