# Description: Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
#               The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.
#               Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:
#               Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining
#               elements of nums are not important as well as the size of nums.
#               Return k.
# Problem: Remove Element
# Difficulty: easy
# Author: Elbert C.

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0

        # need to remove val from the array nums IN-PLACE
        # iterate through array nums using indices
        for i in range(len(nums)):
            # match if nums[i] is not val, then we know we should swap that number into the k's position
            if nums[i] != val:
                # use the number that isn't val to swap into k's position
                nums[k] = nums[i]
                # increment k only if we have performed swap
                # since we know the old k's position is filled correctly with a number that ISN'T val
                k += 1
        return k