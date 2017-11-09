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

## 面试题13 O(1)时间删除链表结点
> 要求：O(1)时间删除链表结点
>
> 思路：如果有后续结点，后续结点的值前移，删除后续结点，如果没有，只能顺序查找了

```python
def delete_node(link, node):
    if node == link:  # 只有一个结点
        del node
    if node.next is None:  # node是尾结点
        while link:
            if link.next == node:
                link.next = None
            link = link.next
    else:
        node.val = node.next.val
        n_node = node.next
        node.next = n_node.next
        del n_node
```
## 面试题14 调整数组顺序使奇数位于偶数前面
> 思路：使用两个指针，前后各一个，为了更好的扩展性，可以把判断奇偶部分抽取出来

```python
def reorder(nums, func):
    left, right = 0, len(nums) - 1
    while left < right:
        while not func(nums[left]):
            left += 1
        while func(nums[right]):
            right -= 1
        if left < right:
            nums[left], nums[right] = nums[right], nums[left]


def is_even(num):
    return (num & 1) == 0
```