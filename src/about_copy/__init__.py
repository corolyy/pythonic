#!/usr/bin/env python
# -*-coding:utf-8-*-
import copy
'''
'''
'''
首先，对赋值操作我们要有以下认识：

赋值是将一个对象的地址赋值给一个变量，让变量指向该地址（ 旧瓶装旧酒 ）。
修改不可变对象（str、tuple）需要开辟新的空间
修改可变对象（list等）不需要开辟新的空间
'''
# 浅拷贝仅仅复制了容器中元素的地址
a = ['hello', [1, 2, 3]]
b = copy.copy(a)
a[0] = 'world'
a[1].append(4)
print a # ['world', [1, 2, 3, 4]]
print b # ['hello', [1, 2, 3, 4]]

# 深拷贝，完全拷贝了一个副本，容器内部元素地址都不一样
a = ['hello', [1, 2, 3]]
b = copy.deepcopy(a)
a[0] = 'world'
a[1].append(4)
print a # ['world', [1, 2, 3, 4]]
print b # ['hello', [1, 2, 3]]