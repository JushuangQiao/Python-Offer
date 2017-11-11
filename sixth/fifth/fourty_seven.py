# coding=utf-8
"""
不用加减乘除做加法
方法一：使用位运算，Python中大整数会自动处理，因此对carry需要加个判断
方法二：使用sum
"""


def bit_add(n1, n2):
    carry = 1
    while carry:
        s = n1 ^ n2
        carry = 0xFFFFFFFF & ((n1 & n2) << 1)
        carry = -(~(carry - 1) & 0xFFFFFFFF) if carry > 0x7FFFFFFF else carry
        n1 = s
        n2 = carry
    return n1


def add(n1, n2):
    return sum([n1, n2])

if __name__ == '__main__':
    a = 222
    b = -199
    print bit_add(a, b)
    print add(a, b)
