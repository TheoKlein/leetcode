#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#
# https://leetcode.com/problems/find-the-duplicate-number/description/
#
# algorithms
# Medium (49.45%)
# Total Accepted:    186.2K
# Total Submissions: 376.6K
# Testcase Example:  '[1,3,4,2,2]'
#
# Given an array nums containing n + 1 integers where each integer is between 1
# and n (inclusive), prove that at least one duplicate number must exist.
# Assume that there is only one duplicate number, find the duplicate one.
# 
# Example 1:
# 
# 
# Input: [1,3,4,2,2]
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: [3,1,3,4,2]
# Output: 3
# 
# Note:
# 
# 
# You must not modify the array (assume the array is read only).
# You must use only constant, O(1) extra space.
# Your runtime complexity should be less than O(n^2).
# There is only one duplicate number in the array, but it could be repeated
# more than once.
# 
# 
#
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # use binary search to look for the wrong count in sub range (n/2, n]
        l, r = 0, len(nums) - 1
        m = (l + r) // 2

        while r - l > 1:
            count = 0
            for n in nums:
                if m < n <= r:
                    count += 1
            if count > r - m:   # fail on right sub range's number
                l = m
            else:
                r = m
            m = (l + r) // 2
        return r


