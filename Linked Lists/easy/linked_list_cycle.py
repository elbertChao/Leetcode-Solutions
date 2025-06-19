# Description: My implementation for the solution for the Linked List Cycle problem on leetcode/neetcode
# Problem: Given head, the head of a linked list, determine if the linked list has a cycle in it.
#       There is a cycle in a linked list if there is some node in the list that can be reached again by
#       continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's
#       next pointer is connected to. Note that pos is not passed as a parameter.
#       Return true if there is a cycle in the linked list. Otherwise, return false.
# Difficulty: easy
# Author: Elbert C.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# Hashset solution
# time complexity: O(n) where n is the number of nodes in the linked list
# space complexity: O(n) due to the hashset used to store visited nodes
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        curr = head
        while curr:
            if curr in seen:
                return True
            else:
                seen.add(curr)
                curr = curr.next
        return False
    
# Fast & slow pointer solution
# time complexity: O(n) where n is the number of nodes in the linked list
# linear time complexity since we traverse with length of list + (1-2) for the cycle
# and the worst case is that we traverse the entire list once
# space complexity: O(1) since we are not using any extra space
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
                
        return False