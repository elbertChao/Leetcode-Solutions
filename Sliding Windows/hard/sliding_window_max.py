# Question # 239 in Sliding Window
# Description: my implementation for the solution for the Koko Eating Bananas problem on leetcode
# Problem: You are given an array of integers nums, there is a sliding window of size k which is
#           moving from the very left of the array to the very right. You can only see the k numbers
#           in the window. Each time the sliding window moves right by one position.
#           Return the max sliding window.
# Difficulty: hard
# Author: Elbert C.

import collections
from typing import List

# O(n) TC and SC because it is performing the pops and appending of our queue each number is added only once and removed once
# SC is same for the worse case scenario our k might just be 1

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        l = r = 0
        queue = collections.deque()
        
        while r < len(nums):
            # pop all values that are smaller than the one we are currently looking at
            while queue and nums[queue[-1]] < nums[r]:
                queue.pop()
            queue.append(r)

            # remove left value if its out of bounds
            if l > queue[0]:
                queue.popleft()
            
            # make sure window size is of size k
            if (r+1) >= k:
                ans.append(nums[queue[0]])
                l += 1
            
            r += 1

        return ans