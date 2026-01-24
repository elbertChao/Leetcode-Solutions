# Question # 1929 in Arrays
# Description: Given an integer array nums of length n, you want to
#               create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).
#               Specifically, ans is the concatenation of two nums arrays.
#               Return the array ans.
# Problem: Concatenation of Array
# Difficulty: easy
# Author: Elbert C.

from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # this is O(n) TC because the outer loot runs for a constant number of times,
        # while the inner runs for the length of n where n is the length of the nums list
        # SC = O(n) since we need to create another ans array
        # ans = []
        
        # for i in range(0,2):
        #     for j in nums:
        #         ans.append(j)
        
        # return ans

        # To get better SC = O(1) we can append the values in nums in place
        length = len(nums)
        i = 0
        while i < length:
            nums.append(nums[i])
            i += 1
        return nums
    
print (Solution().getConcatenation([1,2,3]))