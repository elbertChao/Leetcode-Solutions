# Question # 1266 in Arrays
# Description: my implementation for the solution for the Minimum Time Visiting All Points problem on leetcode
# Problem: On a 2D plane, there are n points with integer coordinates points[i] = [xi, yi]. Return the minimum 
#          time in seconds to visit all the points in the order given by points.
        # You can move according to these rules:
        # In 1 second, you can either:
        # move vertically by one unit,
        # move horizontally by one unit, or
        # move diagonally sqrt(2) units (in other words, move one unit vertically then one unit horizontally in 1 second).
        # You have to visit the points in the same order as they appear in the array.
        # You are allowed to pass through points that appear later in the order, but these do not count as visits.

# Difficulty: easy
# Author: Elbert C.

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        totalTime = 0
        
        # this will get x1 being the first x value in the set of coordinates
        # and y1 is the first y value in the set of coords
        # if we have [[1,1][3,4],[-1,0]]
        # x1 = 1, y1 = 1
        x1, y1 = points.pop()
        while points: # keep iterating while we still have coordinates in the points list
            x2, y2 = points.pop() # x2 = 3, y2 = 4
            totalTime += max(abs(y2-y1), abs(x2-x1))
            x1, y1 = x2, y2 # change initial coords to be the x2, y2 coords so we can move on to the next set of coords
        
        return totalTime
