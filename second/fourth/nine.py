# coding=utf-8
"""
斐波那契数列
直接使用生成器， 节省内存
"""


def fib(num):
    a, b = 0, 1
    for i in xrange(num):
        yield b
        a, b = b, a + b


if __name__ == '__main__':
    print [n for n in fib(10)]
