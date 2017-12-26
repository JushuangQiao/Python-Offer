# coding=utf-8
"""
求旋转数组中的最小值
二分法
需要考虑[1, 0, 0, 1]这种数据，只能从头查找
"""


def find_min(nums):
    if not nums:
        return False
    length = len(nums)
    left, right = 0, length - 1
    while nums[left] >= nums[right]:
        if right - left == 1:
            return nums[right]
        mid = (left + right) / 2
        if nums[left] == nums[mid] == nums[right]:
            return min(nums)
        if nums[left] <= nums[mid]:
            left = mid
        if nums[right] >= nums[mid]:
            right = mid
    return nums[0]

if __name__ == '__main__':
    print find_min([2, 2, 4, 5, 6, 2])
    print find_min([1, 0, 0, 1])
