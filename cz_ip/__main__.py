#!/usr/bin/env python

from __future__ import print_function

from . import locate

try:
    raw_input
    input = raw_input
except NameError:
    pass

if __name__ == '__main__':
    while True:
        try:
            ip = input().strip()
        except EOFError:
            break
        if ip:
            print(ip, locate(ip), sep="\t")
