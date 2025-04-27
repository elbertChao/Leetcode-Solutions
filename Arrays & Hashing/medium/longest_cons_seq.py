# Description: my implementation for the solution for the Longest Consecutive Sequence problem on leetcode
# Problem : Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.
#           A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element.
#           The elements do not have to be consecutive in the original array.
# Difficulty: medium
# Author: Elbert C.

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        checker_set = set(nums)
        longest = 0

        # iterate through array and check if the number has a left neighbour aka the start of a seq
        for num in checker_set:
            # this means no number left of this one is found
            # this is a start of a seq, smallest in a seq
            if num - 1 not in checker_set:
                curr_seq_num = num
                curr_streak = 1

                # keep iterating while there exists a number 1 greater than curr_seq_num
                while curr_seq_num + 1 in checker_set:
                    curr_seq_num += 1
                    curr_streak += 1
        
                #update what the longest streak found is 
                longest = max(longest, curr_streak)

        return longest