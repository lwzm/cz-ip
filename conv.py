#!/usr/bin/env python3

import sqlite3

from cz_ip import ip_to_int


def extract(s):
    """
    8.8.8.8         8.8.8.8         美国 加利福尼亚州圣克拉拉县山景市谷歌公司DNS服务器
    8.8.8.9         8.8.8.255       美国 加利福尼亚州圣克拉拉县山景市谷歌公司
    ...
    """
    b, e, desc = s.split(None, 2)
    return (ip_to_int(b), ip_to_int(e), desc.replace("CZ88.NET", "").strip())


def check(ips):
    n = -1
    cnt = 0
    for ip in ips:
        if not ip.strip():
            break
        cnt += 1
        b, e, _ = extract(ip)
        assert b == n + 1
        n = e
    return cnt, ips[-1]


def main():
    with open('ip.txt', encoding="gbk") as f:
        ips = list(f)

    check(ips)

    con = sqlite3.connect("cz_ip/ip.db")
    c = con.cursor()

    c.executescript("""
    drop table if exists cz;

    create table cz (
        i int primary key,
        s text
    );
    """)

    for ip in ips:
        if not ip.strip():
            break
        i, _, s = extract(ip)
        c.execute("insert into cz (i, s) values (?, ?)", (i, s))
    con.commit()


if __name__ == '__main__':
    main()
