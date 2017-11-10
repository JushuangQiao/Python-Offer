# 6.3 知识迁移能力

## 面试题38 数字在排序数组中出现的次数
> 思路: 使用二分法分别找到数组中第一个和最后一个出现的值的坐标，然后相减

```python
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
```


## 面试题39 二叉树的深度
> 思路: 分别递归的求左右子树的深度

```python
def get_depth(tree):
    if not tree:
        return 0
    if not tree.left and not tree.right:
        return 1
    return 1 + max(get_depth(tree.left), get_depth(tree.right))
```

## 面试题40 数组中只出现一次的数字
> 要求：数组中除了两个只出现一次的数字外，其他数字都出现了两遍
>
> 思路: 按位异或，在得到的值中找到二进制最后一个1，然后把数组按照该位是0还是1分为两组

```python
def get_only_one_number(nums):
    if not nums:
        return None
    tmp_ret = 0
    for n in nums:  # 获取两个值的异或结果
        tmp_ret ^= n
    last_one = get_bin(tmp_ret)
    a_ret, b_ret = 0, 0
    for n in nums:
        if is_one(n, last_one):
            a_ret ^= n
        else:
            b_ret ^= n
    return [a_ret, b_ret]


def get_bin(num):  # 得到第一个1
    ret = 0
    while num & 1 == 0 and ret < 32:
        num = num >> 1
        ret += 1
    return ret


def is_one(num, t):  # 验证t位是不是1
    num = num >> t
    return num & 0x01
```

## 面试题41 和为s的两个数字VS和为s的连续正数序列
### 和为s的两个数字
> 要求：输入一个递增排序的数组和一个数字s，在数组中查找两个数，使其和为s
>
> 思路: 设置头尾两个指针，和大于s，尾指针减小，否砸头指针增加

```python
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
```
### 和为s的连续整数序列
> 要求：输入一个正数s， 打印出所有和为s的正整数序列(至少两个数)
>
> 思路: 使用两个指针，和比s小，大指针后移，比s大，小指针后移

```python
def sum_to_s(s):
    a, b = 1, 2
    ret = []
    while a < s / 2 + 1:
        if sum(range(a, b+1)) == s:
            ret.append(range(a, b+1))
            a += 1
        elif sum(range(a, b+1)) < s:
            b += 1
        else:
            a += 1
    return ret
```

## 面试题42 翻转单词顺序与左旋转字符串
### 翻转单词顺序
> 要求：翻转一个英文句子中的单词顺序，标点和普通字符一样处理
>
> 思路: Python中字符串是不可变对象，不能用书中的方法，可以直接转化成列表然后转回去

```python
def reverse_words(sentence):
    tmp = sentence.split()
    return ' '.join(tmp[::-1])  # 使用join效率更好，+每次都会创建新的字符串
```
### 左旋转字符串
> 思路: 把字符串的前面的若干位移到字符串的后面

```python
def rotate_string(s, n):
    if not s:
        return ''
    n %= len(s)
    return s[n:] + s[:n]
```