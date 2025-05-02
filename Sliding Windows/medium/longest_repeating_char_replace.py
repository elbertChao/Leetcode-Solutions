# Description: My implementation for the solution for the Longest Repeating Character Replacement problem on leetcode/neetcode
# Problem: You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character.
#          You can perform this operation at most k times.
#          Return the length of the longest substring containing the same letter you can get after performing the above operations.
# Difficulty: medium
# Author: Elbert C.

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {} # hashmap to keep key-value pairs
        l, longest = 0, 0

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            
            # check validity of sliding window
            # meaning: window_len - max_freq <= k
            if (r - l + 1) - max(count.values()) > k: # this means it is NOT valid
                count[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)
        
        return longest