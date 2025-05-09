# Description: My implementation for the solution for the Find Min of Sorted Array problem on leetcode/neetcode
# Problem: Given the sorted rotated array nums of unique elements, return the minimum element
# Difficulty: medium
# Author: Elbert C.

class Solution:
    def findMin(self, nums: List[int]) -> int:
        ans = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            # array is sorted in proper order so left most is already min
            if nums[l] < nums[r]:
                ans = min(ans, nums[l])
                break
            # not sorted in proper order, perform binary search
            m = (l + r) // 2
            ans = min(ans, nums[m])

            if nums[m] >= nums[l]: # the middle number is greater than left numbers, so need to look right now
                # search right
                l = m + 1
            else:
                # search left
                r = m - 1
        return ans