# Question # 42 in Arrays (graph question)
# Description: my implementation for the solution for the Trapping Rain Water problem on leetcode
# Problem: Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
# Difficulty: hard
# Author: Elbert C.

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        # O(N) TC and O(1) SC since we are only taking constant spacing, no extra arrays

        # edge case for empty height lists
        if not height:
            return 0

        # create our pointers, l and r along with their max_l and max_r used to decide when to move pointers
        l, r = 0, len(height) - 1
        max_l, max_r = height[l], height[r]
        total_water = 0

        while l < r:
            if max_l <= max_r:
                l += 1
                max_l = max(max_l, height[l])
                total_water += max_l - height[l]
            else:
                r -= 1
                max_r = max(max_r, height[r])
                total_water += max_r - height[r]

        return total_water