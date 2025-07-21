# Question # 2661 in Arrays
# Description: my implementation for the solution for the First Completely Painted Row or Column problem on leetcode
# Problem: You are given a 0-indexed integer array arr, and an m x n integer matrix mat. arr and mat both contain all the integers in the range [1, m * n].
#           Go through each index i in arr starting from index 0 and paint the cell in mat containing the integer arr[i].
#           Return the smallest index i at which either a row or a column will be completely painted in mat.
# Difficulty: medium
# Author: Elbert C.

from typing import List


class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        ROWS, COLS = len(mat), len(mat[0])

        # fill our hashmap that maps the number -> position
        num_to_position = {}
        for r in range(ROWS):
            for c in range(COLS):
                num_to_position[mat[r][c]] = (r, c)
        
        # use a row count and col count to determine if any rows/cols are fully painted
        row_count = [0] * ROWS
        col_count = [0] * COLS

        # now begin painting and marking our counts to find complete painted rows/cols
        for i in range(len(arr)):
            r, c = num_to_position[arr[i]]
            row_count[r] += 1
            col_count[c] += 1

            # check if any of the rows/cols are completed
            if col_count[c] == ROWS or row_count[r] == COLS:
                return i