
from distutils.core import setup
from setuptools import find_packages

setup(
      name='mydal',
      version='0.1.0',
      packages=find_packages(exclude=['test*']),
      author='Opemipo Ogunkola',
      descriptions = 'MyDAL - My Data structures and ALgorithms Library'
)
