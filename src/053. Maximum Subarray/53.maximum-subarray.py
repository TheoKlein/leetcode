#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#
# https://leetcode.com/problems/maximum-subarray/description/
#
# algorithms
# Easy (42.69%)
# Total Accepted:    460K
# Total Submissions: 1.1M
# Testcase Example:  '[-2,1,-3,4,-1,2,1,-5,4]'
#
# Given an integer array nums, find the contiguous subarray (containing at
# least one number) which has the largest sum and return its sum.
# 
# Example:
# 
# 
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# 
# 
# Follow up:
# 
# If you have figured out the O(n) solution, try coding another solution using
# the divide and conquer approach, which is more subtle.
# 
#
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def getMax(nums, l, r):
            if l == r:
                return nums[l]

            m = (l + r) // 2
            lMax = getMax(nums, l, m)
            rMax = getMax(nums, m + 1, r)
            crossMax = getCrossMax(nums, l, m, r)

            return max(max(lMax, rMax), crossMax)

        def getCrossMax(nums, l, m, r):
            lMax = nums[m]
            rMax = nums[m + 1]
            lSum = 0
            rSum = 0

            for i in reversed(range(l, m + 1)):
                lSum += nums[i]
                lMax = max(lMax, lSum)

            for i in range(m + 1, r + 1):
                rSum += nums[i]
                rMax = max(rMax, rSum)

            return max(max(lMax, rMax), lMax + rMax)
        
        return getMax(nums, 0, len(nums) - 1)
