# coding=utf-8
"""
求普通二叉树中两个结点的最低公共祖先
先求出两个结点到根结点的路径，然后从路径中找出最后一个公共结点
"""
from collections import deque


class TreeNode(object):
    """树结点"""
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Tree(object):
    def __init__(self):
        self.root = None
        self.nodes = []  # 树中的结点

    def construct_tree(self, values=None):
        """使用列表构造二叉树"""
        if not values:
            return None
        self.root = TreeNode(values[0])
        self.nodes.append(self.root)
        queue = deque([self.root])
        leng = len(values)
        nums = 1
        while nums < leng:
            node = queue.popleft()
            if node:
                node.left = TreeNode(values[nums]) if values[nums] else None
                queue.append(node.left)
                self.nodes.append(node.left)
                if nums + 1 < leng:
                    node.right = TreeNode(values[nums + 1]) if values[nums + 1] else None
                    queue.append(node.right)
                    self.nodes.append(node.right)
                    nums += 1
                nums += 1

    def get_node(self, index):
        """根据索引返回树中的某个结点"""
        if index >= len(self.nodes):
            return None
        return self.nodes[index]


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

if __name__ == '__main__':
    vals = [0, 1, 2, 3, 4, 5, 6, 7]
    tree = Tree()
    tree.construct_tree(vals)
    r = tree.root  # 树的根结点
    n1 = tree.get_node(7)  # 结点1
    n2 = tree.get_node(4)  # 结点2
    s = Solution(r, n1, n2)
    parent = s.get_last_common_node()  # 公共结点
    print parent, parent.val if parent else None
