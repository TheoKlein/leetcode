#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#
# https://leetcode.com/problems/valid-anagram/description/
#
# algorithms
# Easy (51.96%)
# Total Accepted:    333K
# Total Submissions: 640.8K
# Testcase Example:  '"anagram"\n"nagaram"'
#
# Given two strings s and t , write a function to determine if t is an
# of s.
# 
# Example 1:
# 
# 
# Input: s = "anagram", t = "nagaram"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: s = "rat", t = "car"
# Output: false
# 
# 
# Note:
# You may assume the string contains only lowercase alphabets.
# 
# Follow up:
# What if the inputs contain unicode characters? How would you adapt your
# solution to such case?
# 
#
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_c = dict()
        t_c = dict()
        for c in s:
            s_c[c] = s_c.get(c, 0) + 1

        for c in t:
            t_c[c] = t_c.get(c, 0) + 1
        return True if s_c == t_c else False

    def isAnagram_sort(self, s: str, t: str) -> bool:
        s = ''.join(sorted(s))
        t = ''.join(sorted(t))
        return True if s == t else False

