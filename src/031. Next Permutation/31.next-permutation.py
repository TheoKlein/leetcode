#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#
# https://leetcode.com/problems/next-permutation/description/
#
# algorithms
# Medium (30.45%)
# Total Accepted:    236.3K
# Total Submissions: 776K
# Testcase Example:  '[1,2,3]'
#
# Implement next permutation, which rearranges numbers into the
# lexicographically next greater permutation of numbers.
# 
# If such arrangement is not possible, it must rearrange it as the lowest
# possible order (ie, sorted in ascending order).
# 
# The replacement must be in-place and use only constant extra memory.
# 
# Here are some examples. Inputs are in the left-hand column and its
# corresponding outputs are in the right-hand column.
# 
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1
# 
#
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # check nums are in descending order
        i = j = len(nums) - 1
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1
        if i == 0:
            nums.reverse()
            return

        k = i - 1   # target index
        while nums[j] <= nums[k]:
            j -= 1
        nums[k], nums[j] = nums[j], nums[k] # swap
        l, r = k + 1, len(nums) - 1
        while l < r:    # swap remaining numbers
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

