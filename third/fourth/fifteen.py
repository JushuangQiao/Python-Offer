# coding=utf-8
"""
链表中倒数第k个结点
使用快慢指针，快的先走k-1步，需要考虑控链表以及k为0
"""


def last_kth(link, k):
    if not link or k <= 0:
        return None
    move = link
    while move and k-1 >= 0:
        move = move.next
        k -= 1
    while move:
        move = move.next
        link = link.next
    if k == 0:
        return link.val
    return None


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Nodes(object):
    def __init__(self, values=None):
        self.nodes = self._set_link(values) if values else None

    def get_link(self):
        return self.nodes

    def _set_link(self, values):
        head = ListNode(0)
        move = head
        try:
            for val in values:
                tmp = ListNode(val)
                move.next = tmp
                move = move.next
        except Exception as e:
            print e
        return head.next


if __name__ == '__main__':
    nodes = Nodes((1, 2, 3, 4, 5, 6, 7, 8, 9, 20, 22))
    link = nodes.get_link()
    print last_kth(link, 12)
