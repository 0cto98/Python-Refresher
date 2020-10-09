from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize(["helloworld.pyx", "primes.pyx"], annotate=True, language_level = "3"),
)
