# Question # 200 in Arrays
# Description: my implementation for the solution for the Number of Islands problem on leetcode
# Problem: Given an m x n 2D binary grid 'grid' which represents a map of '1's (land) and '0's (water), return the number of islands.
# Difficulty: medium
# Author: Elbert C.

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # we know automatically its not valid islands if grid doesn't exist
        # like grid = []
        if not grid:
            return 0

        numIslands = 0
        numRows = len(grid)
        numCols = len(grid[0])
        eleVisited = set() # no duplicates, so using set is useful
        
        def iterate_bfs(row, col):
            search_queue = deque()
            eleVisited.add((row, col))
            search_queue.append((row, col))

            while search_queue:
                r, c = search_queue.popleft() # so first iteration r=0 and col=0
                # bfs so search up down left right
                directions = [[1,0], [-1, 0], [0, -1], [0, 1]]

                for dir_r, dir_c in directions:
                    row, col = r+dir_r, c+dir_c

                    if (row in range(numRows) and col in range(numCols) and grid[row][col] == '1' and (row, col) not in eleVisited):
                        search_queue.append((row, col))
                        eleVisited.add((row, col))

        for row in range(numRows):
            for col in range(numCols):
                # if the current element is a 1 and the row, col pair isn't already visited, proceed
                if grid[row][col] == '1' and (row, col) not in eleVisited:
                    # perform the interate_bfs function
                    # checking adjacent elements for the end of the island
                    iterate_bfs(row, col)
                    numIslands += 1
        
        return numIslands
        