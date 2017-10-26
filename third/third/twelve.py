# coding=utf-8
"""
输入n，打印出从1到最大的n位数
Python中已经对大整数可以进行自动转换了，所以不需要考虑大整数溢出问题
"""


def print_max_n(n):
    for i in xrange(10 ** n):
        print i


if __name__ == '__main__':
    print_max_n(4)
