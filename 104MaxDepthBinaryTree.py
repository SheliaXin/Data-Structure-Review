# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/maximum-depth-of-binary-tree/

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root
node down to the farthest leaf node.

Note: A leaf is a node with no children.
Solution: Recursion (DFS)

Time complexity: O(n)
Space complexity: O(log(n))
"""
import unittest

class TreeNode(object):
    """ Definition of a binary tree node."""
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        else:
            left_depth = self.maxDepth(root.left)
            right_depth = self.maxDepth(root.right)
            return max(left_depth, right_depth) + 1


class TestMaxDepth(unittest.TestCase):
    def testCase1(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.right.left = TreeNode(4)
        s = Solution()
        self.assertEqual(s.maxDepth(root),3)

    def testCase2(self):
        root = TreeNode(2)
        s = Solution()
        self.assertEqual(s.maxDepth(root),1)


if __name__ == "__main__":
    unittest.main()
