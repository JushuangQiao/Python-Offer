# coding=utf-8
"""
连续子数组的最大和
动态规划问题
"""


def max_sum(nums):
    ret = float("-inf")  # 负无穷
    if not nums:
        return ret
    current = 0
    for i in nums:
        if current <= 0:
            current = i
        else:
            current += i
        ret = max(ret, current)
    return ret

if __name__ == '__main__':
    test = [1, 2, -2, 3, 6, 0, -2]
    print max_sum(test)
