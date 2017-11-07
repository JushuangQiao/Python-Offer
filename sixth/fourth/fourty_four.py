# coding=utf-8
"""
从扑克牌中随机抽取5张牌，判断是不是顺子，大小王可以当任意值
使用排序
"""
import random


def is_continus(nums, k):
    data = [random.choice(nums) for _ in range(k)]
    data.sort()
    print data
    zero = data.count(0)
    small, big = zero, zero + 1
    while big < k:
        if data[small] == data[big]:
            return False
        tmp = data[big] - data[small]
        if tmp > 1:
            if tmp - 1 > zero:
                return False
            else:
                zero -= tmp - 1
                small += 1
                big += 1
        else:
            small += 1
            big += 1
    return True

if __name__ == '__main__':
    test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
            0, 0]
    t = 5
    print is_continus(test, t)
