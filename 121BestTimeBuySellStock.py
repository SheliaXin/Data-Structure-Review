# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Say you have an array for which the ith element is the price of a given stock
on day i.

If you were only permitted to complete at most one transaction (i.e., buy one
and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

[7,1,5,3,6,4] -> day 2 - 5: 5

Time complexity : O(n)O(n). Only a single pass is needed.
Space complexity : O(1)O(1). Only two variables are used.
"""

import unittest

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        low = float("inf")
        max_profit = 0

        for p in prices:
            low = min(low, p)
            max_profit = max(p - low, max_profit)

        return(max_profit)


class testMaxProfit(unittest.TestCase):
    def testCase1(self):
        s = Solution()
        self.assertEqual(s.maxProfit([7,1,5,3,6,4]), 5)

    def testCase2(self):
        s = Solution()
        self.assertEqual(s.maxProfit([7,1]), 0)

    def testCase3(self):
        s = Solution()
        self.assertEqual(s.maxProfit([]), 0)

if __name__ == "__main__":
    unittest.main()
