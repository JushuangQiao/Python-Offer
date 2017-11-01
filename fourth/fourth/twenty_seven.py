# coding=utf-8
"""
将二叉搜索树转化成一个排序的双向链表，只调整树中结点的指向，不用新结点
中序遍历，根结点的left指向左子树的最后一个(最大)值，right指向右子树的(最小)值
"""

from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Tree(object):
    """
    非二叉搜索树，建树的时候values中的顺序需要注意
    之后有时间会改成二叉搜索树
    """
    def __init__(self):
        self.root = None

    def construct_tree(self, values=None):
        # 结点值不存在的话，values中用None表示
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


class Solution(object):

    @staticmethod
    def convert(tree):
        """结点转换"""
        if not tree:
            return None
        p_last = Solution.convert_nodes(tree, None)
        while p_last and p_last.left:  # 获取链表头结点
            p_last = p_last.left
        return p_last

    @staticmethod
    def convert_nodes(tree, last):
        if not tree:
            return None
        if tree.left:
            last = Solution.convert_nodes(tree.left, last)
        if last:
            last.right = tree
        tree.left = last
        last = tree
        if tree.right:
            last = Solution.convert_nodes(tree.right, last)
        return last

    @staticmethod
    def print_nodes(tree):
        # 正序链表打印
        ret = []
        while tree:
            tmp = []
            tmp.append(tree.left.val if tree.left else None)
            tmp.append(tree.val)
            tmp.append(tree.right.val if tree.right else None)
            ret.append(tmp)
            tree = tree.right
        print ret

if __name__ == '__main__':
    r = Tree()
    # r.construct_tree([2, 1])
    # r.construct_tree([2, None, 3])
    # r.construct_tree([2, 1, 3])
    # r.construct_tree([])
    r.construct_tree([5, 3, 6, 2, 4, None, 7, 1])
    t = Solution.convert(r.root)
    Solution.print_nodes(t)

