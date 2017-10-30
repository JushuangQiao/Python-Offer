# coding=utf-8
"""
栈的压入弹出序列，判断给定的两个序列中，后者是不是前者的弹出序列
序列中不存在相同值
使用一个辅助栈, 如果辅助栈栈顶元素不等于出栈元素，则从入栈中找改值，直到入栈为空
如果最后出栈序列为空，则是入栈的弹出序列
"""


def pop_order(push_stack, pop_stack):
    if not push_stack or not pop_stack:
        return False
    stack = []
    while pop_stack:
        pop_val = pop_stack[0]
        if stack and stack[-1] == pop_val:
            stack.pop()
            pop_stack.pop(0)
        else:
            while push_stack:
                if push_stack[0] != pop_val:
                    stack.append(push_stack.pop(0))
                else:
                    push_stack.pop(0)
                    pop_stack.pop(0)
                    break
        if not push_stack:
            while stack:
                if stack.pop() != pop_stack.pop(0):
                    return False
    if not pop_stack:
        return True
    return False


if __name__ == '__main__':
    print pop_order([1, 2, 3], [2, 3, 1])
