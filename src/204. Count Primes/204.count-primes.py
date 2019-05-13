#
# @lc app=leetcode id=204 lang=python3
#
# [204] Count Primes
#
# https://leetcode.com/problems/count-primes/description/
#
# algorithms
# Easy (28.86%)
# Total Accepted:    232.4K
# Total Submissions: 805.2K
# Testcase Example:  '10'
#
# Count the number of prime numbers less than a non-negative number, n.
# 
# Example:
# 
# 
# Input: 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
# 
# 
#
class Solution:
    def countPrimes(self, n: int) -> int:   
        if n <= 2:
            return 0     
        primes = [1] * n
        primes[0], primes[1] = 0, 0

        for i in range(2, n):
            if primes[i] == 1:
                for j in range(2, (n - 1) // i + 1):
                    primes[i * j] = 0
        return sum(primes)

