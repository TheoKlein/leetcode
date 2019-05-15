#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#
# https://leetcode.com/problems/generate-parentheses/description/
#
# algorithms
# Medium (54.67%)
# Total Accepted:    333.1K
# Total Submissions: 609.3K
# Testcase Example:  '3'
#
# 
# Given n pairs of parentheses, write a function to generate all combinations
# of well-formed parentheses.
# 
# 
# 
# For example, given n = 3, a solution set is:
# 
# 
# [
# ⁠ "((()))",
# ⁠ "(()())",
# ⁠ "(())()",
# ⁠ "()(())",
# ⁠ "()()()"
# ]
# 
#
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if not n:
            return []
        l, r, res = n, n, []
        self.dfs(l, r, res, "")
        return res

    def dfs(self, l, r, res, string):
        if l < r:
            return
        if not l and not r:
            res.append(string)
            return
        if l:
            self.dfs(l - 1, r, res, string + ")")
        if r:
            self.dfs(l, r - 1, res, string + "(")
        

