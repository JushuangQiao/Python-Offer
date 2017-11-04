# coding=utf-8
"""
把数组中的值拼接，找出能产生的最小的数[321,32,3]最小的数是321323
Python中不需要考虑大整数，需要自己定义一个数组排序规则，直接调用库函数就可以
"""


def cmp(a, b):
    return int(str(a)+str(b)) - int(str(b)+str(a))


def print_mini(nums):
    if not nums:
        return
    print int(''.join([str(num) for num in sorted(nums, cmp=cmp)]))


if __name__ == '__main__':
    test = []
    print_mini(test)
