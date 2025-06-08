# Description: My implementation for the solution for the Reverse Linked List problem on leetcode/neetcode
# Problem: Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.
# Difficulty: easy
# Author: Elbert C.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# below is just so that the code can run in this environment, not required in leetcode
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# ********** ITERATIVE SOLUTION BELOW **********
# Time Complexity: O(n) where n is the number of nodes in the linked list
# Space Complexity: O(1) since we are not using any extra space
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # initialize prev & curr to None/null and head to begin
        prev, curr = None, head

        while curr: # continue iteration until the end null value is reached
            temp = curr.next # temporary variable to keep what the current pointer is
            curr.next = prev # curr's pointer is now pointing to prev
            prev = curr
            curr = temp
        return prev # by the end curr will point to None and prev will be the head

# ********** RECURSIVE SOLUTION BELOW **********
# Time Complexity: O(n) where n is the number of nodes in the linked list
# Space Complexity: O(n) due to the recursive stack space used
class Solution2:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # check base case first to see if the head is None
        if not head:
            return None

        new_head = head # new_head is set to our current node
        if head.next: # if there exists subsequent nodes/children continue
            new_head = self.reverseList(head.next) # recursive call to reverse the rest of the list
        # after the recursive call, we set the next node's next to point to the current head
            head.next.next = head
        head.next = None # set the current head's next to None to avoid cycles

        return new_head # return the new head of the reversed list
    
# Example usage:
# head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
# solution = Solution()
# reversed_head = solution.reverseList(head)
# while reversed_head:
#     print(reversed_head.val, end=" -> ")
#     reversed_head = reversed_head.next
# Output: 5 -> 4 -> 3 -> 2 -> 1 ->