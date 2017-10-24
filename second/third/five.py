# coding=utf-8
"""
从尾到头打印单链表
思路1：使用栈
思路2：递归
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Link(object):

    @staticmethod
    def link(values):
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


def print_links(links):
    stack = []
    while links:
        stack.append(links.val)
        links = links.next
    while stack:
        print stack.pop()


def print_link_recursion(links):
    if links:
        print_link_recursion(links.next)
        print links.val

if __name__ == '__main__':
    head = Link.link([1, 2, 3, 4, 5, 6])
    # print_links(head)
    print_link_recursion(head)
