# Description: My implementation for the solution for the Reorder List problem on leetcode/neetcode
# Problem: You are given the head of a singly linked-list. The list can be represented as:
#           L0 → L1 → … → Ln - 1 → Ln
#           Reorder the list to be on the following form:
#           L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
#           You may not modify the values in the list's nodes. Only nodes themselves may be changed.
# Difficulty: medium
# Author: Elbert C.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # break linked lists into 2 halves
        slow, fast = head, head.next

        # find where our 2nd half is with slow/fast pointers
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # we know our 2nd half start so mark that as our second linked list
        second = slow.next
        prev = slow.next = None # first node of 2nd half is now the tail because we want to reverse 2nd half

        # reversing the 2nd half list
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        # merge the two halves
        first, second = head, prev

        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2