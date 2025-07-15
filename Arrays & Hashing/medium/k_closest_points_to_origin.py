# Question # 973 in Arrays
# Description: my implementation for the solution for the K Closest Points to Origin problem on leetcode
# Problem: Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).
#           The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).
#           You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).
# Difficulty: medium
# Author: Elbert C.

import heapq
from traitlets import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Trivial solution would be to just find the k number of lowest euclidean values which
        # would just be the squares of xi and yi for each term and comparing
        # this would just be TC: O(nlogn) and SC: O(n) since you would need another array to store the new version
        # of the array

        # Better: use a min heap solution where you store the distance, x, and y values for each point in a heap
        # use heapq.heapify() to sort into min heap using logn time
        # heapq.heappop() the x, y terms into answer array k times, so TC = klogn
        min_heap = []
        for x, y in points:
            dist = x**2 + y**2
            min_heap.append([dist, x, y])
        
        heapq.heapify(min_heap)
        ans = []

        while k > 0:
            dist, x, y = heapq.heappop(min_heap)
            ans.append([x, y])
            k -= 1
        
        return ans
    
