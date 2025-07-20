# Question # 200 in Arrays
# Description: my implementation for the solution for the Number of Islands problem on leetcode
# Problem: Given an m x n 2D binary grid 'grid' which represents a map of '1's (land) and '0's (water), return the number of islands.
# Difficulty: medium
# Author: Elbert C.

# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         # we know automatically its not valid islands if grid doesn't exist
#         # like grid = []
#         if not grid:
#             return 0

#         numIslands = 0
#         numRows = len(grid)
#         numCols = len(grid[0])
#         eleVisited = set() # no duplicates, so using set is useful
        
#         def iterate_bfs(row, col):
#             search_queue = deque()
#             eleVisited.add((row, col))
#             search_queue.append((row, col))

#             while search_queue:
#                 r, c = search_queue.popleft() # so first iteration r=0 and col=0
#                 # bfs so search up down left right
#                 directions = [[1,0], [-1, 0], [0, -1], [0, 1]]

#                 for dir_r, dir_c in directions:
#                     row, col = r+dir_r, c+dir_c

#                     if (row in range(numRows) and col in range(numCols) and grid[row][col] == '1' and (row, col) not in eleVisited):
#                         search_queue.append((row, col))
#                         eleVisited.add((row, col))

#         for row in range(numRows):
#             for col in range(numCols):
#                 # if the current element is a 1 and the row, col pair isn't already visited, proceed
#                 if grid[row][col] == '1' and (row, col) not in eleVisited:
#                     # perform the interate_bfs function
#                     # checking adjacent elements for the end of the island
#                     iterate_bfs(row, col)
#                     numIslands += 1
        
#         return numIslands
    




import collections
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # initially we see that islands are 1's that have adjacent 1's beside them
        # so we know we can check in all the adjacent directions (N, E, S, W)
        # this is like a breadth first search, where we keep searching in the 4
        # directions until we reach the end, aka 0 meaning it is water
        # then add a number to our number of islands variable

        # keep track of # of islands, # of rows/cols, and the elements we already visited
        numIslands = 0
        rows, cols = len(grid), len(grid[0])
        visited = set() # using a hashset because there will not be any duplications here
        
        # edge case wherer we will have no grid, meaning no islands automatically
        if not grid:
            return 0
        
        # use a bfs algorithm since checking adjacency in the 4 directions is practically the same as what bfs does
        def bfs(r, c): # bfs is iterative so use a queue
            queue = collections.deque()
            # add and keep track that we visited the row and col as well as keeping track in our queue
            visited.add((r, c))
            queue.append((r, c))

            while queue: # while the queue isnt empty keep searching in adjacent directions
                # pop from our queue
                row, col = queue.popleft()
                directions = [[0,1],[0,-1],[1,0],[-1,0]] # NSEW
                for dr, dc in directions: # Check if we are in bounds of our grid still, it is STILL land, and not ALREADY visited
                    r, c = row + dr, col + dc
                    if (r in range(rows) and
                        c in range(cols) and
                        grid[r][c] == '1' and 
                        (r, c) not in visited):
                        queue.append((r, c))
                        visited.add(r, c)

        
        # now we can begin to iterate through the grid
        for r in range(rows):
            for c in range (cols):
                if grid[r][c] == '1' and (r, c) not in visited: # only do something if we encounter a 1, encountering 0 has no purpose
                    bfs(r, c)
                    numIslands += 1
        
        return numIslands