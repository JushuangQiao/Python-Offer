# 7.2 案例二

## 面试题50 树中两个结点的最低公共祖先
> 要求：求普通二叉树中两个结点的最低公共祖先
>
>方法一：先求出两个结点到根结点的路径，然后从路径中找出最后一个公共结点
>
>备注：文件fifty.py中包含该代码的具体测试数据

```python
class Solution(object):

    def __init__(self, root, node1, node2):
        self.root = root  # 树的根结点
        self.node1 = node1
        self.node2 = node2  # 需要求的两个结点

    @staticmethod
    def get_path(root, node, ret):
        """获取结点的路径"""
        if not root or not node:
            return False
        ret.append(root)
        if root == node:
            return True
        left = Solution.get_path(root.left, node, ret)
        right = Solution.get_path(root.right, node, ret)
        if left or right:
            return True
        ret.pop()

    def get_last_common_node(self):
        """获取公共结点"""
        route1 = []
        route2 = []  # 保存结点路径
        ret1 = Solution.get_path(self.root, self.node1, route1)
        ret2 = Solution.get_path(self.root, self.node2, route2)
        ret = None
        if ret1 and ret2:  # 路径比较
            length = len(route1) if len(route1) <= len(route2) else len(route2)
            index = 0
            while index < length:
                if route1[index] == route2[index]:
                    ret = route1[index]
                index += 1
        return ret
```
