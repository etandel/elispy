from setuptools import setup, find_packages
from elispy import __version__


setup(
    name='elispy',
    version=__version__,
    description='S-expression EDSL for Python',
    packages=find_packages(),
)

