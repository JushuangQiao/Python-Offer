# coding=utf-8
"""
0到n-1排成一圈，从0开始每次数m个数删除，求最后剩余的数
当 n > 1 时： f(n,m) = [f(n-1, m)+m]%n,当 n = 1 时： f(n,m)=0
"""


def last_num(n, m):
    ret = 0
    if n == 1:
        return 0
    for i in range(2, n+1):
        ret = (m + ret) % i
    return ret

if __name__ == '__main__':
    print last_num(3, 4)
