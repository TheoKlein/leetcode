#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#
# https://leetcode.com/problems/unique-paths/description/
#
# algorithms
# Medium (47.46%)
# Total Accepted:    284.9K
# Total Submissions: 600.3K
# Testcase Example:  '3\n2'
#
# A robot is located at the top-left corner of a m x n grid (marked 'Start' in
# the diagram below).
# 
# The robot can only move either down or right at any point in time. The robot
# is trying to reach the bottom-right corner of the grid (marked 'Finish' in
# the diagram below).
# 
# How many possible unique paths are there?
# 
# 
# Above is a 7 x 3 grid. How many possible unique paths are there?
# 
# Note: m and n will be at most 100.
# 
# Example 1:
# 
# 
# Input: m = 3, n = 2
# Output: 3
# Explanation:
# From the top-left corner, there are a total of 3 ways to reach the
# bottom-right corner:
# 1. Right -> Right -> Down
# 2. Right -> Down -> Right
# 3. Down -> Right -> Right
# 
# 
# Example 2:
# 
# 
# Input: m = 7, n = 3
# Output: 28
# 
#
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if not m or not n:
            return 0

        buff = [[1 for i in range(n)] for j in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                buff[i][j] = buff[i - 1][j] + buff[i][j - 1]
        return buff[-1][-1]

