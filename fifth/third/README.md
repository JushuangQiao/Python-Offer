# 5.3 时间效率与空间效率的平衡

## 面试题34 丑数 [LeetCode](https://leetcode.com/problems/ugly-number-ii/)
> 要求：只含有2、3、5因子的数是丑数，求第1500个丑数
>
> 思路: 按顺序保存已知的丑数，下一个是已知丑数中某三个数乘以2，3，5中的最小值

```python
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
```

## 面试题35 第一个只出现一次的字符
> 要求：求字符串中第一个只出现一次的字符
>
> 思路: 使用两个hash，一个记录每个字符穿线的次数，另一个记录每个字符第一次出现的位置

```python
def first_not_repeating_char(string):
    if not string:
        return -1
    count = {}
    loc = {}
    for k, s in enumerate(string):
        count[s] = count[s] + 1 if count.get(s) else 1
        loc[s] = loc[s] if loc.get(s) else k
    ret = float('inf')
    for k in loc.keys():
        if count.get(k) == 1 and loc[k] < ret:
            ret = loc[k]
    return ret
```

## 面试题36 数组中的逆序对
> 要求：在一个数组中，前面的数字比后面的大，就是一个逆序对，求总数
>
> 思路: 归并排序,先把数组依次拆开，然后合并的时候统计逆序对数目，并排序

```python
import copy


def get_inverse_pairs(nums):
    if not nums:
        return 0
    start, end = 0, len(nums) - 1
    tmp = copy.deepcopy(nums)
    return inverse_pairs(tmp, start, end)


def inverse_pairs(tmp, start, end):
    if start == end:  # 递归结束条件
        return 0
    mid = (end - start) / 2  # 分别对左右两边递归求值
    left = inverse_pairs(tmp, start, start+mid)
    right = inverse_pairs(tmp, start+mid+1, end)

    count = 0  # 本次逆序对数目
    l_right, r_right = start + mid, end
    t = []
    while l_right >= start and r_right >= start + mid + 1:
        if tmp[l_right] > tmp[r_right]:
            t.append(tmp[l_right])
            count += (r_right - mid - start)
            l_right -= 1
        else:
            t.append(tmp[r_right])
            r_right -= 1
    while l_right >= start:
        t.append(tmp[l_right])
        l_right -= 1
    while r_right >= start+mid+1:
        t.append(tmp[r_right])
        r_right -= 1
    tmp[start:end+1] = t[::-1]
    return count + left + right
```

## 面试题37 两个链表的第一个公共结点
> 思路: 先获取到两个链表的长度，然后长的链表先走多的几步，之后一起遍历
>
> 文件thirty_seven.py中包含了设置链表公共结点的代码，可以用来测试

```python
def get_first_common_node(link1, link2):
    if not link1 or not link2:
        return None
    length1 = length2 = 0
    move1, move2 = link1, link2
    while move1:  # 获取链表长度
        length1 += 1
        move1 = move1.next
    while move2:
        length2 += 1
        move2 = move2.next
    while length1 > length2:  # 长链表先走多的长度
        length1 -= 1
        link1 = link1.next
    while length2 > length1:
        length2 -= 1
        link2 = link2.next
    while link1:  # 链表一起走
        if link1 == link2:
            return link1
        link1, link2 = link1.next, link2.next
    return None
```