# coding=utf-8
"""
求从1到n整数的十进制表示中，1出现的次数
思路：获取每个位数区间上所有数中包含1的个数，然后分别对高位分析，然后递归的处理低位数
"""


def get_digits(n):
    # 求整数n的位数
    ret = 0
    while n:
        ret += 1
        n /= 10
    return ret


def get_1_digits(n):
    """
    获取每个位数之间1的总数
    :param n: 位数
    """
    if n <= 0:
        return 0
    if n == 1:
        return 1
    current = 9 * get_1_digits(n-1) + 10 ** (n-1)
    return get_1_digits(n-1) + current


def get_1_nums(n):
    if n < 10:
        return 1 if n >= 1 else 0
    digit = get_digits(n)  # 位数
    low_nums = get_1_digits(digit-1)  # 最高位之前的1的个数
    high = int(str(n)[0])  # 最高位
    low = n - high * 10 ** (digit-1)  # 低位

    if high == 1:
        high_nums = low + 1  # 最高位上1的个数
        all_nums = high_nums
    else:
        high_nums = 10 ** (digit - 1)
        all_nums = high_nums + low_nums * (high - 1)  # 最高位大于1的话，统计每个多位数后面包含的1
    return low_nums + all_nums + get_1_nums(low)


def test_n(num):
    # 常规方法用来比较
    ret = 0
    for n in range(1, num+1):
        for s in str(n):
            if s == '1':
                ret += 1
    return ret

if __name__ == '__main__':
    test = 9923446
    import time
    t = time.clock()
    print test_n(test)
    print time.clock() - t
    t1 = time.clock()
    print get_1_nums(test)
    print time.clock() - t1
