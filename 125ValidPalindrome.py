# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given a string, determine if it is a palindrome, considering only alphanumeric
characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

"""

import unittest

class Solution(object):
    def isPalindrome(self, s):
        """
        Time complexity : O(n). Single pass.
        Space complexity : O(1). Constant space required.

        :type s: str
        :rtype: bool
        """
        import re

        s = re.sub(r'[^\w]','',s).lower()
        i,j = 0, len(s)-1

        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1

        return True


    def isPalindrome2(self, s):
        """
        Time complexity : O(1)?
        Space complexity : O(1). Constant space required.

        :type s: str
        :rtype: bool
        """
        
        import re
        word = " ".join(re.findall("[a-zA-Z0-9]+", s)).replace(" ", "").upper()
        if len(word)%2 == 0:
            return word[:int(len(word)/2)] == word[int(len(word)/2):][::-1]
        else:
            return word[:int(len(word)/2)] == word[int(len(word)/2)+1:][::-1]


class testIsPalindrome(unittest.TestCase):
    def testCase1(self):
        s = Solution()
        self.assertTrue(s.isPalindrome("A man, a plan, a canal: Panama"))
        self.assertTrue(s.isPalindrome2("A man, a plan, a canal: Panama"))

    def testCase2(self):
        s = Solution()
        self.assertTrue(s.isPalindrome(""))
        self.assertTrue(s.isPalindrome2(""))

    def testCase3(self):
        s = Solution()
        self.assertFalse(s.isPalindrome("Not"))
        self.assertFalse(s.isPalindrome2("Not"))

if __name__ == "__main__":
    unittest.main()
