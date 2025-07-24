# Question # 539 in Arrays
# Description: my implementation for the solution for the Minimum Time Difference problem on leetcode
# Problem: Given a list of 24-hour clock time points in "HH:MM" format, return the minimum minutes difference between any two time-points in the list.
# Difficulty: medium
# Author: Elbert C.

from typing import List


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort() # O(nlogn) TC for sorting

        def time_to_mins(time):
            h, m = map(int, time.split(":")) # applies the int() function to each term after splitting it
            return h*60 + m

        # use the first iteration which is the time difference between the last time item and the first item
        min_t = (24*60 - time_to_mins(timePoints[-1])) + (time_to_mins(timePoints[0]))

        for i in range(len(timePoints) - 1): # only need to iterate until the total length - 1 since we already did the last and first term
            t = time_to_mins(timePoints[i+1]) - time_to_mins(timePoints[i])
            if t < min_t:
                min_t = t
            
        return min_t