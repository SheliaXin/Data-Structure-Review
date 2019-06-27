"""
Given two sorted integer arrays nums1 and nums2,
merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal
to m + n) to hold additional elements from nums2.

Solution: Two pointers / Start from the end
Time complexity: O(m + n)
Space complexity : O(1)
"""
import unittest

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        last, i, j = n+m-1, m-1, n-1
        while i >= 0 and j >= 0:
            if nums1[i] < nums2[j]:
                nums1[last] = nums2[j]
                j -= 1
            else:
                nums1[last] = nums1[i]
                i -= 1
            last -= 1

        if j >= 0:
            nums1[:(j+1)] = nums2[:(j+1)]

        return nums1


class testMerge(unittest.TestCase):
    def testCase1(self):
        s = Solution()
        self.assertEqual(s.merge([1,0], 1, [2], 1), [1,2])

    def testCase2(self):
        s = Solution()
        self.assertEqual(s.merge([2,0], 1, [1], 1), [1,2])

    def testCase3(self):
        s = Solution()
        self.assertEqual(s.merge([0], 0, [2], 1), [2])

if __name__ == "__main__":
    unittest.main()
