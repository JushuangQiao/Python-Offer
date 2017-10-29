# 4.2 画图让抽象问题形象化

## 面试题19 二叉树的镜像
> 思路一：可以按层次遍历，每一层从右到左
>
> 思路二：使用递归

```python
def mirror_bfs(root):
    ret = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            ret.append(node.val)
            queue.append(node.right)
            queue.append(node.left)
    return ret


def mirror_pre(root):
    ret = []

    def traversal(root):
        if root:
            ret.append(root.val)
            traversal(root.right)
            traversal(root.left)
    traversal(root)
    return ret
```
