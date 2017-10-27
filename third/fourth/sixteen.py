# coding=utf-8
"""
反转链表
需要考虑空链表，只有一个结点的链表
"""


def reverse_link(head):
    if not head or not head.next:
        return head
    then = head.next
    head.next = None
    last = then.next
    while then:
        then.next = head
        head = then
        then = last
        if then:
            last = then.next
    return head


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Nodes(object):
    def __init__(self, values=None):
        self.nodes = self._set_link(values) if values else None

    def get_link(self):
        return self.nodes

    def print_self(self):
        Nodes.print_link(self.nodes)

    @staticmethod
    def print_link(link=None):
        count = 1
        while link:
            if count == 1:
                print link.val,
            elif count % 5 == 0:
                print '->', link.val
            else:
                print '->', link.val,
            count += 1
            link = link.next
        print

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
    nodes = Nodes([1, 2, 3])
    link = nodes.get_link()
    nodes.print_self()
    head = reverse_link(link)
    nodes.nodes = head
    Nodes.print_link(head)
    nodes.print_self()
