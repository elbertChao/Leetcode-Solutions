# Description: my implementation for the solution for the Valid Palindrome problem on leetcode
# Problem: A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters,
#          it reads the same forward and backward. Alphanumeric characters include letters and numbers.
#          Given a string s, return true if it is a palindrome, or false otherwise.
# Difficulty: easy
# Author: Elbert C.

import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # ideas:
        # one loop going from left to right and the other going right to left
        # both interating with length of half the total string length

        # strip string of all capitalization, spaces, and punctuation
        new_s = re.sub("[^a-zA-Z0-9]", "", s)
        formatted_s = new_s.lower()

        # initialize 2 pointers, left and right
        # one starts at the beginning, other one starts at the end of the string
        leftCount = 0
        rightCount = len(formatted_s)-1

        # continue interating until you've reached the middle point of the string
        # for palindromes
        while leftCount < rightCount:
            # letters dont match so instantly isn't a palindrome so exit and return False
            if formatted_s[leftCount] != formatted_s[rightCount]:
                return False
            # increment/decrement pointers
            leftCount += 1
            rightCount -= 1
        
        return True