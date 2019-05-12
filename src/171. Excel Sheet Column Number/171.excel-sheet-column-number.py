#
# @lc app=leetcode id=171 lang=python3
#
# [171] Excel Sheet Column Number
#
# https://leetcode.com/problems/excel-sheet-column-number/description/
#
# algorithms
# Easy (51.39%)
# Total Accepted:    217.4K
# Total Submissions: 423K
# Testcase Example:  '"A"'
#
# Given a column title as appear in an Excel sheet, return its corresponding
# column number.
# 
# For example:
# 
# 
# ⁠   A -> 1
# ⁠   B -> 2
# ⁠   C -> 3
# ⁠   ...
# ⁠   Z -> 26
# ⁠   AA -> 27
# ⁠   AB -> 28 
# ⁠   ...
# 
# 
# Example 1:
# 
# 
# Input: "A"
# Output: 1
# 
# 
# Example 2:
# 
# 
# Input: "AB"
# Output: 28
# 
# 
# Example 3:
# 
# 
# Input: "ZY"
# Output: 701
# 
#
class Solution:
    def titleToNumber(self, s: str) -> int:
        res = 0
        for i in range(1, len(s) + 1):
            res += (ord(s[len(s) - i]) - ord('A') + 1) * (26 ** (i - 1))
        return res

