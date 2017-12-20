#!/usr/bin/env python
# -*-coding:utf-8-*-
"""Py2"""
"""
range: list, all members store in memory
xrange: xrange, calculate lazily(act like)
"""
print type(range(5)) # --> list
for i in range(5):
    print i

print  type(xrange(5)) # --> xrange
for i in xrange(5):
    print  i

x = xrange(5)
try:
    next(x)
except Exception as e:
    print str(e) # --> TypeError: xrange object is not an iterator