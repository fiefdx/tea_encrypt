# -*- coding: utf-8 -*-
'''
tea_encrypt: Interleaving and padding random numbers TEA 
             use c extension with cython or pure python
'''

from setuptools import setup
from setuptools.extension import Extension

from tea_encrypt.version import __version__

WITH_EXTENSION = False
try:
    from Cython.Distutils import build_ext
    import numpy
    WITH_EXTENSION = True
    print("Install tea_encrypt with C extension!")
except ImportError:
    print("Warning: Install tea_encrypt without C extension!")
    print("If you want install tea_encrypt with C extension, please install Numpy and Cython first!")

with open("README.md", "r") as fh:
    long_description = fh.read()

kwargs = {
    "name": "tea_encrypt",
    "version": __version__,
    "description": "tea_encrypt",
    "long_description": long_description,
    "long_description_content_type": "text/markdown",
    "url": "https://github.com/fiefdx/tea_encrypt",
    "author": "fiefdx",
    "author_email": "fiefdx@163.com",
    "packages": [
        'tea_encrypt',
        'tea_encrypt.utils',
    ],
    "install_requires": [],
    "include_package_data": True,
    "license": "MIT",
    "classifiers": [
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ]
}

if WITH_EXTENSION:
    strtea = Extension(
        name = 'tea_encrypt.strtea',
        sources = ['lib/strctea.pyx', 'lib/strtealink.pxd', 'lib/strtea.c'],
        include_dirs = ['lib', numpy.get_include()]
    )

    kwargs["cmdclass"] = {'build_ext': build_ext}
    kwargs["ext_modules"] = [strtea]
else:
    pass

setup(**kwargs)
