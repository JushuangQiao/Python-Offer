# coding=utf-8
# test_module.py
from use_module import single


a = single
b = single
print a.val, b.val
print a is b
a.val = 233
print a.val, b.val
