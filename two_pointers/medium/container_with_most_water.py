# Description: my implementation for the solution for the Container with Most Water problem on leetcode
# Problem: You are given an integer array heights where heights[i] represents the height of the i^th bar.
#          You may choose any two bars to form a container. Return the maximum amount of water a container can store.
# Difficulty: medium
# Author: Elbert C.

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max = 0
        l = 0
        r = len(heights) - 1

        if r == -1: return 0 # empty array edge case, so exit with 0

        while l < r:
            # (r-1) is our width and min(two bars) is our length
            area = (r-l) * min(heights[l], heights[r])

            # update our max container value
            if area >= max:
                max = area
            
            # only move the pointer that is of less value or equal value
            # this is because we want to maximize the length we use when calculating area
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        
        return max