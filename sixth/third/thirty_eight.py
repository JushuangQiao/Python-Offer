# coding=utf-8
"""
统计一个数字在排序数组中出现的次数
使用二分法分别找到数组中第一个和最后一个出现的值的坐标，然后相减
"""


def get_k_counts(nums, k):
    first = get_first_k(nums, k)
    last = get_last_k(nums, k)
    if first < 0 and last < 0:
        return 0
    if first < 0 or last < 0:
        return 1
    return last - first + 1


def get_first_k(nums, k):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) / 2
        if nums[mid] < k:
            if mid + 1 < len(nums) and nums[mid+1] == k:
                return mid + 1
            left = mid + 1
        elif nums[mid] == k:
            if mid - 1 < 0 or (mid - 1 >= 0 and nums[mid-1] < k):
                return mid
            right = mid - 1
        else:
            right = mid - 1
    return -1


def get_last_k(nums, k):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) / 2
        if nums[mid] < k:
            left = mid + 1
        elif nums[mid] == k:
            if mid + 1 == len(nums) or (mid + 1 < len(nums) and nums[mid+1] > k):
                return mid
            left = mid + 1
        else:
            if mid - 1 >= 0 and nums[mid-1] == k:
                return mid - 1
            right = mid - 1
    return -1

if __name__ == '__main__':
    test = [1, 2, 2, 3, 3, 3, 4]
    print get_k_counts(test, 5)
