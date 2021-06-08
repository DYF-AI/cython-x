import os
from setuptools import setup
from Cython.Build import cythonize
from setuptools.dist import Distribution

class BinaryDistribution(Distribution):
    def is_pure(self):
        return False

setup(
    name='say_hello',
    version='0.1',
    description='A sample Python project',
    ext_modules = cythonize("helloworld.pyx"),
    include_package_data=True,
    distclass=BinaryDistribution,
)