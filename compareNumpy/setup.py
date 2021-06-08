from setuptools import setup
from Cython.Build import cythonize

setup(
     ext_modules=cythonize("compute_cy.pyx"),
)

setup(
     ext_modules=cythonize("compute_cy_typed.pyx"),
)

setup(
     ext_modules=cythonize("compute_cy_typed_memview.pyx"),
)

setup(
     ext_modules=cythonize("compute_cy_typed_memview_index.pyx"),
)

setup(
     ext_modules=cythonize("compute_cy_typed_memview_index_fusetype.pyx"),
)