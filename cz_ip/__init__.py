#!/usr/bin/env python3

import os.path
import sqlite3

db_path = os.path.join(os.path.dirname(__file__), "ip.db")
_c = sqlite3.connect(db_path).cursor()


def ip_to_int(s):
    a, b, c, d = map(int, s.split('.'))
    return (a << 24) + (b << 16) + (c << 8) + d


def find(ip):
    _c.execute("select s from cz where i <= ? order by i desc limit 1", (ip_to_int(ip),))
    o = _c.fetchone()
    if o:
        return o[0]
