# coding=utf-8
"""
调整数组顺序使奇数位于偶数前面
使用两个指针，前后各一个，为了更好的扩展性，可以把判断奇偶部分抽取出来
"""


def reorder(nums, func):
    left, right = 0, len(nums) - 1
    while left < right:
        while not func(nums[left]):
            left += 1
        while func(nums[right]):
            right -= 1
        if left < right:
            nums[left], nums[right] = nums[right], nums[left]


def is_even(num):
    return (num & 1) == 0

if __name__ == '__main__':
    tests = [2, 3]
    reorder(tests, is_even)
    print tests
