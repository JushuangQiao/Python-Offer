# 数据结构

## 面试题3 二维数组中的查找
### 题目：二维数组中，每行从左到右递增，每列从上到下递增，给出一个数，判断它是否在数组中
### 思路：从左下角或者右上角开始比较

```python
def find_integer(matrix, num):
    """
    :param matrix: [[]]
    :param num: int
    :return: bool
    """
    if not matrix:
        return False
    rows, cols = len(matrix), len(matrix[0])
    row, col = rows - 1, 0
    while row >= 0 and col <= cols - 1:
        if matrix[row][col] == num:
            return True
        elif matrix[row][col] > num:
            row -= 1
        else:
            col += 1
    return False
```

## 面试题4 替换空格
### 题目：把字符串中的空格替换成'20%'
###  方法1：直接使用Python字符串的内置函数
```python
>>> ' a  b  '.replace(' ', '20%')
```
### 方法2: 使用正则表达式
```python
>>> import re
>>> ret = re.compile(' ')
>>> ret.sub('20%', '  a  b  ')
```

## 面试题5 从尾到头打印单链表
### 方法1：使用栈,可以使用列表模拟
```python
def print_links(links):
    stack = []
    while links:
        stack.append(links.val)
        links = links.next
    while stack:
        print stack.pop()
```
### 方法2：直接递归
```python
def print_link_recursion(links):
    if links:
        print_link_recursion(links.next)
        print links.val
```
