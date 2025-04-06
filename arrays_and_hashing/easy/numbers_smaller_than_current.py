# Question # 1365 in Arrays
# Description: my implementation for the solution for the How Many Numbers Are Smaller Than the Current Number problem on leetcode
# Problem: Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for
#          each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].
#          Return the answer in an array.
# Difficulty: easy
# Author: Elbert C.

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # SLOW O(n^2) solution
        # ansArr = []
        # ansCount = 0

        # for i in range(0, len(nums)):
        #     for j in range(0, len(nums)):
        #         if nums[j] < nums[i]:
        #             ansCount += 1
        #     ansArr.append(ansCount)
        #     ansCount = 0

        # return ansArr

        # FASTER O(nlogn) solution:
        temp = sorted((nums)) # sorts array, using the ascending order
        myDict = {}
        ansArr = []

        for i, value in enumerate(temp):
            if value not in myDict: # for example we have [8,1,2,2,3] as our nums list
                                    # the 2nd two would not be added so once 3 gets added
                                    # the index i is 3 meaning that there are 3 numbers less than 3
                myDict[value] = i # [1:0, 2:1, 3:3, 8:4] is our myDict
        
        # now go through every number in nums list and just append it's index number which is the number of
        # how many numbers are smaller than the current number i
        for i in nums:
            ansArr.append(myDict[i])
        
        return ansArr