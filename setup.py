# -*- coding: utf-8 -*-
'''
tes_encrypt: Interleaving and padding random numbers TEA 
             use c and cython or pure python
'''

from setuptools import setup

from tea_encrypt.version import __version__

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name = "tea_encrypt",
    version = __version__,
    description = "tea_encrypt",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/fiefdx/tea_encrypt",
    author = "fiefdx",
    author_email = "fiefdx@163.com",
    packages = [
        'tea_encrypt',
        'tea_encrypt.utils',
    ],
    install_requires = [],
    include_package_data = True,
    license = "MIT",
    classifiers = [
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ]
)
