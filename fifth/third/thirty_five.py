# coding=utf-8
"""
求字符串中第一个只出现一次的字符
使用两个hash，一个记录每个字符穿线的次数，另一个记录每个字符第一次出现的位置
"""


def first_not_repeating_char(string):
    if not string:
        return -1
    count = {}
    loc = {}
    for k, s in enumerate(string):
        count[s] = count[s] + 1 if count.get(s) else 1
        loc[s] = loc[s] if loc.get(s) else k
    ret = float('inf')
    for k in loc.keys():
        if count.get(k) == 1 and loc[k] < ret:
            ret = loc[k]
    return ret

if __name__ == '__main__':
    test = 'abaccbdse'
    print first_not_repeating_char(test)
