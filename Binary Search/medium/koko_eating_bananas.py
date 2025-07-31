# Question # 875 in Arrays
# Description: my implementation for the solution for the Koko Eating Bananas problem on leetcode
# Problem: Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.
#           Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has
#           less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.
#           Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
#           Return the minimum integer k such that she can eat all the bananas within h hours.
# Difficulty: medium
# Author: Elbert C.

import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        ans = r # for now we know the max # in our piles is a solution but not minimum

        while l <= r:
            k = (l + r) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)

            if hours <= h: # we need to search the left side for a better solution if there is one
                r = k - 1
                ans = min(ans, k)
            else: # need to search right side, answer was too small of a k value
                l = k + 1
        
        return ans
