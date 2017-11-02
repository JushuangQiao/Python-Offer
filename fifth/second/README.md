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

## 面试题31 连续字数组的最大和

## 面试题32 从1到n整数中1出现的次数

## 面试题33 把数组排成最小的数
