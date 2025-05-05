# Description: My implementation for the solution for the Valid Parentheses problem on leetcode/neetcode
# Problem: Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#           An input string is valid if:
#           Open brackets must be closed by the same type of brackets.
#           Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
# Difficulty: easy
# Author: Elbert C.

class Solution:
    def isValid(self, s: str) -> bool:
        MAP = {')':'(', ']':'[', '}':'{'}
        stack = []

        # handle the edge case of if there is only 1 character or empty strings
        # cannot be valid
        if len(s) < 2: return False

        # iterate through all characters in s
        for char in s:
            if char in MAP.values(): # if the character is an OPENING bracket type
                stack.append(char)
            # get the value of the character from our map which is an OPENING bracket to compare
            # with the value that we pop from our stack as it should be equivalent if the type
            # of opening bracket is the same, else it is false so return false
            elif len(stack) == 0 or MAP.get(char) != stack.pop():
                return False
        
        if len(stack) == 0:
            return True
        else:
            return False