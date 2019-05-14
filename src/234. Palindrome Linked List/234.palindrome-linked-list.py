#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#
# https://leetcode.com/problems/palindrome-linked-list/description/
#
# algorithms
# Easy (35.92%)
# Total Accepted:    253.7K
# Total Submissions: 706.3K
# Testcase Example:  '[1,2]'
#
# Given a singly linked list, determine if it is a palindrome.
# 
# Example 1:
# 
# 
# Input: 1->2
# Output: false
# 
# Example 2:
# 
# 
# Input: 1->2->2->1
# Output: true
# 
# Follow up:
# Could you do it in O(n) time and O(1) space?
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        tmp = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next

            # slow move one step and reverse the link
            tmp, tmp.next, slow = slow, tmp, slow.next

        # deal with edge case
        if fast:
            slow = slow.next

        while tmp and tmp.val == slow.val:
            slow = slow.next
            tmp = tmp.next

        # is palindrome if tmp if None
        return not tmp
        

        

