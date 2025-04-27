# Description: my implementation for the solution for the Product Except Self problem on leetcode
# Problem : Given an array of numbers return an array where each element is a product of all the
#           numbers except its self.
# Difficulty: medium
# Author: Elbert C.

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # for each number it will have every number BEFORE & AFTER multiplied
        # use prefix and suffix and multiply in-place to keep O(1) space complexity

        # initialize default array
        ansArr = [1] * len(nums)

        # first for loop to multiply each number with its prefix value in place
        prefix = 1
        for i in range(len(nums)):
            ansArr[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(len(nums)-1, -1, -1):
            ansArr[i] *= suffix
            suffix *= nums[i]

        return ansArr