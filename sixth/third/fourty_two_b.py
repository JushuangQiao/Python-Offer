# coding=utf-8
"""
把字符串的前面的若干位移到字符串的后面
"""


def rotate_string(s, n):
    if not s:
        return ''
    n %= len(s)
    return s[n:] + s[:n]

if __name__ == '__main__':
    test = 'abcdefg'
    print rotate_string(test, 1)
