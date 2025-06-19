# Description: My implementation for the solution for the Merge Two Sorted Linked Lists problem on leetcode/neetcode
# Problem: You are given the heads of two sorted linked lists list1 and list2.
#           Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
#           Return the head of the merged linked list.
# Difficulty: easy
# Author: Elbert C.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 and list2: # iterate while both lists are not None
            if list1.val <= list2.val: # list1's value is larger so add list1 to end of list (tail.next)
                tail.next = list1
                list1 = list1.next # update list1's pointer
            else: # vice versa
                tail.next = list2
                list2 = list2.next
            tail = tail.next # update end of list pointer regardless

        # append remainder of the none empty list
        if list1:
            tail.next = list1
        else:
            tail.next = list2

        return dummy.next # return the list