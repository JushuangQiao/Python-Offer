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

## 面试题23 从上往下打印二叉树

## 面试题24 二叉树的后序遍历序列
