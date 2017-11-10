# 4.3 举例让抽象问题具体化

## 面试题21 包含min函数的栈
> 要求：栈的push，pop，min操作的时间复杂度都是O(1)
>
> 思路：使用一个辅助栈保存最小值

```python
class MyStack(object):

    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, val):
        self.stack.append(val)
        if self.min and self.min[-1] < val:
            self.min.append(self.min[-1])
        else:
            self.min.append(val)

    def pop(self):
        if self.stack:
            self.min.pop()
            return self.stack.pop()
        return None

    def min(self):
        return self.min[-1] if self.min else None
```

## 面试题22 栈的压入弹出序列
> 要求：判断给定的两个序列中，后者是不是前者的弹出序列，给定栈不包含相同值
>
> 思路：使用一个辅助栈, 如果辅助栈栈顶元素不等于出栈元素，则从入栈中找改值，直到入栈为空
>
> 如果最后出栈序列为空，则是入栈的弹出序列值
>

```python
 def pop_order(push_stack, pop_stack):
    if not push_stack or not pop_stack:
        return False
    stack = []
    while pop_stack:
        pop_val = pop_stack[0]
        if stack and stack[-1] == pop_val:
            stack.pop()
            pop_stack.pop(0)
        else:
            while push_stack:
                if push_stack[0] != pop_val:
                    stack.append(push_stack.pop(0))
                else:
                    push_stack.pop(0)
                    pop_stack.pop(0)
                    break
        if not push_stack:
            while stack:
                if stack.pop() != pop_stack.pop(0):
                    return False
    if not pop_stack:
        return True
    return False
```

## 面试题23 从上往下打印二叉树
> 思路：广度优先搜索，按层次遍历
>

```python
 def bfs(tree):
    if not tree:
        return None
    stack = [tree]
    ret = []
    while stack:
        node = stack.pop(0)
        ret.append(node.val)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return ret
```

## 面试题24 二叉搜索树的后序遍历序列
> 要求：判断给定的整数数组是不是二叉搜索树的后序遍历序列
>
> 整数数组中不包含重复值
>
> 整数序列的最后一个值是根结点，然后比根结点小的值是左子树，剩下的是右子树，递归左右子树
>

```python
 def is_post_order(order):
    length = len(order)
    if length:
        root = order[-1]
        left = 0
        while order[left] < root:
            left += 1
        right = left
        while right < length - 1:
            if order[right] < root:
                return False
            right += 1
        left_ret = True if left == 0 else is_post_order(order[:left])
        right_ret = True if left == right else is_post_order(order[left:right])
        return left_ret and right_ret
    return False
```

## 面试题25 二叉树中和为某一值的路径
> 要求：输入一棵二叉树和一个值，求从根结点到叶结点的和等于该值的路径
>
> 深度优先搜索变形
>

```python
 def find_path(tree, num):
    ret = []
    if not tree:
        return ret
    path = [tree]
    sums = [tree.val]

    def dfs(tree):
        if tree.left:
            path.append(tree.left)
            sums.append(sums[-1]+tree.left.val)
            dfs(tree.left)
        if tree.right:
            path.append(tree.right)
            sums.append(sums[-1] + tree.right.val)
            dfs(tree.right)
        if not tree.left and not tree.right:
            if sums[-1] == num:
                ret.append([p.val for p in path])
        path.pop()
        sums.pop()

    dfs(tree)
    return ret
```