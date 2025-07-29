# Question # 539 in Arrays
# Description: my implementation for the solution for the Minimum Time Difference problem on leetcode
# Problem: Given a list of 24-hour clock time points in "HH:MM" format, return the minimum minutes difference between any two time-points in the list.
# Difficulty: medium
# Author: Elbert C.

from typing import List, Self

# O(nlogn) Solution
# class Solution:
#     def findMinDifference(self, timePoints: List[str]) -> int:
#         timePoints.sort() # O(nlogn) TC for sorting

#         def time_to_mins(time):
#             h, m = map(int, time.split(":")) # applies the int() function to each term after splitting it
#             return h*60 + m

#         # use the first iteration which is the time difference between the last time item and the first item
#         min_t = (24*60 - time_to_mins(timePoints[-1])) + (time_to_mins(timePoints[0]))

#         for i in range(len(timePoints) - 1): # only need to iterate until the total length - 1 since we already did the last and first term
#             m = time_to_mins(timePoints[i+1]) - time_to_mins(timePoints[i])
#             if m == 0:
#                 return 0
#             if m < min_t:
#                 min_t = m
            
#         return min_t
    

# O(n) time with BUCKET SORTING
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def time_to_mins(time):
            h, m = map(int, time.split(":")) # applies the int() function to each term after splitting it
            return h*60 + m
        
        buckets = [False] * (24*60) # 1440 buckets
        first_m, last_m = 24*60, 0

        for t in timePoints:
            mins = time_to_mins(t)
            if buckets[mins]:
                return 0
            buckets[mins] = True
            first_m = min(first_m, mins)
            last_m = max(last_m, mins)

        # use the first iteration which is the time difference between the last time item and the first item
        ans = (24*60 - last_m) + (first_m)

        prev_m = first_m
        for mins in range(first_m + 1, len(buckets)): # only need to iterate until the total length - 1 since we already did the last and first term
            if buckets[mins]:
                diff_mins = mins - prev_m
                ans = min(ans, diff_mins)
                prev_m = mins
            
            
        return ans
    
test = Solution().findMinDifference(['00:00', '23:59'])
print(test)