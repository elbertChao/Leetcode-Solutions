# Description: my implementation for the solution for the Is Anagram problem on leetcode
# Difficulty: easy
# Author: Elbert C.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if the strings are of different length, automatically not an anagram
        if len(s) != len(t):
            return False

        # use a hashset, one for string S and one for string T
        # keeps track of the number of occurances of each letter
        countOfS = {}
        countOfT = {}

        for i in range(len(s)):
            # assign the current value of the occurance of the letter to increase by 1
            # or if it hasn't appeared in the set yet, set it to 0
            countOfS[s[i]] = 1 + countOfS.get(s[i], 0)
            countOfT[t[i]] = 1 + countOfT.get(t[i], 0)

        for j in countOfS:
            # if the count of occurances of a letter in S is not equal to T's string count
            if countOfS[j] != countOfT.get(j, 0): return False
        
        return True
            
