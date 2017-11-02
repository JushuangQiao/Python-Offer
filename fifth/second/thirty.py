# coding=utf-8
"""
求数组中最小的k个数
思路：使用heapq，该模块是一个最小堆，需要转化成最大堆，
只要在入堆的时候把值取反就可以转化成最大堆，仅适用于数字
"""
import random
import heapq


def get_least_k_nums(nums, k):
    # 数组比较小的时候可以直接使用
    return heapq.nsmallest(k, nums)


class MaxHeap(object):
    def __init__(self, k):
        self.k = k
        self.data = []

    def push(self, elem):
        elem = -elem  # 入堆的时候取反，堆顶就是最大值的相反数了
        if len(self.data) < self.k:
            heapq.heappush(self.data, elem)
        else:
            least = self.data[0]
            if elem > least:
                heapq.heapreplace(self.data, elem)

    def get_least_k_nums(self):
        return sorted([-x for x in self.data])

if __name__ == '__main__':
    test = random.sample(xrange(100000), 100)
    print get_least_k_nums(test, 4)
    h = MaxHeap(4)
    for t in test:
        h.push(t)
    print h.get_least_k_nums()
