# coding=utf-8
"""
O(1)时间删除链表结点
如果有后续结点，后续结点的值前移，删除后续结点，如果没有，只能顺序查找了
"""


def delete_node(link, node):
    if node == link:  # 只有一个结点
        del node
    if node.next is None:  # node是尾结点
        while link:
            if link.next == node:
                link.next = None
            link = link.next
    else:
        node.val = node.next.val
        n_node = node.next
        node.next = n_node.next
        del n_node


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


if __name__ == '__main__':
    node1 = ListNode(1)
    node1.next = ListNode(2)
    node1.next.next = ListNode(3)
    delete_node(node1, ListNode(4))
    print node1.val, node1.next.val

