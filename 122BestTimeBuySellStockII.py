# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Say you have an array for which the ith element is the price of a given stock
on day i.

Design an algorithm to find the maximum profit. You may complete as many
transactions as you like (i.e., buy one and sell one share of the stock
multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you
must sell the stock before you buy again).

Input: [7,1,5,3,6,4]
Output: 7
Explanation:
    Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
    Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.

Time complexity : O(n). Single pass.
Space complexity : O(1). Constant space required.
"""

import unittest

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        low = float("inf")
        last = 0
        profit, tot_profit = 0, 0

        for p in prices:
            low = min(p, low)
            profit = max(profit, p-low)
            if p < last:
                low = p
                tot_profit += profit
                profit = 0
            last = p

        tot_profit += profit

        return(tot_profit)

    def maxProfit2(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        return sum([prices[i+1] - prices[i] for i in range(len(prices)-1) if prices[i+1] > prices[i] ])


class testMaxProfit(unittest.TestCase):
    def testCase1(self):
        s = Solution()
        self.assertEqual(s.maxProfit([7,1,5,3,6,4]), 7)

    def testCase2(self):
        s = Solution()
        self.assertEqual(s.maxProfit([7,1]), 0)

    def testCase3(self):
        s = Solution()
        self.assertEqual(s.maxProfit([]), 0)

    def testCase4(self):
        s = Solution()
        self.assertEqual(s.maxProfit([1,2,3,4,5]), 4)

if __name__ == "__main__":
    unittest.main()
