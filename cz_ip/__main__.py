#!/usr/bin/env python

from . import locate

try:
    raw_input
    input = raw_input
except NameError:
    pass

if __name__ == '__main__':
    while True:
        try:
            ip = input("ip: ")
        except EOFError:
            break
        print(locate(ip))
