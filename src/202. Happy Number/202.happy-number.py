#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#
# https://leetcode.com/problems/happy-number/description/
#
# algorithms
# Easy (44.37%)
# Total Accepted:    215.7K
# Total Submissions: 486.3K
# Testcase Example:  '19'
#
# Write an algorithm to determine if a number is "happy".
# 
# A happy number is a number defined by the following process: Starting with
# any positive integer, replace the number by the sum of the squares of its
# digits, and repeat the process until the number equals 1 (where it will
# stay), or it loops endlessly in a cycle which does not include 1. Those
# numbers for which this process ends in 1 are happy numbers.
# 
# Example: 
# 
# 
# Input: 19
# Output: true
# Explanation: 
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1
# 
#
class Solution:
    def isHappy(self, n: int) -> bool:
        hash_table = dict()
        sqrt_sum = 0
        while sqrt_sum != 1:
            sqrt_sum = 0
            while n != 0:
                sqrt_sum += (n % 10) * (n % 10);
                n = n // 10;
                
            if sqrt_sum in hash_table:
                return False
                
            hash_table[sqrt_sum] = 1
            n = sqrt_sum
        return True


