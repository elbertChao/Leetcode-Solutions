# Question # 347 in Arrays
# Description: my implementation for the solution for the Top K Frequent Elements problem on leetcode
# Problem: Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
# Difficulty: medium
# Author: Elbert C.

from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
         
         # count the frequency for the numbers and put them into 'count'
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        # add the number to their respective frequency bucket
        for num, c in count.items():
            freq[c].append(num)
        
        # pop freq numbers from the end of the list since we are going for the most to least frequent
        ans = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans