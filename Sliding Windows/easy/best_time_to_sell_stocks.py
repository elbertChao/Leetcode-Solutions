# Description: My implementation for the solution for the Best Time to Sell Stocks problem on leetcode/neetcode
# Problem: You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.
#          You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.
#          Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.
# Difficulty: easy
# Author: Elbert C.

from typing import List

# OPTIMIZED SOLUTION
# This is a two-pointer technique or sliding window technique to find the maximum profit.
# The time complexity is O(n) and the space complexity is O(1). Since worst case we will
# have to traverse the entire array to find the maximum profit.
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         l, r, max_profit = 0, 1, 0

#         # iterate while the right pointer hasnt reached the end of the array
#         while r < len(prices):
#             if prices[l] < prices[r]: # check if we are at the right location for pointers for profit
#                 profit = prices[r] - prices[l]
#                 if profit > max_profit:
#                     max_profit = profit
#                 r += 1 # continue moving right to see if there is better time to sell
#             else: # wrong location, move both pointers to their new locations
#                 l = r
#                 r += 1

#         return max_profit

# 2 Pointers practice again:
# Use 2 pointers 'buy' & 'sell'
# only need to move sell to check for profits
# move both pointers if we aren't at a point of profit
# 1 pass through array so its O(n) TC and O(1) SC since its constant space

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell, max = 0, 1, 0

        while sell < len(prices):
            profit = prices[sell] - prices[buy]
            if profit > 0:
               if profit > max:
                   max = profit
               sell += 1
            else:
                buy = sell
                sell = buy + 1
        return max
    
# BRUTE FORCE SOLUTION
# This is a brute force solution to find the maximum profit.
# time complexity is O(n^2) and the space complexity is O(1). Since we will have to traverse the entire array

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         max_profit = 0
#         amount = 0
#         for i in range(0, len(prices)):
#             for j in range(i+1, len(prices)):
#                 amount = prices[j] - prices[i]
#                 if amount > max_profit:
#                     max_profit = amount

#         return max_profit

max_profit = Solution().maxProfit([2, 4, 1]) #[7, 1, 5, 3, 6, 4]
print(max_profit)

