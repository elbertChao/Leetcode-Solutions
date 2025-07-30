# Question # 295 in Arrays (graph question)
# Description: my implementation for the solution for the Find Median from Data Stream problem on leetcode
# Problem: The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.
#           For example, for arr = [2,3,4], the median is 3.
#           For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
#           Implement the MedianFinder class:
#           MedianFinder() initializes the MedianFinder object.
#           void addNum(int num) adds the integer num from the data stream to the data structure.
#           double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
# Difficulty: hard
# Author: Elbert C.

import heapq


class MedianFinder:

    def __init__(self):
        # sm = max heap, lg = min heap
        self.sm, self.lg = [], []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.sm, num * -1) # * -1 since default it is min heap

        # checks for if all elements in sm <= lg
        if (self.sm and self.lg and
            (self.sm[0] * -1 > self.lg[0])): # need to move num in sm heap to the lg heap
            val = heapq.heappop(self.sm) * -1
            heapq.heappush(self.lg, val)
        
        # checks for if the 2 heaps are uneven sizes
        if len(self.sm) > len(self.lg) + 1:
            val = heapq.heappop(self.sm) * -1
            heapq.heappush(self.lg, val)
        if len(self.lg) > len(self.sm) + 1:
            val = heapq.heappop(self.lg)
            heapq.heappush(self.sm, val * -1)

    def findMedian(self) -> float:
        if len(self.sm) > len(self.lg):
            return self.sm[0] * -1
        if len(self.sm) < len(self.lg):
            return self.lg[0]
        
        return (self.sm[0] * -1 + self.lg[0]) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()