# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given a sorted array nums, remove the duplicates in-place such that each
element appear only once and return the new length.

Do not allocate extra space for another array, you must do this
by modifying the input array in-place with O(1) extra memory.

Solution: (Two Pointers) use pointer to track and replace the duplicates
"""

import unittest

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        slow_point = 0

        for x in nums:
            if nums[slow_point] != x:
                slow_point += 1
                nums[slow_point] = x

        return slow_point+1


class TestRemoveDuplicates(unittest.TestCase):
    def testCase1(self):
        s = Solution()
        self.assertEqual(s.removeDuplicates([1,1,2]), 2)

    def testCase2(self):
        s = Solution()
        self.assertEqual(s.removeDuplicates([]), 0)

    def testCase3(self):
        s = Solution()
        self.assertEqual(s.removeDuplicates([1,1,1,2,3,3,3,3,4]), 4)


if __name__ == "__main__":
    unittest.main()
