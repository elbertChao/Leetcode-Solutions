# Question # 56 in Arrays
# Description: my implementation for the solution for the Spiral Matrix problem on leetcode
# Problem: Given an m x n matrix, return all elements of the matrix in spiral order.
# Difficulty: medium
# Author: Elbert C.

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []

        def finishCheck():
            if len(matrix) == 0:
                return True

        while matrix:
            # add all elements of the first row, this is always the case
            ans.extend(matrix[0])
            matrix.pop(0) # remove the first row
            matrix = [item for item in matrix if len(item)>0]
            
            if finishCheck(): return ans

            for col in matrix:
                ans.append(col[-1]) # all last elements of each array in order
                col.pop(-1)
            matrix = [item for item in matrix if len(item)>0]

            if finishCheck(): return ans

            ans.extend(matrix[-1][::-1]) # add the reverse of the last row
            matrix.pop(-1)
            matrix = [item for item in matrix if len(item)>0]

            if finishCheck(): return ans

            for col in reversed(matrix): # add first elements of all rows in reverse
                ans.append(col[0])
                col.pop(0)
            matrix = [item for item in matrix if len(item)>0]

            if finishCheck(): return ans
