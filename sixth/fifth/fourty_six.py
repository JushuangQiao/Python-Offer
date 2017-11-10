# coding=utf-8
"""
不能使用乘除、for、while、if、else等
方法一：使用range和sum
方法二：使用reduce
"""


def get_sum1(n):
    return sum(range(1, n+1))


def get_sum2(n):
    return reduce(lambda x, y: x+y, range(1, n+1))


if __name__ == '__main__':
    print get_sum1(4)
    print get_sum2(40)
