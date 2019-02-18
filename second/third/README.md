# 数据结构

## 面试题3 二维数组中的查找 [LeetCode](https://leetcode.com/problems/search-a-2d-matrix-ii/)
> 题目：二维数组中，每行从左到右递增，每列从上到下递增，给出一个数，判断它是否在数组中
>
> 思路：从左下角或者右上角开始比较

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
> 题目：把字符串中的空格替换成'20%'
>
>方法1：直接使用Python字符串的内置函数

```python
>>> ' a  b  '.replace(' ', '20%')
```
> 方法2: 使用正则表达式

```python
>>> import re
>>> ret = re.compile(' ')
>>> ret.sub('20%', '  a  b  ')
```

## 面试题5 从尾到头打印单链表
> 方法1：使用栈,可以使用列表模拟

```python
def print_links(links):
    stack = []
    while links:
        stack.append(links.val)
        links = links.next
    while stack:
        print stack.pop()
```
> 方法2：直接递归

```python
def print_link_recursion(links):
    if links:
        print_link_recursion(links.next)
        print links.val
```

## 面试题6 重建二叉树 [LeetCode](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)
> 要求：用前序和中序遍历结果构建二叉树，遍历结果中不包含重复值
>
> 思路：前序的第一个元素是根结点的值，在中序中找到该值，中序中该值的左边的元素是根结点的左子树，右边是右子树，然后递归的处理左边和右边
>
> **提示**：二叉树结点，以及对二叉树的各种操作，测试代码见six.py
```python
def construct_tree(preorder=None, inorder=None):
    """
    构建二叉树
    """
    if not preorder or not inorder:
        return None
    index = inorder.index(preorder[0])
    left = inorder[0:index]
    right = inorder[index+1:]
    root = TreeNode(preorder[0])
    root.left = construct_tree(preorder[1:1+len(left)], left)
    root.right = construct_tree(preorder[-len(right):], right)
    return root
```

## 面试题7 用两个栈实现队列
> 要求：用两个栈实现队列，分别实现入队和出队操作
> 思路：一个栈负责入队，另一个负责出队，出栈为空则从入栈中导入到出栈中

```python
class MyQueue(object):
    def __init__(self):
        self.stack = []
        self.stack2 = []

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        if self.stack2:
            return self.stack2.pop()
        while self.stack:
            self.stack2.append(self.stack.pop())
        return self.stack2.pop() if self.stack2 else u'队列为空'
```