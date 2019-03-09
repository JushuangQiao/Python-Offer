# coding=utf-8
"""
只含有2、3、5因子的数是丑数，求第1500个丑数
按顺序保存已知的丑数，下一个是已知丑数中某三个数乘以2，3，5中的最小值
"""


class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        ugly = [1]
        t2 = t3 = t5 = 0
        while len(ugly) < n:
            while ugly[t2] * 2 <= ugly[-1]:
                t2 += 1
            while ugly[t3] * 3 <= ugly[-1]:
                t3 += 1
            while ugly[t5] * 5 <= ugly[-1]:
                t5 += 1
            ugly.append(min(ugly[t2]*2, ugly[t3]*3, ugly[t5]*5))
        return ugly[-1]


if __name__ == '__main__':
    print Solution().nthUglyNumber(1500)
