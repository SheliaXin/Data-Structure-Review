# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Design a stack that supports push, pop, top, and retrieving the minimum element
in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
"""
import unittest

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []


    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if len(self.stack) > 0:
            self.stack.append((x, min(self.stack[-1][1], x)))
        else:
            self.stack.append((x,x))


    def pop(self):
        """
        :rtype: None
        """
        return self.stack.pop()[0]


    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1][0]


    def getMin(self):
        """
        :rtype: int
        """
        return self.stack[-1][1]


class testMinStack(unittest.TestCase):
    def testCase1(self):
        s = MinStack()
        s.push(1)
        s.push(2)
        s.push(-3)
        self.assertEqual(s.getMin(), -3)
        self.assertEqual(s.pop(), -3)
        self.assertEqual(s.getMin(), 1)
        self.assertEqual(s.top(), 2)

if __name__ == "__main__":
    unittest.main()
