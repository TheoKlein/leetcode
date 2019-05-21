#
# @lc app=leetcode id=279 lang=python3
#
# [279] Perfect Squares
#
# https://leetcode.com/problems/perfect-squares/description/
#
# algorithms
# Medium (41.82%)
# Total Accepted:    180.1K
# Total Submissions: 430.7K
# Testcase Example:  '12'
#
# Given a positive integer n, find the least number of perfect square numbers
# (for example, 1, 4, 9, 16, ...) which sum to n.
# 
# Example 1:
# 
# 
# Input: n = 12
# Output: 3 
# Explanation: 12 = 4 + 4 + 4.
# 
# Example 2:
# 
# 
# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.
#
class Solution:
    def numSquares(self, n: int) -> int:
        if n < 2:
            return n
        
        square_nums = []
        i = 1
        while i * i <= n:
            square_nums.append(i * i)
            i += 1

        count = 0
        buff = {n}

        while buff:
            count += 1
            tmp = set()
            for num in buff:
                for square_num in square_nums:
                    if num == square_num:
                        return count
                    if num < square_num:
                        break
                    tmp.add(num - square_num)
            buff = tmp
        return count


    def numSquares_TLE(self, n: int) -> int:
        if not n:
            return 0

        buff = [sys.maxsize] * (n + 1)
        for i in range(1, n + 1):
            sqrt_num = int(math.sqrt(i))

            if sqrt_num * sqrt_num == i:
                buff[i] = 1
                continue

            for j in range(1, sqrt_num + 1):
                diff = i - j * j
                buff[i] = min(buff[i], buff[diff] + 1)
        return buff[n]

