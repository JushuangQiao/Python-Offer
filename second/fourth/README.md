# 算法和数据操作

## 面试题8 旋转数组的最小数字
> 要求：把递增数组的前面部分数字移到队尾，求数组中的最小值，例如[3,4,5,6,1,2]
>
> 思路：使用二分法，但要考虑[1, 0, 0, 1]这种数据，只能顺序查找

```python
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
```

## 面试题9 斐波那契数列
> 思路：用生成器

```python
def fib(num):
    a, b = 0, 1
    for i in xrange(num):
        yield b
        a, b = b, a + b
```

## 面试题10 二进制中1的个数
> 要求：求一个整数的二进制表示中，1的个数
>
> 思路：二进制表示中，最后的那个1被减去后，低位都变为0，高位不变，按位与就可以去掉这个1


```python
def num_of_1(n):
    ret = 0
    while n:
        ret += 1
        n = n & n-1
    return ret
```
