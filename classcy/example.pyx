# 定义cython的class


# Versin: 1
cdef class Rectangle_v1:
    cdef int x0, y0
    cdef int x1, y1

    def __init__(self, int x0, int y0, int x1, int y1):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
    
    # 调用area包含了大量的python开销
    def area(self):
        area = (self.x1 - self.x0) * (self.y1 - self.y0)
        if area < 0:
            area = -area
        return area

def rectArea_v1(x0, y0, x1, y1):
    rect = Rectangle_v1(x0, y0, x1, y1)
    return rect.area()
    

# Version: 2
cdef class Rectangle_v2:
    cdef int x0, y0
    cdef int x1, y1

    def __init__(self, int x0, int y0, int x1, int y1):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1

    # 声明为cpdef使其可以作为C函数调用
    cpdef int _area(self):
        area = (self.x1 - self.x0) * (self.y1 - self.y0)
        if area < 0:
            area = -area
        return area

    def area(self):
        return self._area

def rectArea_v2(x0, y0, x1, y1):
    cdef Rectangle_v2 rect = Rectangle_v2(x0, y0, x1, y1)
    return rect._area()


