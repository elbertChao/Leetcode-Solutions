# Question # 735 in Arrays
# Description: my implementation for the solution for the Asteroid Collision problem on leetcode
# Problem: We are given an array asteroids of integers representing asteroids in a row. The indices of the asteriod in the array represent their relative position in space.
#           For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid
#           moves at the same speed. Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode.
#           If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.
# Difficulty: easy
# Author: Elbert C.

from traitlets import List

# TC: O(n) iterating linearly through asteroids, SC: O(n) no collisions and we have to add everything to stack

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for a in asteroids:
            # only do collision if stack is not empty, negative asteroid inc,
            # and current asteroid in stack is positive
            while stack and a < 0 and stack[-1] > 0:
                difference = stack[-1] + a
                if difference < 0:
                    stack.pop() # incoming asteroid wins, remove old asteroid
                elif difference > 0:
                    a = 0 # incoming asteroid is destroyed
                else: # remove both asteroids
                    a = 0
                    stack.pop() 
            if a:
                stack.append(a)
        
        return stack
    

test = Solution().asteroidCollision([2,4,-4,-1])
print(test)