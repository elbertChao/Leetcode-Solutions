# Description: my implementation for the solution for the Contains Duplicate problem on leetcode
# Difficulty: easy
# Author: Elbert C.

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         hashset = set()

         for i in nums:
            # initially check if the current number being checked is already in the hashset
            if i in hashset: return True # if so, return true
            # add the number to the hashset
            hashset.add(i)
        # no numbers were found as duplicates since we added all numbers and never found it already in the hashset
         return False