# Description: my implementation for the solution for the Is Anagram problem on leetcode
# Problem: Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
#          An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
# Difficulty: easy
# Author: Elbert C.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # make 2 hash tables, one for 's' and 't'
        countS = {}
        countT = {}

        if len(s) != len(t): return False # count of each letter cannot be equal

        # check if the # of occurances of each letter are the same in both sets
        for x in range(len(s)):
            countS[s[x]] = 1 + countS.get(s[x], 0)
            countT[t[x]] = 1 + countT.get(t[x], 0)

        # return if they're the same meaning they have the same keys with same values
        return countS == countT
            
