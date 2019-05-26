#
# @lc app=leetcode id=258 lang=python3
#
# [258] Add Digits
#
# https://leetcode.com/problems/add-digits/description/
#
# algorithms
# Easy (54.08%)
# Total Accepted:    237.8K
# Total Submissions: 439.7K
# Testcase Example:  '38'
#
# Given a non-negative integer num, repeatedly add all its digits until the
# result has only one digit.
# 
# Example:
# 
# 
# Input: 38
# Output: 2 
# Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
# Since 2 has only one digit, return it.
# 
# 
# Follow up:
# Could you do it without any loop/recursion in O(1) runtime?
#
class Solution:
    def addDigits(self, num: int) -> int:
        # list the result from 1 to 20
        # we can find out the law
        if num == 0:
            return 0
        return (num - 1) % 9 + 1

    def addDigits_origin(self, num: int) -> int:
        while num / 10 > 0:
            count = 0
            while num > 0:
                count += num % 10
                num /= 10
            num = count
        return num

