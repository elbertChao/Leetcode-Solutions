# Description: My implementation for the solution for the Search in Rotated Sorted Array problem on leetcode/neetcode
# Problem: Given the sorted rotated array nums of unique elements, return the index of the target number in nums.
#           If the target is not in nums, return -1.
# Difficulty: medium
# Author: Elbert C.

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m

            # check if 'm' is in the left sorted portion
            if nums[l] <= nums[m]:
                # check right if target is either larger than 'm'
                # or less than our most left number, meaning it is rotated to now be on the right
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else: # check left instead
                    r = m - 1
            # m is in the right sorted array
            else:
                # check left if target is less than our m value
                # or greater than our most right value, meaning rotation occured and its now on left
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
        return -1