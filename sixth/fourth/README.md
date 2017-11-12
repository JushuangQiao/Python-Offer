# 6.4 抽象建模能力

## 面试题43 n个骰子的点数
> 要求：求出n个骰子朝上一面之和s所有可能值出现的概率
>
> 思路：n出现的可能是前面n-1到n-6出现可能的和，设置两个数组，分别保存每一轮

```python
def get_probability(n):
    if n < 1:
        return []
    data1 = [0] + [1] * 6 + [0] * 6 * (n - 1)
    data2 = [0] + [0] * 6 * n   # 开头多一个0，方便按照习惯从1计数
    flag = 0
    for v in range(2, n+1):  # 控制次数
        if flag:
            for k in range(v, 6*v+1):
                data1[k] = sum([data2[k-j] for j in range(1, 7) if k > j])
            flag = 0
        else:
            for k in range(v, 6*v+1):
                data2[k] = sum([data1[k-j] for j in range(1, 7) if k > j])
            flag = 1
    ret = []
    total = 6 ** n
    data = data2[n:] if flag else data1[n:]
    for v in data:
        ret.append(v*1.0/total)
    print data
    return ret
```

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
> 要求：0到n-1排成一圈，从0开始每次数m个数删除，求最后剩余的数
>
> 思路：当 n > 1 时： f(n,m) = [f(n-1, m)+m]%n,当 n = 1 时： f(n,m)=0，*关键是推导出关系表达式*

```python
def last_num(n, m):
    ret = 0
    if n == 1:
        return 0
    for i in range(2, n+1):
        ret = (m + ret) % i
    return ret
```

