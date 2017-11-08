# coding=utf-8
# use_module.py


class SingleTon(object):

    def __init__(self, val):
        self.val = val


single = SingleTon(2)
