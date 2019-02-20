#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#
# https://leetcode.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (32.93%)
# Total Accepted:    404.3K
# Total Submissions: 1.2M
# Testcase Example:  '["flower","flow","flight"]'
#
# Write a function to find the longest common prefix string amongst an array of
# strings.
# 
# If there is no common prefix, return an empty string "".
# 
# Example 1:
# 
# 
# Input: ["flower","flow","flight"]
# Output: "fl"
# 
# 
# Example 2:
# 
# 
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# 
# 
# Note:
# 
# All given inputs are in lowercase letters a-z.
# 
#
class Solution:
    def longestCommonPrefix(self, strs: 'List[str]') -> 'str':
        def commonPrefix(l, r):
            min_len = min(len(l), len(r))
            for i in range(min_len):
                if l[i] != r[i]:
                    return l[:i]
            return l[:min_len]

        def find_longestCommonPrefix(strs, l, r):
            if l == r:
                return strs[l]
            else:
                mid = (l + r) // 2
                lcpL = find_longestCommonPrefix(strs, l, mid)
                lcpR = find_longestCommonPrefix(strs, mid + 1, r)
                return commonPrefix(lcpL, lcpR)

        if not strs:
            return ""
        return find_longestCommonPrefix(strs, 0, len(strs) - 1)


