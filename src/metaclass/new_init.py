#!/usr/bin/env python
# -*-coding:utf-8-*-
""""""
"""
新式类都有一个__new__的静态方法，它的原型是object.__new__(cls[, ...])
cls是一个类对象，当你调用C(*args, **kargs)来创建一个类C的实例时，python的内部调用是
C.__new__(C, *args, **kargs)，然后返回值是类C的实例c，在确认
c是C的实例后，python再调用C.__init__(c, *args, **kargs)来初始化实例c
"""
class Singleton(object):
    _singletons = {}
    def __new__(cls, *args, **kwargs):
        if not cls._singletons.has_key(cls):
            cls._singletons[cls] = object.__new__(cls)
        return cls._singletons[cls]

a = Singleton()
b = Singleton()
print a is b # True