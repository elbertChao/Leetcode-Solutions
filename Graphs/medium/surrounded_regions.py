# Question # 130 in Arrays (graph question)
# Description: my implementation for the solution for the Surrounded Regions problem on leetcode
# Problem: You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:
#           Connect: A cell is connected to adjacent cells horizontally or vertically.
#           Region: To form a region connect every 'O' cell.
#           Surround: The region is surrounded with 'X' cells if you can connect the region with 'X' cells and none of the region cells are on the edge of the board.
#           To capture a surrounded region, replace all 'O's with 'X's in-place within the original board. You do not need to return anything.
# Difficulty: medium
# Author: Elbert C.

from typing import List


# This is TC = O(m*n) and SC = O(m*n)
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        ROWS, COLS = len(board), len(board[0])

        # 3 steps to perform:
        # 1) capture unsurrounded regions (edge regions) and change O -> T (temp)
        # 2) capture surrounded regions, O -> X
        # 3) uncapture unsurrounded, T -> O

        # DFS function
        def capture(r, c):
            # make sure we are in bounds and not looking at an 'O' aka IGNORE ALL X or T
            if r < 0 or c < 0 or r == ROWS or c == COLS or board[r][c] != 'O':
                return
            
            board[r][c] = 'T'
            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)

        # Step 1:
        for r in range(ROWS):
            for c in range(COLS):
                # find all edge 'O's
                if board[r][c] == 'O' and (r in [0, ROWS-1] or c in [0, COLS-1]):
                    capture(r, c)

        # Step 2:
        for r in range(ROWS):
            for c in range(COLS):
                # find all edge 'O's
                if board[r][c] == 'O':
                    board[r][c] = 'X'
        
        # Step 3:
        for r in range(ROWS):
            for c in range(COLS):
                # find all edge 'O's
                if board[r][c] == 'T':
                    board[r][c] = 'O'