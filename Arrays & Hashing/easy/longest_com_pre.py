# Question # 14 in Arrays
# Description: my implementation for the solution for the Longest Common Prefix problem on leetcode
# Problem: Write a function to find the longest common prefix string amongst an array of strings.
#           If there is no common prefix, return an empty string "".
# Difficulty: easy
# Author: Elbert C.

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # # strs = ["flowers", "flow", "flight"]
        # # out = "fl"

        # # Look at each character in each word, appending letters to a string, until one is mismatched exit
        # out = ""

        # if not strs:
        #     return out

        # for i in range(len(strs[0])):
        #     for s in strs:
        #         if i == len(s) or s[i] != strs[0][i]:
        #             return out
        #     out += strs[0][i]

        # return out
    
        # another solution, using sorting: 
        # sort the list
        # just compare the first and last strings since those 2 should have the least common characters in common

        out = ""

        strs = sorted(strs)
        first_s = strs[0]
        last_s = strs[-1]

        for i in range(min(len(first_s), len(last_s))):
            if first_s[i] != last_s[i]:
                return out
            out += first_s[i]
        
        return out