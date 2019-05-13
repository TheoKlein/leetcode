#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#
# https://leetcode.com/problems/house-robber/description/
#
# algorithms
# Easy (40.96%)
# Total Accepted:    315.2K
# Total Submissions: 769.6K
# Testcase Example:  '[1,2,3,1]'
#
# You are a professional robber planning to rob houses along a street. Each
# house has a certain amount of money stashed, the only constraint stopping you
# from robbing each of them is that adjacent houses have security system
# connected and it will automatically contact the police if two adjacent houses
# were broken into on the same night.
# 
# Given a list of non-negative integers representing the amount of money of
# each house, determine the maximum amount of money you can rob tonight without
# alerting the police.
# 
# Example 1:
# 
# 
# Input: [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money =
# 3).
# Total amount you can rob = 1 + 3 = 4.
# 
# Example 2:
# 
# 
# Input: [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5
# (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.
# 
# 
#
class Solution:
    def rob(self, nums: List[int]) -> int:
        self.buff = [-1] * len(nums)
        return self.recur(nums, len(nums) - 1)

    def recur(self, nums, n):
        # top-down recursive DP
        if n < 0 :
            return 0
        if self.buff[n] > -1:
            return self.buff[n]
        
        self.buff[n] = max(self.recur(nums, n - 2) + nums[n], self.recur(nums, n - 1))
        return self.buff[n]

