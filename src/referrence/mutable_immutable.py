#!/usr/bin/env python
# -*-coding:utf-8-*-
""""""
"""Parameter passed in
        1. the parameter passed in is actually a reference to an object (but
           the reference is passed by value)
        2. some data types are mutable, but others aren't
    So:
        · If you pass a mutable object into a method, the method gets a 
          reference to that same object and you can mutate it to your heart's 
          delight, but if you rebind the reference in the method, the outer 
          scope will know nothing about it, and after you're done, the outer 
          reference will still point at the original object.
        · If you pass an immutable object to a method, you still can't rebind 
          the outer reference, and you can't even mutate the object.
    Mutable:  list, dict, set
    Immutable: strings, tuples, numbers
    [How do I pass a variable by reference?](https://stackoverflow.com/
    questions/986006/how-do-i-pass-a-variable-by-reference)
"""

"""Mutable"""
outer_list = [1, 2, 3]
def mutable_rebind(mutable_list):
    print 'before_rebind: ', mutable_list, id(mutable_list) # before_rebind:  [1, 2, 3] 95069848
    mutable_list = [1, 2, 3, 4, 5]
    print 'after_rebind: ', mutable_list, id(mutable_list) # after_rebind:  [1, 2, 3, 4, 5] 95105432
mutable_rebind(mutable_list=outer_list)
print 'Outer after_rebind: ', outer_list, id(outer_list) # Outer after_rebind:  [1, 2, 3] 95069848

def mutable_change(mutable_list):
    print 'before_change: ', mutable_list, id(
        mutable_list)  # before_change:  [1, 2, 3] 90089112
    mutable_list.append(4)
    print 'after_change: ', mutable_list, id(mutable_list)  # after_change:  [1, 2, 3, 4] 90089112
mutable_change(outer_list)
print 'Outer after_change: ', outer_list, id(outer_list) # [1, 2, 3, 4] 90089112
print '\n{}\n'.format(''.join(['-' for i in range(10)]))
"""Immutable"""
outer_tuple = (1, 2, 3)
def immutable_rebind(mutable_tuple):
    print 'before_rebind: ', mutable_tuple, id(mutable_tuple) # before_rebind:  (1, 2, 3) 80461456
    mutable_tuple = [1, 2, 3, 4, 5]
    print 'after_rebind: ', mutable_tuple, id(mutable_tuple) # after_rebind:  [1, 2, 3, 4, 5] 85473640
mutable_rebind(mutable_list=outer_tuple)
print 'Outer after_rebind: ', outer_tuple, id(outer_tuple) # Outer after_rebind:  (1, 2, 3) 80461456

def immutable_change(mutable_tuple):
    print 'immutable obj can\'t be changed'
immutable_change(outer_tuple)
print 'Outer after_change: ', outer_tuple, id(outer_tuple) # Outer after_rebind:  (1, 2, 3) 80461456