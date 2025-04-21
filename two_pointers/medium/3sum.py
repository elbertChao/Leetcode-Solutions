# Description: my implementation for the solution for the 3Sum problem on leetcode
# Problem: Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.
#          The output should not contain any duplicate triplets. You may return the output and the triplets in any order.
# Difficulty: medium
# Author: Elbert C.

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []

        # sort array so that the numbers are like a number line
        nums.sort()

        for i, val in enumerate(nums):
            # keep checking that we are at the beginning of our tuple starting number for the sum
            # else keep going if we have duplicate numbers
            if i > 0  and val == nums[i-1]:
                continue

            # found starting number, go on with left and right pointers
            l, r = i+1, len(nums)-1
            while l < r:
                three_sum = val + nums[l] + nums[r]
                if three_sum > 0: # means that we need a number on the right of the numberline to decrease
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    ans.append([val, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r: # keep going if more duplicate numbers exist
                        l += 1

        return ans