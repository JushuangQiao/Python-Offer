# coding=utf-8
"""
数组中出现次数超过一半的数字
思路: 使用hash，key是数字，value是出现的次数
注意: 列表的len方法的时间复杂度是O(1)
"""


def get_more_half_num(nums):
    hashes = dict()
    length = len(nums)
    for n in nums:
        hashes[n] = hashes[n] + 1 if hashes.get(n) else 1
        if hashes[n] > length / 2:
            return n

if __name__ == '__main__':
    test = [1, 2, 1, 2, 3, 1, 1]
    print get_more_half_num(test)
