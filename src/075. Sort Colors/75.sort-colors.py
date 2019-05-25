#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#
# https://leetcode.com/problems/sort-colors/description/
#
# algorithms
# Medium (42.12%)
# Total Accepted:    316.6K
# Total Submissions: 751.7K
# Testcase Example:  '[2,0,2,1,1,0]'
#
# Given an array with n objects colored red, white or blue, sort them in-place
# so that objects of the same color are adjacent, with the colors in the order
# red, white and blue.
# 
# Here, we will use the integers 0, 1, and 2 to represent the color red, white,
# and blue respectively.
# 
# Note: You are not suppose to use the library's sort function for this
# problem.
# 
# Example:
# 
# 
# Input: [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# 
# Follow up:
# 
# 
# A rather straight forward solution is a two-pass algorithm using counting
# sort.
# First, iterate the array counting number of 0's, 1's, and 2's, then overwrite
# array with total number of 0's, then 1's and followed by 2's.
# Could you come up with a one-pass algorithm using only constant space?
# 
# 
#
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n0 = n1 = n2 = -1
        for i in range(len(nums)):
            if nums[i] == 0:
                n0, n1, n2 = n0 + 1, n1 + 1, n2 + 1
                nums[n2], nums[n1], nums[n0] = 2, 1, 0
            elif nums[i] == 1:
                n1, n2 = n1 + 1, n2 + 1
                nums[n2], nums[n1] = 2, 1
            else:
                n2 += 1
                nums[n2] = 2
        

