# Question # 448 in Arrays
# Description: my implementation for the solution for the Find All Disappeared Numbers In Array problem on leetcode
# Problem: Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.
# Difficulty: easy
# Author: Elbert C.

# SLOWER SOLUTION: this is O(n) time because you are iterating through the length of sums which is n
class Solution1:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        numsSet = set(nums) # create a hashset of these nums instead
        returnSet = []

        for i in range(1, len(nums)+1): # iterate through 1, n as len(nums) needs a +1 to get to the n value
            if i not in numsSet: # the number was not found
                returnSet.append(i) # add it to the return set
        
        return returnSet