# 6.5 发散思维能力

## 面试题46 求1+2...+n
> 要求：不能使用乘除、for、while、if、else等
>
>方法一：使用range和sum
>
>方法二：使用reduce

```python
def get_sum1(n):
    return sum(range(1, n+1))


def get_sum2(n):
    return reduce(lambda x, y: x+y, range(1, n+1))
```

## 面试题47 不用加减乘除做加法
> 要求：不用加减乘除做加法
>
>方法一：使用位运算，Python中大整数会自动处理，因此对carry需要加个判断
>
>方法二：使用sum

```python
def bit_add(n1, n2):
    carry = 1
    while carry:
        s = n1 ^ n2
        carry = 0xFFFFFFFF & ((n1 & n2) << 1)
        carry = -(~(carry - 1) & 0xFFFFFFFF) if carry > 0x7FFFFFFF else carry
        n1 = s
        n2 = carry
    return n1


def add(n1, n2):
    return sum([n1, n2])
```

## 面试题48 不能被继承的类
>Python中不知道怎么实现不能被继承的类。以后补充代码或者原因。
