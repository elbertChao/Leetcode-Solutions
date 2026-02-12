# Question # 494 in Arrays
# Description: my implementation for the solution for the Target Sum problem on leetcode
# Problem: You are given an integer array nums and an integer target.
#           You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.
#           For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
#           Return the number of different expressions that you can build, which evaluates to target.
# Difficulty: medium
# Author: Elbert C.

from collections import defaultdict
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        # Inefficient O(2^n) time
        # def dfs(i, curr_sum):
        #     if i == len(nums): # have to reach end of nums list
        #         return 1 if curr_sum == target else 0 # either we got our target or not, returning 1 or 0
            
        #     return =  (
        #         dfs(i+1, curr_sum + nums[i]) +
        #         dfs(i+1, curr_sum - nums[i])
        #         )

        # return dfs(0, 0)


        # # more efficient O(n*m) TC and SC with n being the length of nums and m being sum(all nums)
        # cache = {}

        # def dfs(i, curr_sum):
        #     # check if the current combination is in our cache
        #     if (i, curr_sum) in cache:
        #         return cache[(i, curr_sum)]

        #     if i == len(nums): # have to reach end of nums list
        #         return 1 if curr_sum == target else 0 # either we got our target or not, returning 1 or 0
            
        #     cache[(i, curr_sum)] =  (
        #         dfs(i+1, curr_sum + nums[i]) +
        #         dfs(i+1, curr_sum - nums[i])
        #         )
            
        #     return cache[(i, curr_sum)]

        # return dfs(0, 0)
    

        # More space efficient method
        grid = [defaultdict(int) for _ in range(len(nums)+1)]

        grid[0][0] = 1 # [0 elements used, 0 sum] = 1 way to get here *currently*

        for i in range(len(nums)):
            for curr_sum, count in grid[i].items():
                grid[i+1][curr_sum + nums[i]] += count
                grid[i+1][curr_sum - nums[i]] += count

        return grid[len(nums)][target]