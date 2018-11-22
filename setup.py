#!/usr/bin/env python

from setuptools import setup

import cz_ip

author = "lwzm"

with open("README.md") as f:
    long_description = f.read()

setup(
    version=cz_ip.__version__,
    description="Find the location of ip address",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=author,
    author_email="{}@qq.com".format(author),
    keywords="ip address chunzhen cz88".split(),
    url="https://github.com/lwzm/cz-ip",
    name="cz-ip",
    packages=["cz_ip"],
    package_data={"cz_ip": ['ip.db']},
    classifiers=[
        "Environment :: Console",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
    ],
)
