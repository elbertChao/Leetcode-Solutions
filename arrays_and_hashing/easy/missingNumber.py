# Question # 268 in Arrays
# Description: my implementation for the solution for the Missing Number problem on leetcode
# Problem: Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
# Difficulty: easy
# Author: Elbert C.

# SLOWER SOLUTION
class Solution1:
    def missingNumber(self, nums: List[int]) -> int:
        # This following solution works, but the time complexity is
        # O(nlogn) which is quite slow:

        nums.sort() # sort the array of numbers, using O(n) time

        for index, value in enumerate(nums):
            if(index != value): # this lists the array as an enumeration {[1, 1], [2, 2]}...
                                # where you get the index beside it's value, so every number should match if there is nothing missing
                return value-1

        return len(nums) # all numbers aren't missing except the last number which would have been the length of the array


# FASTER SOLUTION
class Solution2:
    def missingNumber(self, nums: List[int]) -> int:
        # This solution is a lot better and faster with a time complexiy of
        # O(n)
        return sum(range(len(nums)+1)) - sum(nums)