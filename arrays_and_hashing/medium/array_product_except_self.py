# Description: my implementation for the solution for the Producs of Array Except Self problem on neetcode
# Problem : Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].
# Difficulty: medium
# Author: Elbert C.

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Create a result array to store the products of all elements except self
        result = [1] * len(nums)

        # Calculate the prefix product for each element
        prefix_product = 1
        for i in range(len(nums)):
            result[i] = prefix_product
            prefix_product *= nums[i]

        # Calculate the suffix product and multiply it with the prefix product
        suffix_product = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= suffix_product
            suffix_product *= nums[i]

        return result