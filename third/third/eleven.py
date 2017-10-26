# coding=utf-8
"""
求数值的整数次方
需要考虑正数、负数和0
浮点数不能直接用==比较
"""


def power(base, exponent):
    if equal_zero(base) and exponent < 0:
        raise ZeroDivisionError
    ret = power_value(base, abs(exponent))
    if exponent < 0:
        return 1.0 / ret
    else:
        return ret


def equal_zero(num):
    if abs(num - 0.0) < 0.0000001:
        return True


def power_value(base, exponent):
    if exponent == 0:
        return 1
    if exponent == 1:
        return base
    ret = power_value(base, exponent >> 1)
    ret *= ret
    if exponent & 1 == 1:
        ret *= base
    return ret

if __name__ == '__main__':
    # print power(0.0, -1)
    print power(-2, -6)
