# Description: My implementation for the solution for the Longest Substring Without Repeating Characters problem on leetcode/neetcode
# Problem: Given a string s, find the length of the longest substring without duplicate characters.
#          A substring is a contiguous sequence of characters within a string.
# Difficulty: medium
# Author: Elbert C.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set() # using set since there can't be duplicates
        l = 0
        longest = 0

        for r in range(len(s)):
            while s[r] in char_set: # letter is already in the set
                # remove that letter that is at the front of our array
                # to move our sliding window
                char_set.remove(s[l])
                l += 1
            char_set.add(s[r])
            longest = max(longest, len(char_set)) # compare and update our answer for longest substring
        
        return longest