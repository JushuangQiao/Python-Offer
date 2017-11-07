# 6.4 抽象建模能力

## 面试题43 n个骰子的点数


## 面试题44 扑克牌的顺子
> 要求：从扑克牌中随机抽取5张牌，判断是不是顺子，大小王可以当任意值
>
> 思路: 使用排序

```python
import random


def is_continus(nums, k):
    data = [random.choice(nums) for _ in range(k)]
    data.sort()
    print data
    zero = data.count(0)
    small, big = zero, zero + 1
    while big < k:
        if data[small] == data[big]:
            return False
        tmp = data[big] - data[small]
        if tmp > 1:
            if tmp - 1 > zero:
                return False
            else:
                zero -= tmp - 1
                small += 1
                big += 1
        else:
            small += 1
            big += 1
    return True
```

## 面试题45 圆圈中最后剩下的数字
