# Description: My implementation for the solution for the Remove Nth Node from Linked List problem on leetcode/neetcode
# Problem: You are given the beginning of a linked list head, and an integer n.
#          Remove the nth node from the end of the list and return the beginning of the list.
# Difficulty: medium
# Author: Elbert C.

# This is a two-pointer technique to find the nth node from the end of the linked list.
# The time complexity is O(n) and the space complexity is O(1). Since worst case we will
# have to traverse the entire linked list to find the nth node from the end.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        # shift right pointer 'n' times
        while n > 0 and right:
            right = right.next
            n -= 1

        # now we can have left and right pointers shift right by 1 until 'right' pointer is at end
        while right:
            left = left.next
            right = right.next
        
        # now we know that the 'left' pointer is at the node just before the one we want to remove
        # remove it by making it's next node skip 1 aka .next.next
        left.next = left.next.next

        return dummy.next