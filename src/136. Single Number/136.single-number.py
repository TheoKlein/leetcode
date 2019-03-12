#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#
# https://leetcode.com/problems/single-number/description/
#
# algorithms
# Easy (59.14%)
# Total Accepted:    423.1K
# Total Submissions: 715.5K
# Testcase Example:  '[2,2,1]'
#
# Given a non-empty array of integers, every element appears twice except for
# one. Find that single one.
# 
# Note:
# 
# Your algorithm should have a linear runtime complexity. Could you implement
# it without using extra memory?
# 
# Example 1:
# 
# 
# Input: [2,2,1]
# Output: 1
# 
# 
# Example 2:
# 
# 
# Input: [4,1,2,1,2]
# Output: 4
# 
# 
#
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash_table = dict()
        for num in nums:
            try:
                hash_table.pop(num)
            except:
                hash_table[num] = 1
        return hash_table.popitem()[0]

