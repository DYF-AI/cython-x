from setuptools import setup

from Cython.Build import cythonize

# setup(ext_modules=cythonize("rect.pyx"))

from setuptools import Extension, setup
from Cython.Build import cythonize
setup(
    ext_modules = cythonize(Extension(
           "rect",                               
           sources=["rect.pyx", "rectangle.cpp"], 
           language="c++",                       
          )
    )
)