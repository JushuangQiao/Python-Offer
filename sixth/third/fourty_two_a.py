# coding=utf-8
"""
翻转一个英文句子中的单词顺序，标点和普通字符一样处理
Python中字符串是不可变对象，不能用书中的方法，可以直接转化成列表然后转回去
"""


def reverse_words(sentence):
    tmp = sentence.split()
    return ' '.join(tmp[::-1])  # 使用join效率更好，+每次都会创建新的字符串

if __name__ == '__main__':
    test = 'I am a engineer.'
    print reverse_words(test)
