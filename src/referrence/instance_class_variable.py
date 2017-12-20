#!/usr/bin/env python
# -*-coding:utf-8-*-
""""""
"""
类变量：
    > 是可在类的所有实例之间共享的值（也就是说，它们不是单独分配给每个实例的）。例如下例中，num_of_instance 就是类变量，用于跟踪存在着多少个Test 的实例。

实例变量：
    > 实例化之后，每个实例单独拥有的变量。
"""
class Test(object):
    num_of_instance = 0

    def __init__(self, name):
        self.name = name
        Test.num_of_instance += 1


print Test.num_of_instance  # 0
t1 = Test('jack')
print Test.num_of_instance  # 1
t2 = Test('lucy')
print t1.name, t1.num_of_instance  # jack 2
print t2.name, t2.num_of_instance  # lucy 2

class Person:
    name="aaa"


p1=Person()
p2=Person()
p1.name="bbb"
#这里p1.name="bbb"是实例调用了类变量,这其实和上面第一个问题一样,
# 就是函数传参的问题,p1.name一开始是指向的类变量name="aaa",
# 但是在实例的作用域里把类变量的引用改变了,就变成了一个实例变量,
# self.name不再引用Person的类变量name了.
print p1.name  # bbb
print p2.name  # aaa
print Person.name  # aaa


class PersonList:
    name=[]

p1=PersonList()
p2=PersonList()
p1.name.append(1)
print p1.name  # [1]
print p2.name  # [1]
print PersonList.name  # [1]

