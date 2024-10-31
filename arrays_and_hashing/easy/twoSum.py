# Question # 1 in Arrays
# Description: my implementation for the solution for the Two Sum problem on leetcode
# Problem: Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#          You may assume that each input would have exactly one solution, and you may not use the same element twice.
#          You can return the answer in any order.
# Difficulty: easy
# Author: Elbert C.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create hashset that will hold the integers to check if the value
        # with the current number you're checking equals your sum
        hashset = set()

        # interate through the list of integers to check if it sums to the
        # target of previously read values in the hashset
        for i in range(0, len(nums)):
            difference = target - nums[i]

            # check if the other number (difference) that makes the sum to target
            # exists in the hashset, if it does then we found our two
            # integer sum value
            if difference in hashset:
                index = nums.index(difference)
                return [index, i]
            hashset.add(nums[i])
