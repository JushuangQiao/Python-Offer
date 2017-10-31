# coding=utf-8
"""
复杂链表的复制
链表中除了指向后一个结点的指针之外，还有一个指针指向任意结点
分为三步完成：
一复制每个结点，并把新结点放在老结点后面，如1->2,复制为1->1->2->2
二为每个新结点设置other指针
三把复制后的结点链表拆开
"""
import random


class Node(object):

    def __init__(self, val):
        self.val = val
        self.next = None
        self.other = None


class Solution(object):

    @staticmethod
    def clone_nodes(head):
        # 结点复制
        move = head
        while move:
            tmp = Node(move.val)
            tmp.next = move.next
            move.next = tmp
            move = tmp.next
        return head

    @staticmethod
    def set_nodes(head):
        # other指针设置
        move = head
        while move:
            m_next = move.next
            if move.other:
                m_next.other = move.other.next
            move = m_next.next
        return head

    @staticmethod
    def reconstruct_nodes(head):
        # 结点拆分
        ret = head.next if head else Node
        move = ret
        while head:
            head = move.next
            if head:
                move.next = head.next
                move = move.next
        return ret

    @staticmethod
    def clone_link(head):
        # 结果
        h = Solution.clone_nodes(head)
        h = Solution.set_nodes(h)
        ret = Solution.reconstruct_nodes(h)
        return ret

    @staticmethod
    def print_nodes(head):
        # 打印结点值，结点other的值，用来比较
        ret = []
        while head:
            tmp = [head.val]
            if head.other:
                tmp.append(head.other.val)
            ret.append(tmp)
            head = head.next
        print ret

    @staticmethod
    def construct_nodes(vals):
        """
        构造一个简单的复杂链表
        :param vals: list
        :return: Nodes
        """
        if not vals:
            return Node
        move = head = Node(vals.pop(0))
        nodes = [None, head]
        for v in vals:
            tmp = Node(v)
            move.next = tmp
            nodes.append(tmp)
            move = move.next
        # print [node.val for node in nodes if node]
        move = head
        while move:
            # 设置other指针为随机结点
            move.other = random.choice(nodes)
            move = move.next
        return head


if __name__ == '__main__':
    link = Solution.construct_nodes([1, 2, 3, 4, 5])
    Solution.print_nodes(link)
    test = Solution.clone_link(link)  # 复制
    Solution.print_nodes(test)
