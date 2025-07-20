# Question # 56 in Arrays
# Description: my implementation for the solution for the Merge Intervals In Array problem on leetcode
# Problem: Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and
#           return an array of the non-overlapping intervals that cover all the intervals in the input.
# Difficulty: medium
# Author: Elbert C.


# Example 1:

# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

from traitlets import List

# class Solution:
#     def merge(self, intervals: List[List[int]]) -> List[List[int]]:
#         # Naive approach is taking all intervals and check if the starting number is less than or equal to the current value of the 
#         # ending number of the previous interval
#         # If yes, append that interval min/max value to answer, continue to complete merge
#         # Inefficient, TC: O(n^2) since we are checking each interval and require 

#         # --------- MORE EFFICIENT WAY (Sorting and storing could be entire array n) ----------
#         # TC: O(nlogn) since thats the TC for .sort() function and it dominates the O(n) linear search performed afterwards, SC: O(n)

#         # Sort the array first so that we have an ascending order to work with
#         # Initially we can use variable 'prev' as the first interval to compare with others
#         # Iterate and check if the first number in our next interval is LESS THAN or EQUAL to previous interval's max number
#         # If so only update prev's ending number, and continue
#         # Else append that new non-overlapped interval and continue iterating
#         # In the end append the prev interval meaning we are done.

#         intervals.sort()
#         answer = []
#         prev = intervals[0]

#         for i in range(1, len(intervals)):
#             if intervals[i][0] <= prev[1]:
#                 prev[1] = max(intervals[i][1], prev[1])
#             else:
#                 answer.append(prev)
#                 prev = intervals[i]
        
#         answer.append(prev)
#         return answer

# Initial approach is check every intervals last number with the intervals next number
# if the next one is lower then merge after you sort
# O(nlogn) TC because .sort() in python uses  

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = []
        prev = intervals[0] # start with the first interval

        for i in range(1, len(intervals)):
            if prev[1] > intervals[i][0]:
                prev[1] = max(prev[1], intervals[i][0])
            else:
                ans.append(prev)
                prev = intervals[i]
        
        ans.append(prev)

        return ans
    
test = Solution().merge([[2,6], [1,3],[8,10],[15,18]])
print(test)

