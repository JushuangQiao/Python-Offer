# 5.2 时间效率

## 面试题29 数组中出现次数超过一半的数字
> 思路: 使用hash，key是数字，value是出现的次数
>
> 注意: 列表的len方法的时间复杂度是O(1)
>

```python
def get_more_half_num(nums):
    hashes = dict()
    length = len(nums)
    for n in nums:
        hashes[n] = hashes[n] + 1 if hashes.get(n) else 1
        if hashes[n] > length / 2:
            return n
```

## 面试题30 最小的k个数
> 要求：求数组中出现次数超过一半的数字
>
> 思路: 使用heapq，该模块是一个最小堆，需要转化成最大堆，只要在入堆的时候把值取反就可以转化成最大堆(仅适用于数字)
>
> 思路二: 数组比较小的时候可以直接使用heapq的nsmallest方法

```python
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
```

## 面试题31 连续子数组的最大和
> 思路: 动态规划问题

```python
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
```

## 面试题32 从1到n整数中1出现的次数
> 要求：求从1到n整数的十进制表示中，1出现的次数
>
> 思路: 获取每个位数区间上所有数中包含1的个数，然后分别对高位分析，然后递归的处理低位数
>
> 此题中，作者的描述我没有理解，按照自己的理解写了一下，具体内容请点击[这里](http://www.cnblogs.com/qiaojushuang/p/7780445.html)

```python
def get_digits(n):
    # 求整数n的位数
    ret = 0
    while n:
        ret += 1
        n /= 10
    return ret


def get_1_digits(n):
    """
    获取每个位数之间1的总数
    :param n: 位数
    """
    if n <= 0:
        return 0
    if n == 1:
        return 1
    current = 9 * get_1_digits(n-1) + 10 ** (n-1)
    return get_1_digits(n-1) + current


def get_1_nums(n):
    if n < 10:
        return 1 if n >= 1 else 0
    digit = get_digits(n)  # 位数
    low_nums = get_1_digits(digit-1)  # 最高位之前的1的个数
    high = int(str(n)[0])  # 最高位
    low = n - high * 10 ** (digit-1)  # 低位

    if high == 1:
        high_nums = low + 1  # 最高位上1的个数
        all_nums = high_nums
    else:
        high_nums = 10 ** (digit - 1)
        all_nums = high_nums + low_nums * (high - 1)  # 最高位大于1的话，统计每个多位数后面包含的1
    return low_nums + all_nums + get_1_nums(low)
```

## 面试题33 把数组排成最小的数
> 要求：把数组中的值拼接，找出能产生的最小的数[321,32,3]最小的数是321323
>
> 思路: Python中不需要考虑大整数，需要自己定义一个数组排序规则，直接调用库函数就可以

```python
def cmp(a, b):
    return int(str(a)+str(b)) - int(str(b)+str(a))


def print_mini(nums):
    print int(''.join([str(num) for num in sorted(nums, cmp=cmp)]))
```