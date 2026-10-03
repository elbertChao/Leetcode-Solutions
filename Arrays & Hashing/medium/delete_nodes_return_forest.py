# Question # 1110 in Arrays
# Description: my implementation for the solution for the Delete nodes and return forest problem on leetcode
# Problem: Given the root of a binary tree, each node in the tree has a distinct value.
#           After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).
#           Return the roots of the trees in the remaining forest. You may return the result in any order.
# Difficulty: medium
# Author: Elbert C.

from typing import List, Optional

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        return