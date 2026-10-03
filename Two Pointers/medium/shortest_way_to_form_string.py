# Question # 1055 in Arrays
# Description: my implementation for the solution for the Shortest way to form string problem on leetcode
# Problem: Given two strings, source and target, return the minimum number of subsequences
#       of source that need to be concatenated to form target. If it is impossible to form target
#       (because target contains a character not found in source), return -1.
# Difficulty: medium
# Author: Elbert C.



class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        # initialize our target index variable & ans
        ans = 0
        target_i = 0

        # keep checking through target and match the most # of characters from source to it
        while target_i < len(target):
            prev_i = target_i

            for char in source:
                if target_i < len(target) and char == target[target_i]:
                    target_i += 1
            
            if target_i == prev_i:
                return -1

            ans += 1
        
        return ans

print(Solution().shortestWay("abc", "abcbdc"))