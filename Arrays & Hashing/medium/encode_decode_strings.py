# Description: my implementation for the solution for the Encode & Decode Strings problem on leetcode
# Problem : Design an algorithm to encode a list of strings to a single string. The encoded 
#           string is then decoded back to the original list of strings.
# Difficulty: medium
# Author: Elbert C.

class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedStr = ""

        for element in strs:
            # get form of 4:neet4:code
            encodedStr += str(len(element)) + ':' + element

        return encodedStr
    def decode(self, s: str) -> List[str]:
        # take first number as the length, after ':' is where we start

        decodedStr = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != ':': # we know we are at the length number
                j += 1
            strLen = int(s[i:j])
            decodedStr.append(s[j+1 : j+1+strLen])
            i = j+1+strLen

        return decodedStr