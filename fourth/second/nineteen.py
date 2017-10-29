# coding=utf-8
"""
求二叉树的镜像
思路一：按层次遍历，每一层从右到左
思路二：递归遍历
"""
from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Tree(object):
    def __init__(self):
        self.root = None

    def construct_tree(self, values=None):
        if not values:
            return None
        self.root = TreeNode(values[0])
        queue = deque([self.root])
        leng = len(values)
        nums = 1
        while nums < leng:
            node = queue.popleft()
            if node:
                node.left = TreeNode(values[nums]) if values[nums] else None
                queue.append(node.left)
                if nums + 1 < leng:
                    node.right = TreeNode(values[nums + 1]) if values[nums + 1] else None
                    queue.append(node.right)
                    nums += 1
                nums += 1

    def bfs(self):
        ret = []
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            if node:
                ret.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
        return ret


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


if __name__ == '__main__':
    t = Tree()
    t.construct_tree([1, 2, 6, 4, 3, 7, 5])
    print t.bfs()
    print mirror_bfs(t.root)
    print mirror_pre(t.root)
