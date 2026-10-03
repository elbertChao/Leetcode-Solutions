# Question # 322 in Arrays
# Description: my implementation for the solution for the Coin Change problem on leetcode
# Problem: You are given an integer array coins representing coins of different denominations and an integer
#       amount representing a total amount of money.
#       Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made
#       up by any combination of the coins, return -1.
#       You may assume that you have an infinite number of each kind of coin.
# Difficulty: medium
# Author: Elbert C.

from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Inefficient solution:
        #   TC = O(n^t) where n is length of coins and t is the amount, you need to always go down your decision tree and branching out all possible coins
        #   SC = O(t) since worst case is you do all 1 dollar coins and you run recursion t times
        # # use a recursive function
        # def dfs(amount):
        #     if amount == 0: # automatically know no coins if amount is 0
        #         return 0
            
        #     ans = 10e5 # number of coins won't exceed the constraint of the max amount value

        #     for coin in coins: # iterate through coins
        #         if amount - coin >= 0: # still need more coins, amount not 0 yet
        #             ans = min(ans, (1 + dfs(amount - coin))) # coin count is min of previous count or the recursive call
        #     return ans


        # min_coins = dfs(amount)
        # return -1 if min_coins >= 10e5 else min_coins # return -1 meaning not possible if we are larger or still at 10e5 amount

        # Better solution with memoization using a cache/DP:
        #   TC = O(n*t)
        #   SC = O(t)

        cache = [amount + 1] * (amount + 1)
        cache[0] = 0 # in order to get to 0 amount, it takes 0 coins

        # find all the different amount coin combos 1 up to amount
        for a in range(1, amount+1):
            for c in coins:
                if a - c >= 0:
                    cache[a] = min(cache[a], 1 + cache[a - c])
        
        print(cache)
        return -1 if cache[amount] > amount else cache[amount]
    
print(Solution().coinChange([2], 3))