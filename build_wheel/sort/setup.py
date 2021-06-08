import os
from setuptools import setup
from Cython.Build import cythonize
from setuptools.dist import Distribution

class BinaryDistribution(Distribution):
    def is_pure(self):
        return False

setup(
    name='sort',
    version='0.2',
    description='A sample Python project',
    ext_modules = cythonize("sort.pyx"),
    include_package_data=True,
    distclass=BinaryDistribution,
)