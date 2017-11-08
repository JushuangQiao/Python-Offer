# coding=utf-8
"""
使用__new__实现单例模式
"""


class SingleTon(object):
    _instance = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super(SingleTon, cls).__new__(cls, *args, **kwargs)
        # print cls._instance
        return cls._instance[cls]


class MyClass(SingleTon):
    class_val = 22

    def __init__(self, val):
        self.val = val

    def obj_fun(self):
        print self.val, 'obj_fun'

    @staticmethod
    def static_fun():
        print 'staticmethod'

    @classmethod
    def class_fun(cls):
        print cls.class_val, 'classmethod'


if __name__ == '__main__':
    a = MyClass(1)
    b = MyClass(2)
    print a is b   # True
    print id(a), id(b)  # 4367665424 4367665424
    # 类型验证
    print type(a)  # <class '__main__.MyClass'>
    print type(b)  # <class '__main__.MyClass'>
    # 实例方法
    a.obj_fun()  # 2 obj_fun
    b.obj_fun()  # 2 obj_fun
    # 类方法
    MyClass.class_fun()  # 22 classmethod
    a.class_fun()  # 22 classmethod
    b.class_fun()  # 22 classmethod
    # 静态方法
    MyClass.static_fun()  # staticmethod
    a.static_fun()  # staticmethod
    b.static_fun()  # staticmethod
    # 类变量
    a.class_val = 33
    print MyClass.class_val  # 22
    print a.class_val  # 33
    print b.class_val  # 33
    # 实例变量
    print b.val  # 2
    print a.val  # 2
