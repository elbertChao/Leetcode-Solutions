# Description: my implementation for the solution for the Missing Number problem on leetcode
# Problem: Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
# Difficulty: easy
# Author: Elbert C.

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # This following solution works, but the time complexity is
        # O(nlogn) which is quite slow:

        # nums.sort()

        # for index, value in enumerate(nums):
        #     if(index != value):
        #         return value-1

        # return len(nums)

        # This solution is a lot better and faster with a time complexiy of
        # O(n)
        return sum(range(len(nums)+1)) - sum(nums)