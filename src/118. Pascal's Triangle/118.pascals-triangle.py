#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#
# https://leetcode.com/problems/pascals-triangle/description/
#
# algorithms
# Easy (45.71%)
# Total Accepted:    247.9K
# Total Submissions: 542.4K
# Testcase Example:  '5'
#
# Given a non-negative integer numRows, generate the first numRows of Pascal's
# triangle.
# 
# 
# In Pascal's triangle, each number is the sum of the two numbers directly
# above it.
# 
# Example:
# 
# 
# Input: 5
# Output:
# [
# ⁠    [1],
# ⁠   [1,1],
# ⁠  [1,2,1],
# ⁠ [1,3,3,1],
# ⁠[1,4,6,4,1]
# ]
# 
# 
#
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows < 1:
            return []
            
        result = list()
        prev_stair = [1]
        result.append(prev_stair)

        for i in range(2, numRows + 1):
            prev_stair = self.recur(prev_stair, i)
            result.append(prev_stair)
        return result

    def recur(self, prev_stair, numRow):
        result = [1] * numRow
        for i in range(1, numRow - 1):
            result[i] = prev_stair[i - 1] + prev_stair[i]
        return result
