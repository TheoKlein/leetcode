#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#
# https://leetcode.com/problems/binary-tree-inorder-traversal/description/
#
# algorithms
# Medium (56.51%)
# Total Accepted:    456.1K
# Total Submissions: 807.1K
# Testcase Example:  '[1,null,2,3]'
#
# Given a binary tree, return the inorder traversal of its nodes' values.
# 
# Example:
# 
# 
# Input: [1,null,2,3]
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  3
# 
# Output: [1,3,2]
# 
# Follow up: Recursive solution is trivial, could you do it iteratively?
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result, buff = [], []
        while True:
            while root:
                buff.append(root)
                root = root.left
            if not buff:
                return result
            n = buff.pop()
            result.append(n.val)
            root = n.right

    def inorderTraversal_v2(self, root: TreeNode) -> List[int]:
        res, buff = [], []
        while root or buff:
            if root:
                buff.append(root)
                root = root.left
            else:
                node = buff.pop()
                res.append(node.val)
                root = node.right
        return res

