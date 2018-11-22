#!/usr/bin/env python2

from setuptools import setup

import cz_ip

author = "lwzm"

setup(
    version=cz_ip.__version__,
    description="Find the location of ip address",
    author=author,
    author_email="{}@qq.com".format(author),
    keywords="ip address chunzhen cz88".split(),
    url="https://github.com/lwzm/cz-ip",
    name="cz-ip",
    packages=["cz_ip"],
    package_data={"cz_ip": ['ip.db']},
)
