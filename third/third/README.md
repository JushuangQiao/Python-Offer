# 3.3 代码的完整性

## 面试题11 数值的整数次方
> 要求：求一个数的整数次方
>
> 思路：需要考虑次方是正数、负数和0，基数是0
>
> 浮点数相等不能直接用==

```python
def power(base, exponent):
    if equal_zero(base) and exponent < 0:
        raise ZeroDivisionError
    ret = power_value(base, abs(exponent))
    if exponent < 0:
        return 1.0 / ret
    else:
        return ret


def equal_zero(num):
    if abs(num - 0.0) < 0.0000001:
        return True


def power_value(base, exponent):
    if exponent == 0:
        return 1
    if exponent == 1:
        return base
    ret = power_value(base, exponent >> 1)
    ret *= ret
    if exponent & 1 == 1:
        ret *= base
    return ret
```

## 面试题12 打印1到最大的n位数
> 要求：输入n，打印出从1到最大的n位数
>
> 思路：Python中已经对大整数可以进行自动转换了，所以不需要考虑大整数溢出问题

```python
def print_max_n(n):
    for i in xrange(10 ** n):
        print i
```
