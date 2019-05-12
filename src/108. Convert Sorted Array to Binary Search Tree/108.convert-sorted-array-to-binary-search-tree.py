#
# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
#
# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/
#
# algorithms
# Easy (50.47%)
# Total Accepted:    257.5K
# Total Submissions: 510.3K
# Testcase Example:  '[-10,-3,0,5,9]'
#
# Given an array where elements are sorted in ascending order, convert it to a
# height balanced BST.
# 
# For this problem, a height-balanced binary tree is defined as a binary tree
# in which the depth of the two subtrees of every node never differ by more
# than 1.
# 
# Example:
# 
# 
# Given the sorted array: [-10,-3,0,5,9],
# 
# One possible answer is: [0,-3,9,-10,null,5], which represents the following
# height balanced BST:
# 
# ⁠     0
# ⁠    / \
# ⁠  -3   9
# ⁠  /   /
# ⁠-10  5
# 
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # avoid to use python list slice function becuase it cause O(n)
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self.recur(nums, 0, len(nums))

    def recur(self, nums, left, right):
        if left == right:
            return None
        
        mid = (left + right) // 2
        node = TreeNode(nums[mid])
        node.left = self.recur(nums, left, mid)
        node.right = self.recur(nums, mid + 1, right)

        return node

