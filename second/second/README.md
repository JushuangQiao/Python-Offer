# 编程语言

## 面试题2 使用Python实现单例模式

### 方法一 使用__new__实现单例模式
> 使用__new__实现单例模式，具体我对__new__的理解可以点[这里](http://www.cnblogs.com/qiaojushuang/p/7805973.html)
```python
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
```

### 方法二 使用装饰器实现单例模式
```python
from functools import wraps


def single_ton(cls):
    _instance = {}

    @wraps(cls)
    def single(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]
    return single


@single_ton
class SingleTon(object):
    val = 123

    def __init__(self, a):
        self.a = a

if __name__ == '__main__':
    s = SingleTon(1)
    t = SingleTon(2)
    print s is t
    print s.a, t.a
    print s.val, t.val
```

### 方法三 使用模块实现单例模式
> 可以使用模块创建单例模式，然后在其他模块中导入该单例，这个需要所有人遵守导入规则，不然就没法实现单例了

```python
# use_module.py
class SingleTon(object):

    def __init__(self, val):
        self.val = val

single = SingleTon(2)

# test_module.py
from use_module import single

a = single
b = single
print a.val, b.val
print a is b
a.val = 233
print a.val, b.val

```

### 方法四 使用metaclass实现单例模式
> 目前我对元类还了解不深，以后来填坑
