#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#
# https://leetcode.com/problems/first-unique-character-in-a-string/description/
#
# algorithms
# Easy (49.89%)
# Total Accepted:    261.8K
# Total Submissions: 524.6K
# Testcase Example:  '"leetcode"'
#
# 
# Given a string, find the first non-repeating character in it and return it's
# index. If it doesn't exist, return -1.
# 
# Examples:
# 
# s = "leetcode"
# return 0.
# 
# s = "loveleetcode",
# return 2.
# 
# 
# 
# 
# Note: You may assume the string contain only lowercase letters.
# 
#
class Solution:
    def firstUniqChar(self, s: str) -> int:
        letter = string.ascii_lowercase
        index = [s.index(c) for c in letter if s.count(c) == 1]
        return min(index) if len(index) > 0 else -1

    def firstUniqChar_lower(self, s: str) -> int:
        for c in s:
            if s.count(c) == 1:
                return s.index(c)
        return -1

