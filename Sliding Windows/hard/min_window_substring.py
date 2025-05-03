# Description: My implementation for the solution for the Minimum Window Substring problem on leetcode/neetcode
# Problem: Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every
#          character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".
#          The testcases will be generated such that the answer is unique.
# Difficulty: hard
# Author: Elbert C.

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == "" or t == "":
            return ""

        # initalizing our 2 count hashmaps
        t_count = {}
        window_count = {}
        l = 0
        ans = [-1, -1]
        ans_length = float('inf')

        # initialize our t_count map to use to check for substring validity
        for c in t:
            t_count[c] = t_count.get(c, 0) + 1
        
        # have and need variables are used for O(1) checks for validity
        have, need = 0, len(t_count)

        # now iterate through with a right pointer through string 's'
        for r in range(len(s)):
            char = s[r]
            window_count[char] = window_count.get(char, 0) + 1

            # check if the character that was just added is in t's counter map
            # and the count of the frequency required is the same
            if char in t_count and window_count[char] == t_count[char]:
                have += 1
            
            # while loop because the required chars could be at the end of the substring
            while have == need:
                # update our answer if a shorter substring was found
                if (r - l + 1) < ans_length:
                    ans = [l, r]
                    ans_length = (r - l + 1)
                
                # pop the char from the left of our window hashmap
                window_count[s[l]] -= 1

                # once a char was popped out that was a char we needed, leave while loop
                if s[l] in t_count and window_count[s[l]] < t_count[s[l]]:
                    have -= 1

                # keep moving left pointer to keep popping chars until a needed char is popped
                l += 1

        l_ans, r_ans = ans
        return s[l_ans:r_ans+1] if ans_length != float("inf") else ""