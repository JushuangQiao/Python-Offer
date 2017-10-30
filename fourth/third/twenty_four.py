# coding=utf-8
"""
判断给定的整数数组是不是二叉搜索树的后序遍历序列
整数数组中不包含重复值
整数序列的最后一个值是根结点，然后比根结点小的值是左子树，剩下的是右子树，递归左右子树
"""


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


if __name__ == '__main__':
    print is_post_order([9, 6, 7])
