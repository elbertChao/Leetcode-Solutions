# Description: My implementation for the solution for the Best Time to Sell Stocks problem on leetcode/neetcode
# Problem: You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.
#          You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.
#          Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.
# Difficulty: easy
# Author: Elbert C.

class Solution:
    class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r, max_profit = 0, 1, 0

        # iterate while the right pointer hasnt reached the end of the array
        while r < len(prices):
            if prices[l] < prices[r]: # check if we are at the right location for pointers for profit
                profit = prices[r] - prices[l]
                if profit > max_profit:
                    max_profit = profit
                else:
                    r += 1 # continue moving right to see if there is better time to sell
            else: # wrong location, move both pointers to their new locations
                l = r
                r += 1

        return max_profit