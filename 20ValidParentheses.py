# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.
"""

import unittest

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        map_dict = {'(': ')', '{': '}', '[': ']'}
        stack = []

        for x in s:
            if x in map_dict:
                stack.append(x)

            if x in map_dict.values():
                if len(stack) == 0 or x != map_dict[stack.pop()]:
                    return False

        if len(stack) != 0:
            return False

        return True

class TestIsValid(unittest.TestCase):
    def testCase1(self):
        s = Solution()
        self.assertTrue(s.isValid('({[]})'))

    def testCase2(self):
        s = Solution()
        self.assertFalse(s.isValid('({[]}'))

    def testCase3(self):
        s = Solution()
        self.assertFalse(s.isValid('({[]]]]'))

    def testCase4(self):
        s = Solution()
        self.assertTrue(s.isValid('({[aaa]})'))

if __name__ == '__main__':
    unittest.main()
