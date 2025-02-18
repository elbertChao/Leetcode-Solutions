# Question # 1 in Arrays
# Description: my implementation for the solution for the Two Sum problem on leetcode
# Problem: Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#          You may assume that each input would have exactly one solution, and you may not use the same element twice.
#          You can return the answer in any order.
# Difficulty: easy
# Author: Elbert C.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapCheck = {}

        # use value:index pairs
        for i, num in enumerate(nums):
            answer = target - num # answer number we are searching for
            # 2 cases depending on if the ordering of the numbers in the given nums list is
            # in ascending or descending or random order
            if answer in mapCheck and mapCheck[answer] > i:
                return [i, mapCheck[answer]]
            if answer in mapCheck and mapCheck[answer] < i:
                return [mapCheck[answer], i]
            mapCheck[num] = i
