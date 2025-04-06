# Description: my implementation for the solution for the Anagram Groups problem on leetcode
# Problem : Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.
#           An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
# Difficulty: medium
# Author: Elbert C.

from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped_anagrams = {}
        
        for s in strs:
            # sort the string to get a canonical form of the anagram
            # sorted returns a list like ['a', 'e', 't'] for the word eat
            # joining converts the list to a string
            sorted_s = ''.join(sorted(s))
            
            # create key if it doesn't exist
            if sorted_s not in grouped_anagrams:
                grouped_anagrams[sorted_s] = []

            # now we can add it to our set
            grouped_anagrams[sorted_s].append(s) # using the string in canonical form as the key
        
        # return answer
        return list(grouped_anagrams.values())
