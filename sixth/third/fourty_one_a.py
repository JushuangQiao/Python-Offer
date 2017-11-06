# coding=utf-8
"""
输入一个递增排序的数组和一个数字s，在数组中查找两个数，使其和为s
设置头尾两个指针，和大于s，尾指针减小，否砸头指针增加
"""


def sum_to_s(nums, s):
    head, end = 0, len(nums) - 1
    while head < end:
        if nums[head] + nums[end] == s:
            return [nums[head], nums[end]]
        elif nums[head] + nums[end] > s:
            end -= 1
        else:
            head += 1
    return None

if __name__ == '__main__':
    test = [-4, 0, 1, 2, 4, 6, 8, 10, 12, 15, 18]
    s = 12
    print sum_to_s(test, s)
