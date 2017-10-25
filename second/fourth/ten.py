# coding=utf-8
"""
求一个整数的二进制表示中，1的个数
二进制表示中，最后的那个1被减去后，低位都变为0，高位不变，按位与就可以去掉这个1
"""


def num_of_1(n):
    ret = 0
    while n:
        ret += 1
        n = n & n-1
    return ret

if __name__ == '__main__':
    print bin(100).count('1') == num_of_1(100)
