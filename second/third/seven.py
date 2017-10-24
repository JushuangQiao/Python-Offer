# coding=utf-8
"""
用两个栈实现队列
"""


class MyQueue(object):
    def __init__(self):
        self.stack = []
        self.stack2 = []

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        if self.stack2:
            return self.stack2.pop()
        while self.stack:
            self.stack2.append(self.stack.pop())
        return self.stack2.pop() if self.stack2 else u'队列为空'


if __name__ == '__main__':
    q = MyQueue()
    q.push(1)
    q.push(2)
    print q.pop()
    q.push(3)
    print q.pop()
    q.push(4)
    print q.pop()
    print q.pop()
    print q.pop()
