# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given a non-empty array of integers, every element appears twice except for one.
Find that single one.

Note:
Your algorithm should have a linear runtime complexity.
Could you implement it without using extra memory?

Approach 1: Hash Table
    1. Iterate through all elements in nums
    2. Try if hash_table has the key for pop
    3. If not, set up key/value pair
    4. In the end, there is only one element in hash_table, so use popitem to get it
Time complexity: O(n) - loop through all elements
Space complexity: O(n) - hash table

Approach 2: Math
    2*(a+b+c)−(a+a+b+b+c)=c
Time complexity: O(n) - two sum
Space complexity: O(n) - set()

Approach 3: Bit Manipulation
    - XOR: exclusive or, a logical operation that outputs true only when inputs
    differ (one is true, the other is false).[1]
    (a xor b) xor b = a
Time complexity: O(n) - loop
Space complexity: O(1)
"""
import unittest

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash_table = {}
        for i in nums:
            try:
                hash_table.pop(i)
            except:
                hash_table[i] = 1
        return hash_table.popitem()[0]

    def singleNumber2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return 2*sum(set(nums)) - sum(nums)

    def singleNumber3(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in nums:
            res ^= i
        return res

class testSingleNumber(unittest.TestCase):
    def testCase1(self):
        s = Solution()
        self.assertEqual(s.singleNumber([2,2,1]), 1)
        self.assertEqual(s.singleNumber2([2,2,1]), 1)
        self.assertEqual(s.singleNumber3([2,2,1]), 1)

if __name__ == "__main__":
    unittest.main()
