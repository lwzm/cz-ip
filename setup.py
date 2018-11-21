#!/usr/bin/env python3

import sys
from setuptools import setup

setup(
    name="cz-ip",
    author='lwzm',
    version="1.0",
    packages=["cz_ip"],
    package_data={"cz_ip": ['ip.db']},
)
